# Indexbuffer3D

Package| [flash.display3D](package-detail.html)  
---|---  
Class| public final class IndexBuffer3D  
Inheritance| IndexBuffer3D ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
IndexBuffer3D is used to represent lists of vertex indices comprising graphic elements retained by the graphics subsystem. 

Indices managed by an IndexBuffer3D object may be used to select vertices from a vertex stream. Indices are 16-bit unsigned integers. The maximum allowable index value is 65535 (0xffff). The graphics subsystem does not retain a reference to vertices provided to this object. Data uploaded to this object may be modified or discarded without affecting the stored values.

IndexBuffer3D cannot be instantiated directly. Create instances by using Context3D::CreateIndexBuffer()

See also

flash.display.Context3D.createIndexBuffer()  
flash.display.Context3D.drawTriangles()

  

* * *