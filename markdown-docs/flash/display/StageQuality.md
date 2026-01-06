# Stagequality

Package| [flash.display](package-detail.html)  
---|---  
Class| public final class StageQuality  
Inheritance| StageQuality ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
The StageQuality class provides values for the `Stage.quality` property and for the value of the `quality` parameter to the `BitmapData.drawWithQuality()` method. 

Higher quality settings produce better rendering of scaled bitmaps. However, higher quality settings are computationally more expensive. In particular, when rendering scaled video, using higher quality settings can reduce the frame rate.

In the desktop profile of Adobe AIR, `quality` can be set to `StageQuality.BEST` or `StageQuality.HIGH` (and the default value is `StageQuality.HIGH`). Attempting to set it to another value has no effect (and the property remains unchanged). In the moble profile of AIR, all four quality settings are available. The default value on mobile devices is `StageQuality.MEDIUM`.

For content running in Adobe AIR, setting the `quality` property of one Stage object changes the rendering quality for all Stage objects (used by different NativeWindow objects). 

**_Note:_** The operating system draws the device fonts, which are therefore unaffected by the `quality` property.

See also

[flash.display.Stage.quality](../display/Stage.html#quality)   
[flash.display.BitmapData.drawWithQuality()](../display/BitmapData.html#drawWithQuality\(\))

  

* * *