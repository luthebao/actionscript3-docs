# ActionScript 3.0 API Reference Helper

## Overview
Quick reference for finding and using ActionScript 3.0 APIs from the markdown documentation.

## Core Classes Location

### Top Level Classes
Located in: `markdown-docs/`
- `Array.md` - Array operations and methods
- `Boolean.md` - Boolean primitive
- `Date.md` - Date and time handling
- `Error.md` - Error handling base class
- `Function.md` - Function objects
- `JSON.md` - JSON parsing and serialization
- `Math.md` - Mathematical operations
- `Number.md` - Numeric operations
- `Object.md` - Base object class
- `RegExp.md` - Regular expressions
- `String.md` - String manipulation
- `Vector.md` - Typed arrays
- `XML.md`, `XMLList.md` - E4X XML processing

### Display Classes
Located in: `markdown-docs/flash/display/`
- `DisplayObject.md` - Base display class
- `DisplayObjectContainer.md` - Container base
- `Sprite.md` - Interactive containers
- `MovieClip.md` - Timeline animation
- `Shape.md` - Non-interactive graphics
- `Bitmap.md`, `BitmapData.md` - Raster graphics
- `Stage.md` - Root display container
- `Graphics.md` - Drawing API
- `Loader.md` - External content loading

### Event Classes
Located in: `markdown-docs/flash/events/`
- `Event.md` - Base event class
- `EventDispatcher.md` - Event dispatching
- `MouseEvent.md` - Mouse interactions
- `KeyboardEvent.md` - Keyboard input
- `TimerEvent.md` - Timer events
- `IOErrorEvent.md` - I/O errors
- `ProgressEvent.md` - Loading progress

### Network Classes
Located in: `markdown-docs/flash/net/`
- `URLLoader.md` - Load external data
- `URLRequest.md` - Request configuration
- `URLVariables.md` - URL parameters
- `Socket.md` - TCP socket connections
- `SharedObject.md` - Local storage

### Text Classes
Located in: `markdown-docs/flash/text/`
- `TextField.md` - Text display and input
- `TextFormat.md` - Text formatting
- `StyleSheet.md` - CSS styling
- `Font.md` - Embedded fonts

### Utility Classes
Located in: `markdown-docs/flash/utils/`
- `Timer.md` - Timed events
- `ByteArray.md` - Binary data
- `Dictionary.md` - Hash maps
- `getTimer.md`, `setTimeout.md` - Timing utilities
- `describeType.md` - Runtime reflection

### Media Classes
Located in: `markdown-docs/flash/media/`
- `Sound.md`, `SoundChannel.md` - Audio playback
- `Video.md` - Video display
- `Camera.md` - Webcam access
- `Microphone.md` - Audio input

### Geometry Classes
Located in: `markdown-docs/flash/geom/`
- `Point.md` - 2D point
- `Rectangle.md` - Rectangle
- `Matrix.md` - Transformation matrix
- `Transform.md` - Display object transforms

### Filter Classes
Located in: `markdown-docs/flash/filters/`
- `BlurFilter.md` - Blur effect
- `DropShadowFilter.md` - Drop shadow
- `GlowFilter.md` - Glow effect
- `ColorMatrixFilter.md` - Color transformations
- `BevelFilter.md`, `GradientGlowFilter.md`, etc.

## Common API Patterns

### Array Methods
```actionscript
// From Array.md
arr.push(item)              // Add to end
arr.pop()                   // Remove from end
arr.shift()                 // Remove from start
arr.unshift(item)           // Add to start
arr.splice(index, count)    // Remove/insert
arr.slice(start, end)       // Copy portion
arr.concat(arr2)            // Merge arrays
arr.join(separator)         // Join to string
arr.indexOf(item)           // Find index
arr.forEach(callback)       // Iterate
arr.map(callback)           // Transform
arr.filter(callback)        // Filter subset
arr.some(callback)          // Test any
arr.every(callback)         // Test all
```

### String Methods
```actionscript
// From String.md
str.charAt(index)           // Get character
str.charCodeAt(index)       // Get char code
str.indexOf(search)         // Find substring
str.lastIndexOf(search)     // Find from end
str.substr(start, length)   // Extract portion
str.substring(start, end)   // Extract range
str.slice(start, end)       // Extract (negative indices ok)
str.toLowerCase()           // Convert to lowercase
str.toUpperCase()           // Convert to uppercase
str.split(delimiter)        // Split to array
str.replace(search, replace) // Replace first
str.match(regexp)           // Match pattern
str.search(regexp)          // Search pattern
```

### Display List Methods
```actionscript
// From DisplayObjectContainer.md
container.addChild(child)
container.addChildAt(child, index)
container.removeChild(child)
container.removeChildAt(index)
container.getChildAt(index)
container.getChildByName(name)
container.contains(child)
container.numChildren
container.swapChildren(child1, child2)
```

### Event Handling
```actionscript
// From EventDispatcher.md
dispatcher.addEventListener(type, listener, useCapture, priority, useWeakReference)
dispatcher.removeEventListener(type, listener, useCapture)
dispatcher.dispatchEvent(event)
dispatcher.hasEventListener(type)
dispatcher.willTrigger(type)
```

