# Shaderinput

Package| [flash.display](package-detail.html)  
---|---  
Class| public final dynamic class ShaderInput  
Inheritance| ShaderInput ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
A ShaderInput instance represents a single input image for a shader kernel. A kernel can be defined to accept zero, one, or more source images that are used in the kernel execution. A ShaderInput instance provides a mechanism for specifying the input image that is used when the shader executes. To specify a value for the input, create a BitmapData, ByteArray, or Vector.<Number> instance containing the image data and assign it to the `input` property. 

The ShaderInput instance representing a Shader instance's input image is accessed as a property of the Shader instance's `data` property. The ShaderInput property has the same name as the input's name in the shader code. For example, if a shader defines an input named `src`, the ShaderInput instance representing the `src` input is available as the `src` property, as this example shows:
    
    
    myShader.data.src.input = new BitmapData(50, 50, true, 0xFF990000);

For some uses of a Shader instance, you do not need to specify an input image, because it is automatically specified by the operation. You only need to specify an input when a Shader is used for the following:

  * Shader fill
  * ShaderFilter, only for the second or additional inputs if the shader is defined to use more than one input. (The object to which the filter is applied is automatically used as the first input.)
  * Shader blend mode, only for the third or additional inputs if the shader is defined to use more than two inputs. (The objects being blended are automatically used as the first and second inputs.)
  * ShaderJob background execution

If the shader is being executed using a ShaderJob instance to process a ByteArray containing a linear array of data, set the ShaderInput instance's `height` to 1 and `width` to the number of 32-bit floating point values in the ByteArray. In that case, the input in the shader must be defined with the `image1` data type.

Generally, developer code does not create a ShaderInput instance directly. A ShaderInput instance is created for each of a shader's inputs when the Shader instance is created.

See also

[flash.display.ShaderData](../display/ShaderData.html)   
[flash.display.Shader.data](../display/Shader.html#data)   
[flash.display.ShaderJob](../display/ShaderJob.html)

  

* * *