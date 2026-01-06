# Shaderjob

Package| [flash.display](package-detail.html)  
---|---  
Class| public class ShaderJob  
Inheritance| ShaderJob ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
A ShaderJob instance is used to execute a shader operation in stand-alone mode. The shader operation executes and returns its result data. It is up to the developer to determine how to use the result. 

There are two primary reasons for using a shader in stand-alone mode:

  * Processing non-image data: Using a ShaderJob instance you have control over input values and over how the shader result is used. The shader can return the result as binary data or number data instead of image data.
  * Background processing: Some shaders are complex and require a notable amount of time to execute. Executing a complex shader in the main execution of an application could slow down other parts of the application such as user interaction or updating the screen. Using a ShaderJob instance, you can execute the shader in the background. When the shader is executed in this way, the shader operation runs separate from the main execution of the application.

The `shader` property (or constructor parameter) specifies the Shader instance representing the shader that is used for the operation. You provide any parameter or input that the shader expects using the associated ShaderParameter or ShaderInput instance.

Before execution a ShaderJob operation, you provide an object into which the result is written, by setting it as the value of the `target` property. When the shader operation completes the result is written into the `target` object.

To begin a background shader operation, call the `start()` method. When the operation finishes the result is written into the `target` object. At that point the ShaderJob instance dispatches a `complete` event, notifying listeners that the result is available.

To execute a shader synchronously (that is, not running in the background), call the `start()` method and pass `true` as an argument. The shader runs in the main execution thread and your code pauses until the operation completes. When it finishes the result is written into the `target` object. At that point the application continues running at the next line of code.

See also

[Shader](Shader.html)   
[ShaderInput](ShaderInput.html)   
[ShaderParameter](ShaderParameter.html)   
[ShaderEvent](../events/ShaderEvent.html)

  

* * *