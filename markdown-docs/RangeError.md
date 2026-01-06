# Rangeerror

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class RangeError  
Inheritance| RangeError ![Inheritance](images/inherit-arrow.gif) [Error](Error.html) ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A RangeError exception is thrown when a numeric value is outside the acceptable range. When working with arrays, referring to an index position of an array item that does not exist will throw a RangeError exception. Using `Number.toExponential()`, `Number.toPrecision()`, and `Number.toFixed()` methods will throw a RangeError exception in cases where the arguments are outside the acceptable range of numbers. You can extend `Number.toExponential()`, `Number.toPrecision()`, and `Number.toFixed()` to avoid throwing a RangeError. 

Other situations that cause this exception to be thrown include the following: 

  * Any Flash runtime API that expects a depth number is invoked with an invalid depth number.
  * Any Flash runtime API that expects a frame number is invoked with an invalid frame number.
  * Any Flash runtime API that expects a layer number is invoked with an invalid layer number.

[View the examples.](#includeExamplesSummary)

See also

[Number.toExponential()](Number.html#toExponential\(\))   
[Number.toPrecision()](Number.html#toPrecision\(\))   
[Number.toFixed()](Number.html#toFixed\(\))

  

* * *