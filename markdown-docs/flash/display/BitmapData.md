# Bitmapdata

Package| [flash.display](package-detail.html)  
---|---  
Class| public class BitmapData  
Inheritance| BitmapData ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IBitmapDrawable](IBitmapDrawable.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The BitmapData class lets you work with the data (pixels) of a Bitmap object bitmap image. You can use the methods of the BitmapData class to create arbitrarily sized transparent or opaque bitmap images and manipulate them in various ways at runtime. You can also access the BitmapData for a bitmap image that you load with the `flash.display.Loader` class.

This class lets you separate bitmap rendering operations from the internal display updating routines of Flash Player. By manipulating a BitmapData object directly, you can create complex images without incurring the per-frame overhead of constantly redrawing the content from vector data.

The methods of the BitmapData class support effects that are not available through the filters available to non-bitmap display objects.

A BitmapData object contains an array of pixel data. This data can represent either a fully opaque bitmap or a transparent bitmap that contains alpha channel data. Either type of BitmapData object is stored as a buffer of 32-bit integers. Each 32-bit integer determines the properties of a single pixel in the bitmap.

Each 32-bit integer is a combination of four 8-bit channel values (from 0 to 255) that describe the alpha transparency and the red, green, and blue (ARGB) values of the pixel. (For ARGB values, the most significant byte represents the alpha channel value, followed by red, green, and blue.)

The four channels (alpha, red, green, and blue) are represented as numbers when you use them with the `BitmapData.copyChannel()` method or the `DisplacementMapFilter.componentX` and `DisplacementMapFilter.componentY` properties, and these numbers are represented by the following constants in the BitmapDataChannel class:

  * `BitmapDataChannel.ALPHA`
  * `BitmapDataChannel.RED`
  * `BitmapDataChannel.GREEN`
  * `BitmapDataChannel.BLUE`

You can attach BitmapData objects to a Bitmap object by using the `bitmapData` property of the Bitmap object.

You can use a BitmapData object to fill a Graphics object by using the `Graphics.beginBitmapFill()` method.

In the AIR runtime, the DockIcon, Icon, InteractiveIcon, and SystemTrayIcon classes each include a `bitmaps` property that is an array of BitmapData objects that define the bitmap images for an icon.

In AIR 1.5 and Flash Player 10, the maximum size for a BitmapData object is 8,191 pixels in width or height, and the total number of pixels cannot exceed 16,777,215 pixels. (So, if a BitmapData object is 8,191 pixels wide, it can only be 2,048 pixels high.) In Flash Player 9 and earlier and AIR 1.1 and earlier, the limitation is 2,880 pixels in height and 2,880 in width.

Starting with AIR 3 and Flash player 11, the size limits for a BitmapData object have been removed. The maximum size of a bitmap is now dependent on the operating system.

Calls to any method or property of a BitmapData object throw an ArgumentError error if the BitmapData object is invalid (for example, if it has `height == 0` and `width == 0`) or it has been disposed of via dispose(). 

[View the examples.](#includeExamplesSummary)

See also

[flash.display.Bitmap.bitmapData](../display/Bitmap.html#bitmapData)   
[flash.desktop.DockIcon.bitmaps](../desktop/DockIcon.html#bitmaps)   
[flash.display.Graphics.beginBitmapFill()](../display/Graphics.html#beginBitmapFill\(\))   
[flash.desktop.Icon.bitmaps](../desktop/Icon.html#bitmaps)   
[flash.desktop.InteractiveIcon.bitmaps](../desktop/InteractiveIcon.html#bitmaps)   
[flash.display.Loader](../display/Loader.html)   
[flash.desktop.SystemTrayIcon.bitmaps](../desktop/SystemTrayIcon.html#bitmaps)

  

* * *