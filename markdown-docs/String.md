# String

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class String  
Inheritance| String ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Runtime version:**|  AIR 1.0   
---|---  
  
The String class is a data type that represents a string of characters. The String class provides methods and properties that let you manipulate primitive string value types. You can convert the value of any object into a String data type object using the `String()` function. 

Because all string indexes are zero-based, the index of the last character for any string `x` is `x.length - 1`. 

You can call any of the methods of the String class whether you use the constructor method `new String()` to create a new string variable or simply assign a string literal value. Unlike previous versions of ActionScript, it makes no difference whether you use the constructor, the global function, or simply assign a string literal value. The following lines of code are equivalent: 
    
    
    
     var str:String = new String("foo");
    
     var str:String = "foo";
    
     var str:String = String("foo");

When setting a string variable to `undefined`, the Flash runtimes coerce `undefined` to `null`. So, the statement:
    
    
    
     var s:String = undefined;

sets the value to `null` instead of `undefined`. Use the `String()` function if you need to use `undefined`. 

From AIR SDK version 50 (when using the ActionScript compiler from the 'normal' AIR SDK, rather than Flex or Animate), a "verbatim string" mechanism was added. In a normal string literal, a backslash is used as an escape character, so for example `"\n"` is used for a newline character. This behaviour can be removed if the string literal is preceeded by the `@` character. Hence `"sometimes\never"` would result in a string split across two lines with "sometimes" and "ever", whereas `@"sometimes\never"` would retain the value as written here. This is particularly useful for strings containing file paths on Windows. 

[View the examples.](#includeExamplesSummary)

See also

[String() global function](package.html#String\(\))

  

* * *