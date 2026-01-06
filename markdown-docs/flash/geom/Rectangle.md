# Rectangle

Package| [flash.geom](package-detail.html)  
---|---  
Class| public class Rectangle  
Inheritance| Rectangle ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
A Rectangle object is an area defined by its position, as indicated by its top-left corner point (_x_ , _y_) and by its width and its height. 

The `x`, `y`, `width`, and `height` properties of the Rectangle class are independent of each other; changing the value of one property has no effect on the others. However, the `right` and `bottom` properties are integrally related to those four properties. For example, if you change the value of the `right` property, the value of the `width` property changes; if you change the `bottom` property, the value of the `height` property changes. 

The following methods and properties use Rectangle objects:

  * The `applyFilter()`, `colorTransform()`, `copyChannel()`, `copyPixels()`, `draw()`, `fillRect()`, `generateFilterRect()`, `getColorBoundsRect()`, `getPixels()`, `merge()`, `paletteMap()`, `pixelDisolve()`, `setPixels()`, and `threshold()` methods, and the `rect` property of the BitmapData class
  * The `getBounds()` and `getRect()` methods, and the `scrollRect` and `scale9Grid` properties of the DisplayObject class
  * The `getCharBoundaries()` method of the TextField class
  * The `pixelBounds` property of the Transform class
  * The `bounds` parameter for the `startDrag()` method of the Sprite class
  * The `printArea` parameter of the `addPage()` method of the PrintJob class

You can use the `new Rectangle()` constructor to create a Rectangle object.

**Note:** The Rectangle class does not define a rectangular Shape display object. To draw a rectangular Shape object onscreen, use the `drawRect()` method of the Graphics class.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.DisplayObject.scrollRect](../display/DisplayObject.html#scrollRect)   
[flash.display.BitmapData](../display/BitmapData.html)   
[flash.display.DisplayObject](../display/DisplayObject.html)   
[flash.display.NativeWindow](../display/NativeWindow.html)   
[flash.text.TextField.getCharBoundaries()](../text/TextField.html#getCharBoundaries\(\))   
[flash.geom.Transform.pixelBounds](../geom/Transform.html#pixelBounds)   
[flash.display.Sprite.startDrag()](../display/Sprite.html#startDrag\(\))   
[flash.printing.PrintJob.addPage()](../printing/PrintJob.html#addPage\(\))

  

* * *