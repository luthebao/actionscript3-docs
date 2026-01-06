# Uint

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class uint  
Inheritance| uint ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The uint class provides methods for working with a data type representing a 32-bit unsigned integer. Because an unsigned integer can only be positive, its maximum value is twice that of the int class. 

The range of values represented by the uint class is 0 to 4,294,967,295 (2^32-1).

You can create a uint object by declaring a variable of type uint and assigning the variable a literal value. The default value of a variable of type uint is `0`.

The uint class is primarily useful for pixel color values (ARGB and RGBA) and other situations where the int data type does not work well. For example, the number 0xFFFFFFFF, which represents the color value white with an alpha value of 255, can't be represented using the int data type because it is not within the valid range of the int values.

The following example creates a uint object and calls the ` toString()` method:
    
    
    
     var myuint:uint = 1234;
    
     trace(myuint.toString()); // 1234
    
     

The following example assigns the value of the `MIN_VALUE` property to a variable without the use of the constructor:
    
    
    
     var smallest:uint = uint.MIN_VALUE;
    
     trace(smallest.toString()); // 0
    
     

[View the examples.](#includeExamplesSummary)

See also

[int](int.html)   
[Number](Number.html)

  

* * *