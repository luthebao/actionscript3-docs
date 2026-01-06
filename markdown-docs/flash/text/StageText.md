# Stagetext

Package| [flash.text](package-detail.html)  
---|---  
Class| public final class StageText  
Inheritance| StageText ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The StageText class is used to present the user with a native text input field. 

This class enables mobile applications to gather user input using native text input controls on mobile devices. Input controls on mobile devices often have extensive user interfaces and supporting behaviors that don't exist on the desktop. For example, many mobile devices support text input features like the following:

  * auto-complete
  * auto-correct
  * touch-based text selection
  * customizable soft keyboards

The underlying operating system (or a component library bundled with the operating system) draws native text input fields. Native text input fields provide an experience that is familiar to anyone who has used other applications on the same device. However, because the operating system draws the text input fields instead of the player, _you cannot use embedded fonts_.

_AIR profile support:_ This feature is supported on iOS and Android platforms. StageText uses native text input fields on Android and iOS mobile devices. On other platforms, StageText uses the Flash Runtime TextField.

When native inputs are used, StageText objects are not display objects and you cannot add them to the Flash display list. Instead, you display a StageText object by attaching it directly to a stage using the `stage` property. The StageText instance attached to a stage is displayed on top of any Flash display objects. You control the size and position of the rendering area with the `viewPort` property. There is no way to control depth ordering of different StageText objects. Overlapping two instances is not recommended.

When a StageText object has focus, it has the first opportunity to handle keyboard input. The stage to which the StageText object is attached does not dispatch any keyboard input events.

Because the StageText class wraps a different native control on every platform, its features are supported to varying degrees by each platform. Where features are supported, they may behave differently between platforms. When you attempt to use a particular feature on a particular platform, it is best to test the behavior. Only on desktop platforms where native controls are not used is StageText behavior similar to Flash Runtime text behavior.

StageText on Apple TV takes focus by default. To manage focus between different objects in your application keep a note of below points:

  * To override default focus from StageText, or to assign focus to any other display object use stage.focus
  * To assign focus to StageText, use stageText.assignFocus()

  

* * *