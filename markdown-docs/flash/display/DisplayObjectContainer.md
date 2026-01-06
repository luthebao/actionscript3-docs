# Displayobjectcontainer

Package| [flash.display](package-detail.html)  
---|---  
Class| public class DisplayObjectContainer  
Inheritance| DisplayObjectContainer ![Inheritance](../../images/inherit-arrow.gif) [InteractiveObject](InteractiveObject.html) ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [Loader](../display/Loader.html), [Sprite](../display/Sprite.html), [Stage](../display/Stage.html), [TextLine](../text/engine/TextLine.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The DisplayObjectContainer class is the base class for all objects that can serve as display object containers on the display list. The display list manages all objects displayed in the Flash runtimes. Use the DisplayObjectContainer class to arrange the display objects in the display list. Each DisplayObjectContainer object has its own child list for organizing the z-order of the objects. The z-order is the front-to-back order that determines which object is drawn in front, which is behind, and so on. 

DisplayObject is an abstract base class; therefore, you cannot call DisplayObject directly. Invoking `new DisplayObject()` throws an `ArgumentError` exception.

The DisplayObjectContainer class is an abstract base class for all objects that can contain child objects. It cannot be instantiated directly; calling the `new DisplayObjectContainer()` constructor throws an `ArgumentError` exception. 

For more information, see the "Display Programming" chapter of the _ActionScript 3.0 Developer's Guide_.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.DisplayObject](../display/DisplayObject.html)

  

* * *