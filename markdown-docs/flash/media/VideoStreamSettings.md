# Videostreamsettings

Package| [flash.media](package-detail.html)  
---|---  
Class| public class VideoStreamSettings  
Inheritance| VideoStreamSettings ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [H264VideoStreamSettings](../media/H264VideoStreamSettings.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The VideoStreamSettings class enables specifying video compression settings for each NetStream. All parameters (resolution, frame rate, bandwidth, etc.) are gated by `Camera` capture parameters. You can use methods (`setMode()`, etc.) to specify desired encoder parameters and you can use the properties (`width`, etc.) to retrieve the actual compression parameters used. Properties will be validated once `Camera` is attached to `NetStream` object and compression has started. 

**Note** Current implementation does not support setting properties per `NetStream` and `Camera` parameters will be used instead for each publishing `NetStream`.

  

* * *