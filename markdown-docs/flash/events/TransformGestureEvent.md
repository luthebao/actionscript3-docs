# Transformgestureevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class TransformGestureEvent  
Inheritance| TransformGestureEvent ![Inheritance](../../images/inherit-arrow.gif) [GestureEvent](GestureEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The TransformGestureEvent class lets you handle complex movement input events (such as moving fingers across a touch screen) that the device or operating system interprets as a gesture. A gesture can have one or more touch points. When a user interacts with a device such as a mobile phone or tablet with a touch screen, the user typically touches and moves across the screen with his or her fingers or a pointing device. You can develop applications that respond to this user interaction with the GestureEvent, PressAndTapGestureEvent, and TransformGestureEvent classes. Create event listeners using the event types defined here, or in the related GestureEvent and TouchEvent classes. And, use the properties and methods of these classes to construct event handlers that respond to the user touching the device. 

A device or operating system interprets gesture input. So, different devices or operating systems have different requirements for individual gesture types. A swipe on one device might require different input movement than a swipe on another device. Refer to the hardware or operating system documentation to discover how the device or operating system interprets contact as a specific gesture.

Use the Multitouch class to determine the current environment's support for touch interaction, and to manage the support of touch interaction if the current environment supports it.

**Note:** When objects are nested on the display list, touch events target the deepest possible nested object that is visible in the display list. This object is called the target node. To have a target node's ancestor (an object containing the target node in the display list) receive notification of a touch event, use `EventDispatcher.addEventListener()` on the ancestor node with the type parameter set to the specific touch event you want to detect.

While the user is in contact with the device, the TransformGestureEvent object's scale, rotation, and offset properties are incremental values from the previous gesture event. For example, as a gesture increases the size of a display object, the scale values might go in sequence `1.03`, `1.01`, `1.01`, `1.02` indicating the display object scaled 1.0717 times its original size by the end of the gesture.

For TransformGestureEvent objects, properties not modified by the current gesture are set to identity values. For example, a pan gesture does not have a rotation or scale transformation, so the `rotation` value of the event object is `0`, the `scaleX` and `scaleY` properties are `1`.

[View the examples.](#includeExamplesSummary)

See also

[flash.ui.Multitouch](../ui/Multitouch.html)   
[flash.events.TouchEvent](../events/TouchEvent.html)   
[flash.events.GestureEvent](../events/GestureEvent.html)   
[flash.events.PressAndTapGestureEvent](../events/PressAndTapGestureEvent.html)   
[flash.events.MouseEvent](../events/MouseEvent.html)   
[flash.events.EventDispatcher.addEventListener()](../events/EventDispatcher.html#addEventListener\(\))

  

* * *