# Cameraroll

Package| [flash.media](package-detail.html)  
---|---  
Class| public class CameraRoll  
Inheritance| CameraRoll ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 2  
---|---  
  
The CameraRoll class allows you to access image data in the system media library or "camera roll." 

_AIR profile support:_ This feature is supported on mobile devices, but it is not supported on desktop operating systems or AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

The `CameraRoll.addBitmapData()` method adds an image to the device's dedicated media library. To check at run time whether your application supports the `CameraRoll.addBitmapData()` method, check the `CameraRoll.supportsAddBitmapData` property.

The `CameraRoll.browseForImage()` method opens an image-choosing dialog that allows a user to choose an image in the media library. When the user selects an image, the CameraRoll object dispatches a `select` event. Use the MediaEvent object dispatched for this event to access the chosen image. To check at run time whether your application supports the `CameraRoll.browseForImage()` method, check the `CameraRoll.supportsBrowseForImage` property.

  

* * *