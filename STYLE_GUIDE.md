# AI Agent Style Guide: Documentation Synthesis

This guide defines the standards for generating high-density, LLM-friendly ActionScript 3.0 documentation from raw HTML source files.

## 🎯 Goal

Transform verbose, multi-page HTML documentation into concise, single-page markdown summaries that fit within context windows while preserving all critical API signatures and behavioral notes.

## 🛠 Synthesis Process

1. **Identify Logical Groups**: Do not create one file per class. Group related classes (e.g., all `flash.filters` in `Filters.md`, all `flash.sensors` in `Bridge_Sensors.md`).
2. **Extract Core Signatures**: Priorities include:
    - Constructor parameters and defaults.
    - Public properties (noting if read-only).
    - Public methods with types: `name(arg:Type):ReturnType`.
    - Constants and Enumerations.
3. **Consolidate Events**: List the events dispatched by a class in a dedicated section with their corresponding `flash.events` class type.
4. **Detect Platform Nuances**: Explicitly mark features as **[AIR Only]** or **[Mobile Only]** where applicable.

## 📝 Formatting Standards

### 1. Title and Header

Use the package name or functional area as the H1.

```markdown
# flash.package.Name Reference
```

### 2. Class Sections

Use H2/H3 for classes. Include a 1-sentence description.

```markdown
## ClassName
Description of the class's primary purpose.
- `property:Type`: Description (mention if static).
- `method(arg:Type):ReturnType`: Description.
```

### 3. Signatures

Always use exact ActionScript 3.0 type syntax. Use backticks for code.

- ✅ `addEventListener(type:String, listener:Function):void`
- ❌ `addEventListener - takes a type and a function`

### 4. Code Examples

Include brief (5-15 lines) idiomatic examples. Use `actionscript` or `javascript` labels for syntax highlighting.

```actionscript
var sprite:Sprite = new Sprite();
sprite.graphics.beginFill(0xFF0000);
sprite.graphics.drawRect(0, 0, 100, 100);
```

### 5. Tables for Constants

Use tables for large groups of constants (like `Keyboard` codes) to save vertical space.

## 🚫 Avoid

- **Boilerplate**: Remove "Language version", "Runtime version", "Inheritance", and long "See also" lists unless they contain critical context.
- **Fluff**: Avoid conversational filler. The content should be dense and reference-grade.
- **Complexity**: If a class is rarely used or redundant, omit it or group it under a "Minor Classes" section.

## 📂 Mapping Instructions

- Source: `html-docs/package/name/Class.html`
- Output: `docs/FunctionalArea.md`
- Updates: Always update `README.md` statistics and "Status" sections after creating a new summary.
