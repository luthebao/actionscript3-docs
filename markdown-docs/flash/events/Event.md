# Event

Package| [flash.events](package-detail.html)  
---|---  
Class| public class Event  
Inheritance| Event ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [AccelerometerEvent](../events/AccelerometerEvent.html), [ActivityEvent](../events/ActivityEvent.html), [AudioOutputChangeEvent](../events/AudioOutputChangeEvent.html), [BrowserInvokeEvent](../events/BrowserInvokeEvent.html), [ContextMenuEvent](../events/ContextMenuEvent.html), [DatagramSocketDataEvent](../events/DatagramSocketDataEvent.html), [DeviceRotationEvent](../events/DeviceRotationEvent.html), [DNSResolverEvent](../events/DNSResolverEvent.html), [DRMAuthenticateEvent](../events/DRMAuthenticateEvent.html), [DRMAuthenticationCompleteEvent](../events/DRMAuthenticationCompleteEvent.html), [DRMDeviceGroupEvent](../events/DRMDeviceGroupEvent.html), [DRMLicenseRequestEvent](../events/DRMLicenseRequestEvent.html), [DRMReturnVoucherCompleteEvent](../events/DRMReturnVoucherCompleteEvent.html), [DRMStatusEvent](../events/DRMStatusEvent.html), [FileListEvent](../events/FileListEvent.html), [FocusEvent](../events/FocusEvent.html), [GameInputEvent](../events/GameInputEvent.html), [GeolocationEvent](../events/GeolocationEvent.html), [GestureEvent](../events/GestureEvent.html), [HTMLUncaughtScriptExceptionEvent](../events/HTMLUncaughtScriptExceptionEvent.html), [HTTPStatusEvent](../events/HTTPStatusEvent.html), [InvokeEvent](../events/InvokeEvent.html), [KeyboardEvent](../events/KeyboardEvent.html), [LocationChangeEvent](../events/LocationChangeEvent.html), [MediaEvent](../events/MediaEvent.html), [MouseEvent](../events/MouseEvent.html), [NativeProcessExitEvent](../events/NativeProcessExitEvent.html), [NativeWindowBoundsEvent](../events/NativeWindowBoundsEvent.html), [NativeWindowDisplayStateEvent](../events/NativeWindowDisplayStateEvent.html), [NetDataEvent](../events/NetDataEvent.html), [NetMonitorEvent](../events/NetMonitorEvent.html), [NetStatusEvent](../events/NetStatusEvent.html), [OutputProgressEvent](../events/OutputProgressEvent.html), [PermissionEvent](../events/PermissionEvent.html), [ProgressEvent](../events/ProgressEvent.html), [RemoteNotificationEvent](../events/RemoteNotificationEvent.html), [SampleDataEvent](../events/SampleDataEvent.html), [ServerSocketConnectEvent](../events/ServerSocketConnectEvent.html), [ShaderEvent](../events/ShaderEvent.html), [SoftKeyboardEvent](../events/SoftKeyboardEvent.html), [SQLEvent](../events/SQLEvent.html), [SQLUpdateEvent](../events/SQLUpdateEvent.html), [StageOrientationEvent](../events/StageOrientationEvent.html), [StageVideoAvailabilityEvent](../events/StageVideoAvailabilityEvent.html), [StageVideoEvent](../events/StageVideoEvent.html), [StatusEvent](../events/StatusEvent.html), [StorageVolumeChangeEvent](../events/StorageVolumeChangeEvent.html), [SyncEvent](../events/SyncEvent.html), [TextEvent](../events/TextEvent.html), [ThrottleEvent](../events/ThrottleEvent.html), [TimerEvent](../events/TimerEvent.html), [TouchEvent](../events/TouchEvent.html), [UpdateEvent](../../air/update/events/UpdateEvent.html), [VideoEvent](../events/VideoEvent.html), [VideoTextureEvent](../events/VideoTextureEvent.html), [VsyncStateChangeAvailabilityEvent](../events/VsyncStateChangeAvailabilityEvent.html), [WebSocketEvent](../events/WebSocketEvent.html), [WebViewDrawEvent](../events/WebViewDrawEvent.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Event class is used as the base class for the creation of Event objects, which are passed as parameters to event listeners when an event occurs. 

The properties of the Event class carry basic information about an event, such as the event's type or whether the event's default behavior can be canceled. For many events, such as the events represented by the Event class constants, this basic information is sufficient. Other events, however, may require more detailed information. Events associated with a mouse click, for example, need to include additional information about the location of the click event and whether any keys were pressed during the click event. You can pass such additional information to event listeners by extending the Event class, which is what the MouseEvent class does. ActionScript 3.0The Adobe® AIR™ API defines several Event subclasses for common events that require additional information. Events associated with each of the Event subclasses are described in the documentation for each class.

The methods of the Event class can be used in event listener functions to affect the behavior of the event object. Some events have an associated default behavior. For example, the `doubleClick` event has an associated default behavior that highlights the word under the mouse pointer at the time of the event. For example, the `closing` event dispatched by a NativeWindow object has an associated default behavior that closes the window. Your event listener can cancel this behavior by calling the `preventDefault()` method. You can also make the current event listener the last one to process an event by calling the `stopPropagation()` or `stopImmediatePropagation()` method.

Other sources of information include:

  * A useful description about the timing of events, code execution, and rendering at runtime in Ted Patrick's blog entry: [Flash Player Mental Model - The Elastic Racetrack](http://www.onflex.org/ted/2005/07/flash-player-mental-model-elastic.php).
  * A blog entry by Johannes Tacskovics about the timing of frame events, such as ENTER_FRAME, EXIT_FRAME: [The MovieClip Lifecycle](http://blog.johannest.com/2009/06/15/the-movieclip-life-cycle-revisited-from-event-added-to-event-removed_from_stage/).
  * An article by Trevor McCauley about the order of ActionScript operations: [Order of Operations in ActionScript](http://www.senocular.com/flash/tutorials/orderofoperations/).
  * A blog entry by Matt Przybylski on creating custom events: [AS3: Custom Events](http://evolve.reintroducing.com/2007/10/23/as3/as3-custom-events/).

**Note:** Some of the constants in this class are used to define the `type` property for events that are dispatched by ActionScript 3.0 display list, used in SWF content. However, some constants in this class are used to define the `type` property for events that are _not_ related to the ActionScript 3.0 display list and are useful in JavaScript code running in the AIR runtime.

[View the examples.](#includeExamplesSummary)

See also

[flash.events.EventDispatcher](../events/EventDispatcher.html)

  

* * *