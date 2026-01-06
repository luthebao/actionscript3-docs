# Gameinputcontrol

Package| [flash.ui](package-detail.html)  
---|---  
Class| public dynamic class GameInputControl  
Inheritance| GameInputControl ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.7   
---|---  
  
The GameInputControl class represents a control on an input device. The GameInput API maps the physical controls on a device to simple logical controls. 

**Getting Control Values:**

The `value` property returns the current value of a control. This method does not return the latest value directly from the control. Instead it returns the value that was cached the last time the control was sampled. 

There are three ways to get control values from an individual control: 

  1. Polling: Call `value` whenever you want to get the last known value for a control. 
  2. Change Events: Register a change event for a controller. The `Event.CHANGE` event is dispatched whenever the value of a control changes. Upon receiving the event, call `value` to get the value for the control that fired the event. 
  3. Caching Sample Values: Caching is done at the device level. See the `GameInputDevice` class documentation for details on caching and retrieving sampled control values. 

Attempting to read control values from a disabled device causes `value` to throw an `IOError`. However, you can access properties describing a control ( `id`, `minValue` and `maxValue`) even if the device is not enabled. This feature makes it possible to determine if a device fits the needs of your application, without having to first enable the device. 

For more information, see the Adobe Air Developer Center article: [Game controllers on Adobe AIR](http://www.adobe.com/devnet/air/articles/game-controllers-on-air.html). 

For Android, this feature supports a minimum Android OS version of 4.1 and requires the minimum SWF version 20 and namespace 3.7. For iOS, this feature supports a minimum iOS version of 9.0 and requires the minimum SWF version 34 and namespace 23.0. 

See also

[flash.ui.GameInput](../ui/GameInput.html)   
[flash.ui.GameInputDevice](../ui/GameInputDevice.html)   
[flash.events.GameInputEvent](../events/GameInputEvent.html)

  

* * *