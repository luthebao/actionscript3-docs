# Math

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class Math  
Inheritance| Math ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Math class contains methods and constants that represent common mathematical functions and values. 

Use the methods and properties of this class to access and manipulate mathematical constants and functions. All the properties and methods of the Math class are static and must be called using the syntax `Math.method(``_parameter_``)` or `Math.constant`. In ActionScript, constants are defined with the maximum precision of double-precision IEEE-754 floating-point numbers.

Several Math class methods use the measure of an angle in radians as a parameter. You can use the following equation to calculate radian values before calling the method and then provide the calculated value as the parameter, or you can provide the entire right side of the equation (with the angle's measure in degrees in place of `degrees`) as the radian parameter.

To calculate a radian value, use the following formula:
    
    
    
     radians = degrees * Math.PI/180
    
     

To calculate degrees from radians, use the following formula:
    
    
    
     degrees = radians * 180/Math.PI
    
     

The following is an example of passing the equation as a parameter to calculate the sine of a 45° angle:

`Math.sin(45 * Math.PI/180)` is the same as `Math.sin(.7854)`

**Note:** The Math functions acos, asin, atan, atan2, cos, exp, log, pow, sin, and sqrt may result in slightly different values depending on the algorithms used by the CPU or operating system. Flash runtimes call on the CPU (or operating system if the CPU doesn't support floating point calculations) when performing the calculations for the listed functions, and results have shown slight variations depending upon the CPU or operating system in use. 

  

* * *