# Error

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class Error  
Inheritance| Error ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
Subclasses| [ArgumentError](ArgumentError.html), [DefinitionError](DefinitionError.html), [DRMManagerError](flash/errors/DRMManagerError.html), [EvalError](EvalError.html), [InvalidSWFError](flash/errors/InvalidSWFError.html), [PermissionError](flash/errors/PermissionError.html), [RangeError](RangeError.html), [ReferenceError](ReferenceError.html), [ScriptTimeoutError](flash/errors/ScriptTimeoutError.html), [SecurityError](SecurityError.html), [SQLError](flash/errors/SQLError.html), [StackOverflowError](flash/errors/StackOverflowError.html), [SyntaxError](SyntaxError.html), [TypeError](TypeError.html), [URIError](URIError.html), [VerifyError](VerifyError.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The Error class contains information about an error that occurred in a script. In developing ActionScript 3.0 applications, when you run your compiled code in the debugger version of a Flash runtime, a dialog box displays exceptions of type Error, or of a subclass, to help you troubleshoot the code. You create an Error object by using the `Error` constructor function. Typically, you throw a new Error object from within a `try` code block that is caught by a `catch` code block. 

You can also create a subclass of the Error class and throw instances of that subclass.

[View the examples.](#includeExamplesSummary)

  

* * *