# ActionScript 3.0 Documentation

Complete ActionScript 3.0 API documentation, available in both original HTML and LLM-friendly markdown formats.

## 📚 Documentation Formats

### Markdown Documentation (LLM-Friendly)
The `markdown-docs/` directory contains **643 clean markdown files** optimized for:
- ✅ Language model consumption (Claude, GPT, etc.)
- ✅ Easy reading and searching
- ✅ Code examples preserved and formatted
- ✅ No HTML clutter or navigation

**Quick Start:**
```bash
# Browse the docs
cd markdown-docs/

# Find a class
cat markdown-docs/Array.md
cat markdown-docs/flash/display/Sprite.md
```

See [markdown-docs/README.md](markdown-docs/README.md) for detailed structure and usage.

### Original HTML Documentation
The `html-docs/` directory contains the original HTML documentation from [airsdk.dev](https://airsdk.dev/reference/actionscript/3.0/).

## 🤖 Claude Skills for VSCode Copilot

The `.claude/skills/` directory contains ActionScript 3.0 programming skills for AI assistants:

1. **actionscript-basics.md** - Core language features, OOP, classes, functions
2. **actionscript-collections.md** - Arrays, Vectors, Dictionaries, data structures
3. **actionscript-display-graphics.md** - Display list, graphics, bitmaps
4. **actionscript-events.md** - Event system, async patterns, timers
5. **actionscript-api-reference.md** - Quick API reference and navigation guide

These skills help AI coding assistants understand ActionScript 3.0 patterns and best practices.

## 🔧 Tools

### HTML to Markdown Converter
```bash
python3 convert_html_to_md.py --input html-docs --output markdown-docs
```

Converts HTML documentation to clean markdown format.

## 📖 Key Resources

### Original Documentation
- [All Classes](https://airsdk.dev/reference/actionscript/3.0/all-classes.html)
- [Package Summary](https://airsdk.dev/reference/actionscript/3.0/package-summary.html)
- [Class Summary](https://airsdk.dev/reference/actionscript/3.0/class-summary.html)
- [Language Elements](https://airsdk.dev/reference/actionscript/3.0/language-elements.html)
- [Appendices](https://airsdk.dev/reference/actionscript/3.0/appendices.html)

### Markdown Documentation
- **Core Classes**: `markdown-docs/{Array,String,Object,Math}.md`
- **Display**: `markdown-docs/flash/display/`
- **Events**: `markdown-docs/flash/events/`
- **Network**: `markdown-docs/flash/net/`
- **Migration Guide**: `markdown-docs/migration.md` (AS2 → AS3)
- **All Classes**: `markdown-docs/all-classes.md`

## 📊 Statistics

- **HTML Files**: 643
- **Markdown Files**: 643
- **Claude Skills**: 5
- **Coverage**: Complete ActionScript 3.0 + AIR API

## 🚀 Use Cases

1. **AI-Assisted Coding** - Use Claude skills in VSCode Copilot
2. **Documentation Search** - grep through markdown files
3. **Learning** - Read clean markdown docs
4. **Reference** - Quick API lookups
5. **LLM Context** - Feed docs to language models
