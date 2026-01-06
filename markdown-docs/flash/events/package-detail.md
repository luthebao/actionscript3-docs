# Package Detail

The flash.events package supports the new DOM event model and includes the EventDispatcher base class.

  

* * *

Interfaces

| Interface| Description  
---|---|---  
|  _[IEventDispatcher](IEventDispatcher.html)_|  The IEventDispatcher interface defines methods for adding or removing event listeners, checks whether specific types of event listeners are registered, and dispatches events.  
  
Classes

| Class| Description  
---|---|---  
| [AccelerometerEvent](AccelerometerEvent.html)|  The Accelerometer class dispatches AccelerometerEvent objects when acceleration updates are obtained from the Accelerometer sensor installed on the device.  
| [ActivityEvent](ActivityEvent.html)|  A Camera or Microphone object dispatches an ActivityEvent object whenever a camera or microphone reports that it has become active or inactive.  
| [AsyncErrorEvent](AsyncErrorEvent.html)|  An object dispatches an AsyncErrorEvent when an exception is thrown from native asynchronous code, which could be from, for example, LocalConnection, NetConnection, SharedObject, or NetStream.  
| [AudioOutputChangeEvent](AudioOutputChangeEvent.html)|  This event fires when user selects a different audio output device from Flash Player's settings UI, or an audio device gets added to / removed from the system.  
| [BrowserInvokeEvent](BrowserInvokeEvent.html)|  The NativeApplication object of an AIR application dispatches a `browserInvoke` event when the application is invoked as the result of a SWF file in the browser using the browser invocation feature.  
| [ContextMenuEvent](ContextMenuEvent.html)|  An InteractiveObject dispatches a ContextMenuEvent object when the user opens or interacts with the context menu.  
| [DataEvent](DataEvent.html)|  An object dispatches a DataEvent object when raw data has completed loading.  
| [DatagramSocketDataEvent](DatagramSocketDataEvent.html)|  A DatagramSocketDataEvent object is dispatched when Datagram socket has received data.  
| [DeviceRotationEvent](DeviceRotationEvent.html)|  The DeviceRotation class dispatches DeviceRotationEvent and returns roll, yaw, pitch and quaternion data when DeviceRotation updates are obtained from the combined readings from Accelerometer and Gyroscope sensors' readings installed on the device.  
| [DNSResolverEvent](DNSResolverEvent.html)|  The DNSResolverEvent class represents the results of a Domain Name System (DNS) lookup operation.  
| [DRMAuthenticateEvent](DRMAuthenticateEvent.html)|  A NetStream object dispatchs a DRMAuthenticateEvent object when attempting to play digital rights management (DRM) encrypted content that requires a user credential for authentication.  
| [DRMAuthenticationCompleteEvent](DRMAuthenticationCompleteEvent.html)|  The DRMManager dispatches a DRMAuthenticationCompleteEvent object when a call to the `authenticate()` method of the DRMManager object succeeds.  
| [DRMAuthenticationErrorEvent](DRMAuthenticationErrorEvent.html)|  The DRMManager dispatches a DRMAuthenticationErrorEvent object when a call to the `authenticate()` method of the DRMManager object fails.  
| [DRMDeviceGroupErrorEvent](DRMDeviceGroupErrorEvent.html)|  Issued by the DRMManager when any error occurs during any device group related calls. It is the application's responsibility to explicitly handle the error events.These events include cases where the user inputs valid credentials, but the voucher protecting the encrypted content restricts the access to the content.  
| [DRMDeviceGroupEvent](DRMDeviceGroupEvent.html)|  Issued by the DRMManager when a device group related call successfully completes.  
| [DRMErrorEvent](DRMErrorEvent.html)|  The DRMErrorEvent class provides information about errors that occur when playing digital rights management (DRM) encrypted files.  
| [DRMLicenseRequestEvent](DRMLicenseRequestEvent.html)|  The DRMManager dispatches a DRMLicenseRequestEvent object before each call to the `loadVoucher()` or `loadPreviewVoucher()` methods of the DRMManager object succeeds.  
| [DRMReturnVoucherCompleteEvent](DRMReturnVoucherCompleteEvent.html)|  The DRMManager dispatches a DRMVoucherReturnCompleteEvent object when a call to the `returnVoucher()` method of the DRMManager object succeeds.  
| [DRMReturnVoucherErrorEvent](DRMReturnVoucherErrorEvent.html)|  The DRMManager dispatches a DRMReturnVoucherErrorEvent object when a call to the `returnVoucher()` method of the DRMManager object fails.  
| [DRMStatusEvent](DRMStatusEvent.html)|  A NetStream object dispatches a DRMStatusEvent object when the content protected using digital rights management (DRM) begins playing successfully (when the voucher is verified, and when the user is authenticated and authorized to view the content).  
| [ErrorEvent](ErrorEvent.html)|  An object dispatches an ErrorEvent object when an error causes an asynchronous operation to fail.  
| [Event](Event.html)|  The Event class is used as the base class for the creation of Event objects, which are passed as parameters to event listeners when an event occurs.  
| [EventDispatcher](EventDispatcher.html)|  The EventDispatcher class is the base class for all runtime classes that dispatch events.  
| [EventPhase](EventPhase.html)|  The EventPhase class provides values for the `eventPhase` property of the Event class.  
| [FileListEvent](FileListEvent.html)|  A File object dispatches a FileListEvent object when a call to the `getDirectoryListingAsync()` method of a File object successfully enumerates a set of files and directories or when a user selects files after a call to the `browseForOpenMultiple()` method.  
| [FocusEvent](FocusEvent.html)|  An object dispatches a FocusEvent object when the user changes the focus from one object in the display list to another.  
| [FullScreenEvent](FullScreenEvent.html)|  The Stage object dispatches a FullScreenEvent object whenever the Stage enters or leaves full-screen display mode.  
| [GameInputEvent](GameInputEvent.html)|  The `GameInputEvent` class represents an event that is dispatched when a game input device has either been added or removed from the application platform.  
| [GeolocationEvent](GeolocationEvent.html)|  A Geolocation object dispatches GeolocationEvent objects when it receives updates from the location sensor installed on the device.  
| [GestureEvent](GestureEvent.html)|  The GestureEvent class lets you handle multi-touch events on devices that detect complex user contact with the device (such as pressing two fingers on a touch screen at the same time).  
| [GesturePhase](GesturePhase.html)|  The GesturePhase class is an enumeration class of constant values for use with the GestureEvent, PressAndTapGestureEvent, and TransformGestureEvent classes.  
| [HTMLUncaughtScriptExceptionEvent](HTMLUncaughtScriptExceptionEvent.html)|  An HTMLLoader object dispatches an HTMLUncaughtScriptExceptionEvent object whenever a JavaScript exception is thrown and not handled with a `catch` statement.  
| [HTTPStatusEvent](HTTPStatusEvent.html)|  The application dispatches HTTPStatusEvent objects when a network request returns an HTTP status code.  
| [IMEEvent](IMEEvent.html)|  An IMEEvent object is dispatched when the user enters text using an input method editor (IME).  
| [InvokeEvent](InvokeEvent.html)|  The NativeApplication object of an AIR application dispatches an `invoke` event when the application is invoked.  
| [IOErrorEvent](IOErrorEvent.html)|  An IOErrorEvent object is dispatched when an error causes input or output operations to fail.  
| [KeyboardEvent](KeyboardEvent.html)|  A KeyboardEvent object id dispatched in response to user input through a keyboard.  
| [LocationChangeEvent](LocationChangeEvent.html)|  An HTMLLoader or StageWebView object dispatches a LocationChangeEvent object when a new page loads.  
| [MediaEvent](MediaEvent.html)|  CameraRoll and CameraUI classes dispatch MediaEvent objects when a media stream is available.  
| [MouseEvent](MouseEvent.html)|  A MouseEvent object is dispatched into the event flow whenever mouse events occur.  
| [NativeDragEvent](NativeDragEvent.html)|  Native drag events are dispatched by the interactive objects involved in a drag-and-drop operation.  
| [NativeProcessExitEvent](NativeProcessExitEvent.html)|  This event is dispatched by the NativeProcess object when the process exits.  
| [NativeWindowBoundsEvent](NativeWindowBoundsEvent.html)|  A NativeWindow object dispatches a NativeWindowBoundsEvent object when the size or location of the window changes.  
| [NativeWindowDisplayStateEvent](NativeWindowDisplayStateEvent.html)|  A NativeWindow object dispatches events of the NativeWindowDisplayStateEvent class when the window display state changes.  
| [NetDataEvent](NetDataEvent.html)|  A NetStream object dispatches a NetDataEvent object when a data message is encountered in the media stream.  
| [NetMonitorEvent](NetMonitorEvent.html)|  A NetMonitor object dispatches NetMonitorEvent objects when a NetStream object is created.  
| [NetStatusEvent](NetStatusEvent.html)|  A NetConnection, NetStream, or SharedObject object dispatches NetStatusEvent objects when a it reports its status.  
| [OutputProgressEvent](OutputProgressEvent.html)|  A FileStream object dispatches OutputProgressEvent objects as pending asynchronous file write operations are performed.  
| [PermissionEvent](PermissionEvent.html)|   
| [PressAndTapGestureEvent](PressAndTapGestureEvent.html)|  The PressAndTapGestureEvent class lets you handle press-and-tap gesture on touch-enabled devices.  
| [ProgressEvent](ProgressEvent.html)|  A ProgressEvent object is dispatched when a load operation has begun or a socket has received data.  
| [RemoteNotificationEvent](RemoteNotificationEvent.html)|  Contains events that are dispatched by `flash.notifications.RemoteNotifier` in response to push notification events from APNs.  
| [SampleDataEvent](SampleDataEvent.html)|  Dispatched when a Sound object requests new audio data or when a Microphone object has new audio data to provide.  
| [ScreenMouseEvent](ScreenMouseEvent.html)|  The SystemTrayIcon object dispatches events of type ScreenMouseEvent in response to mouse interaction.  
| [SecurityErrorEvent](SecurityErrorEvent.html)|  An object dispatches a SecurityErrorEvent object to report the occurrence of a security error.  
| [ServerSocketConnectEvent](ServerSocketConnectEvent.html)|  A ServerSocket object dispatches a ServerSocketConnectEvent object when a client attempts to connect to the server socket.  
| [ShaderEvent](ShaderEvent.html)|  A ShaderEvent is dispatched when a shader operation launched from a ShaderJob finishes.  
| [SoftKeyboardEvent](SoftKeyboardEvent.html)|  A SoftKeyboardEvent object is dispatched when a software-driven keyboard is activated or de-activated on a device or operating system.  
| [SoftKeyboardTrigger](SoftKeyboardTrigger.html)|  The SoftKeyboardTrigger class provides enumerator values for the `triggerType` property of the SoftKeyboardEvent class.  
| [SQLErrorEvent](SQLErrorEvent.html)|  A SQLErrorEvent instance is dispatched by a SQLConnection instance or SQLStatement instance when an error occurs while performing a database operation in asynchronous execution mode.  
| [SQLEvent](SQLEvent.html)|  Adobe AIR dispatches SQLEvent objects when one of the operations performed by a SQLConnection or SQLStatement instance completes successfully.  
| [SQLUpdateEvent](SQLUpdateEvent.html)|  A SQLUpdateEvent object is dispatched by a SQLConnection object when a data change occurs on any table associated with the SQLConnection instance.  
| [StageOrientationEvent](StageOrientationEvent.html)|  A Stage object dispatches a StageOrientationEvent object when the orientation of the stage changes.  
| [StageVideoAvailabilityEvent](StageVideoAvailabilityEvent.html)|  This event fires when the state of the `Stage.stageVideos` property changes.  
| [StageVideoEvent](StageVideoEvent.html)|  A StageVideo object dispatches a StageVideoEvent object after the `attachNetStream()` method of the StageVideo object and the `play()` method of the attached NetStream object have both been called.  
| [StatusEvent](StatusEvent.html)|  An object dispatches a StatusEvent object when a device, such as a camera or microphone, or an object such as a LocalConnection object reports its status.  
| [StorageVolumeChangeEvent](StorageVolumeChangeEvent.html)|  The `StorageVolumeInfo.storageVolumeInfo` object dispatches a StorageVolumeChangeEvent event object when a storage volume is mounted or unmounted.  
| [SyncEvent](SyncEvent.html)|  An SharedObject object representing a remote shared object dispatches a SyncEvent object when the remote shared object has been updated by the server.  
| [TextEvent](TextEvent.html)|  An object dispatches a TextEvent object when a user enters text in a text field or clicks a hyperlink in an HTML-enabled text field.  
| [ThrottleEvent](ThrottleEvent.html)|  A ThrottleEvent is dispatched when the Flash Player throttles, pauses, or resumes content.  
| [ThrottleType](ThrottleType.html)|  The ThrottleType class provides values for the playback `state` property of the flash.event.ThrottleEvent class.  
| [TimerEvent](TimerEvent.html)|  A Timer object dispatches a TimerEvent objects whenever the Timer object reaches the interval specified by the `Timer.delay` property.  
| [TouchEvent](TouchEvent.html)|  The TouchEvent class lets you handle events on devices that detect user contact with the device (such as a finger on a touch screen).  
| [TouchEventIntent](TouchEventIntent.html)|  The TouchEventIntent class defines constants for the `touchIntent` property of the TouchEvent class.  
| [TransformGestureEvent](TransformGestureEvent.html)|  The TransformGestureEvent class lets you handle complex movement input events (such as moving fingers across a touch screen) that the device or operating system interprets as a gesture.  
| [UncaughtErrorEvent](UncaughtErrorEvent.html)|  An UncaughtErrorEvent object is dispatched by an instance of the UncaughtErrorEvents class when an uncaught error occurs.  
| [UncaughtErrorEvents](UncaughtErrorEvents.html)|  The UncaughtErrorEvents class provides a way to receive uncaught error events.  
| [VideoEvent](VideoEvent.html)|  This event class reports the current video rendering status.  
| [VideoTextureEvent](VideoTextureEvent.html)|  Almost exactly StageVideoEvent.  
| [VsyncStateChangeAvailabilityEvent](VsyncStateChangeAvailabilityEvent.html)|  The Stage class dispatches VsyncStateChangeAvailabilityEvent when the availablity of Stage for changing vsync state changes.  
| [WebSocketEvent](WebSocketEvent.html)|  An event that contains data received from a `WebSocket` object.  
| [WebViewDrawEvent](WebViewDrawEvent.html)|  A WebViewDrawEvent object is dispatched when a StageWebView object has completed some asynchronous draw event.  
  
© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Mon Feb 12 2024, 3:03 PM GMT  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)