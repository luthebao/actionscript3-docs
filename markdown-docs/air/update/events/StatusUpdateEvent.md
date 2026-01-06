# Statusupdateevent

Package| [air.update.events](package-detail.html)  
---|---  
Class| public class StatusUpdateEvent  
Inheritance| StatusUpdateEvent ![Inheritance](../../../images/inherit-arrow.gif) [UpdateEvent](UpdateEvent.html) ![Inheritance](../../../images/inherit-arrow.gif) [Event](../../../flash/events/Event.html) ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
An updater object dispatches a StatusUpdateEvent object after the updater successfully downloads and interprets the update descriptor file. 

The default behavior is to start downloading the update if the `available` property of the StatusUpdateEvent object is set to `true`. The default behavior can be prevented only when using the ApplicationUpdater class.

See also

[air.update.ApplicationUpdater](../../update/ApplicationUpdater.html)   
[air.update.ApplicationUpdaterUI](../../update/ApplicationUpdaterUI.html)

  

* * *