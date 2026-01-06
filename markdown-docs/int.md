# Int

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class int  
Inheritance| int ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The int class lets you work with the data type representing a 32-bit signed integer. The range of values represented by the int class is -2,147,483,648 (-2^31) to 2,147,483,647 (2^31-1). 

The constant properties of the int class, `MAX_VALUE` and `MIN_VALUE`, are static, which means that you don't need an object to use them, so you don't need to use the constructor. The methods, however, are not static, which means that you do need an object to use them. You can create an int object by using the int class constructor or by declaring a variable of type int and assigning the variable a literal value.

The int data type is useful for loop counters and other situations where a floating point number is not needed, and is similar to the int data type in Java and C++. The default value of a variable typed as int is `0`

If you are working with numbers that exceed `int.MAX_VALUE`, consider using Number. 

The following example calls the `toString()` method of the int class, which returns the string `1234`: 
    
    
    
     var myint:int = 1234;
    
     myint.toString();
    
     

The following example assigns the value of the `MIN_VALUE` property to a variable declared without the use of the constructor:
    
    
    
     var smallest:int = int.MIN_VALUE;
    
     

[View the examples.](#includeExamplesSummary)

See also

[uint](uint.html)   
[Number](Number.html)

  

* * *