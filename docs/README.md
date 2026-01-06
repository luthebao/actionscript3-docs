# ActionScript 3.0 Documentation - Table of Contents

Complete reference documentation for ActionScript 3.0 and Adobe AIR APIs, organized by category.

## 📖 Quick Navigation

- [Core Language](#core-language)
- [Display & Graphics](#display--graphics)
- [Events & Interactivity](#events--interactivity)
- [Media](#media)
- [Networking](#networking)
- [Data & Storage](#data--storage)
- [System & Runtime](#system--runtime)
- [Text](#text)
- [Adobe AIR Features](#adobe-air-features)

---

## Core Language

Fundamental ActionScript 3.0 types and language features.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Object.md](Object.md) | Base object class and prototype chain | `Object` |
| [Array.md](Array.md) | Indexed collections and array methods | `Array` |
| [Vector.md](Vector.md) | Typed arrays for better performance | `Vector.<T>` |
| [String.md](String.md) | String manipulation and methods | `String` |
| [Boolean.md](Boolean.md) | Boolean type and truthiness | `Boolean` |
| [NumericTypes.md](NumericTypes.md) | Numeric types and operations | `Number`, `int`, `uint` |
| [Math.md](Math.md) | Mathematical constants and functions | `Math` |
| [Date.md](Date.md) | Date and time handling | `Date` |
| [Function.md](Function.md) | Functions and bound methods | `Function` |
| [RegExp.md](RegExp.md) | Regular expressions | `RegExp` |
| [JSON.md](JSON.md) | JSON serialization and parsing | `JSON` |
| [XML.md](XML.md) | E4X XML processing | `XML`, `XMLList` |
| [Errors.md](Errors.md) | Exception handling and error types | `Error`, `ArgumentError`, `TypeError`, etc. |
| [SpecialTypes.md](SpecialTypes.md) | Special language constructs | `Class`, `Namespace`, `QName`, `TimeZone`, `arguments` |

---

## Display & Graphics

Visual rendering, sprites, bitmaps, and graphics.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Display.md](Display.md) | Display list, sprites, and stage | `DisplayObject`, `Sprite`, `MovieClip`, `Stage`, `Bitmap` |
| [Geom.md](Geom.md) | Geometric primitives and transformations | `Point`, `Rectangle`, `Matrix`, `Transform` |
| [Filters.md](Filters.md) | Visual effects and filters | `BitmapFilter`, `BlurFilter`, `DropShadowFilter`, `ShaderFilter` |

---

## Events & Interactivity

Event system, user input, and interactive controls.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Events.md](Events.md) | Event dispatching and handling | `Event`, `EventDispatcher`, `EventPhase` |
| [UI.md](UI.md) | User input devices | `Mouse`, `Keyboard`, `GameInput`, `TouchEvent` |

---

## Media

Audio, video, and multimedia functionality.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Media.md](Media.md) | Audio and video playback | `Sound`, `SoundChannel`, `Video`, `Camera`, `Microphone` |

---

## Networking

Network communication and data loading.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Net.md](Net.md) | HTTP, sockets, and network protocols | `URLLoader`, `URLRequest`, `Socket`, `XMLSocket`, `NetConnection` |

---

## Data & Storage

Data structures, serialization, and persistent storage.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Utils.md](Utils.md) | Utility classes and binary data | `ByteArray`, `Timer`, `Dictionary`, `Proxy` |
| [Database.md](Database.md) | SQLite databases and encrypted storage **(AIR)** | `SQLConnection`, `SQLStatement`, `EncryptedLocalStore` |

---

## System & Runtime

System information, security, and runtime features.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [System.md](System.md) | System capabilities, security, and workers | `Capabilities`, `Security`, `Worker`, `ApplicationDomain` |
| [Profiler.md](Profiler.md) | Performance profiling and telemetry **(AIR)** | `Telemetry`, `Sample` |

---

## Text

Text rendering, formatting, and typography.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Text.md](Text.md) | Text fields, fonts, and formatting | `TextField`, `TextFormat`, `Font`, `StyleSheet` |

---

## Adobe AIR Features

Desktop and mobile-specific AIR functionality.

| Document | Description | Key Classes |
|----------|-------------|-------------|
| [Filesystem.md](Filesystem.md) | File system access **(AIR)** | `File`, `FileStream`, `FileMode` |
| [Printing.md](Printing.md) | Print job management **(AIR)** | `PrintJob`, `PrintJobOptions` |
| [Bridge_Sensors.md](Bridge_Sensors.md) | External communication and sensors | `ExternalInterface`, `Geolocation`, `Accelerometer` |
| [Accessibility.md](Accessibility.md) | Screen readers and accessibility | `Accessibility`, `AccessibilityProperties` |

---

## Document Statistics

- **Total Documents**: 30
- **Core Language**: 14 documents
- **Display & Graphics**: 3 documents
- **Events & UI**: 2 documents
- **Media**: 1 document
- **Networking**: 1 document
- **Data & Storage**: 2 documents
- **System & Runtime**: 2 documents
- **Text**: 1 document
- **AIR Features**: 4 documents

---

## Usage Tips

### For Learning
Start with **Core Language** documents to understand ActionScript 3.0 fundamentals, then move to specific areas based on your project needs.

### For Reference
Use your editor's search or `grep` to quickly find specific classes and methods across all documents.

### For AI/LLM Context
Each document is optimized for AI context windows with high-density information and minimal boilerplate. Feed relevant documents to your AI assistant for ActionScript 3.0 coding help.

---

## Related Resources

- [PROGRESS.md](../PROGRESS.md) - Documentation project progress and statistics
- [STYLE_GUIDE.md](../STYLE_GUIDE.md) - Documentation synthesis guidelines
- [README.md](../README.md) - Project overview and getting started

---

## Contributing

To add or update documentation:

1. Follow the [STYLE_GUIDE.md](../STYLE_GUIDE.md) for formatting standards
2. Extract content from `html-docs/` source files
3. Update this table of contents
4. Update [PROGRESS.md](../PROGRESS.md) with completion status

---

*Last Updated: January 2026*
