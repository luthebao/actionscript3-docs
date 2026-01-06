# Errorevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class ErrorEvent  
Inheritance| ErrorEvent ![Inheritance](../../images/inherit-arrow.gif) [TextEvent](TextEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [AsyncErrorEvent](../events/AsyncErrorEvent.html), [DownloadErrorEvent](../../air/update/events/DownloadErrorEvent.html), [DRMAuthenticationErrorEvent](../events/DRMAuthenticationErrorEvent.html), [DRMDeviceGroupErrorEvent](../events/DRMDeviceGroupErrorEvent.html), [DRMErrorEvent](../events/DRMErrorEvent.html), [DRMReturnVoucherErrorEvent](../events/DRMReturnVoucherErrorEvent.html), [IOErrorEvent](../events/IOErrorEvent.html), [SecurityErrorEvent](../events/SecurityErrorEvent.html), [SQLErrorEvent](../events/SQLErrorEvent.html), [StatusFileUpdateErrorEvent](../../air/update/events/StatusFileUpdateErrorEvent.html), [StatusUpdateErrorEvent](../../air/update/events/StatusUpdateErrorEvent.html), [UncaughtErrorEvent](../events/UncaughtErrorEvent.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
An object dispatches an ErrorEvent object when an error causes an asynchronous operation to fail. 

The ErrorEvent class defines only one type of `error` event: `ErrorEvent.ERROR`. The ErrorEvent class also serves as the base class for several other error event classes, including the AsyncErrorEvent, IOErrorEvent, SecurityErrorEvent, SQLErrorEvent, and UncaughtErrorEvent classes.

You can check for `error` events that do not have any listeners by registering a listener for the `uncaughtError` (UncaughtErrorEvent.UNCAUGHT_ERROR) event.

An uncaught error also causes an error dialog box displaying the error event to appear when content is running in the debugger version of Flash Player or the AIR Debug Launcher (ADL) application.

[View the examples.](#includeExamplesSummary)

See also

[UncaughtErrorEvent](../events/UncaughtErrorEvent.html)

  

* * *