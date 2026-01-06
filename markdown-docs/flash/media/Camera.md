# Camera

Package| [flash.media](package-detail.html)  
---|---  
Class| public final class Camera  
Inheritance| Camera ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Use the Camera class to capture video from the client system or device camera. Use the Video class to monitor the video locally. Use the NetConnection and NetStream classes to transmit the video to Flash Media Server. Flash Media Server can send the video stream to other servers and broadcast it to other clients running Flash Player or AIR. 

A Camera instance captures video in landscape aspect ratio. On devices that can change the screen orientation, such as mobile phones, a Video object attached to the camera will only show upright video in a landscape-aspect orientation. Thus, mobile apps should use a landscape orientation when displaying video and should not auto-rotate.

On iOS, the video from the front camera is mirrored. On Android, it is not.

On mobile devices with an autofocus camera, autofocus is enabled automatically. If the camera does not support continuous autofocus, and many mobile device cameras do not, then the camera is focused when the Camera object is attached to a video stream and whenever the `setMode()` method is called. On desktop computers, autofocus behavior is dependent on the camera driver and settings.

In an AIR application on Android and iOS, the camera does not capture video while an AIR app is not the active, foreground application. In addition, streaming connections can be lost when the application is in the background. On iOS, the camera video cannot be displayed when an application uses the GPU rendering mode. The camera video can still be streamed to a server.

_AIR profile support:_ This feature is not supported on AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles. Note that for AIR for TV devices, `Camera.isSupported` is `true` but `Camera.getCamera()` always returns `null`. Camera access is not supported in mobile browsers.

For information about capturing audio, see the Microphone class. 

**Important:** The runtime displays a Privacy dialog box that lets the user choose whether to allow or deny access to the camera. Make sure your application window size is at least 215 x 138 pixels; this is the minimum size required to display the dialog box. 

To create or reference a Camera object, use the `getCamera()` method.

[View the examples.](#includeExamplesSummary)

See also

[flash.media.Microphone](../media/Microphone.html)   
[Cristophe Coenraets: Video Chat for Android in 30 Lines of Code](http://coenraets.org/blog/2010/07/video-chat-for-android-in-30-lines-of-code/)   
[Michael Chaize: Android, AIR, and the Camera](http://www.riagora.com/2010/07/android-air-and-the-camera/)

  

* * *