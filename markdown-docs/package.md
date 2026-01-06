# Package

Global Functions

| Function| Defined by  
---|---|---  
|  |  [Array](#Array\(\))([...](statements.html#..._\(rest\)_parameter) args):[Array](Array.html) Creates a new array. | Top Level  
|  |  [Boolean](#Boolean\(\))(expression:[Object](Object.html)):[Boolean](Boolean.html) Converts the `expression` parameter to a Boolean value and returns the value. | Top Level  
|  |  [decodeURI](#decodeURI\(\))(uri:[String](String.html)):[String](String.html) Decodes an encoded URI into a string. | Top Level  
|  |  [decodeURIComponent](#decodeURIComponent\(\))(uri:[String](String.html)):[String](String.html) Decodes an encoded URI component into a string. | Top Level  
|  |  [encodeURI](#encodeURI\(\))(uri:[String](String.html)):[String](String.html) Encodes a string into a valid URI (Uniform Resource Identifier). | Top Level  
|  |  [encodeURIComponent](#encodeURIComponent\(\))(uri:[String](String.html)):[String](String.html) Encodes a string into a valid URI component. | Top Level  
|  |  [escape](#escape\(\))(str:[String](String.html)):[String](String.html) Converts the parameter to a string and encodes it in a URL-encoded format, where most nonalphanumeric characters are replaced with `%` hexadecimal sequences. | Top Level  
|  |  [int](#int\(\))(value:[Number](Number.html)):[int](int.html) Converts a given numeric value to an integer value. | Top Level  
|  |  [isFinite](#isFinite\(\))(num:[Number](Number.html)):[Boolean](Boolean.html) Returns `true` if the value is a finite number, or `false` if the value is `Infinity` or `-Infinity`. | Top Level  
|  |  [isNaN](#isNaN\(\))(num:[Number](Number.html)):[Boolean](Boolean.html) Returns `true` if the value is `NaN`(not a number). | Top Level  
|  |  [isXMLName](#isXMLName\(\))(str:[String](String.html)):[Boolean](Boolean.html) Determines whether the specified string is a valid name for an XML element or attribute. | Top Level  
|  |  [Number](#Number\(\))(expression:[Object](Object.html)):[Number](Number.html) Converts a given value to a Number value. | Top Level  
|  |  [Object](#Object\(\))(value:[Object](Object.html)):[Object](Object.html) Every value in ActionScript 3.0 is an object, which means that calling `Object()` on a value returns that value. | Top Level  
|  |  [parseFloat](#parseFloat\(\))(str:[String](String.html)):[Number](Number.html) Converts a string to a floating-point number. | Top Level  
|  |  [parseInt](#parseInt\(\))(str:[String](String.html), radix:[uint](uint.html) = 0):[Number](Number.html) Converts a string to an integer. | Top Level  
|  |  [String](#String\(\))(expression:[Object](Object.html)):[String](String.html) Returns a string representation of the specified parameter. | Top Level  
|  |  [trace](#trace\(\))([...](statements.html#..._\(rest\)_parameter) arguments):[void](specialTypes.html#void) Displays expressions, or writes to log files, while debugging. | Top Level  
|  |  [uint](#uint\(\))(value:[Number](Number.html)):[uint](uint.html) Converts a given numeric value to an unsigned integer value. | Top Level  
|  |  [unescape](#unescape\(\))(str:[String](String.html)):[String](String.html) Evaluates the parameter `str` as a string, decodes the string from URL-encoded format (converting all hexadecimal sequences to ASCII characters), and returns the string. | Top Level  
|  |  [Vector](#Vector\(\))(sourceArray:[Object](Object.html)):[Vector](Vector.html).<T> Creates a new Vector instance whose elements are instances of the specified data type. | Top Level  
|  |  [XML](#XML\(\))(expression:[Object](Object.html)):[XML](XML.html) Converts an object to an XML object. | Top Level  
|  |  [XMLList](#XMLList\(\))(expression:[Object](Object.html)):[XMLList](XMLList.html) Converts an object to an XMLList object. | Top Level  
  
  
  

Global Constants

| Constant| Defined by  
---|---|---  
|  | [Infinity](#Infinity) : [Number](Number.html) A special value representing positive `Infinity`. | Top Level  
|  | [-Infinity](#-Infinity) : [Number](Number.html) A special value representing negative `Infinity`. | Top Level  
|  | [NaN](#NaN) : [Number](Number.html) A special member of the Number data type that represents a value that is "not a number" (`NaN`). | Top Level  
|  | [undefined](#undefined) : [*](specialTypes.html#*) A special value that applies to untyped variables that have not been initialized or dynamic object properties that are not initialized. | Top Level  
  
Function detail

Array| ()| function  
---|---|---  
  
`public function Array([...](statements.html#..._\(rest\)_parameter) args):[Array](Array.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Creates a new array. The array can be of length zero or more, or an array populated by a single specified object. 

  * Calling `Array()` with no arguments returns an empty array.
  * Calling `Array()` with a single integer argument returns an array of the specified length, but whose elements have undefined values.
  * Calling `Array()` with a specified object returns an array with one element of the specified object.

Using the `Array()` function is _similar_ to creating an array with the Array class constructor, but the `Array()` function only allows one, or no, parameter value. You cannot use the the `Array()` function to populate the new array with several values. 

**Note:** If you try to use the `Array()` function to create a new array, and pass several values as parameters to populate the array, you'll get a compiler error. The the `Array()` function only allows one parameter. Use the Array class constructor, instead, to create and populate an array of several values.

The `Array()` function does not cast the type of an object to an array. Use the `as` operator for explicit type conversion, or type casting, when the argument is not a primitive value. For more information, see the Example section of this entry. If you pass an object as a parameter to the `Array()` function, a new array is created containing the object as an element.

Parameters | `[...](statements.html#..._\(rest\)_parameter) args` — You can pass no arguments for an empty array, a single integer argument for an array of a specific length, or a single object to create an array containing the one specified object.   
---|---  
  
Returns | `[Array](Array.html)` — An array of length zero or more.   
---|---  
  
See also

[Array class](Array.html)   
[as operator](operators.html#as)

  
Example   
The following example demonstrates the behavior of the `Array()` function when an argument is not a primitive value. A common use case of casting to an array is the conversion of an Object instance that stores its values in array format. If `Array()` is called with an argument of type `Object`, or any other non-primitive data type, a reference to the object is stored in an element of the new array. In other words, if the only argument passed is an object, a reference to that object becomes the first element of the new array. 
    
    
    var obj:Object = [ "a", "b", "c" ];
          
    var newArray:Array = Array( obj );
    
    trace(newArray == obj);    // false
    trace(newArray[0] == obj); // true
    trace(newArray[0][0])      // a
    trace(newArray[0][1])      // b
    trace(newArray[0][2])      // c

To cast `obj` to an array, use the `as` operator, which returns an array reference if `obj` is a valid array and `null` otherwise: 
    
    
    var obj:Object = [ "a", "b", "c" ];
          
    var newArray:Array = obj as Array;
    
    trace(newArray == obj); // true
    trace(newArray[0]);     // a
    trace(newArray[1]);     // b
    trace(newArray[2]);     // c

Boolean| ()| function|   
---|---|---|---  
  
`public function Boolean(expression:[Object](Object.html)):[Boolean](Boolean.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts the `expression` parameter to a Boolean value and returns the value. 

The return value depends on the data type and value of the argument, as described in the following table:

Input Value | Example | Return Value  
---|---|---  
`0` | `Boolean(0)` | `false`  
`NaN` | `Boolean(NaN)` | `false`  
Number (not `0` or `NaN`) | `Boolean(4)` | `true`  
Empty string | `Boolean("")` | `false`  
Non-empty string | `Boolean("6")` | `true`  
`null` | `Boolean(null)` | `false`  
`undefined` | `Boolean(undefined)` | `false`  
Instance of Object class | `Boolean(new Object())` | `true`  
No argument | `Boolean()` | `false`  
  
Unlike previous versions of ActionScript, the `Boolean()` function returns the same results as does the Boolean class constructor.

Parameters | `expression:[Object](Object.html)` — An expression or object to convert to Boolean.   
---|---  
  
Returns | `[Boolean](Boolean.html)` — The result of the conversion to Boolean.   
---|---  
  
decodeURI| ()| function|   
---|---|---|---  
  
`public function decodeURI(uri:[String](String.html)):[String](String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Decodes an encoded URI into a string. Returns a string in which all characters previously encoded by the `encodeURI` function are restored to their unencoded representation. 

The following table shows the set of escape sequences that are _not_ decoded to characters by the `decodeURI` function. Use `decodeURIComponent()` to decode the escape sequences in this table.

Escape sequences not decoded | Character equivalents  
---|---  
`%23` | `#`  
`%24` | `$`  
`%26` | `&`  
`%2B` | `+`  
`%2C` | `,`  
`%2F` | `/`  
`%3A` | `:`  
`%3B` | `;`  
`%3D` | `=`  
`%3F` | `?`  
`%40` | `@`  
Parameters | `uri:[String](String.html)` — A string encoded with the `encodeURI` function.   
---|---  
  
Returns | `[String](String.html)` — A string in which all characters previously escaped by the `encodeURI` function are restored to their unescaped representation.   
---|---  
  
See also

[decodeURIComponent()](package.html#decodeURIComponent\(\))   
[encodeURI()](package.html#encodeURI\(\))   
[encodeURIComponent()](package.html#encodeURIComponent\(\))

  
Example   

    
    
    package {
        import flash.display.Sprite;
    
    	public class DecodeURIExample extends Sprite {
    		public function DecodeURIExample() {
    			var uri:String = "http://www.example.com/application.jsp?user=<user name='some user'></user>";
    			var encoded:String = encodeURI(uri);
    			var decoded:String = decodeURI(encoded);
    			trace(uri);		// http://www.example.com/application.jsp?user=<user name='some user'></user>
    			trace(encoded);	// http://www.example.com/application.jsp?user=%3Cuser%20name='some%20user'%3E%3C/user%3E
    			trace(decoded);	// http://www.example.com/application.jsp?user=<user name='some user'></user>
    		}
    	}
    }

decodeURIComponent| ()| function|   
---|---|---|---  
  
`public function decodeURIComponent(uri:[String](String.html)):[String](String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Decodes an encoded URI component into a string. Returns a string in which all characters previously escaped by the `encodeURIComponent` function are restored to their uncoded representation. 

This function differs from the `decodeURI()` function in that it is intended for use only with a part of a URI string, called a URI component. A URI component is any text that appears between special characters called _component separators_ (`: / ; and ? `). Common examples of a URI component are "http" and "www.adobe.com".

Another important difference between this function and `decodeURI()` is that because this function assumes that it is processing a URI component it treats the escape sequences that represent special separator characters (`; / ? : @ & = + $ , #`) as regular text that should be decoded. 

Parameters | `uri:[String](String.html)` — A string encoded with the `encodeURIComponent` function.   
---|---  
  
Returns | `[String](String.html)` — A string in which all characters previously escaped by the `encodeURIComponent` function are restored to their unescaped representation.   
---|---  
  
See also

[decodeURI()](package.html#decodeURI\(\))   
[encodeURI()](package.html#encodeURI\(\))   
[encodeURIComponent()](package.html#encodeURIComponent\(\))

encodeURI| ()| function|   
---|---|---|---  
  
`public function encodeURI(uri:[String](String.html)):[String](String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Encodes a string into a valid URI (Uniform Resource Identifier). Converts a complete URI into a string in which all characters are encoded as UTF-8 escape sequences unless a character belongs to a small group of basic characters. 

The following table shows the entire set of basic characters that are _not_ converted to UTF-8 escape sequences by the `encodeURI` function.

Characters not encoded  
---  
`0 1 2 3 4 5 6 7 8 9`  
`a b c d e f g h i j k l m n o p q r s t u v w x y z`  
`A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`  
`; / ? : @ & = + $ , #`  
`- _ . ! ~ * ' ( )`  
Parameters | `uri:[String](String.html)` — A string representing a complete URI.   
---|---  
  
Returns | `[String](String.html)` — A string with certain characters encoded as UTF-8 escape sequences.   
---|---  
  
See also

[decodeURI()](package.html#decodeURI\(\))   
[decodeURIComponent()](package.html#decodeURIComponent\(\))   
[encodeURIComponent()](package.html#encodeURIComponent\(\))

  
Example   

    
    
    package {
        import flash.display.Sprite;
    
    	public class EncodeURIExample extends Sprite {
    		public function EncodeURIExample() {
    			var uri:String = "http://www.example.com/application.jsp?user=<user name='some user'></user>";
    			var encoded:String = encodeURI(uri);
    			var decoded:String = decodeURI(encoded);
    			trace(uri);		// http://www.example.com/application.jsp?user=<user name='some user'></user>
    			trace(encoded);	// http://www.example.com/application.jsp?user=%3Cuser%20name='some%20user'%3E%3C/user%3E
    			trace(decoded);	// http://www.example.com/application.jsp?user=<user name='some user'></user>
    		}
    	}
    }

encodeURIComponent| ()| function|   
---|---|---|---  
  
`public function encodeURIComponent(uri:[String](String.html)):[String](String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Encodes a string into a valid URI component. Converts a substring of a URI into a string in which all characters are encoded as UTF-8 escape sequences unless a character belongs to a very small group of basic characters. 

The `encodeURIComponent()` function differs from the `encodeURI()` function in that it is intended for use only with a part of a URI string, called a URI component. A URI component is any text that appears between special characters called _component separators_ (`: / ; and ? `). Common examples of a URI component are "http" and "www.adobe.com".

Another important difference between this function and `encodeURI()` is that because this function assumes that it is processing a URI component it treats the special separator characters (`; / ? : @ & = + $ , #`) as regular text that should be encoded. 

The following table shows all characters that are _not_ converted to UTF-8 escape sequences by the `encodeURIComponent` function.

Characters not encoded  
---  
`0 1 2 3 4 5 6 7 8 9`  
`a b c d e f g h i j k l m n o p q r s t u v w x y z`  
`A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`  
`- _ . ! ~ * ' ( )`  
Parameters | `uri:[String](String.html)`  
---|---  
  
Returns | `[String](String.html)`  
---|---  
  
See also

[decodeURI()](package.html#decodeURI\(\))   
[decodeURIComponent()](package.html#decodeURIComponent\(\))   
[encodeURI()](package.html#encodeURI\(\))

escape| ()| function|   
---|---|---|---  
  
`public function escape(str:[String](String.html)):[String](String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts the parameter to a string and encodes it in a URL-encoded format, where most nonalphanumeric characters are replaced with `%` hexadecimal sequences. When used in a URL-encoded string, the percentage symbol (`%`) is used to introduce escape characters, and is not equivalent to the modulo operator (`%`). 

The following table shows all characters that are _not_ converted to escape sequences by the `escape()` function.

Characters not encoded  
---  
`0 1 2 3 4 5 6 7 8 9`  
`a b c d e f g h i j k l m n o p q r s t u v w x y z`  
`A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`  
`@ - _ . * + /`  
  
**Note:** Use the `encodeURIComponent()` function, instead of the `escape()` function, to treat special separator characters (`@ + /`) as regular text to encode.

Parameters | `str:[String](String.html)` — The expression to convert into a string and encode in a URL-encoded format.   
---|---  
  
Returns | `[String](String.html)` — A URL-encoded string.   
---|---  
  
See also

[unescape()](package.html#unescape\(\))   
[encodeURIComponent()](package.html#encodeURIComponent\(\))

int| ()| function|   
---|---|---|---  
  
`public function int(value:[Number](Number.html)):[int](int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts a given numeric value to an integer value. Decimal values are truncated at the decimal point. 

Parameters | `value:[Number](Number.html)` — A value to be converted to an integer.   
---|---  
  
Returns | `[int](int.html)` — The converted integer value.   
---|---  
  
See also

[uint()](package.html#uint\(\))

isFinite| ()| function|   
---|---|---|---  
  
`public function isFinite(num:[Number](Number.html)):[Boolean](Boolean.html)`

**Language version:**|  ActionScript 3.0.   
---|---  
**Runtime version:**|   
---|---  
  
Returns `true` if the value is a finite number, or `false` if the value is `Infinity` or `-Infinity`. The presence of `Infinity` or `-Infinity` indicates a mathematical error condition such as division by 0. 

Parameters | `num:[Number](Number.html)` — A number to evaluate as finite or infinite.   
---|---  
  
Returns | `[Boolean](Boolean.html)` — Returns `true` if it is a finite number or `false` if it is infinity or negative infinity   
---|---  
  
isNaN| ()| function|   
---|---|---|---  
  
`public function isNaN(num:[Number](Number.html)):[Boolean](Boolean.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Returns `true` if the value is `NaN`(not a number). The `isNaN()` function is useful for checking whether a mathematical expression evaluates successfully to a number. The most common use of `isNaN()` is to check the value returned from the `parseInt()`and `parseFloat()` functions. The `NaN` value is a special member of the Number data type that represents a value that is "not a number." 

**Note** : The `NaN` value is not a member of the int or uint data types.

The following table describes the return value of `isNaN()` on various input types and values. (If your compiler warnings are set to Strict Mode, some of the following operations will generate compiler warnings.)

Input Type/Value | Example | Return Value  
---|---|---  
0 divided by 0 | `isNaN(0/0)` | `true`  
Non-zero number divided by `0` | `isNaN(5/0)` | `false`  
Square root of a negative number | `isNaN(Math.sqrt(-1))` | `true`  
Arcsine of number greater than 1 or less than 0 | `isNaN(Math.asin(2))` | `true`  
String that can be converted to Number | `isNaN("5")` | `false`  
String that cannot be converted to Number | `isNaN("5a")` | `true`  
Parameters | `num:[Number](Number.html)` — A numeric value or mathematical expression to evaluate.   
---|---  
  
Returns | `[Boolean](Boolean.html)` — Returns `true` if the value is `NaN`(not a number) and `false` otherwise.   
---|---  
  
isXMLName| ()| function|   
---|---|---|---  
  
`public function isXMLName(str:[String](String.html)):[Boolean](Boolean.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Determines whether the specified string is a valid name for an XML element or attribute. 

Parameters | `str:[String](String.html)` — A string to evaluate.   
---|---  
  
Returns | `[Boolean](Boolean.html)` — Returns `true` if the `str` argument is a valid XML name; `false` otherwise.   
---|---  
  
Number| ()| function|   
---|---|---|---  
  
`public function Number(expression:[Object](Object.html)):[Number](Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts a given value to a Number value. The following table shows the result of various input types:  Input Type/Value | Example | Return Value  
---|---|---  
`undefined` | `Number(undefined)` | `NaN`  
`null` | `Number(null)` | `0`  
`true` | `Number(true)` | `1`  
`false` | `Number(false)` | `0`  
`NaN` | `Number(NaN)` | `NaN`  
Empty string | `Number("")` | `0`  
String that converts to Number | `Number("5")` | The number (e.g. `5`)  
String that does not convert to Number | `Number("5a")` | `NaN`  
  
Parameters | `expression:[Object](Object.html)` — A value to be converted to a number.   
---|---  
  
Returns | `[Number](Number.html)` — The converted number value   
---|---  
  
Object| ()| function|   
---|---|---|---  
  
`public function Object(value:[Object](Object.html)):[Object](Object.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Every value in ActionScript 3.0 is an object, which means that calling `Object()` on a value returns that value. 

Parameters | `value:[Object](Object.html)` — An object or a number, string, or Boolean value to convert.   
---|---  
  
Returns | `[Object](Object.html)` — The value specified by the `value` parameter.   
---|---  
  
parseFloat| ()| function|   
---|---|---|---  
  
`public function parseFloat(str:[String](String.html)):[Number](Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts a string to a floating-point number. The function reads, or _parses_ , and returns the numbers in a string until it reaches a character that is not a part of the initial number. If the string does not begin with a number that can be parsed, `parseFloat()` returns `NaN`. White space preceding valid integers is ignored, as are trailing nonnumeric characters. 

Parameters | `str:[String](String.html)` — The string to read and convert to a floating-point number.   
---|---  
  
Returns | `[Number](Number.html)` — A number or `NaN` (not a number).   
---|---  
  
parseInt| ()| function|   
---|---|---|---  
  
`public function parseInt(str:[String](String.html), radix:[uint](uint.html) = 0):[Number](Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts a string to an integer. If the specified string in the parameters cannot be converted to a number, the function returns `NaN`. Strings beginning with 0x are interpreted as hexadecimal numbers. Unlike in previous versions of ActionScript, integers beginning with 0 are _not_ interpreted as octal numbers. You must specify a radix of 8 for octal numbers. White space and zeroes preceding valid integers are ignored, as are trailing nonnumeric characters. 

Parameters | `str:[String](String.html)` — A string to convert to an integer.   
---|---  
| `radix:[uint](uint.html)` (default = `0`)`` — An integer representing the radix (base) of the number to parse. Legal values are from 2 to 36.   
  
Returns | `[Number](Number.html)` — A number or `NaN` (not a number).   
---|---  
  
String| ()| function|   
---|---|---|---  
  
`public function String(expression:[Object](Object.html)):[String](String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Returns a string representation of the specified parameter. 

The following table shows the result of various input types:

Input Type/Value | Return Value  
---|---  
`undefined` | `undefined`  
`null` | `"null"`  
`true` | `"true"`  
`false` | `"false"`  
`NaN` | `"NaN"`  
String | String  
Object | Object.toString()  
Number | String representation of the number  
Parameters | `expression:[Object](Object.html)` — An expression to convert to a string.   
---|---  
  
Returns | `[String](String.html)` — A string representation of the value passed for the `expression` parameter.   
---|---  
  
trace| ()| function|   
---|---|---|---  
  
`public function trace([...](statements.html#..._\(rest\)_parameter) arguments):[void](specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
Displays expressions, or writes to log files, while debugging. A single trace statement can support multiple arguments. If any argument in a trace statement includes a data type other than a String, the trace function invokes the associated `toString()` method for that data type. For example, if the argument is a Boolean value the trace function invokes `Boolean.toString()` and displays the return value. 

Parameters | `[...](statements.html#..._\(rest\)_parameter) arguments` — One or more (comma separated) expressions to evaluate. For multiple expressions, a space is inserted between each expression in the output.   
---|---  
  
Example   
The following example uses the class `TraceExample` to show how the `trace()` method can be used to print a simple string. Generally, the message will be printed to a "Debug" console. 
    
    
    package {
        import flash.display.Sprite;
    
    	public class TraceExample extends Sprite {
    
    		public function TraceExample() {
    			trace("Hello World");
    		}
    	}
    }

uint| ()| function|   
---|---|---|---  
  
`public function uint(value:[Number](Number.html)):[uint](uint.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts a given numeric value to an unsigned integer value. Decimal values are truncated at the decimal point. 

The following table describes the return value of `uint()` on various input types and values.

Input Type/Value | Example | Return Value  
---|---|---  
`undefined` | `uint(undefined)` | `0`  
`null` | `uint(null)` | `0`  
`0` | `uint(0)` | `0`  
`NaN` | `uint(NaN)` | `0`  
Positive floating-point number | `uint(5.31)` | Truncated unsigned integer (e.g. `5`)  
Negative floating-point number | `uint(-5.78)` | Truncates to integer then applies rule for negative integers  
Negative integer | `uint(-5)` | Sum of `uint.MAX_VALUE` and the negative integer (for example, `uint.MAX_VALUE + (-5)`)  
`true` | `uint(true)` | `1`  
`false` | `uint(false)` | `0`  
Empty String | `uint("")` | `0`  
String that converts to Number | `uint("5")` | The number  
String that does not convert to Number | `uint("5a")` | `0`  
Parameters | `value:[Number](Number.html)` — A value to be converted to an integer.   
---|---  
  
Returns | `[uint](uint.html)` — The converted integer value.   
---|---  
  
See also

[int()](package.html#int\(\))

unescape| ()| function|   
---|---|---|---  
  
`public function unescape(str:[String](String.html)):[String](String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Evaluates the parameter `str` as a string, decodes the string from URL-encoded format (converting all hexadecimal sequences to ASCII characters), and returns the string. 

Parameters | `str:[String](String.html)` — A string with hexadecimal sequences to escape.   
---|---  
  
Returns | `[String](String.html)` — A string decoded from a URL-encoded parameter.   
---|---  
  
Vector| ()| function|   
---|---|---|---  
  
`public function Vector(sourceArray:[Object](Object.html)):[Vector](Vector.html).<T>`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
Creates a new Vector instance whose elements are instances of the specified data type. When calling this function, you specify the data type of the result Vector's elements (the Vector's _base type_) using a type parameter. This function uses the same syntax that's used when declaring a Vector instance or calling the `new Vector.<T>()` constructor: 
    
    
    var v:Vector.<String> = Vector.<String>(["Hello", "World"]);

The resulting Vector is populated with the values in the elements of the `sourceArray` argument. If the `sourceArray` argument is already a Vector.<T> instance where `T` is the base type, the function returns that Vector. Otherwise, the result Vector is populated with the elements of the `sourceArray` Array or Vector.

In either case, the data type of all the elements of the `sourceArray` argument must match the base type `T` specified in the function call.

If the `sourceArray` argument has `length` 0, the function returns an empty Vector.

If a Vector is passed as the `sourceArray` argument and its base type is not `T`, or if an Array is passed and its elements are not all instances of data type `T`, an attempt is made to convert the values to the base type. If the values can be automatically converted, the result Vector contains the converted values. If no conversion can be made, an error occurs.

Likewise, if an element in the `sourceArray` argument is an instance of a subclass of the base type `T`, the call succeeds and the element is added to the resulting Vector. This works even if the `sourceArray` argument is a Vector whose base type is a subclass of `T`. In fact, this is the only way to convert a Vector with base type `T` to a Vector with a base type that's a superclass of `T`.

For example, the following code results in a compile error in strict mode, or a TypeError at run time, because it attempts to assign a Vector.<Sprite> to a Vector.<DisplayObject> variable (Sprite is a subclass of DisplayObject):
    
    
    	 var v1:Vector.<Sprite> = new Vector.<Sprite>();
    	 v1[0] = new Sprite();
    	 var v2:Vector.<DisplayObject> = v1;
    	 

The following alternative version of the code successfully copies the elements of a Vector.<Sprite> instance to a Vector.<DisplayObject> instance:
    
    
    	 var v1:Vector.<Sprite> = new Vector.<Sprite>();
    	 v1[0] = new Sprite();
    	 var v2:Vector.<DisplayObject> = Vector.<DisplayObject>(v1);
    	 

Parameters | `sourceArray:[Object](Object.html)` — An Array or Vector instance whose elements become the elements of the result Vector. If the argument is a Vector instance whose associated data type is the same as the specified data type, the argument is returned as the function result.   
---|---  
  
Returns | `[Vector](Vector.html).<T>` — A Vector instance populated with the elements of the `sourceArray` array.   
---|---  
  
Throws | `[TypeError](TypeError.html) ` — If the `sourceArray` argument contains an element that can't be converted to the specified data type.   
---|---  
  
See also

[Vector class](Vector.html)

XML| ()| function|   
---|---|---|---  
  
`public function XML(expression:[Object](Object.html)):[XML](XML.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts an object to an XML object. 

The following table describes return values for various input types.

Parameter Type | Return Value  
---|---  
Boolean | Value is first converted to a string, then converted to an XML object.  
Null | A runtime error occurs (TypeError exception).  
Number | Value is first converted to a string, then converted to an XML object.  
Object | Converts to XML only if the value is a String, Number or Boolean value. Otherwise a runtime error occurs (TypeError exception).  
String | Value is converted to XML.  
Undefined | A runtime error occurs (TypeError exception).  
XML | Input value is returned unchanged.  
XMLList | Returns an XML object only if the XMLList object contains only one property of type XML. Otherwise a runtime error occurs (TypeError exception).  
Parameters | `expression:[Object](Object.html)` — Object to be converted to XML.   
---|---  
  
Returns | `[XML](XML.html)` — An XML object containing values held in the converted object.   
---|---  
  
See also

[XMLList()](package.html#XMLList\(\))

XMLList| ()| function|   
---|---|---|---  
  
`public function XMLList(expression:[Object](Object.html)):[XMLList](XMLList.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Converts an object to an XMLList object. 

The following table describes return values for various input types.

Parameter Type | Return Value  
---|---  
Boolean | Value is first converted to a string, then converted to an XMLList object.  
Null | A runtime error occurs (TypeError exception).  
Number | Value is first converted to a string, then converted to an XMLList object.  
Object | Converts to XMLList only if the value is a String, Number or Boolean value. Otherwise a runtime error occurs (TypeError exception).  
String | Value is converted to an XMLList object.  
Undefined | A runtime error occurs (TypeError exception).  
XML | Value is converted to an XMLList object.  
XMLList | Input value is returned unchanged.  
Parameters | `expression:[Object](Object.html)` — Object to be converted into an XMLList object.   
---|---  
  
Returns | `[XMLList](XMLList.html)` — An XMLList object containing values held in the converted object.   
---|---  
  
See also

[XML()](package.html#XML\(\))

Constant detail

Infinity| constant  
---|---  
  
`public const Infinity:[Number](Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A special value representing positive `Infinity`. The value of this constant is the same as `Number.POSITIVE_INFINITY`. 

See also

[Number.POSITIVE_INFINITY](Number.html#POSITIVE_INFINITY)

  
Example   
The result of division by 0 is `Infinity`, but only when the divisor is a positive number. 
    
    
    
    trace(0 / 0);  // NaN
    trace(7 / 0);  // Infinity
    trace(-7 / 0); // -Infinity

-Infinity| constant|   
---|---|---  
  
`public const -Infinity:[Number](Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A special value representing negative `Infinity`. The value of this constant is the same as `Number.NEGATIVE_INFINITY`. 

See also

[Number.NEGATIVE_INFINITY](Number.html#NEGATIVE_INFINITY)

  
Example   
The result of division by 0 is `-Infinity`, but only when the divisor is a negative number. 
    
    
    
    trace(0 / 0);  // NaN
    trace(7 / 0);  // Infinity
    trace(-7 / 0); // -Infinity

NaN| constant|   
---|---|---  
  
`public const NaN:[Number](Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A special member of the Number data type that represents a value that is "not a number" (`NaN`). When a mathematical expression results in a value that cannot be expressed as a number, the result is `NaN`. The following list describes common expressions that result in `NaN`. 

  * Division by 0 results in `NaN` only if the divisor is also 0. If the divisor is greater than 0, division by 0 results in `Infinity`. If the divisor is less than 0, division by 0 results in `-Infinity`;
  * Square root of a negative number;
  * The arcsine of a number outside the valid range of 0 to 1;
  * `Infinity` subtracted from `Infinity`;
  * `Infinity` or `-Infinity` divided by `Infinity` or `-Infinity`;
  * `Infinity` or `-Infinity` multiplied by 0;

The `NaN` value is not a member of the int or uint data types.

The `NaN` value is not considered equal to any other value, including `NaN`, which makes it impossible to use the equality operator to test whether an expression is `NaN`. To determine whether a number is the `NaN` function, use `isNaN()`.

See also

[isNaN()](package.html#isNaN\(\))   
[Number.NaN](Number.html#NaN)

undefined| constant|   
---|---|---  
  
`public const undefined:[*](specialTypes.html#*)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A special value that applies to untyped variables that have not been initialized or dynamic object properties that are not initialized. In ActionScript 3.0, only variables that are untyped can hold the value undefined, which is not true in ActionScript 1.0 and ActionScript 2.0. For example, both of the following variables are undefined because they are untyped and unitialized: 

  * `var foo;`
  * `var bar:*;`

The `undefined` value also applies to uninitialized or undefined properties of dynamic objects. For example, if an object is an instance of the Object class, the value of any dynamically added property is `undefined` until a value is assigned to that property.

Results vary when `undefined` is used with various functions:

  * The value returned by `String(undefined)` is `"undefined"` (`undefined` is converted to a string).
  * The value returned by `Number(undefined)` is `NaN`.
  * The value returned by `int(undefined)` and `uint(undefined)` is 0.
  * The value returned by `Object(undefined)` is a new Object instance.
  * When the value `undefined` is assigned to a typed variable, the value is converted to the default value of the data type.

Do not confuse `undefined` with `null`. When `null` and `undefined` are compared with the equality (`==`) operator, they compare as equal. However, when `null` and `undefined` are compared with the strict equality (`===`) operator, they compare as not equal.

See also

[null](statements.html#null)

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Mon Feb 26 2024, 5:22 PM GMT\) : Top Level)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Mon Feb 26 2024, 5:22 PM GMT  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)