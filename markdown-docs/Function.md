# Function

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class Function  
Inheritance| Function ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A function is the basic unit of code that can be invoked in ActionScript. Both user-defined and built-in functions in ActionScript are represented by Function objects, which are instances of the Function class. 

Methods of a class are slightly different than Function objects. Unlike an ordinary function object, a method is tightly linked to its associated class object. Therefore, a method or property has a definition that is shared among all instances of the same class. Methods can be extracted from an instance and treated as "bound" methods (retaining the link to the original instance). For a bound method, the `this` keyword points to the original object that implemented the method. For a function, `this` points to the associated object at the time the function is invoked.

[View the examples.](#includeExamplesSummary)

  

* * *