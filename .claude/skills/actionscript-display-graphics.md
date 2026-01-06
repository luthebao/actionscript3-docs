# ActionScript 3.0 Display and Graphics

## Overview
This skill covers the Flash display list, graphics rendering, and visual elements in ActionScript 3.0.

## Display List Hierarchy

### Display Object Hierarchy
```
DisplayObject (abstract base)
├── InteractiveObject
│   ├── DisplayObjectContainer
│   │   ├── Sprite
│   │   │   └── MovieClip
│   │   └── Stage
│   └── SimpleButton, TextField
├── Bitmap
├── Shape
└── Video
```

### Creating Display Objects
```actionscript
import flash.display.*;

// Shape - lightweight, non-interactive
var shape:Shape = new Shape();

// Sprite - container, interactive
var sprite:Sprite = new Sprite();

// MovieClip - timeline animation
var mc:MovieClip = new MovieClip();

// Bitmap - raster image
var bmp:Bitmap = new Bitmap(bitmapData);
```

## Display List Operations

### Adding/Removing Children
```actionscript
// Add to display list
container.addChild(sprite);
container.addChildAt(sprite, 0);  // At specific index

// Remove from display list
container.removeChild(sprite);
container.removeChildAt(0);
container.removeChildren();  // Remove all

// Check parent
if (sprite.parent != null) {
    sprite.parent.removeChild(sprite);
}

// Access children
var child:DisplayObject = container.getChildAt(0);
var childByName:DisplayObject = container.getChildByName("mySprite");
var numChildren:int = container.numChildren;
```

### Z-order Management
```actionscript
// Change display order
container.setChildIndex(sprite, 0);  // Move to back
container.swapChildren(sprite1, sprite2);
container.swapChildrenAt(0, 1);

// Get index
var index:int = container.getChildIndex(sprite);
```

## Positioning and Transformation

### Position and Size
```actionscript
// Position
sprite.x = 100;
sprite.y = 200;

// Size
sprite.width = 150;
sprite.height = 100;

// Scale
sprite.scaleX = 2.0;  // 200%
sprite.scaleY = 0.5;  // 50%

// Rotation (degrees)
sprite.rotation = 45;

// Visibility
sprite.visible = false;

// Alpha (transparency)
sprite.alpha = 0.5;  // 50% transparent
```

### Coordinate Spaces
```actionscript
// Local to global
var globalPt:Point = sprite.localToGlobal(new Point(0, 0));

// Global to local
var localPt:Point = sprite.globalToLocal(new Point(100, 100));

// Convert between objects
var pt:Point = sprite1.localToGlobal(new Point(0, 0));
pt = sprite2.globalToLocal(pt);

// Get bounds
var bounds:Rectangle = sprite.getBounds(container);
var rect:Rectangle = sprite.getRect(container);
```

### Transformation Matrix
```actionscript
import flash.geom.Matrix;

var matrix:Matrix = new Matrix();
matrix.translate(100, 50);
matrix.rotate(Math.PI / 4);  // 45 degrees (radians)
matrix.scale(2, 2);

sprite.transform.matrix = matrix;
```

## Drawing with Graphics

### Basic Shapes
```actionscript
var g:Graphics = shape.graphics;

// Line style
g.lineStyle(2, 0x000000);  // thickness, color
g.lineStyle(2, 0xFF0000, 0.5);  // with alpha

// Fill style
g.beginFill(0xFF0000);     // solid color
g.beginFill(0xFF0000, 0.5);  // with alpha

// Draw shapes
g.drawRect(10, 10, 100, 50);
g.drawRoundRect(10, 10, 100, 50, 10);  // rounded corners
g.drawCircle(50, 50, 30);
g.drawEllipse(10, 10, 100, 50);

// End fill
g.endFill();

// Clear graphics
g.clear();
```

### Drawing Paths
```actionscript
var g:Graphics = shape.graphics;

g.lineStyle(2, 0x000000);
g.moveTo(10, 10);
g.lineTo(100, 10);
g.lineTo(100, 100);
g.lineTo(10, 100);
g.lineTo(10, 10);

// Bezier curves
g.curveTo(50, 0, 100, 50);  // quadratic
g.cubicCurveTo(25, 0, 75, 0, 100, 50);  // cubic
```

### Gradient Fills
```actionscript
import flash.geom.Matrix;
import flash.display.GradientType;

var g:Graphics = shape.graphics;
var colors:Array = [0xFF0000, 0x0000FF];
var alphas:Array = [1, 1];
var ratios:Array = [0, 255];
var matrix:Matrix = new Matrix();
matrix.createGradientBox(200, 200, 0, 0, 0);

g.beginGradientFill(GradientType.LINEAR, colors, alphas, ratios, matrix);
g.drawRect(0, 0, 200, 200);
g.endFill();
```

### Bitmap Fill
```actionscript
import flash.display.BitmapData;

var bmd:BitmapData = new BitmapData(100, 100, false, 0xFF0000);
var g:Graphics = shape.graphics;

g.beginBitmapFill(bmd);
g.drawRect(0, 0, 200, 200);
g.endFill();
```

## Working with Bitmaps

### BitmapData Operations
```actionscript
import flash.display.BitmapData;
import flash.geom.Rectangle;
import flash.geom.Point;

// Create bitmap data
var bmd:BitmapData = new BitmapData(256, 256, true, 0x00000000);

// Draw to bitmap
bmd.draw(sprite);  // Capture display object
bmd.fillRect(new Rectangle(0, 0, 100, 100), 0xFFFF0000);

// Pixel operations
var color:uint = bmd.getPixel(10, 10);
var color32:uint = bmd.getPixel32(10, 10);  // with alpha
bmd.setPixel(10, 10, 0xFF0000);
bmd.setPixel32(10, 10, 0xFF00FF00);

// Copy pixels
bmd.copyPixels(sourceBmd, new Rectangle(0, 0, 100, 100), new Point(50, 50));

// Clone
var copy:BitmapData = bmd.clone();

// Dispose (free memory)
bmd.dispose();
```

