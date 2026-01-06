# Arguments

Package| [Top Level](package-detail.html)  
---|---  
Class| public class arguments  
Inheritance| arguments ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
An arguments object is used to store and access a function's arguments. Within a function's body, you can access its arguments object by using the local arguments variable. 

The arguments are stored as array elements: the first is accessed as `arguments[0]`, the second as `arguments[1]`, and so on. The `arguments.length` property indicates the number of arguments passed to the function. There may be a different number of arguments passed than the function declares. 

Unlike previous versions of ActionScript, ActionScript 3.0 has no `arguments.caller` property. To get a reference to the function that called the current function, you must pass a reference to that function as an argument. An example of this technique can be found in the example for `arguments.callee`. 

ActionScript 3.0 includes a new `...(rest)` keyword that is recommended instead of the arguments class.

[View the examples.](#includeExamplesSummary)

See also

[...(rest)](statements.html#..._\(rest\)_parameter)   
[Function](Function.html)

  

* * *