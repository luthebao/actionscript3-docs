# Locationchangeevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class LocationChangeEvent  
Inheritance| LocationChangeEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.5   
---|---  
  
An HTMLLoader or StageWebView object dispatches a LocationChangeEvent object when a new page loads. 

There are two types of LocationChangeEvent: 

  * `LocationChangeEvent.LOCATION_CHANGING`: dispatched before a change initiated via the content displayed in a StageWebView object. Can be canceled.
  * `LocationChangeEvent.LOCATION_CHANGE`: dispatched after every location change. Cannot be canceled.

See also

[StageWebView](../media/StageWebView.html)

  

* * *