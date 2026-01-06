# Triangleculling

Package| [flash.display](package-detail.html)  
---|---  
Class| public final class TriangleCulling  
Inheritance| TriangleCulling ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
Defines codes for culling algorithms that determine which triangles not to render when drawing triangle paths. 

The terms `POSITIVE` and `NEGATIVE` refer to the sign of a triangle's normal along the z-axis. The normal is a 3D vector that is perpendicular to the surface of the triangle. 

A triangle whose vertices 0, 1, and 2 are arranged in a clockwise order has a positive normal value. That is, its normal points in a positive z-axis direction, away from the current view point. When the `TriangleCulling.POSITIVE` algorithm is used, triangles with positive normals are not rendered. Another term for this is backface culling. 

A triangle whose vertices are arranged in a counter-clockwise order has a negative normal value. That is, its normal points in a negative z-axis direction, toward the current view point. When the `TriangleCulling.NEGATIVE` algorithm is used, triangles with negative normals will not be rendered. 

See also

[flash.display.Graphics.drawTriangles()](../display/Graphics.html#drawTriangles\(\))   
[flash.display.GraphicsTrianglePath](../display/GraphicsTrianglePath.html)   
[Introduction to 3D Vectors](http://www.gamedev.net/reference/articles/article1089.asp)   
[3D Backface Culling](http://www.gamedev.net/reference/articles/article1088.asp)

  

* * *