### Bitmap Filters
```actionscript
import flash.filters.*;

// Blur filter
var blur:BlurFilter = new BlurFilter(4, 4);
sprite.filters = [blur];

// Glow filter
var glow:GlowFilter = new GlowFilter(0xFF0000, 1, 10, 10);

// Drop shadow
var shadow:DropShadowFilter = new DropShadowFilter(5, 45, 0x000000, 0.5);

// Color matrix (tint, saturation, etc.)
var colorMatrix:ColorMatrixFilter = new ColorMatrixFilter([
    1, 0, 0, 0, 0,
    0, 1, 0, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 0, 1, 0
]);

// Apply multiple filters
sprite.filters = [blur, glow, shadow];
```

## Event Handling

### Mouse Events
```actionscript
import flash.events.MouseEvent;

sprite.addEventListener(MouseEvent.CLICK, onClick);
sprite.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
sprite.addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
sprite.addEventListener(MouseEvent.MOUSE_MOVE, onMouseMove);
sprite.addEventListener(MouseEvent.MOUSE_OVER, onMouseOver);
sprite.addEventListener(MouseEvent.MOUSE_OUT, onMouseOut);
sprite.addEventListener(MouseEvent.ROLL_OVER, onRollOver);
sprite.addEventListener(MouseEvent.ROLL_OUT, onRollOut);

function onClick(event:MouseEvent):void {
    trace("Clicked at:", event.localX, event.localY);
    trace("Stage coords:", event.stageX, event.stageY);
}

// Make sprite interactive
sprite.mouseEnabled = true;
sprite.mouseChildren = false;  // Ignore children for mouse events
```

### Touch Events
```actionscript
import flash.events.TouchEvent;

Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;

sprite.addEventListener(TouchEvent.TOUCH_BEGIN, onTouchBegin);
sprite.addEventListener(TouchEvent.TOUCH_MOVE, onTouchMove);
sprite.addEventListener(TouchEvent.TOUCH_END, onTouchEnd);

function onTouchBegin(event:TouchEvent):void {
    trace("Touch ID:", event.touchPointID);
    trace("Position:", event.localX, event.localY);
}
```

## Best Practices

### 1. Memory Management
```actionscript
// Remove from display list
if (sprite.parent != null) {
    sprite.parent.removeChild(sprite);
}

// Remove event listeners
sprite.removeEventListener(MouseEvent.CLICK, onClick);

// Dispose bitmaps
bitmapData.dispose();

// Clear graphics
graphics.clear();

// Nullify references
sprite = null;
```

### 2. Performance Optimization
```actionscript
// Cache as bitmap for static content
sprite.cacheAsBitmap = true;

// Use cacheAsBitmapMatrix for transformed caching
import flash.geom.Matrix;
sprite.cacheAsBitmapMatrix = new Matrix();

// Disable mouse events when not needed
sprite.mouseEnabled = false;
sprite.mouseChildren = false;

// Use Shape instead of Sprite for non-interactive graphics
var shape:Shape = new Shape();  // Lighter weight

// Batch graphics operations
var g:Graphics = shape.graphics;
g.clear();
g.beginFill(0xFF0000);
// ... draw multiple shapes
g.endFill();
```

### 3. Coordinate System
```actionscript
// Always use appropriate coordinate space
var pt:Point = sprite.localToGlobal(new Point(0, 0));

// Check bounds before positioning
var bounds:Rectangle = sprite.getBounds(stage);
if (bounds.right > stage.stageWidth) {
    sprite.x -= bounds.right - stage.stageWidth;
}
```

### 4. Layer Management
```actionscript
// Group related objects
var background:Sprite = new Sprite();
var content:Sprite = new Sprite();
var ui:Sprite = new Sprite();

stage.addChild(background);
stage.addChild(content);
stage.addChild(ui);

// Use containers for logical grouping
var enemiesContainer:Sprite = new Sprite();
var bulletsContainer:Sprite = new Sprite();
```

## Common Patterns

### Simple Button
```actionscript
function createButton(label:String):Sprite {
    var btn:Sprite = new Sprite();
    
    // Draw button
    btn.graphics.beginFill(0x0066CC);
    btn.graphics.drawRoundRect(0, 0, 100, 30, 5);
    btn.graphics.endFill();
    
    // Add label
    var tf:TextField = new TextField();
    tf.text = label;
    tf.width = 100;
    tf.height = 30;
    tf.selectable = false;
    btn.addChild(tf);
    
    // Make interactive
    btn.buttonMode = true;
    btn.mouseChildren = false;
    
    return btn;
}
```

### Drag and Drop
```actionscript
sprite.addEventListener(MouseEvent.MOUSE_DOWN, startDrag);

function startDrag(event:MouseEvent):void {
    var target:Sprite = event.currentTarget as Sprite;
    target.startDrag();
    
    stage.addEventListener(MouseEvent.MOUSE_UP, stopDrag);
}

function stopDrag(event:MouseEvent):void {
    var target:Sprite = event.currentTarget as Sprite;
    target.stopDrag();
    
    stage.removeEventListener(MouseEvent.MOUSE_UP, stopDrag);
}
```
