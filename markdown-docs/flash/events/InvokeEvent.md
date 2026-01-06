# Invokeevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class InvokeEvent  
Inheritance| InvokeEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The NativeApplication object of an AIR application dispatches an `invoke` event when the application is invoked. 

The NativeApplication object always dispatches an `invoke` event when an application is launched, but the event may be dispatched at other times as well. For example, a running application dispatches an additional InvokeEvent when a user activates a file associated with the application.

Only a single instance of a particular application can be launched. Subsequent attempts to launch the application will result in a new `invoke` event dispatched by the NativeApplication object of the running instance. It is an application's responsibility to handle this event and take the appropriate action, such as opening a new application window to display the data in a file.

InvokeEvent objects are dispatched by the NativeApplication object (`NativeApplication.nativeApplication`). To receive `invoke` events, call the `addEventListener()` method of the NativeApplication object. When an event listener registers for an `invoke` event, it will also receive all `invoke` events that occurred before the registration. These earlier events are dispatched after the call to `addEventListener()` returns, but not necessarily before a new `invoke` event that might be might be dispatched after registration. Thus, you should not rely on dispatch order.

See also

[flash.events.BrowserInvokeEvent](../events/BrowserInvokeEvent.html)   
[flash.desktop.NativeApplication](../desktop/NativeApplication.html)

  

* * *