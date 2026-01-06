# Bitmap

Package| [flash.display](package-detail.html)  
---|---  
Class| public class Bitmap  
Inheritance| Bitmap ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Bitmap class represents display objects that represent bitmap images. These can be images that you load with the flash.display.Loader class, or they can be images that you create with the `Bitmap()` constructor. 

The `Bitmap()` constructor allows you to create a Bitmap object that contains a reference to a BitmapData object. After you create a Bitmap object, use the `addChild()` or `addChildAt()` method of the parent DisplayObjectContainer instance to place the bitmap on the display list.

A Bitmap object can share its BitmapData reference among several Bitmap objects, independent of translation or rotation properties. Because you can create multiple Bitmap objects that reference the same BitmapData object, multiple display objects can use the same complex BitmapData object without incurring the memory overhead of a BitmapData object for each display object instance.

A BitmapData object can be drawn to the screen by a Bitmap object in one of two ways: by using the vector renderer as a fill-bitmap shape, or by using a faster pixel-copying routine. The pixel-copying routine is substantially faster than the vector renderer, but the Bitmap object must meet certain conditions to use it:

  * No stretching, rotation, or skewing can be applied to the Bitmap object.
  * No color transform can be applied to the Bitmap object. 
  * No blend mode can be applied to the Bitmap object. 
  * No clipping can be done through mask layers or `setMask()` methods. 
  * The image itself cannot be a mask. 
  * The destination coordinates must be on a whole pixel boundary. 

If you load a Bitmap object from a domain other than that of the Loader object used to load the image, and there is no URL policy file that permits access to the domain of the Loader object, then a script in that domain cannot access the Bitmap object or its properties and methods. For more information, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

**Note:** The Bitmap class is not a subclass of the InteractiveObject class, so it cannot dispatch mouse events. However, you can use the `addEventListener()` method of the display object container that contains the Bitmap object.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.Loader](../display/Loader.html)   
[flash.display.BitmapData](../display/BitmapData.html)

  

* * *