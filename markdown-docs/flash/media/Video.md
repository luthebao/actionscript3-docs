# Video

Package| [flash.media](package-detail.html)  
---|---  
Class| public class Video  
Inheritance| Video ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](../display/DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Video class displays live or recorded video in an application without embedding the video in your SWF file. This class creates a Video object that plays either of the following kinds of video: recorded video files stored on a server or locally, or live video captured by the user. A Video object is a display object on the application's display list and represents the visual space in which the video runs in a user interface. 

When used with Flash Media Server, the Video object allows you to send live video captured by a user to the server and then broadcast it from the server to other users. Using these features, you can develop media applications such as a simple video player, a video player with multipoint publishing from one server to another, or a video sharing application for a user community. 

Flash Player 9 and later supports publishing and playback of FLV files encoded with either the Sorenson Spark or On2 VP6 codec and also supports an alpha channel. The On2 VP6 video codec uses less bandwidth than older technologies and offers additional deblocking and deringing filters. See the flash.net.NetStream class for more information about video playback and supported formats.

Flash Player 9.0.115.0 and later supports mipmapping to optimize runtime rendering quality and performance. For video playback, Flash Player uses mipmapping optimization if you set the Video object's `smoothing` property to `true`. 

Beginning with AIR 25, a new tag has been introduced for Android in app.xml named `disableMediaCodec`. Setting this tag as `true` disables mediacodec and the video is decoded using OpenMax AL. Otherwise, mediacodec is enabled. The value of this tag is `false`, by default. 

As with other display objects on the display list, you can control various properties of Video objects. For example, you can move the Video object around on the Stage by using its `x` and `y` properties, you can change its size using its `height` and `width` properties, and so on. 

To play a video stream, use `attachCamera()` or `attachNetStream()` to attach the video to the Video object. Then, add the Video object to the display list using `addChild()`. 

If you are using Flash Professional, you can also place the Video object on the Stage rather than adding it with `addChild()`, like this: 

  1. If the Library panel isn't visible, select Window > Library to display it.
  2. Add an embedded Video object to the library by clicking the Options menu on the right side of the Library panel title bar and selecting New Video.
  3. In the Video Properties dialog box, name the embedded Video object for use in the library and click OK.
  4. Drag the Video object to the Stage and use the Property Inspector to give it a unique instance name, such as `my_video`. (Do not name it Video.)

In AIR applications on the desktop, playing video in fullscreen mode disables any power and screen saving features (when allowed by the operating system).

**Note:** The Video class is not a subclass of the InteractiveObject class, so it cannot dispatch mouse events. However, you can call the `addEventListener()` method on the display object container that contains the Video object. 

[View the examples.](#includeExamplesSummary)

See also

[attachCamera()](../media/Video.html#attachCamera\(\))   
[attachNetStream()](../media/Video.html#attachNetStream\(\))   
[flash.media.Camera.getCamera()](../media/Camera.html#getCamera\(\))   
[flash.net.NetConnection](../net/NetConnection.html)   
[flash.net.NetStream](../net/NetStream.html)   
[flash.display.DisplayObjectContainer.addChild()](../display/DisplayObjectContainer.html#addChild\(\))   
[flash.display.Stage.addChild()](../display/Stage.html#addChild\(\))   
[Working with Video](http://help.adobe.com/en_US/as3/dev/WS5b3ccc516d4fbf351e63e3d118a9b90204-7e1a.html)

  

* * *