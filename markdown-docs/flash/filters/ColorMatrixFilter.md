# Colormatrixfilter

Package| [flash.filters](package-detail.html)  
---|---  
Class| public final class ColorMatrixFilter  
Inheritance| ColorMatrixFilter ![Inheritance](../../images/inherit-arrow.gif) [BitmapFilter](BitmapFilter.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
The ColorMatrixFilter class lets you apply a 4 x 5 matrix transformation on the RGBA color and alpha values of every pixel in the input image to produce a result with a new set of RGBA color and alpha values. It allows saturation changes, hue rotation, luminance to alpha, and various other effects. You can apply the filter to any display object (that is, objects that inherit from the DisplayObject class), such as MovieClip, SimpleButton, TextField, and Video objects, as well as to BitmapData objects. 

**Note:** For RGBA values, the most significant byte represents the red channel value, followed by green, blue, and then alpha.

To create a new color matrix filter, use the syntax `new ColorMatrixFilter()`. The use of filters depends on the object to which you apply the filter:

  * To apply filters to movie clips, text fields, buttons, and video, use the `filters` property (inherited from DisplayObject). Setting the `filters` property of an object does not modify the object, and you can remove the filter by clearing the `filters` property. 
  * To apply filters to BitmapData objects, use the `BitmapData.applyFilter()` method. Calling `applyFilter()` on a BitmapData object takes the source BitmapData object and the filter object and generates a filtered image as a result.

If you apply a filter to a display object, the `cacheAsBitmap` property of the display object is set to `true`. If you remove all filters, the original value of `cacheAsBitmap` is restored.

A filter is not applied if the resulting image exceeds the maximum dimensions. In AIR 1.5 and Flash Player 10, the maximum is 8,191 pixels in width or height, and the total number of pixels cannot exceed 16,777,215 pixels. (So, if an image is 8,191 pixels wide, it can only be 2,048 pixels high.) In Flash Player 9 and earlier and AIR 1.1 and earlier, the limitation is 2,880 pixels in height and 2,880 pixels in width. For example, if you zoom in on a large movie clip with a filter applied, the filter is turned off if the resulting image reaches the maximum dimensions.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.BitmapData.getPixel()](../display/BitmapData.html#getPixel\(\))   
[flash.display.BitmapData.applyFilter()](../display/BitmapData.html#applyFilter\(\))   
[flash.display.DisplayObject.filters](../display/DisplayObject.html#filters)   
[flash.display.DisplayObject.cacheAsBitmap](../display/DisplayObject.html#cacheAsBitmap)

  

* * *