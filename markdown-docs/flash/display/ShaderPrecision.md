# Shaderprecision

Package| [flash.display](package-detail.html)  
---|---  
Class| public final class ShaderPrecision  
Inheritance| ShaderPrecision ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
This class defines the constants that represent the possible values for the Shader class's `precisionHint` property. Each constant represents one of the precision modes for executing shader operations. 

The precision mode selection affects the following shader operations. These operations are faster on an Intel processor with the SSE instruction set:

  * `sin(x)`
  * `cos(x)`
  * `tan(x)`
  * `asin(x)`
  * `acos(x)`
  * `atan(x)`
  * `atan(x, y)`
  * `exp(x)`
  * `exp2(x)`
  * `log(x)`
  * `log2(x)`
  * `pow(x, y)`
  * `reciprocal(x)`
  * `sqrt(x)`

See also

[flash.display.Shader.precisionHint](../display/Shader.html#precisionHint)

  

* * *