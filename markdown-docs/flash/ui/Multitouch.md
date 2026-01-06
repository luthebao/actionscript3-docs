# Multitouch

Package| [flash.ui](package-detail.html)  
---|---  
Class| public final class Multitouch  
Inheritance| Multitouch ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The Multitouch class manages and provides information about the current environment's support for handling contact from user input devices, including contact that has two or more touch points (such as a user's fingers on a touch screen). When a user interacts with a device such as a mobile phone or tablet with a touch screen, the user typically touches the screen with his or her fingers or a pointing device. While there is a broad range of pointing devices, such as a mouse or a stylus, many of these devices only have a single point of contact with an application. For pointing devices with a single point of contact, user interaction events can be handled as a mouse event, or using a basic set of touch events (called "touch point" events). However, for pointing devices that have several points of contact and perform complex movement, such as the human hand, Flash runtimes support an additional set of event handling API called gesture events. The API for handling user interaction with these gesture events includes the following classes: 

  * flash.events.TouchEvent
  * flash.events.GestureEvent
  * flash.events.GesturePhase
  * flash.events.TransformGestureEvent
  * flash.events.PressAndTapGestureEvent

Use the listed classes to write code that handles touch events. Use the Multitouch class to determine the current environment's support for touch interaction, and to manage the support of touch interaction if the current environment supports touch input.

You cannot create a Multitouch object directly from ActionScript code. If you call `new Multitouch()`, an exception is thrown.

**Note:** The Multitouch feature is not supported for SWF files embedded in HTML running on Mac OS.

[View the examples.](#includeExamplesSummary)

See also

[flash.events.TouchEvent](../events/TouchEvent.html)   
[flash.events.GestureEvent](../events/GestureEvent.html)   
[flash.events.TransformGestureEvent](../events/TransformGestureEvent.html)   
[flash.events.GesturePhase](../events/GesturePhase.html)   
[flash.events.PressAndTapGestureEvent](../events/PressAndTapGestureEvent.html)   
[flash.events.MouseEvent](../events/MouseEvent.html)   
[flash.events.EventDispatcher.addEventListener()](../events/EventDispatcher.html#addEventListener\(\))   
[Michael Chaize: Tetris, Touch API and Android](http://www.riagora.com/2010/05/tetris-touch-api-and-android/)   
[Christian Cantrell: Multitouch and gesture support on the Flash Platform](http://www.adobe.com/devnet/flash/articles/multitouch_gestures.html)   
[Lee Brimelow: Flash Player 10.1 multi-touch FAQ](http://blog.theflashblog.com/?p=1678)   
[Piotr Walczyszyn: Multitouch development in Flex](http://my.adobe.acrobat.com/p84912063/?launcher=false&fcsContent=true&pbMode=normal)

  

* * *