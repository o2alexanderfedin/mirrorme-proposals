#!/usr/bin/env python3
"""
Generate docs/index.html with actual sprint report data.

This script reads sprint reports from the reports/ directory, extracts key metrics,
and updates the docs/index.html file with real data instead of placeholders.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional

# Report data structure
class SprintReport:
    def __init__(self, sprint_number: str, title: str, score: float,
                 recommendation: str, tam: str, summary: str):
        self.sprint_number = sprint_number
        self.title = title
        self.score = score
        self.recommendation = recommendation
        self.tam = tam
        self.summary = summary

def extract_tam_value(tam_text: str) -> float:
    """Extract numeric TAM value in billions from text like '$720M' or '$440M-$880M'"""
    # Extract numbers and convert to billions
    numbers = re.findall(r'\$?(\d+(?:\.\d+)?)\s*([MB])', tam_text)
    if not numbers:
        return 0.0

    # Take the average if range, otherwise single value
    values = []
    for num, unit in numbers:
        val = float(num)
        if unit == 'M':
            val = val / 1000  # Convert millions to billions
        values.append(val)

    return sum(values) / len(values) if values else 0.0

def parse_sprint_report(filepath: Path) -> Optional[SprintReport]:
    """Parse a sprint report markdown file and extract key data."""
    try:
        content = filepath.read_text()

        # Extract sprint number from filename (e.g., "02-franchise-development-program-report.md")
        match = re.match(r'(\d+)-(.+)-report\.md', filepath.name)
        if not match:
            return None
        sprint_number = match.group(1)

        # Extract title (first h1 heading)
        title_match = re.search(r'^#\s+(.+?)(?:\s+-\s+Final Report)?$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Unknown Title"

        # Extract opportunity score (look for "Opportunity Score: XX/100" or "Score: XX/100")
        score_match = re.search(r'(?:Opportunity\s+)?Score[:\s]+(\d+(?:\.\d+)?)/100', content, re.IGNORECASE)
        score = float(score_match.group(1)) if score_match else 0.0

        # Extract recommendation (STRONG GO, GO, CONDITIONAL GO, etc.)
        rec_match = re.search(r'\*\*Recommendation\*\*:\s*\*\*([A-Z\s]+)\*\*', content)
        if not rec_match:
            rec_match = re.search(r'Recommendation:\s*\*\*([A-Z\s]+)\*\*', content)
        recommendation = rec_match.group(1).strip() if rec_match else "UNKNOWN"

        # Normalize recommendation to one of the standard values
        rec_normalized = recommendation.upper()
        if 'STRONG' in rec_normalized and 'GO' in rec_normalized:
            recommendation = "STRONG GO"
        elif 'CONDITIONAL' in rec_normalized and 'GO' in rec_normalized:
            recommendation = "GO"  # Map CONDITIONAL GO to GO for CSS class
        elif 'NO' in rec_normalized and 'GO' in rec_normalized:
            recommendation = "NO-GO"
        elif 'GO' in rec_normalized:
            recommendation = "GO"
        else:
            recommendation = "CONSIDER"

        # Extract TAM (Total Addressable Market)
        # Look for patterns like "$720M total addressable market" or "TAM: $440M-$880M"
        tam_match = re.search(r'\$[\d,]+[MB](?:\s*-\s*\$[\d,]+[MB])?\s+(?:total\s+addressable\s+market|TAM)', content, re.IGNORECASE)
        if not tam_match:
            tam_match = re.search(r'TAM[:\s]+\$[\d,]+[MB](?:\s*-\s*\$[\d,]+[MB])?', content, re.IGNORECASE)
        if not tam_match:
            # Try to find in executive summary section
            exec_summary = re.search(r'##\s+Executive\s+Summary(.+?)##', content, re.DOTALL | re.IGNORECASE)
            if exec_summary:
                tam_match = re.search(r'\$[\d,]+[MB](?:\s*-\s*\$[\d,]+[MB])?\s+total\s+addressable\s+market', exec_summary.group(1), re.IGNORECASE)

        tam = tam_match.group(0).strip() if tam_match else "Market size not specified"

        # Extract executive summary (first 2-3 sentences)
        exec_match = re.search(r'##\s+Executive\s+Summary\s+(.+?)(?:##|\n\n\*\*)', content, re.DOTALL | re.IGNORECASE)
        if exec_match:
            summary_text = exec_match.group(1).strip()
            # Get first 2-3 sentences (up to 300 chars)
            sentences = re.split(r'(?<=[.!?])\s+', summary_text)
            summary = ' '.join(sentences[:2])
            if len(summary) > 300:
                summary = summary[:300] + '...'
        else:
            summary = "No executive summary available."

        # Clean up summary (remove markdown formatting)
        summary = re.sub(r'\*\*(.+?)\*\*', r'\1', summary)  # Remove bold
        summary = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', summary)  # Remove links
        summary = re.sub(r'<br\s*/?>', ' ', summary)  # Remove line breaks

        # Clean up title: remove redundant "Sprint XX:" prefix and other repetitions
        # Examples:
        #   "Sprint 02: Sprint 02: Franchise..." -> "Franchise..."
        #   "Sprint 03 Strategic Report: Healthcare..." -> "Healthcare..."
        #   "Strategic Research Report: Corporate..." -> "Corporate..."
        title = re.sub(r'^Sprint\s+\d+:\s*', '', title)  # Remove "Sprint XX:" prefix
        title = re.sub(r'^Sprint\s+\d+\s+', '', title)   # Remove "Sprint XX " prefix
        title = re.sub(r'^Strategic\s+Research\s+Report:\s*', '', title)  # Remove "Strategic Research Report:"
        title = re.sub(r'^Strategic\s+Report:\s*', '', title)  # Remove "Strategic Report:"
        title = title.strip()

        return SprintReport(sprint_number, title, score, recommendation, tam, summary)

    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def generate_report_card_html(report: SprintReport) -> str:
    """Generate HTML for a report card."""
    # Map recommendation to CSS class
    rec_class = report.recommendation.lower().replace(' ', '-')

    # Create slug from sprint number for file linking
    sprint_slug = f"{report.sprint_number}-{report.title.lower().replace(' ', '-').replace('&', 'and').replace(':', '')}"

    return f'''
                <div class="report-card">
                    <h3>{report.title}</h3>
                    <div>
                        <span class="score-badge">Score: {report.score}/100</span>
                        <span class="recommendation {rec_class}">{report.recommendation}</span>
                    </div>
                    <p>{report.summary}</p>
                    <div class="market-data">
                        <strong>Market Size:</strong> {report.tam}
                    </div>
                    <div class="report-links">
                        <a href="reports/{sprint_slug}-report.html" class="btn btn-primary">HTML</a>
                        <a href="../reports/{sprint_slug}-report.pdf" class="btn btn-secondary">PDF</a>
                        <a href="../reports/{sprint_slug}-report.docx" class="btn btn-secondary">DOCX</a>
                        <a href="../reports/{sprint_slug}-report.md" class="btn btn-secondary">Markdown</a>
                    </div>
                </div>
'''

def update_index_html(reports: List[SprintReport], template_path: Path, output_path: Path):
    """Update the index.html file with actual data."""
    template = template_path.read_text()

    # Calculate stats
    total_reports = len(reports)
    total_tam = sum(extract_tam_value(r.tam) for r in reports)
    avg_score = sum(r.score for r in reports) / total_reports if total_reports > 0 else 0

    # Generate report cards HTML
    report_cards_html = '\n'.join(generate_report_card_html(r) for r in reports)

    # Update stats (handle both zero and non-zero existing values)
    template = re.sub(
        r'<span class="stat-number">\d+</span>\s*<div class="stat-label">Strategic Opportunities</div>',
        f'<span class="stat-number">{total_reports}</span>\n                    <div class="stat-label">Strategic Opportunities</div>',
        template
    )

    template = re.sub(
        r'<span class="stat-number" id="total-tam">\$[\d.]+\s*[BMK]\+?</span>',
        f'<span class="stat-number" id="total-tam">${total_tam:.1f}B+</span>',
        template
    )

    template = re.sub(
        r'<span class="stat-number" id="avg-score">\d+/100</span>',
        f'<span class="stat-number" id="avg-score">{avg_score:.0f}/100</span>',
        template
    )

    # Update reports grid (replace existing content or empty div)
    # Use a more specific pattern that captures the full reports-grid section
    # including all nested report-card divs until the closing </div> at the same indentation level
    grid_pattern = r'(<div class="reports-grid">).*?(</div>\s*</main>)'
    replacement = r'\1' + report_cards_html + r'\n            \2'
    template = re.sub(
        grid_pattern,
        replacement,
        template,
        flags=re.DOTALL
    )

    # Write updated HTML
    output_path.write_text(template)
    print(f"Updated {output_path}")
    print(f"  - Total Reports: {total_reports}")
    print(f"  - Total TAM: ${total_tam:.1f}B")
    print(f"  - Average Score: {avg_score:.1f}/100")

def main():
    """Main execution function."""
    # Paths
    project_root = Path(__file__).parent.parent
    reports_dir = project_root / 'reports'
    docs_dir = project_root / 'docs'
    template_path = docs_dir / 'index.html'

    # Find all sprint report markdown files
    report_files = sorted(reports_dir.glob('*-report.md'))

    if not report_files:
        print("No report files found in reports/ directory")
        return

    print(f"Found {len(report_files)} report files")

    # Parse reports
    reports = []
    for filepath in report_files:
        print(f"Parsing {filepath.name}...")
        report = parse_sprint_report(filepath)
        if report:
            reports.append(report)
            print(f"  ✓ Sprint {report.sprint_number}: {report.title}")
            print(f"    Score: {report.score}/100, Recommendation: {report.recommendation}")
            print(f"    TAM: {report.tam}")
        else:
            print(f"  ✗ Failed to parse {filepath.name}")

    if not reports:
        print("No valid reports parsed")
        return

    # Sort reports by sprint number
    reports.sort(key=lambda r: int(r.sprint_number))

    # Update index.html
    print("\nUpdating index.html...")
    update_index_html(reports, template_path, template_path)
    print("\n✓ Successfully updated docs/index.html")

if __name__ == '__main__':
    main()
