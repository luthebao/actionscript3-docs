# Stage

Package| [flash.display](package-detail.html)  
---|---  
Class| public class Stage  
Inheritance| Stage ![Inheritance](../../images/inherit-arrow.gif) [DisplayObjectContainer](DisplayObjectContainer.html) ![Inheritance](../../images/inherit-arrow.gif) [InteractiveObject](InteractiveObject.html) ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Stage class represents the main drawing area. 

For SWF content running in the browser (in Flash® Player), the Stage represents the entire area where Flash content is shown. For content running in AIR on desktop operating systems, each NativeWindow object has a corresponding Stage object.

The Stage object is not globally accessible. You need to access it through the `stage` property of a DisplayObject instance.

The Stage class has several ancestor classes — DisplayObjectContainer, InteractiveObject, DisplayObject, and EventDispatcher — from which it inherits properties and methods. Many of these properties and methods are either inapplicable to Stage objects, or require security checks when called on a Stage object. The properties and methods that require security checks are documented as part of the Stage class.

In addition, the following inherited properties are inapplicable to Stage objects. If you try to set them, an IllegalOperationError is thrown. These properties may always be read, but since they cannot be set, they will always contain default values.

  * `accessibilityProperties`
  * `alpha`
  * `blendMode`
  * `cacheAsBitmap`
  * `contextMenu`
  * `filters`
  * `focusRect`
  * `loaderInfo`
  * `mask`
  * `mouseEnabled`
  * `name`
  * `opaqueBackground`
  * `rotation`
  * `scale9Grid`
  * `scaleX`
  * `scaleY`
  * `scrollRect`
  * `tabEnabled`
  * `tabIndex`
  * `transform`
  * `visible`
  * `x`
  * `y`

Some events that you might expect to be a part of the Stage class, such as `enterFrame`, `exitFrame`, `frameConstructed`, and `render`, cannot be Stage events because a reference to the Stage object cannot be guaranteed to exist in every situation where these events are used. Because these events cannot be dispatched by the Stage object, they are instead dispatched by every DisplayObject instance, which means that you can add an event listener to any DisplayObject instance to listen for these events. These events, which are part of the DisplayObject class, are called broadcast events to differentiate them from events that target a specific DisplayObject instance. Two other broadcast events, `activate` and `deactivate`, belong to DisplayObject's superclass, EventDispatcher. The `activate` and `deactivate` events behave similarly to the DisplayObject broadcast events, except that these two events are dispatched not only by all DisplayObject instances, but also by all EventDispatcher instances and instances of other EventDispatcher subclasses. For more information on broadcast events, see the DisplayObject class.

See also

[flash.display.DisplayObject](../display/DisplayObject.html)

  

* * *