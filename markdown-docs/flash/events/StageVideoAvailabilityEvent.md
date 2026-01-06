# Stagevideoavailabilityevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class StageVideoAvailabilityEvent  
Inheritance| StageVideoAvailabilityEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
This event fires when the state of the `Stage.stageVideos` property changes. This property can change when a user expands a video to full screen display from a `wmode` that does not support StageVideo (for example, `wmode=normal`, `wmode=opaque`, or `wmode=transparent`). Expanding to full screen can cause the `Stage.stageVideos` vector to become populated. Conversely, exiting full screen display can cause the `Stage.stageVideos` vector to become empty.

**NOTE:** This notification occurs only when the state of the `Stage.stageVideos` property changes. As a result, behavior may vary according to platform and browser. On Windows, for example, the `stageVideoAvailability` event is not dispatched when you go into full screen mode while `wmode` is set to `direct`. On some other platforms, however, the same behavior causes Flash Player to reallocate resources. In those cases, the `Stage.stageVideos` property state changes, and the event fires. You can detect changes to full screen mode by listening to the `flash.events.FullScreenEvent` event. This event is dispatched by the Stage object.

See also

[flash.events.StageVideoEvent](../events/StageVideoEvent.html)   
[flash.media.StageVideoAvailability](../media/StageVideoAvailability.html)   
[flash.events.VideoEvent](../events/VideoEvent.html)   
[flash.events.FullScreenEvent](../events/FullScreenEvent.html)   
[flash.display.Stage.stageVideos](../display/Stage.html#stageVideos)   
[flash.events.FullScreenEvent](../events/FullScreenEvent.html)   
[flash.media.Video](../media/Video.html)   
[flash.net.NetStream](../net/NetStream.html)   
[Working with Video](http://help.adobe.com/en_US/as3/dev/WS5b3ccc516d4fbf351e63e3d118a9b90204-7e1a.html)

  

* * *