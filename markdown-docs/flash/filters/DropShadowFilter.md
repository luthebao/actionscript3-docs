# Dropshadowfilter

Package| [flash.filters](package-detail.html)  
---|---  
Class| public final class DropShadowFilter  
Inheritance| DropShadowFilter ![Inheritance](../../images/inherit-arrow.gif) [BitmapFilter](BitmapFilter.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
The DropShadowFilter class lets you add a drop shadow to display objects. The shadow algorithm is based on the same box filter that the blur filter uses. You have several options for the style of the drop shadow, including inner or outer shadow and knockout mode. You can apply the filter to any display object (that is, objects that inherit from the DisplayObject class), such as MovieClip, SimpleButton, TextField, and Video objects, as well as to BitmapData objects. 

The use of filters depends on the object to which you apply the filter:

  * To apply filters to display objects use the `filters` property (inherited from DisplayObject). Setting the `filters` property of an object does not modify the object, and you can remove the filter by clearing the `filters` property. 
  * To apply filters to BitmapData objects, use the `BitmapData.applyFilter()` method. Calling `applyFilter()` on a BitmapData object takes the source BitmapData object and the filter object and generates a filtered image as a result.

If you apply a filter to a display object, the value of the `cacheAsBitmap` property of the display object is set to `true`. If you clear all filters, the original value of `cacheAsBitmap` is restored.

This filter supports Stage scaling. However, it does not support general scaling, rotation, and skewing. If the object itself is scaled (if `scaleX` and `scaleY` are set to a value other than 1.0), the filter is not scaled. It is scaled only when the user zooms in on the Stage.

A filter is not applied if the resulting image exceeds the maximum dimensions. In AIR 1.5 and Flash Player 10, the maximum is 8,191 pixels in width or height, and the total number of pixels cannot exceed 16,777,215 pixels. (So, if an image is 8,191 pixels wide, it can only be 2,048 pixels high.) In Flash Player 9 and earlier and AIR 1.1 and earlier, the limitation is 2,880 pixels in height and 2,880 pixels in width. If, for example, you zoom in on a large movie clip with a filter applied, the filter is turned off if the resulting image exceeds the maximum dimensions.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.BitmapData.applyFilter()](../display/BitmapData.html#applyFilter\(\))   
[flash.display.DisplayObject.filters](../display/DisplayObject.html#filters)   
[flash.display.DisplayObject.cacheAsBitmap](../display/DisplayObject.html#cacheAsBitmap)

  

* * *