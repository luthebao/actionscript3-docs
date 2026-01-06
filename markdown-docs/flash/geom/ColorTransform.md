# Colortransform

Package| [flash.geom](package-detail.html)  
---|---  
Class| public class ColorTransform  
Inheritance| ColorTransform ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The ColorTransform class lets you adjust the color values in a display object. The color adjustment or _color transformation_ can be applied to all four channels: red, green, blue, and alpha transparency. 

When a ColorTransform object is applied to a display object, a new value for each color channel is calculated like this:

  * New red value = (old red value * `redMultiplier`) + `redOffset`
  * New green value = (old green value * `greenMultiplier`) + `greenOffset`
  * New blue value = (old blue value * `blueMultiplier`) + `blueOffset`
  * New alpha value = (old alpha value * `alphaMultiplier`) + `alphaOffset`

If any of the color channel values is greater than 255 after the calculation, it is set to 255. If it is less than 0, it is set to 0.

You can use ColorTransform objects in the following ways:

  * In the `colorTransform` parameter of the `colorTransform()` method of the BitmapData class
  * As the `colorTransform` property of a Transform object (which can be used as the `transform` property of a display object)

You must use the `new ColorTransform()` constructor to create a ColorTransform object before you can call the methods of the ColorTransform object.

Color transformations do not apply to the background color of a movie clip (such as a loaded SWF object). They apply only to graphics and symbols that are attached to the movie clip.

[View the examples.](#includeExamplesSummary)

See also

[flash.geom.Transform](../geom/Transform.html)   
[flash.display.DisplayObject.transform](../display/DisplayObject.html#transform)   
[flash.display.BitmapData.colorTransform()](../display/BitmapData.html#colorTransform\(\))

  

* * *