#!/usr/bin/env python3
"""
Convert ActionScript HTML documentation to LLM-friendly markdown files.
Creates clean, single markdown files for each HTML file.
"""

import os
import re
import html2text
from bs4 import BeautifulSoup
from pathlib import Path
import argparse


def clean_html_content(html_content):
    """Extract main content from HTML and clean it."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove scripts, styles, navigation
    for element in soup.find_all(['script', 'style', 'nav', 'header', 'footer']):
        element.decompose()
    
    # Remove specific navigation elements
    for element in soup.find_all(class_=['titleTable', 'titleTableTopNav', 'titleTableSubNav']):
        element.decompose()
    
    # Find main content area
    main_content = soup.find('div', class_='MainContent')
    if not main_content:
        main_content = soup.find('body')
    
    if not main_content:
        return None
    
    return str(main_content)


def html_to_markdown(html_content, file_name):
    """Convert HTML to clean markdown."""
    # Clean the HTML first
    cleaned_html = clean_html_content(html_content)
    if not cleaned_html:
        return ""
    
    # Configure html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    h.unicode_snob = True
    h.skip_internal_links = False
    
    # Convert to markdown
    markdown = h.handle(cleaned_html)
    
    # Clean up excessive whitespace
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    # Add title from filename
    title = file_name.replace('.html', '').replace('-', ' ').title()
    header = f"# {title}\n\n"
    
    return header + markdown.strip()


def split_markdown(markdown_content, max_lines=None):
    """Return markdown as-is without splitting."""
    return [markdown_content]


def convert_file(html_path, output_dir, max_lines=None):
    """Convert a single HTML file to markdown."""
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
        
        file_name = os.path.basename(html_path)
        markdown = html_to_markdown(html_content, file_name)
        
        if not markdown or len(markdown.strip()) < 10:
            print(f"Skipping {html_path}: No content extracted")
            return 0
        
        # Get relative path structure
        rel_path = os.path.relpath(html_path, 'html-docs')
        rel_dir = os.path.dirname(rel_path)
        base_name = os.path.splitext(os.path.basename(rel_path))[0]
        
        # Create output directory
        output_subdir = os.path.join(output_dir, rel_dir)
        os.makedirs(output_subdir, exist_ok=True)
        
        # Write single markdown file
        output_path = os.path.join(output_subdir, f"{base_name}.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"Converted: {html_path} -> {output_path}")
        return 1
    
    except Exception as e:
        print(f"Error converting {html_path}: {e}")
        return 0


def convert_all_html(input_dir='html-docs', output_dir='markdown-docs', max_lines=None):
    """Convert all HTML files in directory to markdown."""
    html_files = list(Path(input_dir).rglob('*.html'))
    print(f"Found {len(html_files)} HTML files")
    
    total_files = 0
    for html_file in html_files:
        count = convert_file(str(html_file), output_dir, max_lines)
        total_files += count
    
    print(f"\nConversion complete!")
    print(f"Converted {len(html_files)} HTML files into {total_files} markdown files")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert HTML docs to markdown')
    parser.add_argument('--input', default='html-docs', help='Input directory')
    parser.add_argument('--output', default='markdown-docs', help='Output directory')
    
    args = parser.parse_args()
    
    convert_all_html(args.input, args.output)
