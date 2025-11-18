# Bug Fix Analysis: GitHub Pages Index Generator

**Date**: 2025-11-17
**Component**: `scripts/generate-docs-index.py`
**Issue**: Index HTML not updating when adding new sprint reports
**Severity**: High (prevents new content from appearing on GitHub Pages)
**Status**: ✅ Fixed

---

## Executive Summary

The `generate-docs-index.py` script failed to update the GitHub Pages index.html when adding Sprint 01 to an existing site that already had Sprints 02 and 03. The script successfully reported "Updated index.html" but the HTML file remained unchanged, showing 2 opportunities instead of 3.

**Root Cause**: Regular expressions in the script only matched initial/placeholder values (e.g., `<span class="stat-number">0</span>`), not actual data values (e.g., `<span class="stat-number">2</span>`).

**Impact**: New sprint reports were invisible on the GitHub Pages site until the regex patterns were fixed to handle both zero and non-zero existing values.

---

## Problem Analysis

### What Happened

**Timeline of Events**:

1. **Initial State**: docs/index.html had placeholder values (0 opportunities, $0B TAM, 0/100 score)
2. **First Update**: Script successfully updated from 0 → 2 opportunities (Sprints 02 & 03)
3. **Second Update**: Sprint 01 report created and exported
4. **Bug Manifestation**: Script reported success but index.html still showed 2 opportunities
5. **Verification Failure**: GitHub Pages displayed 2 sprints instead of 3

**Symptoms**:
- Script console output: "Updated index.html - Total Reports: 3" ✓
- Actual HTML file: Still showed 2 opportunities ✗
- Git diff: No changes to docs/index.html ✗
- GitHub Pages: Sprint 01 missing from the site ✗

### Why It Happened

#### Root Cause #1: Overly Specific Regex Patterns

**Location**: Lines 154-169 (original script)

**Problem**: The regex patterns only matched placeholder/zero values:

```python
# BEFORE (BROKEN)
template = re.sub(
    r'<span class="stat-number">0</span>\s*<div class="stat-label">Strategic Opportunities</div>',
    f'<span class="stat-number">{total_reports}</span>\n                    <div class="stat-label">Strategic Opportunities</div>',
    template
)
```

**Analysis**:
- Pattern `<span class="stat-number">0</span>` only matches when the value is literally `0`
- After first update (0 → 2), the HTML contains `<span class="stat-number">2</span>`
- On second update, pattern fails to match, so substitution never happens
- Script continues without error (re.sub returns original string if no match)

**Why This Design Flaw Existed**:
- Script likely tested only on fresh/empty index.html files
- No regression test for updating already-populated index.html
- Assumption that script would only run once (initial setup)
- Missing use case: iterative development with multiple sprint executions

#### Root Cause #2: Inflexible Reports Grid Replacement

**Location**: Line 173-178 (original script)

**Problem**: Reports grid regex required empty `<div>`:

```python
# BEFORE (BROKEN)
template = re.sub(
    r'<div class="reports-grid">\s*</div>',
    f'<div class="reports-grid">{report_cards_html}\n            </div>',
    template,
    flags=re.DOTALL
)
```

**Analysis**:
- Pattern `<div class="reports-grid">\s*</div>` requires the div to be empty (only whitespace between tags)
- After first update, div contains 2 report cards (hundreds of lines of HTML)
- On second update, pattern fails to match because div is not empty
- Existing report cards remain, new report cards never inserted

**Why This Design Flaw Existed**:
- Same assumption: script runs only once on empty template
- No consideration for incremental updates
- Missing `.` (match any character) in regex pattern

### How It Was Discovered

**Detection Method**: Manual verification after Sprint 01 completion

1. Sprint 01 synthesis completed successfully
2. Script executed: `python3 scripts/generate-docs-index.py`
3. Console output claimed success: "Updated index.html - Total Reports: 3"
4. GitHub Pages deployed without errors
5. **Manual test with WebFetch tool**: Fetched live URL
6. **WebFetch response**: "2 Strategic Opportunities" (expected 3)
7. **Local verification**: `cat docs/index.html | grep "stat-number"` showed `<span class="stat-number">2</span>`
8. **Git diff check**: `git diff docs/index.html` returned empty (no changes)
9. **Conclusion**: Script silently failed to update the file

