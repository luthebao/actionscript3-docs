# Vertexbuffer3D

Package| [flash.display3D](package-detail.html)  
---|---  
Class| public class VertexBuffer3D  
Inheritance| VertexBuffer3D ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The VertexBuffer3D class represents a set of vertex data uploaded to a rendering context. 

Use a VertexBuffer3D object to define the data associated with each point in a set of vertexes. You can upload the vertex data either from a Vector array or a ByteArray. (Once uploaded, the data in the original array is no longer referenced; changing or discarding the source array does not change the vertex data.)

The data associated with each vertex is in an application-defined format and is used as the input for the vertex shader program. Identify which values belong to which vertex program input using the Context3D `setVertexBufferAt()` function. A vertex program can use up to eight inputs (also known as vertex attribute registers). Each input can require between one and four 32-bit values. For example, the [x,y,z] position coordinates of a vertex can be passed to a vertex program as a vector containing three 32 bit values. The Context3DVertexBufferFormat class defines constants for the supported formats for shader inputs. You can supply up to sixty-four 32-bit values (256 bytes) of data for each point (but a single vertex shader cannot use all of the data in this case).

The `setVertexBufferAt()` function also identifies which vertex buffer to use for rendering any subsequent `drawTriangles()` calls. To render data from a different vertex buffer, call `setVertexBufferAt()` again with the appropriate arguments. (You can store data for the same point in multiple vertex buffers, say position data in one buffer and texture coordinates in another, but typically rendering is more efficient if all the data for a point comes from a single buffer.)

The Index3DBuffer object passed to the Context3D `drawTriangles()` method organizes the vertex data into triangles. Each value in the index buffer is the index to a vertex in the vertex buffer. A set of three indexes, in sequence, defines a triangle.

You cannot create a VertexBuffer3D object directly. Use the Context3D `createVertexBuffer()` method instead.

To free the render context resources associated with a vertex buffer, call the object's `dispose()` method.

[View the examples.](#includeExamplesSummary)

See also

[Context3D.createVertexBuffer()](Context3D.html#createVertexBuffer\(\))   
[Context3D.setVertexBufferAt()](Context3D.html#setVertexBufferAt\(\))   
[Context3DVertexBufferFormat](Context3DVertexBufferFormat.html)

  

* * *