# Touchevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class TouchEvent  
Inheritance| TouchEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The TouchEvent class lets you handle events on devices that detect user contact with the device (such as a finger on a touch screen). 

When a user interacts with a device such as a mobile phone or tablet with a touch screen, the user typically touches the screen with his or her fingers or a pointing device. You can develop applications that respond to basic touch events (such as a single finger tap) with the TouchEvent class. Create event listeners using the event types defined in this class. For user interaction with multiple points of contact (such as several fingers moving across a touch screen at the same time) use the related GestureEvent, PressAndTapGestureEvent, and TransformGestureEvent classes. And, use the properties and methods of these classes to construct event handlers that respond to the user touching the device.

Use the Multitouch class to determine the current environment's support for touch interaction, and to manage the support of touch interaction if the current environment supports it.

**Note:** When objects are nested on the display list, touch events target the deepest possible nested object that is visible in the display list. This object is called the target node. To have a target node's ancestor (an object containing the target node in the display list) receive notification of a touch event, use `EventDispatcher.addEventListener()` on the ancestor node with the type parameter set to the specific touch event you want to detect.

In AIR 3, and above, you can listen for proximity events on supported Android devices that have an active stylus. On such devices, `proximityMove` and `touchMove` event objects provide a byte array containing path and pressure samples taken since the previous move event. You can use these samples to construct the path of the stylus between touch events. (Note that hit-testing for interaction of the stylus input with the display list only occurs at the end of a path segment.)

[View the examples.](#includeExamplesSummary)

See also

[flash.ui.Multitouch](../ui/Multitouch.html)   
[flash.events.GestureEvent](../events/GestureEvent.html)   
[flash.events.TransformGestureEvent](../events/TransformGestureEvent.html)   
[flash.events.PressAndTapGestureEvent](../events/PressAndTapGestureEvent.html)   
[flash.events.MouseEvent](../events/MouseEvent.html)   
[flash.events.EventDispatcher.addEventListener()](../events/EventDispatcher.html#addEventListener\(\))

  

* * *