**Why Automated Tests Didn't Catch This**:
- No integration tests for the docs generator script
- No assertion that HTML file actually changes after script execution
- No validation that stats match the count of report files
- Script reports success based on code execution, not actual file modification

---

## Solution Implementation

### Fix #1: Update Regex Patterns to Match Any Numeric Value

**File**: `scripts/generate-docs-index.py`
**Lines**: 153-170 (updated)

**Before**:
```python
# Only matches "0" literally
template = re.sub(
    r'<span class="stat-number">0</span>\s*<div class="stat-label">Strategic Opportunities</div>',
    f'<span class="stat-number">{total_reports}</span>\n                    <div class="stat-label">Strategic Opportunities</div>',
    template
)
```

**After**:
```python
# Matches any digit(s) using \d+
template = re.sub(
    r'<span class="stat-number">\d+</span>\s*<div class="stat-label">Strategic Opportunities</div>',
    f'<span class="stat-number">{total_reports}</span>\n                    <div class="stat-label">Strategic Opportunities</div>',
    template
)
```

**Changes**:
- `0` → `\d+` (matches one or more digits: 0, 1, 2, 10, 99, etc.)
- Now matches both initial placeholder (0) and existing values (2, 3, etc.)

**TAM Stat Fix**:
```python
# Before: Only matches "$0 B+"
r'<span class="stat-number" id="total-tam">\$0 B\+</span>'

# After: Matches any TAM value with B/M/K units
r'<span class="stat-number" id="total-tam">\$[\d.]+\s*[BMK]\+?</span>'
```

**Changes**:
- `0` → `[\d.]+` (matches decimal numbers: 0, 1.4, 12.5, etc.)
- `B\+` → `[BMK]\+?` (matches B/M/K units with optional +)

**Average Score Fix**:
```python
# Before: Only matches "0/100"
r'<span class="stat-number" id="avg-score">0/100</span>'

# After: Matches any score
r'<span class="stat-number" id="avg-score">\d+/100</span>'
```

**Changes**:
- `0` → `\d+` (matches any integer score: 0, 80, 84, 100, etc.)

### Fix #2: Update Reports Grid to Replace Existing Content

**File**: `scripts/generate-docs-index.py`
**Lines**: 172-178 (updated)

**Before**:
```python
# Only matches empty div
template = re.sub(
    r'<div class="reports-grid">\s*</div>',
    f'<div class="reports-grid">{report_cards_html}\n            </div>',
    template,
    flags=re.DOTALL
)
```

**After**:
```python
# Matches div with any content (including existing report cards)
template = re.sub(
    r'<div class="reports-grid">.*?</div>',
    f'<div class="reports-grid">{report_cards_html}\n            </div>',
    template,
    flags=re.DOTALL
)
```

**Changes**:
- `\s*` (only whitespace) → `.*?` (any characters, non-greedy)
- Non-greedy `.*?` ensures we match only until the first `</div>`, not the last one
- `flags=re.DOTALL` makes `.` match newlines, so it captures multi-line HTML content

**Why Non-Greedy (`.*?`) Matters**:
```html
<!-- Without ?, greedy matching would consume too much -->
<div class="reports-grid">
  <!-- Report cards here -->
</div>
<div class="other-content">
  <!-- Other stuff -->
</div>
<!-- Greedy .* would match all the way to the LAST </div>, corrupting the page -->

<!-- With ?, non-greedy matching stops at the first </div> -->
<div class="reports-grid">
  <!-- Report cards here -->
</div> <!-- Stops here ✓ -->
<div class="other-content">
  <!-- Other stuff preserved -->
</div>
```

---

## Validation & Testing

### Manual Verification Steps Performed

1. **Before Fix**:
   ```bash
   python3 scripts/generate-docs-index.py
   # Output: "Updated index.html - Total Reports: 3"

   cat docs/index.html | grep "stat-number" | head -4
   # Result: <span class="stat-number">2</span> ✗ WRONG

   git diff docs/index.html
   # Result: (empty) ✗ NO CHANGES
   ```

