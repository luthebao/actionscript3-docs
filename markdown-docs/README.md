# ActionScript 3.0 Markdown Documentation

This directory contains the complete ActionScript 3.0 API documentation converted to clean, LLM-friendly markdown format.

## Structure

The documentation maintains the same directory structure as the original HTML docs:

```
markdown-docs/
├── Top-level classes (Array, String, Object, etc.)
├── flash/
│   ├── display/      - Display list and graphics
│   ├── events/       - Event system
│   ├── net/          - Networking and loading
│   ├── text/         - Text rendering
│   ├── utils/        - Utilities
│   ├── media/        - Audio and video
│   ├── geom/         - Geometry classes
│   ├── filters/      - Visual effects
│   └── ...
├── air/              - AIR-specific APIs
└── avm2/             - AVM2 intrinsics
```

## Features

- **Clean Markdown**: All HTML navigation, scripts, and styling removed
- **Preserved Content**: All class descriptions, methods, properties, and examples retained
- **Code Blocks**: ActionScript code examples properly formatted
- **Single Files**: Each HTML file converted to one markdown file (no splitting)
- **LLM-Friendly**: Optimized for language model consumption and understanding

## Statistics

- **Total Files**: 643 markdown files
- **Source**: Converted from HTML documentation at https://airsdk.dev/reference/actionscript/3.0/

## Usage

### Finding Classes

1. **Top-level classes**: Look in the root directory
   - Example: `Array.md`, `String.md`, `Math.md`

2. **Flash classes**: Navigate to `flash/{category}/`
   - Display: `flash/display/Sprite.md`
   - Events: `flash/events/MouseEvent.md`
   - Network: `flash/net/URLLoader.md`

3. **AIR classes**: Navigate to `air/{category}/`
   - Example: `air/net/WebSocket.md`

### Quick Reference

- **All Classes**: `all-classes.md`
- **Class Summary**: `class-summary.md`
- **Package Summary**: `package-summary.md`
- **Language Elements**: `language-elements.md`
- **Operators**: `operators.md`
- **Statements**: `statements.md`
- **Migration Guide**: `migration.md` (AS2 to AS3)
- **What's New**: `whatsnew.md`
- **Compiler Errors**: `compilerErrors.md`
- **Runtime Errors**: `runtimeErrors.md`

## Conversion

The documentation was converted using `convert_html_to_md.py` script which:

1. Extracts main content from HTML
2. Removes navigation and boilerplate
3. Converts to markdown using html2text
4. Preserves code examples and formatting
5. Maintains directory structure

To reconvert (if needed):
```bash
python3 convert_html_to_md.py --input html-docs --output markdown-docs
```

## Claude Skills

For VSCode Copilot and Claude Code integration, see the `.claude/skills/` directory which contains:

- `actionscript-basics.md` - Language fundamentals
- `actionscript-collections.md` - Arrays, Vectors, Dictionaries
- `actionscript-display-graphics.md` - Display list and drawing
- `actionscript-events.md` - Event system and async patterns
- `actionscript-api-reference.md` - Quick API reference guide
