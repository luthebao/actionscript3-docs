# Perspectiveprojection

Package| [flash.geom](package-detail.html)  
---|---  
Class| public class PerspectiveProjection  
Inheritance| PerspectiveProjection ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The PerspectiveProjection class provides an easy way to assign or modify the perspective transformations of a display object and all of its children. For more complex or custom perspective transformations, use the Matrix3D class. While the PerspectiveProjection class provides basic three-dimensional presentation properties, the Matrix3D class provides more detailed control over the three-dimensional presentation of display objects. 

Projection is a way of representing a three-dimensional object in a two-dimensional space, like a cube projected onto a computer screen. Perspective projection uses a viewing frustum (a rectangular pyramid) to model and project a three-dimensional world and its objects on the screen. The viewing frustum becomes increasingly wider as it moves further from the origin of the viewpoint. The origin of the viewpoint could be a camera or the eyes of an observer facing the screen. The projected perspective produces the illusion of three dimensions with depth and distance, where the objects closer to the screen appear larger than the objects farther from the screen.

![Frustum viewing area](../../images/frustum.jpg)

A default PerspectiveProjection object is a framework defined for perspective transformation of the root object, based on the field of view and aspect ratio (dimensions) of the stage. The projection center, the vanishing point, is set to the center of the stage, which means the three-dimensional display objects disappear toward the center of the stage as they move back in the z axis. The default viewpoint is at point (0,0) looking down the positive z axis. The y-axis points down toward the bottom of the screen. You can gain access to the `root` display object's perspective projection settings and change the field of view and projection center properties of the `perspectiveProjection` property through the `root` object's `DisplayObject.transform` property.

You can also set a different perspective projection setting for a display object through the parent's perspective projection. First, create a PerspectiveProjection object and set its `fieldOfView` and `projectionCenter` properties. Next, assign the PerspectiveProjection object to the parent display object using the `DisplayObject.transform` property. The specified projection matrix and transformation will then apply to all the display object's three-dimensional children.

See also

[flash.display.DisplayObject.transform](../display/DisplayObject.html#transform)   
[flash.geom.Transform](../geom/Transform.html)   
[flash.geom.Matrix3D](../geom/Matrix3D.html)   
[flash.geom.Utils3D](../geom/Utils3D.html)

  

* * *