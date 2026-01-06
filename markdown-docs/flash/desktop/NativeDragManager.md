# Nativedragmanager

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public class NativeDragManager  
Inheritance| NativeDragManager ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Runtime version:**|  AIR 1.0   
---|---  
  
The NativeDragManager class coordinates drag-and-drop operations. With the native drag-and-drop API, you can allow a user to drag data between an AIR application and the native operating system, between two applications, or between components within a single application. 

The following kinds of data can be transferred:

  * Bitmaps
  * Files
  * Text
  * URL strings
  * Serialized objects
  * Object references (valid only within the originating application)

**Note:** all NativeDragManager members are static. An instance of this class does not need to be created.

A drag-and-drop operation is a user interface gesture that begins with the user clicking a visible item and dragging it elsewhere. During the drag gesture, interactive objects on the display list dispatch native drag events as the gesture moves across the AIR application window. Handlers for these events can call the methods of the NativeDragManager class to indicate whether a dragged item can be dropped on an object. In response, the NativeDragManager changes the mouse pointer to provide feedback to the user.

_AIR profile support:_ This feature is not supported on AIR for TV devices. Also, it is not supported on all mobile devices. You can test for support at run time using the `NativeDragManager.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles. 

**Drag actions**

Drag-and-drop gestures are typically used for three types of operations, called _actions_. Since the meaning of these actions depends on the application context, the runtime does not enforce any particular behavior with respect to actions. However, properly implementing the actions improves the user experience with your application. 

The possible actions are:

  * Copy — A copy of the data is made, leaving the original untouched. (When dragging objects within an application, care should be taken to copy the original object itself rather than the reference to that object.)
  * Move — The data is moved from its original context into the context defined by the drop target, such as when moving an item from one list to another.
  * Link — A reference or shortcut to the original data is created, leaving the item in its original context.

The allowed actions can be set for a drag gesture by supplying an `allowedActions` parameter in the `NativeDragManager.doDrag()` call that starts the drag operation. If no `allowedActions` parameter is provided, all of the actions are allowed. Potential drag targets can check which actions are allowed by using the `allowedActions` property of a NativeDragEvent object, and should not accept a drop that allows only incompatible actions (this is not enforced by the runtime, however).

If a drop target only implements a single action, the object can set the `dropAction` property of the NativeDragManager in the handlers for both the `nativeDragEnter` and `nativeDragOver` events. Setting the property before the drop, allows the drag manager to update the mouse pointer to indicate the supported action and also prevents a user from choosing an incompatible action using modifier keys. If the specified action is not one of the allowed actions, then a drop is not allowed, even if the target calls the `acceptDrop()` method.

When accepting a drop, a potential drop target should specify the action chosen by setting the `NativeDragManager.dropAction` property in response to the `nativeDragDrop` event. This action is reported back to the initiating display object in the `nativeDragComplete` event. If no action is set by a drop target, then a default action is chosen from the allowed actions in this order of precedence: copy, move, link. The initiating object is responsible for updating its internal state in response to the chosen action.

String constants for the action names are defined in the NativeDragActions class.

**Sequence of events**

A drag gesture is begun by calling the `NativeDragManager.doDrag()` method within a `mouseDown` or `mouseMove` event handler and proceeds through the following event sequence in response to user actions:

  * `nativeDragStart` event — When `NativeDragManager.doDrag()` is called, the interactive object passed as a paramter to the method becomes the initiator object and dispatches a `nativeDragStart` event.
  * `nativeDragUpdate` event — While the drag is in progress, the initiator object continually dispatches `nativeDragUpdate` events.
  * `nativeDragEnter`, `nativeDragOver` events — When a drag gesture passes over an interactive object, that object dispatches a `nativeDragEnter` event. While the drag gesture remains over the interactive object, it continually dispatches `nativeDragOver` events. In response to either of these events, an object that serves as a potential drop target should check the properties of the event object to decide whether it can accept the drop. If the data format and allowed actions are appropriate, then the event handler for these events must call `NativeDragManager.acceptDrop()`, passing in a reference to the display object to serve as the drag target (typically the object that dispatched the `nativeDragEnter` or `nativeDragOver` event). The user can then drop the dragged item onto the target.
  * `nativeDragExit` event — When a drag gesture passes out of an interactive object, the object dispatches a `nativeDragExit` event. If the object had been designated as the drag target by an earlier call to the `NativeDragManager.acceptDrop()` method, that call is no longer valid and `acceptDrop()` must be called again if the gesture re-enters the interactive object.
  * `nativeDragDrop` event — The target display object dispatches a `nativeDragDrop` event when the user releases the mouse button over the object. The handler for this event can access the data in the `transferable` property of the event object and should set the `NativeDragManager.dropAction` property to signal which action should be taken by the initiator object.
  * `nativeDragComplete` — When the user releases the mouse button at the end of a drag gesture, the initiator object dispatches a `nativeDragComplete` event (whether or not the drop itself was consumated). The handler for this event can check the `dropAction` property of the event object to determine what, if any, modification should be made to its internal data state, such as removing a dragged-out item from a list. If `dropAction` is `NativeDragActions.NONE`, then the dragged item was not dropped on an eligible target.

**Gestures between applications**

When a drag gesture enters an AIR application window from a non-AIR application, there is no initiator object to dispatch the `nativeDragStart` or `nativeDragComplete` event. The events dispatched during the gesture will otherwise follow the same pattern as that of a gesture starting and ending within the same AIR application.

When a drag gesture leaves an AIR application window, there is no target object to dispatch `nativeDragEnter`, `nativeDragOver`, or `nativeDragDrop` events. The initiator object still dispatches a `nativeDragComplete` event, which reports the drag action set by the native operating system (or `none`, if the drop was not accepted).

When a drag gesture moves from one AIR application to another, the initiator and target display objects dispatch events within their separate applications as usual.

**Transfering information**

The data transfered during a drag-and-drop gesture is contained in a Clipboard object. This data object is added to the drag operation with the `NativeDragManager.doDrag()` method that starts the drag gesture. Potential drop targets can access the Clipboard object through the `clipboard` property of the native drag event object. Once a drag operation has started, the Clipboard object can only be accessed in the event handler of a NativeDragEvent. Any other attempt to access the object generates a run-time error.

**Security considerations**

The security sandboxes of the initiator and potential target objects determine how the the data being dragged can be accessed. If both objects are in the same sandbox, then the data can be accessed from any NativeDragEvent object. However, if the initiator and target objects are in different sandboxes, the data can only be accessed in the target sandbox within the event handler for the `nativeDragDrop` event. Other native drag event handlers can still still access the Clipboard object referenced in the event `clipboard` property to determine which data formats are available, but calling the `clipboard.getData()` method generates a security error.

See also

[flash.events.NativeDragEvent](../events/NativeDragEvent.html)   
[flash.desktop.NativeDragActions](../desktop/NativeDragActions.html)   
[flash.desktop.NativeDragOptions](../desktop/NativeDragOptions.html)   
[flash.desktop.Clipboard](../desktop/Clipboard.html)

  

* * *