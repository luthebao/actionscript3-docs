# Typeerror

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class TypeError  
Inheritance| TypeError ![Inheritance](images/inherit-arrow.gif) [Error](Error.html) ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A TypeError exception is thrown when the actual type of an operand is different from the expected type. 

In addition, this exception is thrown when: 

  * An actual parameter to a function or method could not be coerced to the formal parameter type.
  * A value is assigned to a variable and cannot be coerced to the variable's type.
  * The right side of the `is` or `instanceof` operator is not a valid type.
  * The `super` keyword is used illegally.
  * A property lookup results in more than one binding, and is therefore ambiguous.
  * A method is invoked on an incompatible object. For example, a TypeError exception is thrown if a RegExp class method is "grafted" onto a generic object and then invoked.

[View the examples.](#includeExamplesSummary)

See also

[is operator](operators.html#is)   
[instanceof operator](operators.html#instanceof)   
[super statement](statements.html#super)   
[RegExp class](RegExp.html)

  

* * *