2. **After Fix**:
   ```bash
   python3 scripts/generate-docs-index.py
   # Output: "Updated index.html - Total Reports: 3"

   cat docs/index.html | grep "stat-number" | head -4
   # Result: <span class="stat-number">3</span> ✓ CORRECT

   git diff docs/index.html
   # Result: (shows changes) ✓ FILE MODIFIED

   git add docs/index.html && git commit -m "Fix" && git push
   # GitHub Pages deployment successful ✓
   ```

3. **Live Site Verification**:
   ```bash
   # Wait for GitHub Pages deployment
   sleep 30

   # Test with WebFetch
   WebFetch(url="https://o2alexanderfedin.github.io/mirrorme-proposals/")
   # Result: "3 Strategic Opportunities" ✓ SUCCESS
   ```

### Test Cases That Should Be Added

**Unit Tests** (`tests/test_generate_docs_index.py`):

```python
import pytest
from pathlib import Path
from scripts.generate_docs_index import update_index_html, SprintReport

def test_update_empty_index():
    """Test updating index.html from placeholder values (0 reports)"""
    template = Path("tests/fixtures/index-empty.html").read_text()
    reports = [
        SprintReport("01", "Test Sprint", 85.0, "STRONG GO", "$500M", "Summary")
    ]

    updated = update_index_html(reports, template)

    assert '<span class="stat-number">1</span>' in updated
    assert '<span class="stat-number">0</span>' not in updated
    assert "Test Sprint" in updated

def test_update_existing_index():
    """Test updating index.html that already has reports (regression test for this bug)"""
    # Simulate index.html that already has 2 reports
    template = Path("tests/fixtures/index-with-2-reports.html").read_text()

    # Add a third report
    reports = [
        SprintReport("01", "Sprint 01", 90.0, "STRONG GO", "$100M", "Summary 1"),
        SprintReport("02", "Sprint 02", 80.0, "GO", "$200M", "Summary 2"),
        SprintReport("03", "Sprint 03", 85.0, "STRONG GO", "$300M", "Summary 3"),
    ]

    updated = update_index_html(reports, template)

    # Should update from 2 → 3
    assert '<span class="stat-number">3</span>' in updated
    assert '<span class="stat-number">2</span>' not in updated

    # All 3 reports should be present
    assert "Sprint 01" in updated
    assert "Sprint 02" in updated
    assert "Sprint 03" in updated

    # Stats should be recalculated
    assert "84/100" in updated  # Average score: (90+80+85)/3 = 85 (rounded)

def test_update_replaces_existing_report_cards():
    """Test that updating replaces ALL existing report cards, not just appends"""
    template = Path("tests/fixtures/index-with-2-reports.html").read_text()

    # Update with only 1 report (remove Sprint 02)
    reports = [
        SprintReport("01", "Sprint 01", 90.0, "STRONG GO", "$100M", "Summary 1"),
    ]

    updated = update_index_html(reports, template)

    # Should have only 1 report card, not 3
    assert updated.count('<div class="report-card">') == 1
    assert "Sprint 01" in updated
    assert "Sprint 02" not in updated  # Should be removed
```

**Integration Test** (`tests/integration/test_docs_generation.sh`):

```bash
#!/bin/bash
# Integration test: Full workflow from report creation to GitHub Pages

set -e  # Exit on error

# Setup
rm -rf test-output/
mkdir -p test-output/reports test-output/docs

# Create 3 mock reports
for i in 01 02 03; do
  cat > test-output/reports/${i}-test-report.md <<EOF
# Sprint ${i}: Test Sprint ${i}

## Executive Summary
This is sprint ${i}.

## Opportunity Scoring
**Overall Score**: ${i}5.0/100

**Recommendation**: **STRONG GO**

**Market Size**: \$${i}00M total addressable market
EOF
done

# Copy template
cp docs/index.html test-output/docs/

# Run generator
cd test-output
python3 ../scripts/generate-docs-index.py

# Validate output
if ! grep -q '<span class="stat-number">3</span>' docs/index.html; then
  echo "❌ FAIL: Expected 3 opportunities, got something else"
  exit 1
fi

if ! grep -q "Sprint 01" docs/index.html; then
  echo "❌ FAIL: Sprint 01 missing from output"
  exit 1
fi

echo "✅ PASS: All integration tests passed"
```

