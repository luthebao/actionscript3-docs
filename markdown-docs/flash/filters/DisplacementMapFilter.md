# Displacementmapfilter

Package| [flash.filters](package-detail.html)  
---|---  
Class| public final class DisplacementMapFilter  
Inheritance| DisplacementMapFilter ![Inheritance](../../images/inherit-arrow.gif) [BitmapFilter](BitmapFilter.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
The DisplacementMapFilter class uses the pixel values from the specified BitmapData object (called the _displacement map image_) to perform a displacement of an object. You can use this filter to apply a warped or mottled effect to any object that inherits from the DisplayObject class, such as MovieClip, SimpleButton, TextField, and Video objects, as well as to BitmapData objects. 

The use of filters depends on the object to which you apply the filter:

  * To apply filters to a display object, use the `filters` property of the display object. Setting the `filters` property of an object does not modify the object, and you can remove the filter by clearing the `filters` property. 
  * To apply filters to BitmapData objects, use the `BitmapData.applyFilter()` method. Calling `applyFilter()` on a BitmapData object takes the source BitmapData object and the filter object and generates a filtered image.

If you apply a filter to a display object, the value of the `cacheAsBitmap` property of the display object is set to `true`. If you clear all filters, the original value of `cacheAsBitmap` is restored.

The filter uses the following formula:
    
    
    dstPixel[x, y] = srcPixel[x + ((componentX(x, y) - 128) * scaleX) / 256, y + ((componentY(x, y) - 128) *scaleY) / 256)
    

where `componentX(x, y)` gets the `componentX` property color value from the `mapBitmap` property at `(x - mapPoint.x ,y - mapPoint.y)`.

The map image used by the filter is scaled to match the Stage scaling. It is not scaled when the object itself is scaled.

This filter supports Stage scaling. However, general scaling, rotation, and skewing are not supported. If the object itself is scaled (if the `scaleX` and `scaleY` properties are set to a value other than 1.0), the filter effect is not scaled. It is scaled only when the user zooms in on the Stage.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.BitmapData.applyFilter()](../display/BitmapData.html#applyFilter\(\))   
[flash.display.DisplayObject.filters](../display/DisplayObject.html#filters)   
[flash.display.DisplayObject.cacheAsBitmap](../display/DisplayObject.html#cacheAsBitmap)

  

* * *