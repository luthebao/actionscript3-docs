# Context3D

Package| [flash.display3D](package-detail.html)  
---|---  
Class| public final class Context3D  
Inheritance| Context3D ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The Context3D class provides a context for rendering geometrically defined graphics. 

A rendering context includes a drawing surface and its associated resources and state. When possible, the rendering context uses the hardware graphics processing unit (GPU). Otherwise, the rendering context uses software. (If rendering through Context3D is not supported on a platform, the `stage3Ds` property of the Stage object contains an empty list.)

The Context3D rendering context is a programmable pipeline that is very similar to OpenGL ES 2, but is abstracted so that it is compatible with a range of hardware and GPU interfaces. Although designed for 3D graphics, the rendering pipeline does not mandate that the rendering is three dimensional. Thus, you can create a 2D renderer by supplying the appropriate vertex and pixel fragment programs. In both the 3D and 2D cases, the only geometric primitive supported is the triangle.

Get an instance of the Context3D class by calling the `requestContext3D()` method of a Stage3D object. A limited number of Context3D objects can exist per stage; one for each Stage3D in the `Stage.stage3Ds` list. When the context is created, the Stage3D object dispatches a `context3DCreate` event. A rendering context can be destroyed and recreated at any time, such as when another application that uses the GPU gains focus. Your code should anticipate receiving multiple `context3DCreate` events. Position the rendering area on the stage using the `x` and `y` properties of the associated Stage3D instance.

When the rendering context is attached to the stage of an HTML window, the default background of the HTMLLoader object obscures the 3D viewport. To turn off the default background, set the `paintsDefaultBackground` property to `false`:

`window.htmlLoader.paintsDefaultBackground = false;`

To render and display a scene (after getting a Context3D object), the following steps are typical:

  1. Configure the main display buffer attributes by calling `configureBackBuffer()`.
  2. Create and initialize your rendering resources, including: 
     * Vertex and index buffers defining the scene geometry
     * Vertex and pixel programs (shaders) for rendering the scene
     * Textures
  3. Render a frame: 
     * Set the render state as appropriate for an object or collection of objects in the scene.
     * Call the `drawTriangles()` method to render a set of triangles.
     * Change the rendering state for the next group of objects.
     * Call `drawTriangles()` to draw the triangles defining the objects.
     * Repeat until the scene is entirely rendered.
     * Call the `present()` method to display the rendered scene on the stage.

The following limits apply to rendering:

Resource limits:  Resource | Number allowed | Total memory  
---|---|---  
`Vertex buffers` | 4096 | 256 MB  
`Index buffers` | 4096 | 128 MB  
`Programs` | 4096 | 16 MB  
`Textures` | 4096 | 128 MB  
`Cube textures` | 4096 | 256 MB  
  
AGAL limits: 200 opcodes per program.

Draw call limits: 32,768 `drawTriangles()` calls for each `present()` call.

The following limits apply to textures:

Texture limits for AIR 32 bit:  Texture | Maximum size | Total GPU memory  
---|---|---  
`Normal Texture (below Baseline extended)` | 2048x2048 | 512 MB  
`Normal Texture (Baseline extended and above)` | 4096x4096 | 512 MB  
`Rectangular Texture (below Baseline extended)` | 2048x2048 | 512 MB  
`Rectangular Texture (Baseline extended and above)` | 4096x4096 | 512 MB  
`Cube Texture` | 1024x1024 | 256 MB  
  
Texture limits for AIR 64 bit (Desktop):  Texture | Maximum size | Total GPU memory  
---|---|---  
`Normal Texture (below Baseline extended)` | 2048x2048 | 512 MB  
`Normal Texture (Baseline extended to Standard)` | 4096x4096 | 512 MB  
`Normal Texture (Standard extended and above)` | 4096x4096 | 2048 MB  
`Rectangular Texture (below Baseline extended)` | 2048x2048 | 512 MB  
`Rectangular Texture (Baseline extended to Standard)` | 4096x4096 | 512 MB  
`Rectangular Texture (Standard extended and above)` | 4096x4096 | 2048 MB  
`Cube Texture` | 1024x1024 | 256 MB  
  
512 MB is the absolute limit for textures, including the texture memory required for mipmaps. However, for Cube Textures, the memory limit is 256 MB.

You cannot create Context3D objects with the Context3D constructor. It is constructed and available as a property of a Stage3D instance. The Context3D class can be used on both desktop and mobile platforms, both when running in Flash Player and AIR.

[View the examples.](#includeExamplesSummary)

See also

[Context3DBlendFactor](Context3DBlendFactor.html)   
[Context3DClearMask](Context3DClearMask.html)   
[Context3DCompareMode](Context3DCompareMode.html)   
[Context3DProgramType](Context3DProgramType.html)   
[Context3DRenderMode](Context3DRenderMode.html)   
[Context3DStencilAction](Context3DStencilAction.html)   
[Context3DTextureFormat](Context3DTextureFormat.html)   
[Context3DTriangleFace](Context3DTriangleFace.html)   
[Context3DVertexBufferFormat](Context3DVertexBufferFormat.html)   
[flash.display3D.textures.Texture](textures/Texture.html)   
[flash.display3D.textures.CubeTexture](textures/CubeTexture.html)   
[IndexBuffer3D](IndexBuffer3D.html)   
[flash.geom.Matrix3D](../geom/Matrix3D.html)   
[Program3D](Program3D.html)   
[flash.display.Stage3D](../display/Stage3D.html)   
[VertexBuffer3D](VertexBuffer3D.html)

  

* * *