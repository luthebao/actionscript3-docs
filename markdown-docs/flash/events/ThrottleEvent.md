# Throttleevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class ThrottleEvent  
Inheritance| ThrottleEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.2   
---|---  
  
A ThrottleEvent is dispatched when the Flash Player throttles, pauses, or resumes content. There is only one type of ThrottleEvent event: `ThrottleEvent.THROTTLE`. 

This event is a broadcast event, which means that it is dispatched by all EventDispatcher objects with a listener registered for this event. For more information about broadcast events, see the DisplayObject class.

**Note:** This event has neither a "capture phase" nor a "bubble phase", which means that event listeners must be added directly to any potential targets, whether the target is on the display list or not.

The Flash Player can throttle the content to a low frame rate (meaning the frame rate is reduced to a value typically between 2 and 8 fps). Content can be throttled when its tab is hidden or minimized. On a mobile device, content can be throttled when the backlight goes off or screensaver mode comes on. Prior to throttling the content, a ThrottleEvent is dispatched with `ThrottleEvent.state=ThrottleType.THROTTLE`. The `ThrottleEvent.targetFrameRate` property contains the value of the new target frame rate. 

The content can run code in the event listener to prepare for the throttle. This is an opportunity to alert external content that the throttled content is much less responsive. For instance, an active `FileReference.upload()` or `FileReference.download()` method could be canceled. Or, if content is communicating using LocalConnection with another SWF, this is an opportunity to inform that SWF to expect less responsiveness. Note that the throttled content may not be able to complete asynchronous actions prior to entering the throttle. Content enters the throttled state when the event listener returns.

The Flash Player can pause content. For example, content can be paused when it is scrolled offscreen on a mobile device at a time when no audio or video is playing. Prior to pausing the content, a ThrottleEvent is dispatched with `ThrottleEvent.state=ThrottleType.PAUSE` and `ThrottleEvent.targetFrameRate=0`. Similar to when the content receives a `ThrottleType.THROTTLE` event, the content can run code in the event listener to prepare for the pause. When the event listener returns, the content enters the paused state. While paused, the content does not respond to user interaction, such as mouse clicks or keyboard entry. However, ActionScript network events can still be received.

When the Flash Player resumes the content from a throttled or paused state, a ThrottleEvent is dispatched with `ThrottleEvent.state=ThrottleType.RESUME`. `ThrottleEvent.targetFrameRate` describes the frame rate and is normally equal to `Stage.frameRate`. Content may be resumed when any part of the stage becomes visible or when the user makes a request for the content to be resumed.

The platforms that support throttling and pausing are currently the following: Flash Player Desktop Mac and Windows, AIR Mobile, and Flash Player Android. The following platforms do not dispatch the ThrottleEvent automatically because they do not yet support pausing or throttling: AIR for TV devices, AIR for desktop, and Flash Player Linux Desktop.

See also

[flash.display.DisplayObject](../display/DisplayObject.html)   
[flash.display.Stage](../display/Stage.html)   
[flash.events.ThrottleType](../events/ThrottleType.html)

  

* * *