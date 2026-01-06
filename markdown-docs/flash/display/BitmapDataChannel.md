# Bitmapdatachannel

Package| [flash.display](package-detail.html)  
---|---  
Class| public final class BitmapDataChannel  
Inheritance| BitmapDataChannel ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The BitmapDataChannel class is an enumeration of constant values that indicate which channel to use: red, blue, green, or alpha transparency. 

When you call some methods, you can use the bitwise OR operator (`|`) to combine BitmapDataChannel constants to indicate multiple color channels.

The BitmapDataChannel constants are provided for use as values in the following:

  * The `sourceChannel` and `destChannel` parameters of the `flash.display.BitmapData.copyChannel()` method
  * The `channelOptions` parameter of the `flash.display.BitmapData.noise()` method
  * The `flash.filters.DisplacementMapFilter.componentX` and `flash.filters.DisplacementMapFilter.componentY` properties

See also

[flash.display.BitmapData.copyChannel()](../display/BitmapData.html#copyChannel\(\))   
[flash.display.BitmapData.noise()](../display/BitmapData.html#noise\(\))   
[flash.filters.DisplacementMapFilter.componentX](../filters/DisplacementMapFilter.html#componentX)   
[flash.filters.DisplacementMapFilter.componentY](../filters/DisplacementMapFilter.html#componentY)

  

* * *