# Mediapromise

Package| [flash.media](package-detail.html)  
---|---  
Class| public class MediaPromise  
Inheritance| MediaPromise ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IFilePromise](../desktop/IFilePromise.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.5   
---|---  
  
The MediaPromise class represents the promise to deliver a media object. 

The `data` property of a MediaEvent object is a MediaPromise instance. You can use the MediaPromise methods to access the promised media object. Supported media formats include still images and video.

You cannot create a MediaPromise object. Calling `new MediaPromise()` generates a run-time error.

See also

[MediaEvent](../events/MediaEvent.html)   
[IFilePromise](../desktop/IFilePromise.html)   
[Loader.LoadFilePromise()](../display/Loader.html#loadFilePromise\(\))   
[IDataInput](../utils/IDataInput.html)   
[CameraRoll.browseForImage()](../media/CameraRoll.html#browseForImage\(\))   
[CameraUI](../media/CameraUI.html)

  

* * *