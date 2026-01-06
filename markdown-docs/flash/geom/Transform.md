# Transform

Package| [flash.geom](package-detail.html)  
---|---  
Class| public class Transform  
Inheritance| Transform ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Transform class provides access to color adjustment properties and two- or three-dimensional transformation objects that can be applied to a display object. During the transformation, the color or the orientation and position of a display object is adjusted (offset) from the current values or coordinates to new values or coordinates. The Transform class also collects data about color and two-dimensional matrix transformations that are applied to a display object and all of its parent objects. You can access these combined transformations through the `concatenatedColorTransform` and `concatenatedMatrix` properties. 

To apply color transformations: create a ColorTransform object, set the color adjustments using the object's methods and properties, and then assign the `colorTransformation` property of the `transform` property of the display object to the new ColorTransformation object.

To apply two-dimensional transformations: create a Matrix object, set the matrix's two-dimensional transformation, and then assign the `transform.matrix` property of the display object to the new Matrix object.

To apply three-dimensional transformations: start with a three-dimensional display object. A three-dimensional display object has a `z` property value other than zero. You do not need to create the Matrix3D object. For all three-dimensional objects, a Matrix3D object is created automatically when you assign a `z` value to a display object. You can access the display object's Matrix3D object through the display object's `transform` property. Using the methods of the Matrix3D class, you can add to or modify the existing transformation settings. Also, you can create a custom Matrix3D object, set the custom Matrix3D object's transformation elements, and then assign the new Matrix3D object to the display object using the `transform.matrix` property.

To modify a perspective projection of the stage or root object: use the `transform.matrix` property of the root display object to gain access to the PerspectiveProjection object. Or, apply different perspective projection properties to a display object by setting the perspective projection properties of the display object's parent. The child display object inherits the new properties. Specifically, create a PerspectiveProjection object and set its properties, then assign the PerspectiveProjection object to the `perspectiveProjection` property of the parent display object's `transform` property. The specified projection transformation then applies to all the display object's three-dimensional children.

Since both PerspectiveProjection and Matrix3D objects perform perspective transformations, do not assign both to a display object at the same time. Use the PerspectiveProjection object for focal length and projection center changes. For more control over the perspective transformation, create a perspective projection Matrix3D object.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.DisplayObject.transform](../display/DisplayObject.html#transform)   
[flash.geom.ColorTransform](../geom/ColorTransform.html)   
[flash.geom.Matrix](../geom/Matrix.html)   
[flash.geom.Matrix3D](../geom/Matrix3D.html)   
[flash.geom.PerspectiveProjection](../geom/PerspectiveProjection.html)

  

* * *