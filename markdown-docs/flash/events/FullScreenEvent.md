# Fullscreenevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class FullScreenEvent  
Inheritance| FullScreenEvent ![Inheritance](../../images/inherit-arrow.gif) [ActivityEvent](ActivityEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Stage object dispatches a FullScreenEvent object whenever the Stage enters or leaves full-screen display mode. There are two types of `fullScreen` events: `FullScreenEvent.FULL_SCREEN` and `FullScreenEvent.FULL_SCREEN_INTERACTIVE_ACCEPTED`. 

Note that when handling a `FullScreenEvent`, you must not try to change the full screen state i.e. `Stage.displayState` cannot be modified.

See also

[flash.display.Stage.displayState](../display/Stage.html#displayState)

  

* * *