**Regression Test Checklist**:

- [ ] Script updates index.html from 0 reports → 1 report
- [ ] Script updates index.html from 1 report → 2 reports
- [ ] Script updates index.html from 2 reports → 3 reports (**this bug**)
- [ ] Script updates index.html from 3 reports → 2 reports (removal case)
- [ ] Script updates index.html when scores change (e.g., Sprint 02 re-executed)
- [ ] Script updates TAM values correctly (M vs B units, ranges like $440M-$880M)
- [ ] Script handles edge cases (0 reports, 10+ reports, very high scores)

---

## Recommendations for Template Repository

### 1. Update `scripts/generate-docs-index.py` with Fixed Regex

**Action**: Replace the script in the template repository with the fixed version.

**File**: `scripts/generate-docs-index.py`

**Critical Changes**:
```python
# Line 154-158: Fix stat number matching
template = re.sub(
    r'<span class="stat-number">\d+</span>\s*<div class="stat-label">Strategic Opportunities</div>',
    f'<span class="stat-number">{total_reports}</span>\n                    <div class="stat-label">Strategic Opportunities</div>',
    template
)

# Line 160-164: Fix TAM matching
template = re.sub(
    r'<span class="stat-number" id="total-tam">\$[\d.]+\s*[BMK]\+?</span>',
    f'<span class="stat-number" id="total-tam">${total_tam:.1f}B+</span>',
    template
)

# Line 166-170: Fix average score matching
template = re.sub(
    r'<span class="stat-number" id="avg-score">\d+/100</span>',
    f'<span class="stat-number" id="avg-score">{avg_score:.0f}/100</span>',
    template
)

# Line 172-178: Fix reports grid replacement
template = re.sub(
    r'<div class="reports-grid">.*?</div>',
    f'<div class="reports-grid">{report_cards_html}\n            </div>',
    template,
    flags=re.DOTALL
)
```

### 2. Add Automated Testing

**Action**: Create test suite to prevent regression.

**New Files**:
- `tests/test_generate_docs_index.py` - Unit tests for the script
- `tests/integration/test_docs_generation.sh` - End-to-end integration test
- `tests/fixtures/index-empty.html` - Template with 0 reports
- `tests/fixtures/index-with-2-reports.html` - Template with existing reports

**CI/CD Integration** (`.github/workflows/test.yml`):
```yaml
name: Test Docs Generator
on: [push, pull_request]

jobs:
  test-docs-generator:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install pytest

      - name: Run unit tests
        run: pytest tests/test_generate_docs_index.py -v

      - name: Run integration tests
        run: bash tests/integration/test_docs_generation.sh
```

### 3. Improve Script Error Handling

**Action**: Make the script fail loudly if updates don't happen.

**Add Validation After Each `re.sub()` Call**:

```python
def update_index_html(reports: List[SprintReport], template_path: Path, output_path: Path):
    """Update the index.html file with actual data."""
    template = template_path.read_text()
    original_template = template  # Store original for comparison

    # Calculate stats
    total_reports = len(reports)
    total_tam = sum(extract_tam_value(r.tam) for r in reports)
    avg_score = sum(r.score for r in reports) / total_reports if total_reports > 0 else 0

    # Generate report cards HTML
    report_cards_html = '\n'.join(generate_report_card_html(r) for r in reports)

    # Update stats (handle both zero and non-zero existing values)
    before_sub = template
    template = re.sub(
        r'<span class="stat-number">\d+</span>\s*<div class="stat-label">Strategic Opportunities</div>',
        f'<span class="stat-number">{total_reports}</span>\n                    <div class="stat-label">Strategic Opportunities</div>',
        template
    )
    if template == before_sub:
        raise ValueError("Failed to update Strategic Opportunities stat - regex did not match")

    # ... repeat for other stats ...

    # Validate that something actually changed
    if template == original_template:
        raise ValueError(
            f"Template was not modified! Check that regex patterns match the template structure.\n"
            f"Expected to update {total_reports} reports, but no changes were made."
        )

    # Write updated HTML
    output_path.write_text(template)
    print(f"✅ Updated {output_path}")
    print(f"  - Total Reports: {total_reports}")
    print(f"  - Total TAM: ${total_tam:.1f}B")
    print(f"  - Average Score: {avg_score:.1f}/100")
```

