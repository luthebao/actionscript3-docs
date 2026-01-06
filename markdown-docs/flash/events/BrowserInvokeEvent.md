# Browserinvokeevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class BrowserInvokeEvent  
Inheritance| BrowserInvokeEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The NativeApplication object of an AIR application dispatches a `browserInvoke` event when the application is invoked as the result of a SWF file in the browser using the browser invocation feature. The NativeApplication object also dispatches a `browserInvoke` event when a user instantiates the seamless installation feature in the browser and the SWF file in the browser passes an array to the `arguments` parameter of the `launchApplication()` method of the air.swf file. (For details, see "Distributing, installing and running AIR applications" in the AIR developer's guide.) 

Browser invocation is permitted only if an application specifies the following in the application descriptor file:
    
    
    <allowBrowserInvocation>true</allowBrowserInvocation>

If the application is not running, the NativeApplication object dispatches both an InvokeEvent event and a `browserInvoke` event when launched from the browser. Otherwise, if the application _is_ already running, the NativeApplication object dispatches only a `browserInvoke` event when launched from the browser. 

If the application is launched as the result of a seamless installation from the browser (with the user choosing to launch upon installation), the NativeApplication object dispatches a BrowserInvoke event only if arguments were passed (via the SWF file in the browser passing an array to the `arguments` parameter of the `installApplication()` method of the air.swf file). For details, see "Distributing, installing, and running AIR applications" in the AIR developer's guide.

Like the `invokeEvent` events, `browserInvokeEvent` events are dispatched by the NativeApplication object (`NativeApplication.nativeApplication`). To receive `browserInvoke` events, call the `addEventListener()` method of the NativeApplication object. When an event listener registers for a `browserInvoke` event, it will also receive all `browserInvoke` events that occurred before the registration. These are dispatched after the call to `addEventListener()` returns, but not necessarily before other `browserInvoke` events that might be received after registration. This allows you to handle `browserInvoke` events that have occurred before your initialization code is executed (such as when the application was initially invoked from the browser). Keep in mind that if you add an event listener later in execution (after application initialization), it still receives all `browserInvoke` events that have occurred since the application started.

See also

[flash.events.InvokeEvent](../events/InvokeEvent.html)   
[flash.desktop.NativeApplication](../desktop/NativeApplication.html)

  

* * *