# ActionScript 3.0 Documentation

Complete ActionScript 3.0 API documentation, available in both original HTML and LLM-friendly markdown formats.

## 📚 Documentation Formats

### 🚀 Concise Summaries (New & Recommended)

The `/docs` directory contains manually synthesized, high-density documentation designed specifically for LLM context windows. These files consolidate entire packages into single reference sheets.

**Status: ~85% Complete**

- ✅ **Core Language**: [Object.md](docs/Object.md), [Array.md](docs/Array.md), [String.md](docs/String.md), [Math.md](docs/Math.md), [XML.md](docs/XML.md)...
- ✅ **Visual & Display**: [Display.md](docs/Display.md) (Sprites, Bitmaps, Graphics)
- ✅ **Interactive**: [Events.md](docs/Events.md) (DOM-like event flow), [UI.md](docs/UI.md) (Mouse, Keyboard, GameInput)
- ✅ **Media & FX**: [Media.md](docs/Media.md) (Audio/Video), [Filters.md](docs/Filters.md) (Shaders & Blurs)
- ✅ **System & Data**: [Net.md](docs/Net.md) (Sockets, URLLoader), [Utils.md](docs/Utils.md) (ByteArray, Timers), [System.md](docs/System.md) (Security, Workers)
- ✅ **Text & Sensors**: [Text.md](docs/Text.md) (TextField, Styles), [Bridge_Sensors.md](docs/Bridge_Sensors.md) (ExternalInterface, GPS)
- ⏳ **Pending**: Printing API, Desktop Filesystem (AIR), Advanced Profiling.

### Raw Markdown conversion

The `markdown-docs/` directory remains available with 643 raw converted files for deep class-level lookups.

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

## 🔧 Tools & Contribution

### 🤖 AI Agent Synthesis Guide

If you are an AI agent continuing this work, please follow the [STYLE_GUIDE.md](docs/STYLE_GUIDE.md) in the `/docs` folder. It contains instructions on how to synthesize high-density package summaries, formatting standards, and content selection rules.

## 📖 Key Resources

### Original Documentation

- [All Classes](https://airsdk.dev/reference/actionscript/3.0/all-classes.html)
- [Package Summary](https://airsdk.dev/reference/actionscript/3.0/package-summary.html)
- [Class Summary](https://airsdk.dev/reference/actionscript/3.0/class-summary.html)
- [Language Elements](https://airsdk.dev/reference/actionscript/3.0/language-elements.html)
- [Appendices](https://airsdk.dev/reference/actionscript/3.0/appendices.html)

### Synthesized Reference (High Density)

- **Core Elements**: [NumericTypes.md](docs/NumericTypes.md), [String.md](docs/String.md), [Array.md](docs/Array.md), [Vector.md](docs/Vector.md), [XML.md](docs/XML.md)
- **Visuals**: [Display.md](docs/Display.md), [Text.md](docs/Text.md), [Filters.md](docs/Filters.md), [Geom.md](docs/Geom.md)
- **Engine**: [Events.md](docs/Events.md), [Utils.md](docs/Utils.md), [Net.md](docs/Net.md), [System.md](docs/System.md)
- **Hardware**: [UI.md](docs/UI.md), [Bridge_Sensors.md](docs/Bridge_Sensors.md), [Media.md](docs/Media.md)

## 📊 Statistics

- **Raw HTML Files**: 643
- **Synthesized Sheets**: 23 (Consolidated for LLMs)
- **Claude Skills**: 5
- **Progress**: Complete coverage of all major runtime packages.

## 🚀 Use Cases

1. **AI-Assisted Coding** - Use Claude skills in VSCode Copilot
2. **Documentation Search** - grep through markdown files
3. **Learning** - Read clean markdown docs
4. **Reference** - Quick API lookups
5. **LLM Context** - Feed docs to language models
