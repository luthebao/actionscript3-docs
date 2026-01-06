# Gestureevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class GestureEvent  
Inheritance| GestureEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [PressAndTapGestureEvent](../events/PressAndTapGestureEvent.html), [TransformGestureEvent](../events/TransformGestureEvent.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The GestureEvent class lets you handle multi-touch events on devices that detect complex user contact with the device (such as pressing two fingers on a touch screen at the same time). When a user interacts with a device such as a mobile phone or tablet with a touch screen, the user typically touches and moves across the screen with his or her fingers or a pointing device. You can develop applications that respond to this user interaction with the GestureEvent and TransformGestureEvent classes. Create event listeners using the event types defined here, or in the related TouchEvent and TransformGestureEvent classes. And, use the properties and methods of these classes to construct event handlers that respond to the user touching the device. 

Use the Multitouch class to determine the current environment's support for touch interaction, and to manage the support of touch interaction if the current environment supports it.

**Note:** When objects are nested on the display list, touch events target the deepest possible nested object that is visible in the display list. This object is called the target node. To have a target node's ancestor (an object containing the target node in the display list) receive notification of a touch event, use `EventDispatcher.addEventListener()` on the ancestor node with the type parameter set to the specific touch event you want to detect.

[View the examples.](#includeExamplesSummary)

See also

[flash.ui.Multitouch](../ui/Multitouch.html)   
[flash.events.TouchEvent](../events/TouchEvent.html)   
[flash.events.TransformGestureEvent](../events/TransformGestureEvent.html)   
[flash.events.PressAndTapGestureEvent](../events/PressAndTapGestureEvent.html)   
[flash.events.MouseEvent](../events/MouseEvent.html)   
[flash.events.EventDispatcher.addEventListener()](../events/EventDispatcher.html#addEventListener\(\))

  

* * *