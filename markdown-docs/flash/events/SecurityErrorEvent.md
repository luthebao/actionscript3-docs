# Securityerrorevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class SecurityErrorEvent  
Inheritance| SecurityErrorEvent ![Inheritance](../../images/inherit-arrow.gif) [ErrorEvent](ErrorEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [TextEvent](TextEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
An object dispatches a SecurityErrorEvent object to report the occurrence of a security error. Security errors reported through this class are generally from asynchronous operations, such as loading data, in which security violations may not manifest immediately. Your event listener can access the object's `text` property to determine what operation was attempted and any URLs that were involved. If there are no event listeners, the debugger version of Flash Player or the AIR Debug Launcher (ADL) application automatically displays an error message that contains the contents of the `text` property. There is one type of security error event: `SecurityErrorEvent.SECURITY_ERROR`. 

Security error events are the final events dispatched for any target object. This means that any other events, including generic error events, are not dispatched for a target object that experiences a security error.

[View the examples.](#includeExamplesSummary)

See also

[Security class](../system/Security.html)   
[SECURITY_ERROR](../events/SecurityErrorEvent.html#SECURITY_ERROR)

  

* * *