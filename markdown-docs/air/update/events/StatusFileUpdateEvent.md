# Statusfileupdateevent

Package| [air.update.events](package-detail.html)  
---|---  
Class| public class StatusFileUpdateEvent  
Inheritance| StatusFileUpdateEvent ![Inheritance](../../../images/inherit-arrow.gif) [UpdateEvent](UpdateEvent.html) ![Inheritance](../../../images/inherit-arrow.gif) [Event](../../../flash/events/Event.html) ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
Dispatched after the updater successfully validates the file in the call to the `installFromAIRFile()` method. 

The default behavior is to install the update if the available of the available property of the StatusFileUpdateEvent object is set to true. The default behavior can be prevented only when using the ApplicationUpdater class.

See also

[air.update.ApplicationUpdater](../../update/ApplicationUpdater.html)   
[air.update.ApplicationUpdaterUI](../../update/ApplicationUpdaterUI.html)

  

* * *