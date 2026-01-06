# Matrix3D

Package| [flash.geom](package-detail.html)  
---|---  
Class| public class Matrix3D  
Inheritance| Matrix3D ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The Matrix3D class represents a transformation matrix that determines the position and orientation of a three-dimensional (3D) display object. The matrix can perform transformation functions including translation (repositioning along the x, y, and z axes), rotation, and scaling (resizing). The Matrix3D class can also perform perspective projection, which maps points from the 3D coordinate space to a two-dimensional (2D) view. 

A single matrix can combine multiple transformations and apply them at once to a 3D display object. For example, a matrix can be applied to 3D coordinates to perform a rotation followed by a translation. 

When you explicitly set the `z` property or any of the rotation or scaling properties of a display object, a corresponding Matrix3D object is automatically created.

You can access a 3D display object's Matrix3D object through the `transform.matrix3d` property. 2D objects do not have a Matrix3D object. 

The value of the `z` property of a 2D object is zero and the value of its `matrix3D` property is `null`.

**Note:** If the same Matrix3D object is assigned to two different display objects, a runtime error is thrown.

The Matrix3D class uses a 4x4 square matrix: a table of four rows and columns of numbers that hold the data for the transformation. The first three rows of the matrix hold data for each 3D axis (x,y,z). The translation information is in the last column. The orientation and scaling data are in the first three columns. The scaling factors are the diagonal numbers in the first three columns. Here is a representation of Matrix3D elements:

![Matrix3D elements](../../images/Matrix3Delements.jpg)

You don't need to understand matrix mathematics to use the Matrix3D class. It offers specific methods that simplify the task of transformation and projection, such as the `appendTranslation()`, `appendRotation()`, or `interpolateTo()` methods. You also can use the `decompose()` and `recompose()` methods or the `rawData` property to access the underlying matrix elements.

Display objects cache their axis rotation properties to have separate rotation for each axis and to manage the different combinations of rotations. When a method of a Matrix3D object is called to transform a display object, the rotation cache of the object is invalidated.

See also

[flash.display.DisplayObject](../display/DisplayObject.html)   
[flash.geom.Transform](../geom/Transform.html)   
[flash.geom.PerspectiveProjection](../geom/PerspectiveProjection.html)   
[flash.geom.Vector3D](../geom/Vector3D.html)   
[flash.geom.Orientation3D](../geom/Orientation3D.html)   
[flash.geom.Utils3D](../geom/Utils3D.html)   
[flash.geom.Matrix](../geom/Matrix.html)

  

* * *