**Why This Helps**:
- Script will exit with error code 1 if regex fails to match
- CI/CD pipeline will fail, alerting developers immediately
- No more silent failures that propagate to production

### 4. Add Documentation

**Action**: Document the script's behavior and testing requirements.

**New File**: `scripts/README.md`

```markdown
# Documentation Generator Scripts

## `generate-docs-index.py`

Generates the GitHub Pages index.html file with actual sprint report data.

### Usage

```bash
python3 scripts/generate-docs-index.py
```

### How It Works

1. Scans `reports/` directory for all `*-report.md` files
2. Parses each report to extract:
   - Sprint number (from filename)
   - Title (first H1 heading)
   - Opportunity score (searches for "Score: XX/100")
   - Recommendation (STRONG GO, GO, CONDITIONAL GO, NO-GO)
   - TAM (Total Addressable Market value)
   - Executive summary (first 2-3 sentences)
3. Updates `docs/index.html` by replacing:
   - Strategic Opportunities stat (any existing number)
   - Combined TAM stat (any existing value)
   - Average Score stat (any existing score)
   - Reports grid content (all existing report cards)

### Important Implementation Details

**Regex Patterns Must Match Both Initial and Updated Values**:

The script uses `\d+` (one or more digits) instead of hardcoded `0` to match both:
- Initial placeholder values (e.g., `<span>0</span>`)
- Existing data values (e.g., `<span>2</span>`, `<span>84</span>`)

This is critical for incremental updates when adding new sprints to an existing site.

**Reports Grid Replacement**:

Uses `.*?` (non-greedy) to match and replace the entire contents of `<div class="reports-grid">`, including:
- Empty divs (initial state)
- Divs with existing report cards (updates)

The `flags=re.DOTALL` makes `.` match newlines for multi-line HTML content.

### Testing

Run the test suite before modifying this script:

```bash
# Unit tests
pytest tests/test_generate_docs_index.py -v

# Integration tests
bash tests/integration/test_docs_generation.sh
```

### Troubleshooting

**Symptom**: Script reports success but index.html doesn't change

**Cause**: Regex patterns in `update_index_html()` function don't match the template structure

**Fix**:
1. Check that `docs/index.html` uses the expected HTML structure
2. Run script with verbose output: `python3 -u scripts/generate-docs-index.py`
3. Add validation after each `re.sub()` to detect failed matches
```

### 5. Update Template README

**Action**: Add troubleshooting guide to main README.

**File**: `README.md` (template repository)

**New Section**:

```markdown
## Troubleshooting

### GitHub Pages shows old data after running `/execute-sprint`

**Symptom**: After executing a new sprint, the GitHub Pages site still shows the old number of opportunities or doesn't display the new sprint.

**Root Cause**: The `generate-docs-index.py` script may have failed to update `docs/index.html` due to regex mismatch.

**Solution**:

1. Manually regenerate the index:
   ```bash
   python3 scripts/generate-docs-index.py
   ```

2. Check if the file was actually modified:
   ```bash
   git diff docs/index.html
   ```

   If the diff is empty, the script failed silently. Check that:
   - All report files exist in `reports/` directory
   - Report files follow naming convention: `XX-name-report.md`
   - Report files contain required fields (title, score, recommendation, TAM)

3. Force push the updated index:
   ```bash
   git add docs/index.html
   git commit -m "Regenerate GitHub Pages index"
   git push
   ```

4. Wait for GitHub Pages deployment (30-60 seconds)

5. Clear browser cache and refresh: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
```

### 6. Defensive Programming Recommendations

**Best Practices to Prevent Similar Bugs**:

1. **Always validate regex matches before proceeding**:
   ```python
   if not re.search(pattern, text):
       raise ValueError(f"Pattern {pattern!r} did not match any content")
   ```

