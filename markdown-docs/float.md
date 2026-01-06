# Float

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class float  
Inheritance| float ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 51.0   
---|---  
  
A data type representing an IEEE-754 single-precision floating-point number. You can manipulate primitive numeric values by using the methods and properties associated with the float class, as well as normal arithmetic operators. 

Float values are stored as 32-bit values and are supported in ActionScript Byte Code version 47.16 and above. To use single-precision floating point functionality, you will need to compile your application using the AIR compiler version 3.0.0 or above (provided with AIR SDK 51.0), and the target AIR runtime would need to be AIR 51.0 or above.

The properties of the float class are static, which means you do not need an object to use them, so you do not need to use the constructor.

The float data type adheres to the single-precision IEEE-754 standard. 

The float data type is useful when you need to use floating-point values without needing the precision or using the memory associated with the double-precision `Number` type. This can be particularly useful when interacting with graphical systems such as the Stage3D APIs, where `float`-specific functions are now available for program constants and vertex buffers.

The default value of a variable typed as flat is `NaN` (Not a Number). To assign number values to a `float` variable, an 'f' character should be appended to the value - for example:

` var floatVal:float = 1.23f;`

Note that when a `float` value is converted into a `String`, the internal functionality will promote the single-precision value into a double-precision value which will then be converted into a string. Some precision changes may occur during this promotion/conversion process.

See also

[int](int.html)   
[uint](uint.html)   
[Number](Number.html)

  

* * *