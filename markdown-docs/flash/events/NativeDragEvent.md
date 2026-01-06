# Nativedragevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class NativeDragEvent  
Inheritance| NativeDragEvent ![Inheritance](../../images/inherit-arrow.gif) [MouseEvent](MouseEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
Native drag events are dispatched by the interactive objects involved in a drag-and-drop operation. 

The initiating object dispatches:

  * `nativeDragStart` — When the drag operation begins.
  * `nativeDragUpdate` — While the drag operation is in progress.
  * `nativeDragComplete` — When the user releases the dragged item (whether or not the drop was accepted).

The initiating object is the interactive object passed that is to the NativeDragManager object in the call to `NativeDragManager.doDrag()` which began the drag operation.

Potential target interactive objects dispatches:

  * `nativeDragEnter` — When the drag gesture passes within the object boundary.
  * `nativeDragOver` — While the drag gesture remains within the object boundary.
  * `nativeDragExit` — When the drag gesture leaves the object boundary.
  * `nativeDragDrop` — When the user releases the dragged item over the object and the object has accepted the drop with an earlier call to `NativeDragManager.acceptDragDrop()`.

Typically a handler for the `nativeDragEnter` or `nativeDragOver` event evaluates the data being dragged, along with the drag actions allowed, to determine whether an interactive object can accept a drop. To specify that an interactive object is an eligible target, the event handler must call the `NativeDragManager.acceptDrop()`function, passing in a reference to the object. If the user releases the mouse button over the designated object, the object becomes the drop target and dispatches the `nativeDragDrop` event.

Any InteractiveObject type object can be a drag initiator or a drop target.

See also

[flash.desktop.NativeDragManager](../desktop/NativeDragManager.html)   
[flash.desktop.Clipboard](../desktop/Clipboard.html)   
[flash.desktop.NativeDragOptions](../desktop/NativeDragOptions.html)   
[flash.desktop.NativeDragActions](../desktop/NativeDragActions.html)   
[flash.display.InteractiveObject](../display/InteractiveObject.html)

  

* * *