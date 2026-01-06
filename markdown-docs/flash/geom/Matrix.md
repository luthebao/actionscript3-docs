# Matrix

Package| [flash.geom](package-detail.html)  
---|---  
Class| public class Matrix  
Inheritance| Matrix ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Matrix class represents a transformation matrix that determines how to map points from one coordinate space to another. You can perform various graphical transformations on a display object by setting the properties of a Matrix object, applying that Matrix object to the `matrix` property of a Transform object, and then applying that Transform object as the `transform` property of the display object. These transformation functions include translation (_x_ and _y_ repositioning), rotation, scaling, and skewing. 

Together these types of transformations are known as _affine transformations_. Affine transformations preserve the straightness of lines while transforming, so that parallel lines stay parallel.

To apply a transformation matrix to a display object, you create a Transform object, set its `matrix` property to the transformation matrix, and then set the `transform` property of the display object to the Transform object. Matrix objects are also used as parameters of some methods, such as the following:

  * The `draw()` method of a BitmapData object
  * The `beginBitmapFill()` method, `beginGradientFill()` method, or `lineGradientStyle()` method of a Graphics object

A transformation matrix object is a 3 x 3 matrix with the following contents:

![Matrix class properties in matrix notation](../../images/matrix_props1.jpg)

In traditional transformation matrixes, the `u`, `v`, and `w` properties provide extra capabilities. The Matrix class can only operate in two-dimensional space, so it always assumes that the property values `u` and `v` are 0.0, and that the property value `w` is 1.0. The effective values of the matrix are as follows:

![Matrix class properties in matrix notation showing 

 assumed values for u, v, and w](../../images/matrix_props2.jpg)

You can get and set the values of all six of the other properties in a Matrix object: `a`, `b`, `c`, `d`, `tx`, and `ty`.

The Matrix class supports the four major types of transformations: translation, scaling, rotation, and skewing. You can set three of these transformations by using specialized methods, as described in the following table: 

Transformation | Method | Matrix values | Display result | Description  
---|---|---|---|---  
Translation (displacement) | `translate(tx, ty)` | ![Matrix notation of translate method parameters](../../images/matrix_translate.jpg) | ![Illustration of translate method effects](../../images/matrix_translate_image.jpg) | Moves the image `tx` pixels to the right and `ty` pixels down.  
Scaling | `scale(sx, sy)` | ![Matrix notation of scale method parameters](../../images/matrix_scale.jpg) | ![Illustration of scale method effects](../../images/matrix_scale_image.jpg) | Resizes the image, multiplying the location of each pixel by `sx` on the _x_ axis and `sy` on the _y_ axis.  
Rotation | `rotate(q)` | ![Matrix notation of rotate method properties](../../images/matrix_rotate.jpg) | ![Illustration of rotate method effects](../../images/matrix_rotate_image.jpg) | Rotates the image by an angle `q`, which is measured in radians.  
Skewing or shearing  | None; must set the properties `b` and `c` | ![Matrix notation of skew function properties](../../images/matrix_skew.jpg) | ![Illustration of skew function effects](../../images/matrix_skew_image.jpg) | Progressively slides the image in a direction parallel to the _x_ or _y_ axis. The `b` property of the Matrix object represents the tangent of the skew angle along the _y_ axis; the `c` property of the Matrix object represents the tangent of the skew angle along the _x_ axis.  
  
Each transformation function alters the current matrix properties so that you can effectively combine multiple transformations. To do this, you call more than one transformation function before applying the matrix to its display object target (by using the `transform` property of that display object).

Use the `new Matrix()` constructor to create a Matrix object before you can call the methods of the Matrix object.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.DisplayObject.transform](../display/DisplayObject.html#transform)   
[flash.geom.Transform](../geom/Transform.html)   
[flash.display.BitmapData.draw()](../display/BitmapData.html#draw\(\))   
[flash.display.Graphics.beginBitmapFill()](../display/Graphics.html#beginBitmapFill\(\))   
[flash.display.Graphics.beginGradientFill()](../display/Graphics.html#beginGradientFill\(\))   
[flash.display.Graphics.lineGradientStyle()](../display/Graphics.html#lineGradientStyle\(\))

  

* * *