# Interactiveobject

Package| [flash.display](package-detail.html)  
---|---  
Class| public class InteractiveObject  
Inheritance| InteractiveObject ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [DisplayObjectContainer](../display/DisplayObjectContainer.html), [SimpleButton](../display/SimpleButton.html), [TextField](../text/TextField.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The InteractiveObject class is the abstract base class for all display objects with which the user can interact, using the mouse, keyboard, or other user input device. 

You cannot instantiate the InteractiveObject class directly. A call to the `new InteractiveObject()` constructor throws an `ArgumentError` exception.

The InteractiveObject class itself does not include any APIs for rendering content onscreen. To create a custom subclass of the InteractiveObject class, extend one of the subclasses that do have APIs for rendering content onscreen, such as the Sprite, SimpleButton, TextField, or MovieClip classes.

[View the examples.](#includeExamplesSummary)

  

* * *