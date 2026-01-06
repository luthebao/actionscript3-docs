# Vector3D

Package| [flash.geom](package-detail.html)  
---|---  
Class| public class Vector3D  
Inheritance| Vector3D ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The Vector3D class represents a point or a location in the three-dimensional space using the Cartesian coordinates x, y, and z. As in a two-dimensional space, the `x` property represents the horizontal axis and the `y` property represents the vertical axis. In three-dimensional space, the `z` property represents depth. The value of the `x` property increases as the object moves to the right. The value of the `y` property increases as the object moves down. The `z` property increases as the object moves farther from the point of view. Using perspective projection and scaling, the object is seen to be bigger when near and smaller when farther away from the screen. As in a right-handed three-dimensional coordinate system, the positive z-axis points away from the viewer and the value of the `z` property increases as the object moves away from the viewer's eye. The origin point (0,0,0) of the global space is the upper-left corner of the stage. 

![X, Y, Z Axes](../../images/xyzAxes.jpg)

The Vector3D class can also represent a direction, an arrow pointing from the origin of the coordinates, such as (0,0,0), to an endpoint; or a floating-point component of an RGB (Red, Green, Blue) color model.

Quaternion notation introduces a fourth element, the `w` property, which provides additional orientation information. For example, the `w` property can define an angle of rotation of a Vector3D object. The combination of the angle of rotation and the coordinates x, y, and z can determine the display object's orientation. Here is a representation of Vector3D elements in matrix notation:

![Vector3D elements](../../images/Vector3Delements.jpg)

See also

[flash.display.DisplayObject](../display/DisplayObject.html)   
[flash.geom.Point](../geom/Point.html)   
[flash.geom.Matrix3D](../geom/Matrix3D.html)   
[flash.geom.Utils3D](../geom/Utils3D.html)   
[Vector](../../Vector.html)

  

* * *