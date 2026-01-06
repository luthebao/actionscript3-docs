# Displayobject

Package| [flash.display](package-detail.html)  
---|---  
Class| public class DisplayObject  
Inheritance| DisplayObject ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IBitmapDrawable](IBitmapDrawable.html)  
Subclasses| [AVM1Movie](../display/AVM1Movie.html), [Bitmap](../display/Bitmap.html), [InteractiveObject](../display/InteractiveObject.html), [MorphShape](../display/MorphShape.html), [Shape](../display/Shape.html), [StaticText](../text/StaticText.html), [Video](../media/Video.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The DisplayObject class is the base class for all objects that can be placed on the display list. The display list manages all objects displayed in the Flash runtimes. Use the DisplayObjectContainer class to arrange the display objects in the display list. DisplayObjectContainer objects can have child display objects, while other display objects, such as Shape and TextField objects, are "leaf" nodes that have only parents and siblings, no children. 

The DisplayObject class supports basic functionality like the _x_ and _y_ position of an object, as well as more advanced properties of the object such as its transformation matrix. 

DisplayObject is an abstract base class; therefore, you cannot call DisplayObject directly. Invoking `new DisplayObject()` throws an `ArgumentError` exception. 

All display objects inherit from the DisplayObject class.

The DisplayObject class itself does not include any APIs for rendering content onscreen. For that reason, if you want create a custom subclass of the DisplayObject class, you will want to extend one of its subclasses that do have APIs for rendering content onscreen, such as the Shape, Sprite, Bitmap, SimpleButton, TextField, or MovieClip class.

The DisplayObject class contains several broadcast events. Normally, the target of any particular event is a specific DisplayObject instance. For example, the target of an `added` event is the specific DisplayObject instance that was added to the display list. Having a single target restricts the placement of event listeners to that target and in some cases the target's ancestors on the display list. With broadcast events, however, the target is not a specific DisplayObject instance, but rather all DisplayObject instances, including those that are not on the display list. This means that you can add a listener to any DisplayObject instance to listen for broadcast events. In addition to the broadcast events listed in the DisplayObject class's Events table, the DisplayObject class also inherits two broadcast events from the EventDispatcher class: `activate` and `deactivate`.

Some properties previously used in the ActionScript 1.0 and 2.0 MovieClip, TextField, and Button classes (such as `_alpha`, `_height`, `_name`, `_width`, `_x`, `_y`, and others) have equivalents in the ActionScript 3.0 DisplayObject class that are renamed so that they no longer begin with the underscore (_) character.

For more information, see the "Display Programming" chapter of the _ActionScript 3.0 Developer's Guide_.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.DisplayObjectContainer](../display/DisplayObjectContainer.html)

  

* * *