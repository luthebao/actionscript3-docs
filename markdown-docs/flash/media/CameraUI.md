# Cameraui

Package| [flash.media](package-detail.html)  
---|---  
Class| public class CameraUI  
Inheritance| CameraUI ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.5   
---|---  
  
The CameraUI class allows you to capture a still image or video using the default camera application on a device. 

The `launch()` method requests that the device open the default camera application. The captured image or video is available in the MediaEvent object dispatched for the complete event. Since the default camera application can save the image or video in a variety of formats, there is no guarantee that returned media object can be loaded and displayed by the AIR runtime. 

On some platforms, the media object returned by the camera is accessible as a file-based media promise. On others, the media promise is not file-based and the `file` and `relativePath` properties of the MediaPromise object are `null`. Do not use these properties in code that is used on more than one platform.

On Android, the default camera application does not open if the external storage card is not available (such as when the user has mounted the card as a USB mass storage device). In addition, the AIR application that launches the camera loses focus. If the device runs low on resources, the AIR application can be terminated by the operating system before the media capture is complete.

On some platforms, the media object is automatically stored in the device media library. On platforms on which images and video are not automatically stored by the default camera application, you can use the CameraRoll `addBitmapData()` function to store the media object.

_AIR profile support:_ This feature is supported on mobile devices, but it is not supported on desktop operating systems or AIR for TV devices. You can test for support at run time using the `CameraUI.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

[View the examples.](#includeExamplesSummary)

See also

[Michael Chaize: Android, AIR, and the Camera](http://www.riagora.com/2010/07/android-air-and-the-camera/)

  

* * *