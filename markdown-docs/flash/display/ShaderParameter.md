# Shaderparameter

Package| [flash.display](package-detail.html)  
---|---  
Class| public final dynamic class ShaderParameter  
Inheritance| ShaderParameter ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
A ShaderParameter instance represents a single input parameter of a shader kernel. A kernel can be defined to accept zero, one, or more parameters that are used in the kernel execution. A ShaderParameter provides information about the parameter, such as the type of data it expects. It also provides a mechanism for setting the parameter value that is used when the shader executes. To specify a value or values for the shader parameter, create an Array containing the value or values and assign it to the `value` property. 

A ShaderParameter instance representing a parameter for a Shader instance is accessed as a property of the Shader instance's `data` property. The ShaderParameter property has the same name as the parameter's name in the shader code. For example, if a shader defines a parameter named `radius`, the ShaderParameter instance representing the `radius` parameter is available as the `radius` property, as shown here:
    
    
    var radiusParam:ShaderParameter = myShader.data.radius;

In addition to the defined properties of the ShaderParameter class, each ShaderParameter instance has additional properties corresponding to any metadata defined for the parameter. These properties are added to the ShaderParameter object when it is created. The properties' names match the metadata names specified in the shader's source code. The data type of each property varies according to the data type of the corresponding metadata. A text metadata value such as "description" is a String instance. A metadata property with a non-string value (such as `minValue` or `defaultValue`) is represented as an Array instance. The number of elements and element data types correspond to the metadata values.

For example, suppose a shader includes the following two parameter declarations:
    
    
    	 parameter float2 size
    	 <
    	     description: "The size of the image to which the kernel is applied";
    	     minValue: float2(0.0, 0.0);
    	     maxValue: float2(100.0, 100.0);
    	     defaultValue: float2(50.0, 50.0);
    	 >;
    	 
    	 parameter float radius
    	 <
    	     description: "The radius of the effect";
    	     minValue: 0.0;
    	     maxValue: 50.0;
    	     defaultValue: 25.0;
    	 >;
    	 

The ShaderParameter instance corresponding to the `size` parameter has the following metadata properties in addition to its built-in properties:

Property name | Data type | Value  
---|---|---  
`name` | String | `"size"`  
`description` | String | `"The size of the image to which the kernel is applied"`  
`minValue` | Array | `[0, 0]`  
`maxValue` | Array | `[100, 100]`  
`defaultValue` | Array | `[50, 50]`  
  
The ShaderParameter corresponding to the `radius` parameter has the following additional properties:

Property name | Data type | Value  
---|---|---  
`name` | String | `"radius"`  
`description` | String | `"The radius of the effect"`  
`minValue` | Array | `[0]`  
`maxValue` | Array | `[50]`  
`defaultValue` | Array | `[25]`  
  
Generally, developer code does not create a ShaderParameter instance directly. A ShaderParameter instance is created for each of a shader's parameters when the Shader instance is created.

See also

[flash.display.ShaderData](../display/ShaderData.html)   
[flash.display.Shader.data](../display/Shader.html#data)

  

* * *