### Graphics Drawing
```actionscript
// From Graphics.md
graphics.clear()
graphics.lineStyle(thickness, color, alpha)
graphics.beginFill(color, alpha)
graphics.beginGradientFill(type, colors, alphas, ratios, matrix)
graphics.endFill()
graphics.moveTo(x, y)
graphics.lineTo(x, y)
graphics.curveTo(cx, cy, x, y)
graphics.drawRect(x, y, width, height)
graphics.drawCircle(x, y, radius)
graphics.drawEllipse(x, y, width, height)
```

## Quick Search Guide

### Finding Class Documentation
1. Check top-level: `markdown-docs/{ClassName}.md`
2. Check flash package: `markdown-docs/flash/{category}/{ClassName}.md`
3. Check air package: `markdown-docs/air/{category}/{ClassName}.md`

Categories include:
- `display` - Visual elements
- `events` - Event types
- `net` - Networking
- `text` - Text rendering
- `utils` - Utilities
- `media` - Audio/video
- `geom` - Geometry
- `filters` - Visual effects
- `ui` - User interface
- `system` - System access
- `xml` - XML processing

### Finding Specific Features
- **Animation**: `MovieClip.md`, `Timer.md`, `Event.ENTER_FRAME`
- **Drawing**: `Graphics.md`, `Shape.md`, `Sprite.md`
- **Loading**: `Loader.md`, `URLLoader.md`
- **Storage**: `SharedObject.md`, `ByteArray.md`
- **Audio**: `Sound.md`, `SoundChannel.md`
- **Input**: `MouseEvent.md`, `KeyboardEvent.md`
- **Errors**: `Error.md`, `IOErrorEvent.md`, `SecurityErrorEvent.md`

## Documentation Structure

Each class documentation typically contains:
1. **Package and inheritance** - Where the class fits
2. **Description** - What the class does
3. **Properties** - Public properties/constants
4. **Methods** - Public methods
5. **Events** - Events dispatched
6. **Examples** - Code samples

## Usage Tips

### 1. Start with the Right Package
```actionscript
// Display objects
import flash.display.*;

// Events
import flash.events.*;

// Networking
import flash.net.*;

// Text
import flash.text.*;

// Utilities
import flash.utils.*;
```

### 2. Check Method Signatures
Look for:
- Parameter types and names
- Return type
- Optional parameters (shown with defaults)
- Thrown errors

### 3. Use Examples
Most documentation includes practical examples showing:
- Basic usage
- Common patterns
- Edge cases
- Best practices

### 4. Follow Related Links
Documentation often links to:
- Related classes
- Base classes
- Events dispatched
- See also sections

### 5. Search Across Files
Use these search patterns:
- Class name: `grep -r "class ClassName"`
- Method: `grep -r "methodName()"`
- Event: `grep -r "EVENT_NAME"`
- Property: `grep -r "propertyName"`

## Migration Guide

For ActionScript 2.0 to 3.0 migration:
- See `markdown-docs/migration.md` (split into parts)
- Lists all deprecated features
- Shows AS3 equivalents
- Explains behavior changes

## Language Elements

Core language syntax and keywords:
- See `markdown-docs/statements.md` (split into parts)
- See `markdown-docs/operators.md` (split into parts)
- See `markdown-docs/language-elements.md`

## Special Topics

### Compiler Errors
- `markdown-docs/compilerErrors.md` (split into parts)
- Error codes and descriptions
- How to resolve each error

### Runtime Errors
- `markdown-docs/runtimeErrors.md` (split into parts)
- Error codes and causes
- Debugging strategies

### What's New
- `markdown-docs/whatsnew.md` (split into parts)
- New features by version
- Deprecated features
- Breaking changes

## Best Practices for Documentation Use

1. **Bookmark common classes** - Keep frequently used class docs handy
2. **Read full descriptions** - Don't just skim method signatures
3. **Study examples** - Learn patterns from provided code
4. **Check inheritance** - Parent class methods are inherited
5. **Note version requirements** - Some features require specific Flash/AIR versions
6. **Follow conventions** - Documentation shows idiomatic usage
7. **Check "See also"** - Related functionality often grouped together

## Quick Reference Cards

### Creating Objects
```actionscript
new ClassName()             // Constructor
ClassName.staticMethod()    // Static method
instance.method()           // Instance method
instance.property           // Property access
instance.property = value   // Property set
```

### Type Checking
```actionscript
obj is ClassName           // Type check
obj as ClassName           // Type cast (null if fails)
ClassName(obj)             // Type cast (error if fails)
```

### Package Structure
```
Top Level - Core classes (Array, String, etc.)
├── flash.*
│   ├── display - Visual elements
│   ├── events - Event system
│   ├── net - Network/loading
│   ├── text - Text rendering
│   ├── utils - Utilities
│   ├── media - Audio/video
│   ├── geom - Geometry
│   ├── filters - Visual effects
│   └── ...
└── air.* - AIR-specific APIs
```
