# Uncaughterrorevents

Package| [flash.events](package-detail.html)  
---|---  
Class| public class UncaughtErrorEvents  
Inheritance| UncaughtErrorEvents ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The UncaughtErrorEvents class provides a way to receive uncaught error events. An instance of this class dispatches an `uncaughtError` event when a runtime error occurs and the error isn't detected and handled in your code. 

Use the following properties to access an UncaughtErrorEvents instance:

  * `LoaderInfo.uncaughtErrorEvents`: to detect uncaught errors in code defined in the same SWF.
  * `Loader.uncaughtErrorEvents`: to detect uncaught errors in code defined in the SWF loaded by a Loader object.

To catch an error directly and prevent an uncaught error event, do the following:

  * Use a `[try..catch](../../statements.html#try..catch..finally)` block to isolate code that potentially throws a synchronous error
  * When performing an operation that dispatches an event when an error occurs, register a listener for that error event

If the content loaded by a Loader object is an AVM1 (ActionScript 2) SWF file, uncaught errors in the AVM1 SWF file do not result in an `uncaughtError` event. In addition, JavaScript errors in HTML content loaded in an HTMLLoader object (including a Flex HTML control) do not result in an `uncaughtError` event.

See also

[LoaderInfo.uncaughtErrorEvents](../display/LoaderInfo.html#uncaughtErrorEvents)   
[Loader.uncaughtErrorEvents](../display/Loader.html#uncaughtErrorEvents)   
[UncaughtErrorEvent](../events/UncaughtErrorEvent.html)

  

* * *