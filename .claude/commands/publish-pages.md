# Publish to GitHub Pages

Generate and publish a professional landing page showcasing all sprint reports.

## What This Does

1. **Scans** all sprint reports in `reports/` directory
2. **Generates** a beautiful HTML landing page with:
   - Project overview and statistics
   - Cards for each sprint/opportunity with scores and recommendations
   - Links to HTML, PDF, and Markdown versions of reports
   - Responsive design with professional styling
3. **Publishes** to GitHub Pages (if repository is configured)

## Steps to Execute

1. Generate the index.html page
2. Copy reports to docs/pages/ directory
3. Optionally commit and push to GitHub Pages

## Usage

```bash
# Generate the landing page
./scripts/publish/generate-pages.sh

# Or specify custom output directory
./scripts/publish/generate-pages.sh ./public
```

## GitHub Pages Setup

To enable automatic publishing:

1. Create a `gh-pages` branch or use `docs/` folder in main
2. Enable GitHub Pages in repository settings
3. Point to the generated index.html location

## Output

- `docs/pages/index.html` - Landing page
- Links to all sprint reports (HTML/PDF/MD formats)
- Professional, mobile-responsive design

## Requirements

- At least one sprint report in `reports/sprint-*-final-report.md`
- Reports should include score and TAM data (extracted automatically)

## Example

After running this command, you'll have a landing page similar to:
https://o2alexanderfedin.github.io/innova-technology-proposals/

The page will automatically calculate:
- Total number of strategic opportunities
- Combined TAM across all sprints
- Average opportunity score
- Research file count

## Customization

Edit the HTML template in `scripts/publish/generate-pages.sh` to:
- Change color scheme (currently purple gradient)
- Modify card layout
- Add additional statistics
- Update footer branding
