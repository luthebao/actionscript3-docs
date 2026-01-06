# Devicerotation

Package| [flash.sensors](package-detail.html)  
---|---  
Class| public class DeviceRotation  
Inheritance| DeviceRotation ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 26.0   
---|---  
  
The DeviceRotation class dispatches events based on activity detected by the device's acceletometer, gyroscope sensors. This data represents the device's roll, pitch, yaw and quaternions. When the device rotates, the sensors detect this rotation and return this data. The DeviceRotation class provides methods to query whether or not Device rotation event handling is supported, and also to set the rate at which device rotation events are dispatched. 

**Note:** Use the `DeviceRotation.isSupported` property to test the runtime environment for the ability to use this feature. While the Device rotation class and its members are accessible for multiple runtime platforms and devices, this does not imply that the handler is always supported at the runtime. There are a few cases such as Android version etc where this handler is not supported, so you must check the support of this handler by using `DeviceRotation.isSupported` property. If `DeviceRotation.isSupported` is `true` at runtime, then DeviceRotation support currently exists.

_AIR profile support:_ This feature is supported only on mobile devices. It is not supported on desktop or AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles. 

See also

[isSupported](../sensors/DeviceRotation.html#isSupported)   
[flash.events.DeviceRotationEvent](../events/DeviceRotationEvent.html)

  

* * *