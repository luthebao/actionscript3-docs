# Stageorientationevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class StageOrientationEvent  
Inheritance| StageOrientationEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
A Stage object dispatches a StageOrientationEvent object when the orientation of the stage changes. This can occur when the device is rotated, when the user opens a slide-out keyboard, or when the `setAspectRatio()` method of the Stage is called. 

There are two types of StageOrientationEvent event: The `orientationChanging` (`StageOrientationEvent.ORIENTATION_CHANGING`), is dispatched before the screen changes to a new orientation. Calling the `preventDefault()` method of the event object dispatched for orientationChanging prevents the stage from changing orientation. The `orientationChange` (`StageOrientationEvent.ORIENTATION_CHANGE`), is dispatched after the screen changes to a new orientation.

**Note:** If the `autoOrients` property is `false`, then the stage orientation does not change when a device is rotated. Thus, StageOrientationEvents are only dispatched for device rotation when `autoOrients` is `true`.

See also

[Stage.deviceOrientation](../display/Stage.html#deviceOrientation)   
[Stage.autoOrients](../display/Stage.html#autoOrients)

  

* * *