# Program3D

Package| [flash.display3D](package-detail.html)  
---|---  
Class| public final class Program3D  
Inheritance| Program3D ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The Program3D class represents a pair of rendering programs (also called "shaders") uploaded to the rendering context. 

Programs managed by a Program3D object control the entire rendering of triangles during a Context3D `drawTriangles()` call. Upload the binary bytecode to the rendering context using the `upload` method. (Once uploaded, the program in the original byte array is no longer referenced; changing or discarding the source byte array does not change the program.)

Programs always consist of two linked parts: A vertex and a fragment program. 

  1. The vertex program operates on data defined in VertexBuffer3D objects and is responsible for projecting vertices into clip space and passing any required vertex data, such as color, to the fragment shader.
  2. The fragment shader operates on the attributes passed to it by the vertex program and produces a color for every rasterized fragment of a triangle, resulting in pixel colors. Note that fragment programs have several names in 3D programming literature, including fragment shader and pixel shader.

Designate which program pair to use for subsequent rendering operations by passing the corresponding Program3D instance to the Context3D `setProgram()` method.

You cannot create a Program3D object directly; use the Context3D `createProgram()` method instead.

See also

[Context3D.createProgram()](Context3D.html#createProgram\(\))   
[Context3D.setProgram()](Context3D.html#setProgram\(\))

  

* * *