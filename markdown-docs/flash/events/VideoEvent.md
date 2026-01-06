# Videoevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class VideoEvent  
Inheritance| VideoEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
This event class reports the current video rendering status. Use this event for the following purposes:

  * To find out when size of the Video display changes or is initialized. Use this event instead of polling for size changes. When you receive this event you can access `Video.videoSize` and `Video.videoHeight` to get the pixel dimensions of the video that is currently playing.
  * To find out whether the video is decoded by software or the GPU. If the `status` property returns "accelerated", you should switch to using the StageVideo class, if possible. 

See also

[flash.events.StageVideoEvent](../events/StageVideoEvent.html)   
[flash.events.StageVideoAvailabilityEvent](../events/StageVideoAvailabilityEvent.html)   
[flash.display.Stage.stageVideos](../display/Stage.html#stageVideos)   
[flash.media.Video](../media/Video.html)   
[flash.net.NetStream](../net/NetStream.html)   
[Working with Video](http://help.adobe.com/en_US/as3/dev/WS5b3ccc516d4fbf351e63e3d118a9b90204-7e1a.html)

  

* * *