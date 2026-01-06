# Stagevideo

Package| [flash.media](package-detail.html)  
---|---  
Class| public class StageVideo  
Inheritance| StageVideo ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.5   
---|---  
  
The StageVideo object uses the device's hardware acceleration capabilities, if available, to display live or recorded video in an application. Hardware acceleration capabilities are available on most devices. See the flash.net.NetStream class for more information about supported formats. 

_AIR profile support:_ In AIR 3, all AIR for TV devices and some mobile devices support this feature. AIR 3 for iOS uses the StageVideo object for H.264 video with hardware decoding, with limited supported for NetStream functionality. AIR 3 for iOS also supports On2 and Sorenson codecs through the StageVideo object. This support does not use hardware decoding, and it does not limit NetStream functionality. In AIR 2.5, only AIR for TV devices support this feature. Furthermore, ActionScript for this feature in AIR 2.5 for TV is different than the ActionScript for AIR 3 or Flash Player 10.2. The differences are noted in the ActionScript descriptions. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles. The StageVideo class is not supported in the AIR desktop or extendedDesktop profiles. 

The video displayed by the StageVideo object always appears in a rectangular area on the stage behind all Flash display list objects. Therefore, the StageVideo object takes advantage of hardware acceleration while supporting the most common case for displaying video: a rectangular display area overlaid with video controls.

The benefits to using a StageVideo object instead of the Video object are:

  * Improved video display performance because of using hardware acceleration.
  * Decreased CPU usage.
  * Flexibility and creativity for development of content, such as video controls, that appears in front of the StageVideo object.

Because the device's hardware displays the video, a StageVideo object is subject to the following constraints compared to a Video object:

  * For each SWF file, Flash Player limits the number of StageVideo objects that can concurrently display videos to four. However, the actual limit can be lower, depending on device hardware resources. On AIR for TV devices, only one StageVideo object at a time can display a video.
  * The video timing is not synchronized with the timing of Flash content that the runtime displays.
  * The video display area can only be a rectangle. You cannot use more advanced display areas, such as elliptical or irregular shapes.
  * You cannot rotate the video.
  * You cannot bitmap cache the video or use BitmapData to access it.
  * You cannot apply filters to the video.
  * You cannot apply color transforms to the video.
  * You cannot apply an alpha value to the video.
  * Blend modes that you apply to display objects that are in front of the video do not apply to the video.
  * You can place the video only on full pixel boundaries.
  * Though the rendering is the best available for the given device hardware, it is not 100% "pixel identical" across devices. Slight variations occur due to driver and platform differences.
  * A few devices do not support all required color spaces. For example, some devices do not support BT.709, the H.264 standard. In such cases you can use BT.601 for fast display.
  * You cannot use stage video with WMODE settings such as `normal`, `opaque`, or `transparent`. Stage video supports only `WMODE=direct` when not in full screen mode. WMODE has no effect in Safari 4 or higher, IE 9 or higher, or in AIR for TV.
  * When using StageVideo in an AIR for Android application, set the `colorDepth` to _32bit_ in the application descriptor. Using StageVideo with a 16-bit color depth is not supported. 
  * On Android, StageVideo is only supported on devices running Android 3 (Honeycomb) and higher. To enable your app to run on the widest possible selection of Android devices, always provide logic to display video using the Video object when StageVideo is not available.

The following steps summarize how to use a StageVideo object to play a video:

  1. Listen for the StageVideoAvailabilityEvent.STAGE_VIDEO_AVAILABILITY event to find out when the Stage.stageVideos vector has changed. (Not supported for AIR 2.5 for TV.) 
  2. If the StageVideoAvailabilityEvent.STAGE_VIDEO_AVAILABILITY event reports that stage video is available, use the `Stage.stageVideos` Vector object within the event handler to access a StageVideo object. In AIR 2.5 for TV, access `Stage.stageVideos` after the first SWF frame has rendered. **Note** You cannot create a StageVideo object.
  3. Attach a NetStream object using `StageVideo.attachNetStream()`.
  4. Play the video using `NetStream.play()`.
  5. Listen for the `StageVideoEvent.RENDER_STATE` event on the StageVideo object to determine the status of playing the video. Receipt of this event also indicates that the width and height properties of the video have been initialized or changed. 
  6. Listen for the `VideoEvent.RENDER_STATE` event on the Video object. This event provides the same statuses as StageVideoEvent.RENDER_STATE, so you can also use it to determine whether GPU acceleration is available. Receipt of this event also indicates that the width and height properties of the video have been initialized or changed. (Not supported for AIR 2.5 for TV.)

If a `StageVideoEvent.RENDER_STATE` event indicates that the video cannot be played, you can revert to using a Video object instead of a StageVideo object. This event is dispatched after the video has been attached to a NetStream object and is playing. Also, depending on the platform, any change in the playing status can result in dispatching the event. Handle the `StageVideoEvent.RENDER_STATE` event to ensure that the application plays the video or gracefully does not play the video. 

If a running video goes into full screen mode from a WMODE that does not support stage video, stage video can become available. Likewise, if the user exits full screen mode, stage video can become unavailable. In these cases, the Stage.stageVideos vector changes. To receive notification of this change, listen to the StageVideoAvailabilityEvent.STAGE_VIDEO_AVAILABITY event. **NOTE:** This notification is not available in AIR 2.5 for TV.

See also

[flash.events.StageVideoEvent](../events/StageVideoEvent.html)   
[flash.events.StageVideoAvailabilityEvent](../events/StageVideoAvailabilityEvent.html)   
[flash.events.VideoEvent](../events/VideoEvent.html)   
[flash.display.Stage.stageVideos](../display/Stage.html#stageVideos)   
[flash.media.Video](../media/Video.html)   
[flash.net.NetStream](../net/NetStream.html)   
[Using the StageVideo class for hardware-accelerated rendering](http://www.adobe.com/go/learn_as3_stageVideo_en)

  

* * *