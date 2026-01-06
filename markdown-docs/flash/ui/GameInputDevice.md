# Gameinputdevice

Package| [flash.ui](package-detail.html)  
---|---  
Class| public final class GameInputDevice  
Inheritance| GameInputDevice ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.7   
---|---  
  
The `GameInputDevice` class represents a single input device commonly used for gaming. 

This class includes methods and properties that you can use to: 

  * Enable or disable an input device. Devices are initially disabled by default (`enabled` set to `false`). You must explicitly enable a device, by setting `enabled` to `true`, before you can get control values from the device. 
  * Get the name and ID of an input device. The `name` and `id` properties together uniquely identify a device. For Android devices, the device manufacturer supplies these values. For iOS devices, the `id` may change each time you connect the device. 
  * Enumerate the controls on an input device. Physical controls on a device are mapped to logical `GameInputControl` objects and stored in a list. You access a control in the list with the `getControlAt()` method.
  * Manage caching of sampled control values. Sampling a set of control values directly from a device object is one of three ways to get control values. (The other two ways use the `value` method on the `GameInputControl` class, and are described there.) Sample caching is useful when you need to access control values at a faster rate than the frame rate of an application. 

Always set up a listener on this class for the `GameInputEvent.DEVICE_REMOVED` event. This listener lets you handle the case of a device being unexpectedly disconnected or powered off. When a device is disconnected, free its `GameInputDevice` object, as the object is no longer valid after its associated device is disconnected. 

An Android device that is removed and then reconnected retains the ID it had when it was first connected. You can logically reconnect to a device by matching its ID. For iOS devices, the ID may change when you reconnect the device. 

**Note:** You cannot rely on the order of devices in the list. (The order can change when devices are added and removed.) 

For more information, see the Adobe Air Developer Center article: [Game controllers on Adobe AIR](http://www.adobe.com/devnet/air/articles/game-controllers-on-air.html). 

For Android, this feature supports a minimum Android OS version of 4.1 and requires the minimum SWF version 20 and namespace 3.7. For iOS, this feature supports a minimum iOS version of 9.0 and requires the minimum SWF version 34 and namespace 23.0. 

See also

[flash.ui.GameInput](../ui/GameInput.html)   
[flash.ui.GameInputControl](../ui/GameInputControl.html)   
[flash.events.GameInputEvent](../events/GameInputEvent.html)

  

* * *