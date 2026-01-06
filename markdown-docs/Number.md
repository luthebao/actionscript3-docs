# Number

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class Number  
Inheritance| Number ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
A data type representing an IEEE-754 double-precision floating-point number. You can manipulate primitive numeric values by using the methods and properties associated with the Number class. This class is identical to the JavaScript Number class. 

The properties of the Number class are static, which means you do not need an object to use them, so you do not need to use the constructor.

The Number data type adheres to the double-precision IEEE-754 standard. 

The Number data type is useful when you need to use floating-point values. Flash runtimes handle int and uint data types more efficiently than Number, but Number is useful in situations where the range of values required exceeds the valid range of the int and uint data types. The Number class can be used to represent integer values well beyond the valid range of the int and uint data types. The Number data type can use up to 53 bits to represent integer values, compared to the 32 bits available to int and uint. The default value of a variable typed as Number is `NaN` (Not a Number).

[View the examples.](#includeExamplesSummary)

See also

[int](int.html)   
[uint](uint.html)

  

* * *