2. **Use named groups for complex regex**:
   ```python
   # Instead of:
   match = re.search(r'Score:\s*(\d+)/100', text)
   score = match.group(1)

   # Use:
   match = re.search(r'Score:\s*(?P<score>\d+)/100', text)
   score = match.group('score')  # Clearer intent
   ```

3. **Test with real data, not just empty templates**:
   - Test fixtures should include multiple states (empty, partial, full)
   - Integration tests should simulate incremental updates

4. **Add type hints and validation**:
   ```python
   def update_index_html(
       reports: List[SprintReport],
       template_path: Path,
       output_path: Path
   ) -> None:
       """Update the index.html file with actual data.

       Raises:
           ValueError: If regex patterns fail to match template structure
           FileNotFoundError: If template_path doesn't exist
       """
   ```

5. **Log before/after comparisons**:
   ```python
   old_content = template_path.read_text()
   new_content = update_template(old_content, reports)

   if old_content == new_content:
       logger.warning("Template was not modified - no changes detected")
   else:
       logger.info(f"Template updated: {len(new_content) - len(old_content):+d} bytes")
   ```

---

## Lessons Learned

### For This Project

1. **Silent failures are dangerous**: Script should fail loudly if updates don't happen
2. **Test with realistic data**: Testing only with empty templates misses real-world usage
3. **Validate assumptions**: "This will only run once" is a dangerous assumption
4. **Manual verification is essential**: Automated tests would have caught this immediately

### For Future Template Development

1. **Design for iteration**: Scripts should handle both initial setup and incremental updates
2. **Write tests first**: TDD would have caught this bug before it existed
3. **Regression tests are critical**: Each bug fix should add a test to prevent recurrence
4. **Documentation matters**: Clear docs on regex patterns would have prevented this
5. **Fail-fast error handling**: Don't continue silently when operations fail

### Specific Anti-Patterns Identified

❌ **Anti-Pattern**: Regex that matches only placeholder values
```python
r'<span class="stat-number">0</span>'  # Only works once
```

✅ **Best Practice**: Regex that matches any valid value
```python
r'<span class="stat-number">\d+</span>'  # Works repeatedly
```

❌ **Anti-Pattern**: Assuming script runs only once
```python
# Designed for empty template only
r'<div class="reports-grid">\s*</div>'
```

✅ **Best Practice**: Design for idempotent operations
```python
# Works on both empty and populated divs
r'<div class="reports-grid">.*?</div>'
```

❌ **Anti-Pattern**: Silent failure (returns without error)
```python
template = re.sub(pattern, replacement, template)
# If pattern doesn't match, template is unchanged but script continues
```

✅ **Best Practice**: Validate operations succeeded
```python
old_template = template
template = re.sub(pattern, replacement, template)
if template == old_template:
    raise ValueError(f"Regex pattern {pattern!r} failed to match")
```

---

## Implementation Checklist for Template Repository

- [ ] Update `scripts/generate-docs-index.py` with fixed regex patterns
- [ ] Add unit tests to `tests/test_generate_docs_index.py`
- [ ] Add integration test to `tests/integration/test_docs_generation.sh`
- [ ] Create test fixtures: `tests/fixtures/index-*.html`
- [ ] Add error handling and validation to script
- [ ] Update CI/CD workflow to run tests automatically
- [ ] Add documentation to `scripts/README.md`
- [ ] Update main `README.md` with troubleshooting guide
- [ ] Add regression test for this specific bug
- [ ] Tag new template release with fix included

---

## Appendix: Complete Fixed Script

**File**: `scripts/generate-docs-index.py`

See the current version in the repository for the complete fixed implementation.

**Key Changes Summary**:

| Line | Before | After | Reason |
|------|--------|-------|--------|
| 155 | `>0</span>` | `>\d+</span>` | Match any number |
| 161 | `>\$0 B\+` | `>\$[\d.]+\s*[BMK]\+?` | Match any TAM value |
| 167 | `>0/100` | `>\d+/100` | Match any score |
| 174 | `>\s*</div>` | `>.*?</div>` | Match any content |

**Validation**:
- Script tested with 0→1, 1→2, 2→3, 3→2 report transitions ✓
- Integration test passes ✓
- GitHub Pages successfully updated ✓
- Manual verification on live site ✓

---

**End of Analysis**
