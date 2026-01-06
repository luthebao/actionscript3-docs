# Specialtypes

The three special types are the untyped specifier (*), `void`, and `Null`.

  
| Type| Description  
---|---|---  
| [*](#*)| Specifies that a property is untyped.  
| [void](#void)| Specifies that a function cannot return any value.  
| [Null](#Null)| A special data type that represents the lack of a value.  
  
Special Type detail

*| special type  
---|---  
  
Usage   
`propertyName:*`  

**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a property is untyped. Use of the asterisk symbol for a type annotation is equivalent to using no type annotation. Expressions that read from untyped properties are considered untyped expressions. Use of untyped expressions or properties is recommended in the following circumstances: 

  * When you want to defer type checking to runtime. You can use an untyped property or expression to circumvent compile-time type checking in strict mode. Note, however, that runtime type checking of assignment statements occurs whether you use strict mode or not.
  * When you want to store the value `undefined` in a property. Unlike previous versions of ActionScript, the value `undefined` is not a member of the Object data type. You must use an untyped property to store the value `undefined`.

See also

[Object](Object.html)

void| special type|   
---|---|---  
  
Usage   
`functionName():void {}`  

**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a function cannot return any value. The `void` type is a special type that contains exactly one value: `undefined`. It is special in that its use is limited to the return type of a function. You cannot use `void` as a type annotation for a property.

See also

[undefined](package.html#undefined)

Null| special type|   
---|---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
A special data type that represents the lack of a value. The `Null` data type includes only one value: `null`. The `Null` data type is special in that it is not associated with a class. This means that you cannot use the `Null` data type as a type annotation for a property.

See also

[null](statements.html#null)

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:13 PM GMT+01:00\) : Special Types)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:13 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)