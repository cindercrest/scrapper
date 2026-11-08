# CLI Web Scraper

A simple Python CLI tool to scrape headings and links from any webpage and save them to a JSON file.

## Features

- Takes any URL directly from the terminal
- Spoofs a standard User-Agent header to avoid bot blocks
- Extracts `<h1>`, `<h2>`, `<h3>` headings and `<a>` links
- Saves scraped results to `scraped_output.json`

## Requirements

```bash
pip install requests beautifulsoup4
```

## Usage

```bash
python scrapper.py <URL>
```

### Example

```bash
python scrapper.py https://news.ycombinator.com
```
