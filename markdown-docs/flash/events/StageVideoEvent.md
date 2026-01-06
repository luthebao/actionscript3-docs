# Stagevideoevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class StageVideoEvent  
Inheritance| StageVideoEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.5   
---|---  
  
A StageVideo object dispatches a StageVideoEvent object after the `attachNetStream()` method of the StageVideo object and the `play()` method of the attached NetStream object have both been called. Also, depending on the platform, any change in the playing status can result in dispatching the event. The one type of StageVideoEvent is `StageVideoEvent.RENDER_STATE`. 

  

* * *