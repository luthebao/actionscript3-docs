# Operators

Symbolic operators are characters that specify how to combine, compare, or modify the values of an expression.

  
| Arithmetic  
---|---  
| +| [addition](#addition)| Adds numeric expressions.  
| \--| [decrement](#decrement)| Subtracts 1 from the operand.  
| /| [division](#division)| Divides `expression1` by `expression2`.  
| ++| [increment](#increment)| Adds 1 to an expression.  
| %| [modulo](#modulo)| Calculates the remainder of `expression1` divided by `expression2`.  
| *| [multiplication](#multiplication)| Multiplies two numerical expressions.  
| -| [subtraction](#subtraction)| Used for negating or subtracting.  
| Arithmetic compound assignment  
| +=| [addition assignment](#addition_assignment)| Assigns `expression1` the value of `expression1 + expression2`.  
| /=| [division assignment](#division_assignment)| Assigns `expression1` the value of `expression1 / expression2`.  
| %=| [modulo assignment](#modulo_assignment)| Assigns `expression1` the value of `expression1 % expression2`.  
| *=| [multiplication assignment](#multiplication_assignment)| Assigns `expression1` the value of `expression1 * expression2`.  
| -=| [subtraction assignment](#subtraction_assignment)| Assigns `expression1` the value of `expression1 - expression2`.  
| Assignment  
| =| [assignment](#assignment)| Assigns the value of `expression2` (the operand on the right) to the variable, array element, or property in `expression1`.  
| Bitwise  
| &| [bitwise AND](#bitwise_AND)| Converts `expression1` and `expression2` to 32-bit unsigned integers, and performs a Boolean AND operation on each bit of the integer parameters.  
| <<| [bitwise left shift](#bitwise_left_shift)| Converts `expression1` and `shiftCount` to 32-bit integers, and shifts all the bits in `expression1` to the left by the number of places specified by the integer resulting from the conversion of `shiftCount`.  
| ~| [bitwise NOT](#bitwise_NOT)| Converts `expression` to a 32-bit signed integer, and then applies a bitwise one's complement.  
| || [bitwise OR](#bitwise_OR)| Converts `expression1` and `expression2` to 32-bit unsigned integers, and places a 1 in each bit position where the corresponding bits of either ` expression1` or `expression2` are 1.  
| >>| [bitwise right shift](#bitwise_right_shift)| Converts `expression` and `shiftCount` to 32-bit integers, and shifts all the bits in `expression` to the right by the number of places specified by the integer that results from the conversion of `shiftCount`.  
| >>>| [bitwise unsigned right shift](#bitwise_unsigned_right_shift)| The same as the bitwise right shift (`>>`) operator except that it does not preserve the sign of the original expression because the bits on the left are always filled with 0.  
| ^| [bitwise XOR](#bitwise_XOR)| Converts `expression1` and `expression2` to 32-bit unsigned integers, and places a 1 in each bit position where the corresponding bits in `expression1` or `expression2`, but not both, are 1.  
| Bitwise compound assignment  
| &=| [bitwise AND assignment](#bitwise_AND_assignment)| Assigns `expression1` the value of `expression1` `& expression2`.  
| <<=| [bitwise left shift and assignment](#bitwise_left_shift_and_assignment)| Performs a bitwise left shift (`<<=`) operation and stores the contents as a result in `expression1`.  
| |=| [bitwise OR assignment](#bitwise_OR_assignment)| Assigns `expression1` the value of ` expression1 | expression2`.  
| >>=| [bitwise right shift and assignment](#bitwise_right_shift_and_assignment)| Performs a bitwise right-shift operation and stores the result in `expression`.  
| >>>=| [bitwise unsigned right shift and assignment](#bitwise_unsigned_right_shift_and_assignment)| Performs an unsigned bitwise right-shift operation and stores the result in `expression`.  
| ^=| [bitwise XOR assignment](#bitwise_XOR_assignment)| Assigns `expression1` the value of ` expression1 ^ expression2`.  
| Comment  
| /*..*/| [block comment delimiter](#block_comment_delimiter)| Delimits one or more lines of script comments.  
| //| [line comment delimiter](#line_comment_delimiter)| Indicates the beginning of a script comment.  
| Comparison  
| ==| [equality](#equality)| Tests two expressions for equality.  
| >| [greater than](#greater_than)| Compares two expressions and determines whether `expression1` is greater than `expression2`; if it is, the result is `true`.  
| >=| [greater than or equal to](#greater_than_or_equal_to)| Compares two expressions and determines whether `expression1` is greater than or equal to `expression2` (`true`) or `expression1` is less than `expression2` (`false`).  
| !=| [inequality](#inequality)| Tests for the exact opposite of the equality (`==`) operator.  
| <| [less than](#less_than)| Compares two expressions and determines whether `expression1` is less than `expression2`; if so, the result is `true`.  
| <=| [less than or equal to](#less_than_or_equal_to)| Compares two expressions and determines whether `expression1` is less than or equal to `expression2`; if it is, the result is `true`.  
| ===| [strict equality](#strict_equality)| Tests two expressions for equality, but does not perform automatic data conversion.  
| !==| [strict inequality](#strict_inequality)| Tests for the exact opposite of the strict equality (`===`) operator.  
| Logical  
| &&| [logical AND](#logical_AND)| Returns `expression1` if it is `false` or can be converted to `false`, and `expression2` otherwise.  
| &&=| [logical AND assignment](#logical_AND_assignment)| Assigns `expression1` the value of `expression1 && expression2`.  
| !| [logical NOT](#logical_NOT)| Inverts the Boolean value of a variable or expression.  
| ||| [logical OR](#logical_OR)| Returns `expression1` if it is `true` or can be converted to `true`, and `expression2` otherwise.  
| ||=| [logical OR assignment](#logical_OR_assignment)| Assigns `expression1` the value of `expression1 || expression2`.  
| ??| [nullish coalescing](#nullish_coalescing)| Returns `expression1` unless if it is `null` or `undefined`, and `expression2` otherwise.  
| Other  
| []| [array access](#array_access)| Initializes a new array or multidimensional array with the specified elements (`a0`, and so on), or accesses elements in an array.  
|  | [as](#as)| Evaluates whether an expression specified by the first operand is a member of the data type specified by the second operand.  
| ,| [comma](#comma)| Evaluates `expression1`, then `expression2`, and so on.  
| ?:| [conditional](#conditional)| Evaluates `expression1`, and if the value of `expression1` is `true`, the result is the value of `expression2`; otherwise the result is the value of `expression3`.  
|  | [delete](#delete)| Destroys the object property specified by `reference`; the result is `true` if the property does not exist after the operation completes, and `false` otherwise.  
| .| [dot](#dot)| Accesses class variables and methods, gets and sets object properties, and delimits imported packages or classes.  
|  | [in](#in)| Evaluates whether a property is part of a specific object.  
|  | [instanceof](#instanceof)| Evaluates whether an expression's prototype chain includes the prototype object for `function`.  
|  | [is](#is)| Evaluates whether an object is compatible with a specific data type, class, or interface.  
| ::| [name qualifier](#name_qualifier)| Identifies the namespace of a property, a method, an XML property, or an XML attribute.  
|  | [new](#new)| Instantiates a class instance.  
| ?.| [null condition member access](#null_condition_member_access)| Accesses class variables and methods, gets and sets object properties, with an inherent null-object check.  
| {}| [object initializer](#object_initializer)| Creates a new object and initializes it with the specified `name` and `value` property pairs.  
| ()| [parentheses](#parentheses)| Performs a grouping operation on one or more parameters, performs sequential evaluation of expressions, or surrounds one or more parameters and passes them as arguments to a function that precedes the parentheses.  
| /| [RegExp delimiter](#RegExp_delimiter)| When used before and after characters, indicates that the characters have a literal value and are considered a regular expression (RegExp), not a variable, string, or other ActionScript element.  
| :| [type](#type)| Used for assigning a data type; this operator specifies the variable type, function return type, or function parameter type.  
|  | [typeof](#typeof)| Evaluates `expression` and returns a string specifying the expression's data type.  
|  | [void](#void)| Evaluates an expression and then discards its value, returning `undefined`.  
| String  
| +| [concatenation](#concatenation)| Concatenates (combines) strings.  
| +=| [concatenation assignment](#concatenation_assignment)| Assigns `expression1` the value of `expression1 + expression2`.  
| "| [string delimiter](#string_delimiter)| When used before and after characters, indicates that the characters have a literal value and are considered a string, not a variable, numerical value, or other ActionScript element.  
| XML  
| @| [attribute identifier](#attribute_identifier)| Identifies attributes of an XML or XMLList object.  
| { }| [braces (XML)](#braces_\(XML\))| Evaluates an expression that is used in an XML or XMLList initializer.  
| [ ]| [brackets (XML)](#brackets_\(XML\))| Accesses a property or attribute of an XML or XMLList object.  
| +| [concatenation (XMLList)](#concatenation_\(XMLList\))| Concatenates (combines) XML or XMLList values into an XMLList object.  
| +=| [concatenation assignment (XMLList)](#concatenation_assignment_\(XMLList\))| Assigns `expression1`, which is an XMLList object, the value of `expression1 + expression2`.  
|  | [delete (XML)](#delete_\(XML\))| Deletes the XML elements or attributes specified by `reference`.  
| ..| [descendant accessor](#descendant_accessor)| Navigates to descendant elements of an XML or XMLList object, or (combined with the @ operator) finds matching attributes of descendants.  
| .| [dot (XML)](#dot_\(XML\))| Navigates to child elements of an XML or XMLList object, or (combined with the @ operator) returns attributes of an XML or XMLList object.  
| ( )| [parentheses (XML)](#parentheses_\(XML\))| Evaluates an expression in an E4X XML construct.   
| < >| [XML literal tag delimiter](#XML_literal_tag_delimiter)| Defines an XML tag in an XML literal.  
  
Operator detail

\+ addition| operator  
---|---  
  
Usage | `expression1 + expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Adds numeric expressions. If both expressions are integers, the sum is an integer; if either or both expressions are floating-point numbers, the sum is a floating-point number. 

If one expression is a string, all other expressions are converted to strings and concatenated instead of summed. Otherwise, if an expression is not a number, Flash® Player converts it to a number.

Operands | `expression1:[Number](Number.html)` — A value to be added.   
---|---  
| `expression2:[Number](Number.html)` — A value to be added.   
  
Result | `[Number](Number.html)` — An integer or floating-point number.  
---|---  
  
Example   

See also

[\+ (concatenation)](#concatenation)

+= addition assignment| operator|   
---|---|---  
  
Usage | `expression1 += expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of ` expression1 + expression2`. For example, the following two statements have the same result: 
    
    
    x += y; 
    x = x + y; 

All the rules of the addition (+) operator apply to the addition assignment (`+=`) operator. 

Operands | `expression1:[Number](Number.html)` — A number.   
---|---  
| `expression2:[Number](Number.html)` — A number.   
  
Result | `[Number](Number.html)` — The result of the addition.  
---|---  
  
Example   

See also

[\+ (addition)](#addition)

[] array access| operator|   
---|---|---  
  
Usage | 
    
    
    myArray = [a0, a1,...aN]
    myArray[i] = value 
    myObject[propertyName]  
  
---|---  
  
**Runtime version:**|   
---|---  
  
Initializes a new array or multidimensional array with the specified elements (`a0`, and so on), or accesses elements in an array. The array access operator lets you dynamically set and retrieve instance, variable, and object names. It also lets you access object properties. 

Usage 1: An array is an object whose properties are called elements, which are each identified by a number called an index. When you create an array, you surround the elements with the array access ([]) operator (or brackets). An array can contain elements of various types. For example, the following array, called `employee`, has three elements; the first is a number and the second two are strings (inside quotation marks): 
    
    
    var employee:Array = [15, "Barbara", "Jay"]; 

You can nest brackets to simulate multidimensional arrays. You can nest arrays up to 256 levels deep. The following code creates an array called `ticTacToe` with three elements; each element is also an array with three elements: 
    
    
    var ticTacToe:Array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; 
    			
    /* Select Debug > List Variables in test mode 
    to see a list of the array elements.*/ 

Usage 2: Surround the index of each element with brackets ([]) to access it directly; you can add a new element to an array, or you can change or retrieve the value of an existing element. The first index in an array is always 0, as shown in the following example: 
    
    
    var my_array:Array = new Array(); 
    my_array[0] = 15; 
    my_array[1] = "Hello"; 
    my_array[2] = true; 

You can use brackets to add a fourth element, as shown in the following example: 
    
    
    my_array[3] = "George"; 

You can use brackets to access an element in a multidimensional array. The first set of brackets identifies the element in the original array, and the second set identifies the element in the nested array. The following `trace()` statement finds the third element (index 2) of the second array (index 1). 
    
    
    var ticTacToe:Array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; 
    trace(ticTacToe[1][2]); // 6 

Usage 3: You can use the array access operator to dynamically set and retrieve values for a property of an object: 
    
    
    var obj:Object = new Object();
    obj.prop1 = "foo";
    trace(obj["prop" + 1]); // foo
    obj.prop2 = "bar";
    for (j in obj) {
    	trace(obj[j]);
    } 
    /* Output of for loop: 
    foo
    bar */
    

Operands | `myArray:[Object](Object.html)` — The name of an array.   
---|---  
| `a0, a1,...aN:[Object](Object.html)` — Elements in an array; any native type or object instance, including nested arrays.   
| `i:[Number](Number.html)` — An integer index greater than or equal to 0.   
| `myObject:[Object](Object.html)` — The name of an object.   
| `propertyName:[String](String.html)` — A string that names a property of the object.   
  
Result | `[Object](Object.html)` — Usage 1: A reference to an array.  Usage 2: A value from the array; either a native type or an object instance (including an Array instance).  Usage 3: A property from the object; either a native type or an object instance (including an Array instance).   
---|---  
  
Example   

See also

[Array class](Array.html)   
[Object class](Object.html)

as| operator|   
---|---|---  
  
Usage | `expression as datatype`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates whether an expression specified by the first operand is a member of the data type specified by the second operand. If the first operand is a member of the data type, the result is the first operand. Otherwise, the result is the value `null`. 

The expression used for the second operand must evaluate to a data type.

Operands | `expression:[*](specialTypes.html#*)` — The value to check against the data type specified.   
---|---  
| `datatype:[Class](Class.html)` — The data type used to evaluate the `expression` operand. The special * type, which means untyped, cannot be used.   
  
Result | `[Object](Object.html)` — The result is `expression` if `expression` is a member of the data type specified in `datatype`. Otherwise, the result is the value `null`.  
---|---  
  
Example   

See also

[instanceof](#instanceof)   
[is](#is)

= assignment| operator|   
---|---|---  
  
Usage | `expression1 = expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns the value of `expression2` (the operand on the right) to the variable, array element, or property in `expression1`. Assignment can be either by value or by reference. Assignment by value copies the actual value of `expression2` and stores it in `expression1`. Assignment by value is used when `expression2` is a primitive value, which means that its data type is either Boolean, Number, int, uint, or String. Assignment by reference stores a reference to `expression2` in `expression1`. Assignment by reference is commonly used with the `new` operator. The `new` operator creates an object in memory, and a reference to that location in memory is assigned to a variable. 

**Note:** In ActionScript 3.0 all values (including primitive values) are objects, and all assignment is done by reference, but primitive objects have special operators that allow them to behave as if they are assigned by value.

Operands | `expression1:[*](specialTypes.html#*)` — A variable, element of an array, or property of an object.   
---|---  
| `expression2:[*](specialTypes.html#*)` — A value of any type.   
  
Result | `[Object](Object.html)` — The assigned value, `expression2`.  
---|---  
  
Example   

See also

[== (equality)](#equality)

@ attribute identifier| operator|   
---|---|---  
  
Usage | 
    
    
     myXML.@attributeName   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Identifies attributes of an XML or XMLList object. For example, `myXML.@id` identifies attributes named `id` for the `myXML` XML object. You can also use the following syntax to access attributes: `myXML.attribute("id")`, `myXML["@id"]`, and `myXML.@["id"]`. The syntax `myXML.@id` is recommended. To return an XMLList object of all attribute names, use `@*`. To return an attribute with a name that matches an ActionScript reserved word, use the `attribute()` method instead of the `@` operator. 

Operands | `attributeName:[*](specialTypes.html#*)` — The name of the attribute.   
---|---  
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)   
[XML.attribute()](XML.html#attribute\(\))   
[XML.attributes()](XML.html#attributes\(\))

& bitwise AND| operator|   
---|---|---  
  
Usage | `expression1 **&** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Converts `expression1` and `expression2` to 32-bit unsigned integers, and performs a Boolean AND operation on each bit of the integer parameters. Floating-point numbers are converted to integers by discarding any digits after the decimal point. The result is a new 32-bit integer. 

A positive integer is converted to an unsigned hexadecimal value with a maximum value of 4294967295 or 0xFFFFFFFF; a value larger than the maximum has its most significant digits discarded when it is converted so the value is still 32-bit. A negative number is converted to an unsigned hexadecimal value using the two's complement notation, with a minimum value of -2147483648 or 0x800000000; a number less than the minimum is converted to two's complement with greater precision before the most significant digits are discarded. 

The result is interpreted as a 32-bit two's complement number, so the result is an integer in the range -2147483648 to 2147483647. 

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[&= (bitwise AND assignment)](#bitwise_AND_assignment)   
[~ (bitwise NOT)](#bitwise_NOT)   
[| (bitwise OR)](#bitwise_OR)   
[|= (bitwise OR assignment)](#bitwise_OR_assignment)   
[^ (bitwise XOR)](#bitwise_XOR)   
[^= (bitwise XOR assignment)](#bitwise_XOR_assignment)

&= bitwise AND assignment| operator|   
---|---|---  
  
Usage | `expression1 **& =** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of `expression1` `& expression2`. For example, the following two expressions are equivalent: 
    
    
    x &= y; 
    x = x & y; 

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[int](int.html)` — The value of `expression1 & expression2`.  
---|---  
  
Example   

See also

[& (bitwise AND)](#bitwise_AND)   
[~ (bitwise NOT)](#bitwise_NOT)   
[| (bitwise OR)](#bitwise_OR)   
[|= (bitwise OR assignment)](#bitwise_OR_assignment)   
[^ (bitwise XOR)](#bitwise_XOR)   
[^= (bitwise XOR assignment)](#bitwise_XOR_assignment)

<< bitwise left shift| operator|   
---|---|---  
  
Usage | `expression1 **< <** shiftCount`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Converts `expression1` and `shiftCount` to 32-bit integers, and shifts all the bits in `expression1` to the left by the number of places specified by the integer resulting from the conversion of `shiftCount`. The bit positions that are emptied as a result of this operation are filled in with 0 and bits shifted off the left end are discarded. Shifting a value left by one position is the equivalent of multiplying it by 2. 

A floating-point number is converted to an integer by discarding any digits after the decimal point. A positive integer is converted to an unsigned hexadecimal value with a maximum value of 4294967295 or 0xFFFFFFFF; a value larger than the maximum has its most significant digits discarded when it is converted so the value is still 32-bit. A negative number is converted to an unsigned hexadecimal value using the two's complement notation, with a minimum value of -2147483648 or 0x800000000; a number less than the minimum is converted to two's complement with greater precision before the most significant digits are discarded. 

The result is interpreted as a 32-bit two's complement number, so the result is an integer in the range -2147483648 to 2147483647. 

If the result is a negative integer, a runtime error occurs if you attempt to assign the result to a variable of type `uint`. Although ActionScript has no "unsigned bitwise left shift" operator, you can achieve the same effect, and avoid the runtime error, by using `uint(expression1 << shiftCount)`:
    
    
    var num1:uint = 0xFF;
    var num2:uint = uint(num1 << 24); // uint() prevents runtime error

Operands | `expression1:[Number](Number.html)` — A number or expression to be shifted left.   
---|---  
| `shiftCount:[Number](Number.html)` — A number or expression that converts to an integer from 0 to 31.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[<<= (bitwise left shift and assignment)](#bitwise_left_shift_and_assignment)   
[>> (bitwise right shift)](#bitwise_right_shift)   
[>>= (bitwise right shift and assignment)](#bitwise_right_shift_and_assignment)   
[>>> (bitwise unsigned right shift)](#bitwise_unsigned_right_shift)   
[>>>= (bitwise unsigned right shift and assignment)](#bitwise_unsigned_right_shift_and_assignment)

<<= bitwise left shift and assignment| operator|   
---|---|---  
  
Usage | `expression1 **< <=** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Performs a bitwise left shift (`<<=`) operation and stores the contents as a result in `expression1`. The following two expressions are equivalent: 
    
    
    A <<= B
    A = (A << B)

Operands | `expression1:[Number](Number.html)` — A number or expression to be shifted left.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that converts to an integer from 0 to 31.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[<< (bitwise left shift)](#bitwise_left_shift)   
[>> (bitwise right shift)](#bitwise_right_shift)   
[>>= (bitwise right shift and assignment)](#bitwise_right_shift_and_assignment)

~ bitwise NOT| operator|   
---|---|---  
  
Usage | `**~** expression`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Converts `expression` to a 32-bit signed integer, and then applies a bitwise one's complement. That is, every bit that is a 0 is set to 1 in the result, and every bit that is a 1 is set to 0 in the result. The result is a signed 32-bit integer. This operator is also known as the one's complement operator or the bitwise complement operator. 

For example, the hexadecimal value 0x7777 is represented as this binary number:
    
    
    0111011101110111

The bitwise negation of that hexadecimal value, ~0x7777, is this binary number:
    
    
    1000100010001000

In hexadecimal, this is 0x8888. Therefore, ~0x7777 is 0x8888.

The most common use of bitwise operators is for representing flag bits (Boolean values packed into 1 bit each). 

A floating-point number is converted to an integer by discarding any digits after the decimal point. A positive integer is converted to an unsigned hexadecimal value with a maximum value of 4294967295 or 0xFFFFFFFF; a value larger than the maximum has its most significant digits discarded when it is converted so the value is still 32-bit. A negative number is converted to an unsigned hexadecimal value using the two's complement notation, with a minimum value of -2147483648 or 0x800000000; a number less than the minimum is converted to two's complement with greater precision before the most significant digits are discarded. 

The result is interpreted as a 32-bit two's complement number, so the result is an integer in the range -2147483648 to 2147483647. 

Operands | `expression:[Number](Number.html)` — A number to be converted.   
---|---  
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[& (bitwise AND)](#bitwise_AND)   
[&= (bitwise AND assignment)](#bitwise_AND_assignment)   
[| (bitwise OR)](#bitwise_OR)   
[|= (bitwise OR assignment)](#bitwise_OR_assignment)   
[^ (bitwise XOR)](#bitwise_XOR)   
[^= (bitwise XOR assignment)](#bitwise_XOR_assignment)

| bitwise OR| operator|   
---|---|---  
  
Usage | `expression1 | expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Converts `expression1` and `expression2` to 32-bit unsigned integers, and places a 1 in each bit position where the corresponding bits of either `expression1 ` or `expression2` are 1. 

A floating-point number is converted to an integer by discarding any digits after the decimal point. A positive integer is converted to an unsigned hexadecimal value with a maximum value of 4294967295 or 0xFFFFFFFF; a value larger than the maximum has its most significant digits discarded when it is converted so the value is still 32-bit. A negative number is converted to an unsigned hexadecimal value using the two's complement notation, with a minimum value of -2147483648 or 0x800000000; a number less than the minimum is converted to two's complement with greater precision before the most significant digits are discarded. 

The result is interpreted as a 32-bit two's complement number, so the result is an integer in the range -2147483648 to 2147483647. 

Operands | `expression1:[Number](Number.html)` — A number.   
---|---  
| `expression2:[Number](Number.html)` — A number.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[& (bitwise AND)](#bitwise_AND)   
[&= (bitwise AND assignment)](#bitwise_AND_assignment)   
[~ (bitwise NOT)](#bitwise_NOT)   
[|= (bitwise OR assignment)](#bitwise_OR_assignment)   
[^ (bitwise XOR)](#bitwise_XOR)   
[^= (bitwise XOR assignment)](#bitwise_XOR_assignment)

|= bitwise OR assignment| operator|   
---|---|---  
  
Usage | `expression1 **|=** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of `expression1 | expression2`. For example, the following two statements are equivalent: 
    
    
    x |= y; 
    x = x | y; 

Operands | `expression1:[Number](Number.html)` — A number to be converted.   
---|---  
| `expression2:[Number](Number.html)` — A number to be converted.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[& (bitwise AND)](#bitwise_AND)   
[&= (bitwise AND assignment)](#bitwise_AND_assignment)   
[~ (bitwise NOT)](#bitwise_NOT)   
[| (bitwise OR)](#bitwise_OR)   
[^ (bitwise XOR)](#bitwise_XOR)   
[^= (bitwise XOR assignment)](#bitwise_XOR_assignment)

>> bitwise right shift| operator|   
---|---|---  
  
Usage | `expression **> >** shiftCount`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Converts `expression` and `shiftCount` to 32-bit integers, and shifts all the bits in `expression` to the right by the number of places specified by the integer that results from the conversion of `shiftCount`. Bits that are shifted off the right end are discarded. To preserve the sign of the original expression, the bits on the left are filled in with 0 if the most significant bit (the bit farthest to the left) of `expression` is 0, and filled in with 1 if the most significant bit is 1. Shifting a value right by one position is the equivalent of dividing by 2 and discarding the remainder. 

A floating-point number is converted to an integer by discarding any digits after the decimal point. A positive integer is converted to an unsigned hexadecimal value with a maximum value of 4294967295 or 0xFFFFFFFF; a value larger than the maximum has its most significant digits discarded when it is converted so the value is still 32-bit. A negative number is converted to an unsigned hexadecimal value using the two's complement notation, with a minimum value of -2147483648 or 0x800000000; a number less than the minimum is converted to two's complement with greater precision before the most significant digits are discarded. 

The result is interpreted as a 32-bit two's complement number, so the result is an integer in the range -2147483648 to 2147483647. 

Operands | `expression:[Number](Number.html)` — A number or expression to be shifted right.   
---|---  
| `shiftCount:[Number](Number.html)` — A number or expression that converts to an integer from 0 to 31.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[>>= (bitwise right shift and assignment)](#bitwise_right_shift_and_assignment)

>>= bitwise right shift and assignment| operator|   
---|---|---  
  
Usage | `expression **> >=** shiftCount`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Performs a bitwise right-shift operation and stores the result in `expression`. 

The following two statements are equivalent: 
    
    
    A >>= B; 
    A = (A >> B);

Operands | `expression:[Number](Number.html)` — A number or expression to be shifted right.   
---|---  
| `shiftCount:[Number](Number.html)` — A number or expression that converts to an integer from 0 to 31.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[>> (bitwise right shift)](#bitwise_right_shift)

>>> bitwise unsigned right shift| operator|   
---|---|---  
  
Usage | `expression **> >>** shiftCount`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
The same as the bitwise right shift (`>>`) operator except that it does not preserve the sign of the original expression because the bits on the left are always filled with 0. 

A floating-point number is converted to an integer by discarding any digits after the decimal point. A positive integer is converted to an unsigned hexadecimal value with a maximum value of 4294967295 or 0xFFFFFFFF; a value larger than the maximum has its most significant digits discarded when it is converted so the value is still 32-bit. A negative number is converted to an unsigned hexadecimal value using the two's complement notation, with a minimum value of -2147483648 or 0x800000000; a number less than the minimum is converted to two's complement with greater precision before the most significant digits are discarded. 

The result is interpreted as a 32-bit unsigned integer, so the result is an integer in the range 0 to 4294967295. 

**Note:** ActionScript has no complementary "bitwise unsigned left shift" operator, but you can achieve the same effect by using `uint(expression << shiftCount)`.

Operands | `expression:[Number](Number.html)` — A number or expression to be shifted right.   
---|---  
| `shiftCount:[Number](Number.html)` — A number or expression that converts to an integer between 0 and 31.   
  
Result | `[uint](uint.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[>> (bitwise right shift)](#bitwise_right_shift)   
[>>= (bitwise right shift and assignment)](#bitwise_right_shift_and_assignment)

>>>= bitwise unsigned right shift and assignment| operator|   
---|---|---  
  
Usage | `expression **> >>=** shiftCount`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Performs an unsigned bitwise right-shift operation and stores the result in `expression`. The following two statements are equivalent: 
    
    
    A >>>= B; 
    A = (A >>> B); 

Operands | `expression:[Number](Number.html)` — A number or expression to be shifted right.   
---|---  
| `shiftCount:[Number](Number.html)` — A number or expression that converts to an integer from 0 to 31.   
  
Result | `[uint](uint.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[>>> (bitwise unsigned right shift)](#bitwise_unsigned_right_shift)   
[>>= (bitwise right shift and assignment)](#bitwise_right_shift_and_assignment)

^ bitwise XOR| operator|   
---|---|---  
  
Usage | `expression1 ^ expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Converts `expression1` and `expression2` to 32-bit unsigned integers, and places a 1 in each bit position where the corresponding bits in `expression1` or `expression2`, but not both, are 1. 

A floating-point number is converted to an integer by discarding any digits after the decimal point. A positive integer is converted to an unsigned hexadecimal value with a maximum value of 4294967295 or 0xFFFFFFFF; a value larger than the maximum has its most significant digits discarded when it is converted so the value is still 32-bit. A negative number is converted to an unsigned hexadecimal value using the two's complement notation, with a minimum value of -2147483648 or 0x800000000; a number less than the minimum is converted to two's complement with greater precision before the most significant digits are discarded. 

The result is interpreted as a 32-bit two's complement number, so the result is an integer in the range -2147483648 to 2147483647. 

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[& (bitwise AND)](#bitwise_AND)   
[&= (bitwise AND assignment)](#bitwise_AND_assignment)   
[~ (bitwise NOT)](#bitwise_NOT)   
[| (bitwise OR)](#bitwise_OR)   
[|= (bitwise OR assignment)](#bitwise_OR_assignment)   
[^= (bitwise XOR assignment)](#bitwise_XOR_assignment)

^= bitwise XOR assignment| operator|   
---|---|---  
  
Usage | `expression1 **^=** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of ` expression1 ^ expression2`. For example, the following two statements are equivalent: 
    
    
    x ^= y 
    x = x ^ y 

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[int](int.html)` — The result of the bitwise operation.  
---|---  
  
Example   

See also

[& (bitwise AND)](#bitwise_AND)   
[&= (bitwise AND assignment)](#bitwise_AND_assignment)   
[~ (bitwise NOT)](#bitwise_NOT)   
[| (bitwise OR)](#bitwise_OR)   
[|= (bitwise OR assignment)](#bitwise_OR_assignment)   
[^ (bitwise XOR)](#bitwise_XOR)

/*..*/ block comment delimiter| operator|   
---|---|---  
  
Usage | 
    
    
    /* comment */
    
    
    /* comment
    
    
       comment */  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Delimits one or more lines of script comments. Characters that appear between the opening delimiter (`/*`) and the closing delimiter (`*/`) are interpreted as a comment and ignored by the ActionScript compiler. Use these delimiters to identify comments on multiple successive lines; for single-line comments, use the `//` delimiter. 

You will receive an error message if you omit the closing block comment delimiter (`*/`), or if you attempt to nest comments. After an opening delimiter (`/*`) is used, the first closing delimiter (`*/`) ends the comment, regardless of the number of opening delimiters placed before it.

Operands | `comment:[*](specialTypes.html#*)` — Any characters.   
---|---  
  
Example   

See also

[// (line comment delimiter)](#line_comment_delimiter)

{ } braces (XML)| operator|   
---|---|---  
  
Usage | 
    
    
     myXML = <{tagName} {attributeName} = {attributeValue}>{content}</{tagName}>  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates an expression that is used in an XML or XMLList initializer. An XML or XMLList initializer is a literal value that is assigned to a variable of type XML or XMLList. An expression that is delimited by the XML `{` and `}` operators can be used in an XML or XMLList initializer instead of literal names or values. An expression can be used in place of `tagName`, `attributeName`, `attributeValue`, and `content`. 

Operands | `myXML:[*](specialTypes.html#*)` — An XML or XMLList object.   
---|---  
| `tagName:[*](specialTypes.html#*)` — An expression that evaluates to the name of an XML tag.   
| `attributeName:[*](specialTypes.html#*)` — An expression that evaluates to the name of an XML attribute.   
| `attributeValue:[*](specialTypes.html#*)` — An expression that evaluates to the value of an XML attribute.   
| `content:[*](specialTypes.html#*)` — An expression that evaluates to the contents of an XML tag.   
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)

[ ] brackets (XML)| operator|   
---|---|---  
  
Usage | 
    
    
     myXML[expression]  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Accesses a property or attribute of an XML or XMLList object. The brackets operator allows you to access property names that are not accessible with the dot (`.`) operator. 

Operands | `myXML:[*](specialTypes.html#*)` — An XML or XMLList object.   
---|---  
| `expression:[*](specialTypes.html#*)` — An expression that evaluates to the name of an XML tag or attribute.   
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)

, comma| operator|   
---|---|---  
  
Usage | `(expression1**,** expression2[**,** expressionN... ])`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates `expression1`, then `expression2`, and so on. This operator is primarily used with the `for` loop statement and is often used with the parentheses `()` operator.

Operands | `expression1:[*](specialTypes.html#*)` — An expression to be evaluated.   
---|---  
| `expression2:[*](specialTypes.html#*)` — An expression to be evaluated.   
| `expressionN:[*](specialTypes.html#*)` — Any number of additional expressions to be evaluated.   
  
Result | `[Object](Object.html)` — The values of the evaluated expressions.  
---|---  
  
Example   

See also

[() (parentheses)](#parentheses)

\+ concatenation| operator|   
---|---|---  
  
Usage | `expression1 + expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Concatenates (combines) strings. If one expression is a string, all other expressions are converted to strings and concatenated. 

If both expressions are numbers, this operator behaves as an addition operator.

Operands | `expression1:[String](String.html)` — A string to be concatenated.   
---|---  
| `expression2:[String](String.html)` — A string to be concatenated.   
  
Result | `[String](String.html)` — The concatenated string.  
---|---  
  
Example   

See also

[\+ (addition)](#addition)

\+ concatenation (XMLList)| operator|   
---|---|---  
  
Usage | 
    
    
    expression1 + expression2  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Concatenates (combines) XML or XMLList values into an XMLList object. An XMLList object results only if both operands are XML or XMLList values. 

Operands | `expression1:[*](specialTypes.html#*)` — An XML or XMLList value.   
---|---  
| `expression2:[*](specialTypes.html#*)` — An XML or XMLList value.   
  
Result | `[XMLList](XMLList.html)` — The concatenated XMLList object.  
---|---  
  
Example   

See also

[XMLList class](XMLList.html)   
[XMLList global function](package.html#XMLList\(\))

+= concatenation assignment| operator|   
---|---|---  
  
Usage | `expression1 += expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of `expression1 + expression2`. For example, the following two statements have the same result: 
    
    
    x += y; 
    x = x + y;

All the rules of the concatenation (`+`) operator apply to the concatenation assignment (`+=`) operator. Note that using concatenation assignment for the `text` property of a `TextField` (i.e. `someTextField.text += moreText` is much less efficient than `TextField.appendText()`, particularly with a `TextField` that contains a significant amount of content. 

Operands | `expression1:[String](String.html)` — A string.   
---|---  
| `expression2:[String](String.html)` — A string.   
  
Result | `[Number](Number.html)` — The result of the concatenation.  
---|---  
  
Example   

See also

[\+ (concatenation)](#concatenation)

+= concatenation assignment (XMLList)| operator|   
---|---|---  
  
Usage | 
    
    
    expression1 += expression2  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1`, which is an XMLList object, the value of `expression1 + expression2`. For example, the following two statements have the same result: 
    
    
    x += y; 
    x = x + y; 

All the rules of the XMLList concatenation (`+`) operator apply to the XMLList concatenation assignment (`+=`) operator. 

Operands | `expression1:[XMLList](XMLList.html)` — The XMLList object to which you are adding a new value.   
---|---  
| `expression2:[*](specialTypes.html#*)` — An XML or XMLList value.   
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)   
[XML() global function](package.html#XML\(\))   
[XMLList() global function](package.html#XMLList\(\))

?: conditional| operator|   
---|---|---  
  
Usage | 
    
    
    expression1 ? expression2 : expression3  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates `expression1`, and if the value of `expression1` is `true`, the result is the value of `expression2`; otherwise the result is the value of `expression3`.

Operands | `expression1:[Boolean](Boolean.html)` — An expression that evaluates to a Boolean value; usually a comparison expression, such as `x < 5`.   
---|---  
| `expression2:[*](specialTypes.html#*)` — A value of any type.   
| `expression3:[*](specialTypes.html#*)` — A value of any type.   
  
Result | `[*](specialTypes.html#*)` — The value of `expression2` or `expression3`.  
---|---  
  
Example   

\-- decrement| operator|   
---|---|---  
  
Usage | 
    
    
    --expression
    
    
    expression--  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Subtracts 1 from the operand. The operand can be a variable, element in an array, or property of an object. The pre-decrement form of the operator (`--expression`) subtracts 1 from `expression` and returns the result. The post-decrement form of the operator (`expression--`) subtracts 1 from `expression` and returns the initial value of `expression` (the value prior to the subtraction).

Operands | `expression:[Number](Number.html)` — A number or a variable that evaluates to a number.   
---|---  
  
Result | `[Number](Number.html)` — The result of the decremented value.  
---|---  
  
Example   

delete| operator|   
---|---|---  
  
Usage | 
    
    
     delete reference  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Destroys the object property specified by `reference`; the result is `true` if the property does not exist after the operation completes, and `false` otherwise. The `delete` operator returns `true` if it is called on a nonexistent property or a dynamic property not defined in a class. 

The `delete` operator can fail and return `false` if the `reference` parameter cannot be deleted. You cannot delete fixed properties or variables that are declared with the `var` statement. A fixed property is a variable or method defined in a class definition. 

The `delete` operator cannot be used to destroy a property of a class, unless that class is a dynamic class added at runtime. Properties of sealed classes cannot be destroyed using `delete`. Set the property to `null` instead.

**Note:** You cannot delete an object, but you can make an object eligible for garbage collection by removing all references to the object. The most common reference to an object is a variable that points to it. You can remove such a reference by setting the variable to `null`. The garbage collector removes any object that has no references.

Operands | `reference:[*](specialTypes.html#*)` — The name of the property to eliminate.   
---|---  
  
Result | `[Boolean](Boolean.html)` — The value `true` if the deletion succeeded and `false` if it failed.  
---|---  
  
Example   

See also

[var](statements.html#var)

delete (XML)| operator|   
---|---|---  
  
Usage | 
    
    
     delete reference  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Deletes the XML elements or attributes specified by `reference`.

Operands | `reference:[XMLList](XMLList.html)` — An XMLList object that specifies the XML elements or attributes to delete.   
---|---  
  
Result | `[Boolean](Boolean.html)` — Always returns a value of `true`. The result is always `true` because the XMLList operand always refers to a valid (though possibly empty) XMLList object.  
---|---  
  
Example   

.. descendant accessor| operator|   
---|---|---  
  
Usage | 
    
    
     myXML..childElement1..@attributeName   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Navigates to descendant elements of an XML or XMLList object, or (combined with the @ operator) finds matching attributes of descendants. The matching elements or attributes need not be direct children of the XML or XMLList object; they can be lower in the tree (for example, grandchildren). The result is an XMLList object, because more than one child element or attribute can match. 

The order of nodes in the XMLList object returned is the result of a depth-first traversal. For example, consider the following:
    
    
    var myXML:XML = <a>
    			<b>one
    				<c> 
    					<b>two</b> 
    				</c> 
    			</b>
    			<b>three</b>
    		</a>;
    
    trace(myXML..b[0].toXMLString());
    trace("______________");
    trace(myXML..b[1].toXMLString());
    trace("______________");
    trace(myXML..b[2].toXMLString());

The following output would result:
    
    
    <b>
      one
      <c>
        <b>two</b>
      </c>
    </b>
    ______________
    <b>two</b>
    ______________
    <b>three</b>
    

To return descendants with names that match ActionScript reserved words, use the `XML.descendants()` method instead of the descendant (..) operator, as the following example shows: 
    
    
    var xml:XML = 
    <enrollees>
    	<student id="239">
    		<class name="Algebra" />
     		<class name="Spanish 2"/>
    	</student>
    	<student id="206">
    		<class name="Trigonometry" />
     		<class name="Spanish 2" />
    	</student>
     </enrollees>;
     trace(xml.descendants("class")); 
     

Operands | `myXML:[Object](Object.html)` — The XML or XMLList object.   
---|---  
| `childElement1_or_attributeName` — The name of an XML property or the name of an attribute.   
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)   
[XML.descendants()](XML.html#descendants\(\))

/ division| operator|   
---|---|---  
  
Usage | `expression1 / expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Divides `expression1` by `expression2`. The result of the division operation is a double-precision floating-point number.

Operands | `expression:[Number](Number.html)` — A number or a variable that evaluates to a number.   
---|---  
  
Result | `[Number](Number.html)` — The floating-point result of the operation.  
---|---  
  
Example   

See also

[% (modulo)](#modulo)

/= division assignment| operator|   
---|---|---  
  
Usage | `expression1 /= expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of ` expression1 / expression2`. For example, the following two statements are equivalent: 
    
    
    x /= y; 
    x = x / y;

Operands | `expression1:[Number](Number.html)` — A number or a variable that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or a variable that evaluates to a number.   
  
Result | `[Number](Number.html)` — A number.  
---|---  
  
Example   

See also

[/ (division)](#division)

. dot| operator|   
---|---|---  
  
Usage | 
    
    
    object.property_or_method  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Accesses class variables and methods, gets and sets object properties, and delimits imported packages or classes.

Operands | `object:[Object](Object.html)` — An instance of a class. The object can be an instance of any of the built-in ActionScript classes or a class you define. This operand is always to the left of the dot (.) operator.   
---|---  
| `property_or_method:[*](specialTypes.html#*)` — The name of a property or method associated with an object. All the valid methods and properties for the built-in classes are listed in the method and property summary tables for that class. This operand is always to the right of the dot (.) operator.   
  
Result | `[*](specialTypes.html#*)` — The variable, method, or property named on the right side of the dot.  
---|---  
  
Example   

See also

[dot (XML) operator](#dot_\(XML\))

. dot (XML)| operator|   
---|---|---  
  
Usage | 
    
    
    myXML.childElement
    myXML.@attributeName   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Navigates to child elements of an XML or XMLList object, or (combined with the @ operator) returns attributes of an XML or XMLList object. The object returned is an XMLList, because more than one child element or attribute can match. 

To return elements with names that match ActionScript reserved words, use the `XML.elements()` method or the `XML.descendants()` method instead of the XML dot (.) operator, as the following example shows: 
    
    
    var xml:XML = 
    	<student id="206">
    		<class name="Trigonometry" />
    		<class name="Spanish 2" />
    	</student>;
    trace(xml.elements("class"));
    trace(xml.descendants("class")); 
    

Operands | `myXML:[Object](Object.html)` — The XML or XMLList object.   
---|---  
| `childElement:[*](specialTypes.html#*)` — The name of an XML property.   
| `attributeName:[*](specialTypes.html#*)` — The name of an attribute.   
  
Result | `[XMLList](XMLList.html)` — The XMLList specified.  
---|---  
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)   
[XML.descendants()](XML.html#descendants\(\))   
[XML.elements()](XML.html#elements\(\))

== equality| operator|   
---|---|---  
  
Usage | `expression1 **==** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Tests two expressions for equality. The result is `true` if the expressions are equal. 

If the data types of the two operands match, the definition of equal depends on the data type of the operands:

  * Values of type int, uint, and Boolean are considered equal if they have the same value.
  * Numbers with matching values are considered equal, unless they are both `NaN`.
  * If the value of both operands is `null` or `undefined`, they are considered equal.
  * String expressions are equal if they have the same number of characters and the characters are identical.
  * For XML objects: 
    * If one operand is a text or attribute node and the other has simple content, both operands are converted to strings with the `toString()` method and are considered equal if the resulting strings match. 
    * Otherwise, objects are considered equal only if the qualified name, attributes, and child properties for both objects match.
  * XMLList objects are considered equal if they have the same number of properties and both the order and values of the properties match.
  * For Namespace objects, values are considered equal if the `uri` properties of both objects match.
  * For QName objects, values are considered equal if the `uri` properties of both objects match and the `localName` properties of both objects match.
  * Variables representing objects, arrays, and functions are compared by reference. Two such variables are equal if they refer to the same object, array, or function. Two separate arrays are never considered equal, even if they have the same number of elements.

If the data types of the operands do not match, the result is `false` except in the following circumstances: 

  * The operands' values are `undefined` and `null`, in which case the result is `true`.
  * Automatic data type conversion converts the data types of String, Boolean, int, uint, and Number values to compatible types and the converted values are equal, in which case operands are considered equal.
  * One operand is of type XML with simple content (`hasSimpleContent() == true`), and after both operands are converted to strings with the `toString()` method, the resulting strings match.
  * One operand is of type XMLList, and either of the following conditions is true: 
    * The `length` property of the XMLList object is 0, and the other object is `undefined`.
    * The `length` property of the XMLList object is 1, and one element of the XMLList object matches the other operand.

Operands | `expression1:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or expression.   
---|---  
| `expression2:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or expression.   
  
Result | `[Boolean](Boolean.html)` — A value of `true` if the expressions are equal, and `false` otherwise.  
---|---  
  
Example   

See also

[!= (inequality)](#inequality)   
[&& (logical AND)](#logical_AND)   
[! (logical NOT)](#logical_NOT)   
[|| (logical OR)](#logical_OR)   
[=== (strict equality)](#strict_equality)   
[!== (strict inequality)](#strict_inequality)

> greater than| operator|   
---|---|---  
  
Usage | `expression1 > expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Compares two expressions and determines whether `expression1` is greater than `expression2`; if it is, the result is `true`. If `expression1` is less than or equal to `expression2`, the result is `false`. 

If both operands are of type String, the operands are compared using alphabetical order; all capital letters come before lowercase letters. Otherwise, operands are first converted to numbers, then compared.

Operands | `expression1:[Object](Object.html)` — A string, integer, or floating-point number.   
---|---  
| `expression2:[Object](Object.html)` — A string, integer, or floating-point number.   
  
Result | `[Boolean](Boolean.html)` — A value of `true` if `expression1` is greater than `expression2`; `false` otherwise.  
---|---  
  
Example   

>= greater than or equal to| operator|   
---|---|---  
  
Usage | `expression1 >= expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Compares two expressions and determines whether `expression1` is greater than or equal to `expression2` (`true`) or `expression1` is less than `expression2` (`false`).

Operands | `expression1:[Object](Object.html)` — A string, integer, or floating-point number.   
---|---  
| `expression2:[Object](Object.html)` — A string, integer, or floating-point number.   
  
Result | `[Boolean](Boolean.html)` — A value of `true` if `expression1` is greater than or equal to `expression2`; `false` otherwise.  
---|---  
  
Example   

See also

[> (greater than)](#greater_than)

in| operator|   
---|---|---  
  
Usage | `expression1 **in** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates whether a property is part of a specific object. To use the `in` operator, specify a property name as the first operand and an object as the second operand. If the object you specify contains such a property, the result is `true`; otherwise the result is `false`. 

If the specified object is an Array object, you can use the `in` operator to check whether a particular index number is valid. If you pass an integer as the first operand, the result is `true` if the index is within the valid range of index numbers, and `false` otherwise.

Result | `[Boolean](Boolean.html)` — A value of `true` if `expression1` is a property of the object represented by `expression2`, and `false` otherwise.  
---|---  
  
Example   

See also

[instanceof](#instanceof)

++ increment| operator|   
---|---|---  
  
Usage | 
    
    
    ++expression
    
    
     expression++  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Adds 1 to an expression. The expression can be a variable, an element in an array, or a property of an object. The pre-increment form of the operator (`++expression`) adds 1 to ` expression` and returns the result. The post-increment form of the operator (`expression++`) adds 1 to `expression` and returns the initial value of `expression` (the value prior to the addition). 

Operands | `expression:[Number](Number.html)` — A number or a variable that evaluates to a number.   
---|---  
  
Result | `[Number](Number.html)` — The result of the increment.  
---|---  
  
Example   

!= inequality| operator|   
---|---|---  
  
Usage | `expression1 **!=** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Tests for the exact opposite of the equality (`==`) operator. If `expression1` is equal to `expression2`, the result is `false`. As with the equality (`==`) operator, the definition of equal depends on the data types being compared. 

If the data types of the two operands match, the definition of equal depends on the data type of the operands:

  * Values of type int, uint, and Boolean are considered equal if they have the same value.
  * Numbers with matching values are considered equal, unless they are both `NaN`.
  * If the value of both operands is `null` or `undefined`, they are considered equal.
  * String expressions are equal if they have the same number of characters and the characters are identical.
  * For XML objects: 
    * If one operand is a text or attribute node and the other has simple content, both operands are converted to strings with the `toString()` method and are considered equal if the resulting strings match. 
    * Otherwise, objects are considered equal only if the qualified name, attributes, and child properties for both objects match.
  * XMLList objects are considered equal if they have the same number of properties and both the order and values of the properties match.
  * For Namespace objects, values are considered equal if the `uri` properties of both objects match.
  * For QName objects, values are considered equal if the `uri` properties of both objects match and the `localName` properties of both objects match.
  * Variables representing objects, arrays, and functions are compared by reference. Two such variables are equal if they refer to the same object, array, or function. Two separate arrays are never considered equal, even if they have the same number of elements.

If the data types of the operands do not match, the inequality operator (`!=`) returns `true` except in the following circumstances: 

  * The operands' values are `undefined` and `null`, in which case the result is `true`.
  * Automatic data type conversion converts the data types of String, Boolean, int, uint, and Number values to compatible types and the converted values are equal, in which case operands are considered equal.
  * One operand is of type XML with simple content (`hasSimpleContent() == true`), and after both operands are converted to strings with the `toString()` method the resulting strings match.
  * One operand is of type XMLList, and either of the following conditions is true: 
    * The `length` property of the XMLList object is 0, and the other object is `undefined`.
    * The `length` property of the XMLList object is 1, and one element of the XMLList object matches the other operand.

Operands | `expression1:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or function.   
---|---  
| `expression2:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or function.   
  
Result | `[Boolean](Boolean.html)` — A value of `true` if the expressions are not equal, and `false` otherwise.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[&& (logical AND)](#logical_AND)   
[! (logical NOT)](#logical_NOT)   
[|| (logical OR)](#logical_OR)   
[=== (strict equality)](#strict_equality)   
[!== (strict inequality)](#strict_inequality)

instanceof| operator|   
---|---|---  
  
Usage | `expression instanceof function`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates whether an expression's prototype chain includes the prototype object for `function`. The `instanceof` operator is included for backward compatibility with ECMAScript edition 3, and may be useful for advanced programmers who choose to use prototype-based inheritance with constructor functions instead of classes. 

To check whether an object is a member of a specific data type, use the `is` operator.

When used with classes, the `instanceof` operator is similar to the `is` operator because a class's prototype chain includes all of its superclasses. Interfaces, however, are not included on prototype chains, so the `instanceof` operator always results in `false` when used with interfaces, whereas the `is` operator results in `true` if an object belongs to a class that implements the specified interface.

**Note:** The ActionScript `is` operator is the equivalent of the Java `instanceof` operator.

Operands | `expression:[Object](Object.html)` — The object that contains the prototype chain to evaluate.   
---|---  
| `function:[Object](Object.html)` — A function object (or class).   
  
Result | `[Boolean](Boolean.html)` — Returns `true` if the prototype chain of `expression` includes the prototype object for `function`, and `false` otherwise.  
---|---  
  
Example   

See also

[is](#is)   
[prototype](Object.html#prototype)

is| operator|   
---|---|---  
  
Usage | `expression1 is expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates whether an object is compatible with a specific data type, class, or interface. Use the `is` operator instead of the `instanceof` operator for type comparisons. You can also use the `is` operator to check whether an object implements an interface. 

Result | `[Boolean](Boolean.html)` — A value of `true` if `expression1` is compatible with the data type, class, or interface specified in `expression2`, and `false` otherwise.  
---|---  
  
Example   

See also

[as](#as)   
[instanceof](#instanceof)

< less than| operator|   
---|---|---  
  
Usage | `expression1 **<** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Compares two expressions and determines whether `expression1` is less than `expression2`; if so, the result is `true`. If `expression1` is greater than or equal to `expression2`, the result is `false`. 

If both operands are of type String, the operands are compared using alphabetical order; all capital letters come before lowercase letters. Otherwise, operands are first converted to numbers, then compared.

Operands | `expression1:[Object](Object.html)` — A string, integer, or floating-point number.   
---|---  
| `expression2:[Object](Object.html)` — A string, integer, or floating-point number.   
  
Result | `[Boolean](Boolean.html)` — A value of `true` if `expression1` is less than `expression2`; `false` otherwise.  
---|---  
  
Example   

<= less than or equal to| operator|   
---|---|---  
  
Usage | `expression1 **< =** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Compares two expressions and determines whether `expression1` is less than or equal to `expression2`; if it is, the result is `true`. If ` expression1` is greater than `expression2`, the result is `false`. 

If both operands are of type String, the operands are compared using alphabetical order; all capital letters come before lowercase letters. Otherwise, operands are first converted to numbers, then compared.

Operands | `expression1:[Object](Object.html)` — A string, integer, or floating-point number.   
---|---  
| `expression2:[Object](Object.html)` — A string, integer, or floating-point number.   
  
Result | `[Boolean](Boolean.html)` — A value of `true` if `expression1` is less than or equal to `expression2`; `false` otherwise.  
---|---  
  
Example   

// line comment delimiter| operator|   
---|---|---  
  
Usage | `**//** comment`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Indicates the beginning of a script comment. Characters that appear between the comment delimiter (`//`) and the end-of-line character are interpreted as a comment and are ignored. Use this delimiter for single-line comments; for comments on multiple successive lines, use the `/*` and `*/` delimiters. 

Operands | `comment:[*](specialTypes.html#*)` — Any characters.   
---|---  
  
Example   

See also

[/*..*/ (block comment delimiter)](#block_comment_delimiter)

&& logical AND| operator|   
---|---|---  
  
Usage | `expression1 **& &** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Returns `expression1` if it is `false` or can be converted to `false`, and `expression2` otherwise. Examples of values that can be converted to `false` are 0, `NaN`, `null`, and `undefined`. If you use a function call as `expression2`, the function is not called if `expression1` evaluates to `false`. 

If both operands are of type Boolean, the result is `true` only if both operands are `true`, as shown in the following table:

Expression  | Evaluates   
---|---  
`true && true` | `true`  
`true && false` | `false`  
`false && false` | `false`  
`false && true` | `false`  
  
Operands | `expression1:[*](specialTypes.html#*)` — A value or expression of any type.   
---|---  
| `expression2:[*](specialTypes.html#*)` — A value of expression of any type.   
  
Result | `[*](specialTypes.html#*)` — A Boolean value if both operands are of type Boolean. Otherwise, the result is the value of either expression.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[!= (inequality)](#inequality)   
[! (logical NOT)](#logical_NOT)   
[|| (logical OR)](#logical_OR)   
[||= (logical OR assignment)](#logical_OR_assignment)   
[&&= (logical AND assignment)](#logical_AND_assignment)   
[=== (strict equality)](#strict_equality)   
[!== (strict inequality)](#strict_inequality)

&&= logical AND assignment| operator|   
---|---|---  
  
Usage | `expression1 &&= expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of `expression1 && expression2`. For example, the following two statements are equivalent: 
    
    
    x &&= y; 
    x = x && y; 

Operands | `expression1:[*](specialTypes.html#*)` — A value of any type.   
---|---  
| `expression2:[*](specialTypes.html#*)` — A value of any type.   
  
Result | `[*](specialTypes.html#*)` — A Boolean value if both operands are members of the Boolean data type. Otherwise, the result will be the value of either of the two expressions.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[!= (inequality)](#inequality)   
[|| (logical OR)](#logical_OR)   
[||= (logical OR assignment)](#logical_OR_assignment)   
[&& (logical AND)](#logical_AND)   
[! (logical NOT)](#logical_NOT)   
[=== (strict equality)](#strict_equality)   
[!== (strict inequality)](#strict_inequality)

! logical NOT| operator|   
---|---|---  
  
Usage | `**!** expression`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Inverts the Boolean value of a variable or expression. If `expression` is a variable with the absolute or converted value `true`, the value of `!expression` is `false`. If the expression `x && y` evaluates to `false`, the expression `!(x && y)` evaluates to `true`. 

The following expressions illustrate the result of using the logical NOT (!) operator: 

  * `!true` returns `false`.
  * `!false` returns `true`.

Operands | `expression:[Boolean](Boolean.html)` — An expression or a variable that evaluates to a Boolean value.   
---|---  
  
Result | `[Boolean](Boolean.html)` — The Boolean result of the logical operation.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[!= (inequality)](#inequality)   
[&& (logical AND)](#logical_AND)   
[|| (logical OR)](#logical_OR)   
[&&= (logical AND assignment)](#logical_AND_assignment)   
[||= (logical OR assignment)](#logical_OR_assignment)   
[=== (strict equality)](#strict_equality)   
[!== (strict inequality)](#strict_inequality)

|| logical OR| operator|   
---|---|---  
  
Usage | `expression1 || expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Returns `expression1` if it is `true` or can be converted to `true`, and `expression2` otherwise. If you use a function call as `expression2`, the function is not called if `expression1` evaluates to `true`. 

If both operands are of type Boolean, the result is `true` if either or both expressions are `true`; the result is `false` only if both expressions are `false`, as shown in the following table: 

Expression  | Evaluates   
---|---  
`true || true` | `true`  
`true || false` | `true`  
`false || false` | `false`  
`false || true` | `true`  
  
Operands | `expression1:[*](specialTypes.html#*)` — A value of any type.   
---|---  
| `expression2:[*](specialTypes.html#*)` — A value of any type.   
  
Result | `[*](specialTypes.html#*)` — A Boolean value if both operands are members of the Boolean data type. Otherwise, the result will be the value of either of the two expressions.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[!= (inequality)](#inequality)   
[&& (logical AND)](#logical_AND)   
[&&= (logical AND assignment)](#logical_AND_assignment)   
[||= (logical OR assignment)](#logical_OR_assignment)   
[! (logical NOT)](#logical_NOT)   
[=== (strict equality)](#strict_equality)   
[!== (strict inequality)](#strict_inequality)

||= logical OR assignment| operator|   
---|---|---  
  
Usage | `expression1 ||= expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of `expression1 || expression2`. For example, the following two statements are equivalent: 
    
    
    x ||= y; 
    x = x || y; 

Operands | `expression1:[*](specialTypes.html#*)` — A value of any type.   
---|---  
| `expression2:[*](specialTypes.html#*)` — A value of any type.   
  
Result | `[*](specialTypes.html#*)` — A Boolean value if both operands are members of the Boolean data type. Otherwise, the result will be the value of either of the two expressions.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[!= (inequality)](#inequality)   
[|| (logical OR)](#logical_OR)   
[&& (logical AND)](#logical_AND)   
[&&= (logical AND assignment)](#logical_AND_assignment)   
[! (logical NOT)](#logical_NOT)   
[=== (strict equality)](#strict_equality)   
[!== (strict inequality)](#strict_inequality)

% modulo| operator|   
---|---|---  
  
Usage | `expression1 **%** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Calculates the remainder of `expression1` divided by `expression2`. If either operand is non-numeric, the modulo (`%`) operator attempts to convert it to a number. 

The sign of the modulo result matches the sign of the dividend (the first number). For example, `-4 % 3` and `-4 % -3` both evaluate to `-1`.

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number. A string that contains only numeric characters evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number. A string that contains only numeric characters evaluates to a number.   
  
Result | `[Number](Number.html)` — The result of the arithmetic operation.  
---|---  
  
Example   

See also

[/ (division)](#division)   
[Math.round()](Math.html#round\(\))

%= modulo assignment| operator|   
---|---|---  
  
Usage | `expression1 **%=** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of `expression1 % expression2`. The following two statements are equivalent: 
    
    
    x %= y; 
    x = x % y; 

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[Number](Number.html)` — The result of the arithmetic operation.  
---|---  
  
Example   

See also

[% (modulo)](#modulo)

* multiplication| operator|   
---|---|---  
  
Usage | `expression1 ***** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Multiplies two numerical expressions. If both expressions are integers, the product is an integer. If either or both expressions are floating-point numbers, the product is a floating-point number.

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[Number](Number.html)` — An integer or floating-point number.  
---|---  
  
Example   

*= multiplication assignment| operator|   
---|---|---  
  
Usage | `expression1 ***=** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of ` expression1 * expression2`. For example, the following two expressions are equivalent: 
    
    
    x *= y 
    x = x * y 

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[Number](Number.html)` — The value of `expression1 * expression2` . If an expression cannot be converted to a numeric value, it returns `NaN` (not a number).  
---|---  
  
Example   

See also

[* (multiplication)](#multiplication)

:: name qualifier| operator|   
---|---|---  
  
Usage | 
    
    
    namespace::property
    
    
    namespace::method()
    
    
    namespace::xmlObject.property
    
    
    namespace::xmlObject.@attribute  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Identifies the namespace of a property, a method, an XML property, or an XML attribute.

Operands | `namespace:[Object](Object.html)` — The identifying namespace.   
---|---  
| `propertyName:[Object](Object.html)` — The property, method, XML property, or XML attribute to identify.   
  
Example   

See also

[Namespace class](Namespace.html)   
[XML class](XML.html)

new| operator|   
---|---|---  
  
Usage | `**new** constructor(parameters)`  
---|---  
  
**Runtime version:**|   
---|---  
  
Instantiates a class instance. The `new` operator can be used with a class or a variable of type Class to create an instance of a class. The `new` operator is commonly used with a class object to create an instance of a class. For example, the statement `new Sprite()` creates an instance of the Sprite class. 

The `new` operator can also be used to associate a class with an embedded asset, which is an external object such as an image, sound, or font that is compiled into a SWF file. Each embedded asset is represented by a unique embedded asset class. To access an embedded asset, you must use the `new` operator to instantiate its associated class. Subsequently, you can call the appropriate methods and properties of the embedded asset class to manipulate the embedded asset.

If you prefer to define classes with Function objects instead of the `class` keyword, you can use the `new` operator to create objects based on constructor functions. Do not confuse constructor functions with constructor methods of a class. A constructor function is a Function object that is defined with the `function` keyword, but that is not part of a class definition. If you use constructor functions to create objects, you must use prototype inheritance instead of class inheritance.

Operands | `constructor:[*](specialTypes.html#*)` — A class, a function, or a variable that holds a value of type Class.   
---|---  
| `parameters:[*](specialTypes.html#*)` — One or more parameters, separated by commas.   
  
Example   

See also

[[] (array access)](#array_access)   
[class statement](statements.html#class)   
[Object.constructor](Object.html#constructor)   
[Object.prototype](Object.html#prototype)   
[{} (object initializer)](#object_initializer)

?. null condition member access| operator|   
---|---|---  
  
Usage | `object?.property_or_method`  
---|---  
  
**Language version:**|  ActionScript 3.1  
---|---  
**Runtime version:**|  AIR 50  
---|---  
  
Accesses class variables and methods, gets and sets object properties, with an inherent null-object check. If the object on which this operator is applied is null, then rather than throwing a null reference error, the expression evaluates to null. 

For example `sprite.stage.nativeWindow` would return the native window on which the 'sprite' object is placed. But if the sprite was not on the stage, this would throw a null reference error. Using the null condition member access, this becomes `sprite.stage?.nativeWindow` which would then result in a 'null' value if the sprite was not on the stage, rather than throwing an errro.

Operands | `object:[Object](Object.html)` — An instance of a class. The object can be an instance of any of the built-in ActionScript classes or a class you define. This operand is always to the left of the dot (.) operator.   
---|---  
| `property_or_method:[*](specialTypes.html#*)` — The name of a property or method associated with an object. All the valid methods and properties for the built-in classes are listed in the method and property summary tables for that class. This operand is always to the right of the dot (.) operator.   
  
Result | `[*](specialTypes.html#*)` — If the `object` is `null`, this values to `null`. Otherwise it returns the variable, method, or property named on the right side of the dot.  
---|---  
  
Example   

See also

[dot operator](#dot)

?? nullish coalescing| operator|   
---|---|---  
  
Usage | `expression1 ?? expression2`  
---|---  
  
**Language version:**|  ActionScript 3.1  
---|---  
**Runtime version:**|  AIR 50  
---|---  
  
Returns `expression1` unless it is `null` or `undefined`, and `expression2` otherwise. If you use a function call as `expression2`, the function is not called unless `expression1` evaluates to `null` or `undefined`. 

This is essentially a short-hand way of writing "`(expression1 == null || expression1 == undefined) ? expression2 : expression1`". If `expression1` is a 'false' or zero value, this is a defined value and so would be returned (i.e. "`(0 ?? 1)`" would return `0`, whereas "`(null ?? 1)`" would return `1`, as would "`(0 || 1)`"). 

Operands | `expression1:[*](specialTypes.html#*)` — A value of any type.   
---|---  
| `expression2:[*](specialTypes.html#*)` — A value of any type.   
  
Result | `[*](specialTypes.html#*)` — The result will be the value of either of the two expressions.  
---|---  
  
See also

[== (equality)](#equality)   
[|| (logical OR)](#logical_OR)

{} object initializer| operator|   
---|---|---  
  
Usage | 
    
    
    object = {name1 : value1, name2 : value2,... nameN : valueN}  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Creates a new object and initializes it with the specified `name` and `value` property pairs. Using this operator is the same as using the `new Object` syntax and populating the property pairs using the assignment operator. The prototype of the newly created object is generically named the Object object. 

This operator is also used to mark blocks of contiguous code associated with flow control statements (`for`, `while`, `if`, `else`, `switch`) and functions. 

Operands | `object:[Object](Object.html)` — The object to create.   
---|---  
| `name1,2,...N:[Object](Object.html)` — The names of the properties.   
| `value1,2,...N:[Object](Object.html)` — The corresponding values for each `name` property.   
  
Result | `[Object](Object.html)` — An Object object.  
---|---  
  
Example   

See also

[braces (XML)](#braces_\(XML\))   
[Object class](Object.html)

() parentheses| operator|   
---|---|---  
  
Usage | 
    
    
    (expression1[, expression2])
    
    
    (expression1, expression2)
    
    
    function(parameter1,..., parameterN)   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Performs a grouping operation on one or more parameters, performs sequential evaluation of expressions, or surrounds one or more parameters and passes them as arguments to a function that precedes the parentheses. 

Usage 1: Controls the order in which the operators execute. Parentheses override the normal precedence order and cause the expressions within the parentheses to be evaluated first. When parentheses are nested, the contents of the innermost parentheses are evaluated before the contents of the outer ones.

Usage 2: Evaluates a series of expressions, separated by commas, in sequence, and returns the result of the final expression. 

Usage 3: Surrounds one or more parameters and passes them to the function that precedes the parentheses.

Operands | `expression1:[Object](Object.html)` — An expression, which can include numbers, strings, variables, or text.   
---|---  
| `expression2:[Object](Object.html)` — An expression, which can include numbers, strings, variables, or text.   
| `function:[Function](Function.html)` — The function to be performed on the contents of the parentheses.   
| `parameter1...parameterN:[Object](Object.html)` — A series of parameters to execute before the results are passed as arguments to the function outside the parentheses.   
  
Example   

See also

[parentheses (XML)](#parentheses_\(XML\))   
[with](statements.html#with)

( ) parentheses (XML)| operator|   
---|---|---  
  
Usage | 
    
    
    myXML.(expression)  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates an expression in an ECMAScript for XML (E4X) XML construct. For example, `myXML.(lastName == "Smith")` identifies XML elements with the name `lastName` and the value `"Smith"`. The result is an XMLList object.

Operands | `myXML:[*](specialTypes.html#*)` — An XML or XMLList object.   
---|---  
| `expression:[*](specialTypes.html#*)` — The expression defining the matching elements.   
  
Result | `[XMLList](XMLList.html)` — The XMLList specified by the parentheses.  
---|---  
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)

/ RegExp delimiter| operator|   
---|---|---  
  
Usage | 
    
    
    /pattern/flags  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
When used before and after characters, indicates that the characters have a literal value and are considered a regular expression (RegExp), not a variable, string, or other ActionScript element. Note, however, that two sequential forward slash characters (`//`) indicate the beginning of a comment. 

Operands | `pattern:[String](String.html)` — A sequence of one or more characters, defining the pattern of the regular expression.   
---|---  
| `flags:[String](String.html)` — A sequence of zero or more of the following characters: `g` (for the `global` flag), `i` (for the `ignoreCase` flag), `s` (for the `dotall` flag), `x` (for the `extended` flag).   
  
Example   

See also

[RegExp class](RegExp.html)

=== strict equality| operator|   
---|---|---  
  
Usage | `expression1 === expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Tests two expressions for equality, but does not perform automatic data conversion. The result is `true` if both expressions, including their data types, are equal. 

The strict equality (`===`) operator is the same as the equality (`==`) operator in three ways:

  * Numbers and Boolean values are compared by value and are considered equal if they have the same value.
  * String expressions are equal if they have the same number of characters and the characters are identical.
  * Variables representing objects, arrays, and functions are compared by reference. Two such variables are equal if they refer to the same object, array, or function. Two separate arrays are never considered equal, even if they have the same number of elements.

The strict equality (`===`) operator differs from the equality (`==`) operator in only two ways: 

  * The strict equality operator performs automatic data conversion only for the number types (Number, int, and uint), whereas the equality operator performs automatic data conversion for all primitive data types.
  * When comparing `null` and `undefined`, the strict equality operator returns `false`.

The strict equality operator generates different results in ActionScript 3.0 than it did in ActionScript 2.0 in two situations involving primitive values (for example, `var x:Number = 1`) with primitive objects (for example, `var x:Number = new Number(1)`). This is because ActionScript 3.0 removes the distinction between primitive values and primitive wrapper objects. 

First, comparisons between primitive values and primitive objects that contain the same value return `true` in ActionScript 3.0, but `false` in earlier versions. In earlier versions, the data type of a primitive value is either Boolean, Number, or String, whereas the data type of a primitive object is always Object rather than Boolean, Number or String. The practical effect of this difference is that the following code results in `false` in previous versions of ActionScript because the data types of the operands do not match, but the result is `true` in ActionScript 3.0 because primitive values are typed as either Boolean, Number, int, uint, or String, whether they are wrapped in an object or not.
    
    
    var num1:Number = 1;
    var num2:Number = new Number(1);
    trace(num1 === num2); // true in ActionScript 3.0, false in ActionScript 2.0
    			

Second, comparisons between two primitive objects that contain the same value result in `true` in ActionScript 3.0, but `false` in previous versions. 
    
    
    var num1:Number = new Number(1);
    var num2:Number = new Number(1);
    trace(num1 == num2);  // true in ActionScript 3.0, false in ActionScript 2.0
    trace(num1 === num2); // true in ActionScript 3.0, false in ActionScript 2.0

This is because in previous versions of ActionScript, both variables belong to the data type Object, so they are compared by reference and the result is `false` for both the equality and strict equality operations. In ActionScript 3.0, however, both variables belong to the data type Number, so they are compared by value and the result is `true` for both the equality and strict equality operators. 

Operands | `expression1:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or function.   
---|---  
| `expression2:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or function.   
  
Result | `[Boolean](Boolean.html)` — The Boolean result of the comparison.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[!= (inequality)](#inequality)   
[&& (logical AND)](#logical_AND)   
[! (logical NOT)](#logical_NOT)   
[|| (logical OR)](#logical_OR)   
[!== (strict inequality)](#strict_inequality)

!== strict inequality| operator|   
---|---|---  
  
Usage | `expression1 **!==** expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Tests for the exact opposite of the strict equality (`===`) operator. The strict inequality operator performs the same as the inequality operator except that only the int and uint data types are converted. 

If `expression1` is equal to `expression2`, and their data types are equal, the result is `false`.

The strict inequality (`!==`) operator is the same as the inequality (`!=`) operator in three ways:

  * Numbers and Boolean values are compared by value and are considered equal if they have the same value.
  * String expressions are equal if they have the same number of characters and the characters are identical.
  * Variables representing objects, arrays, and functions are compared by reference. Two such variables are equal if they refer to the same object, array, or function. Two separate arrays are never considered equal, even if they have the same number of elements.

The strict inequality operator differs from the inequality (`!=`) operator in only two ways: 

  * The strict inequality (`!==`) operator performs automatic data conversion only for the number types, Number, int, and uint, whereas the inequality (`!=`) operator performs automatic data conversion for all primitive data types.
  * When comparing `null` and `undefined`, the strict inequality (`!==`) operator returns `true`.

Operands | `expression1:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or function.   
---|---  
| `expression2:[Object](Object.html)` — A number, string, Boolean value, variable, object, array, or function.   
  
Result | `[Boolean](Boolean.html)` — The Boolean result of the comparison.  
---|---  
  
Example   

See also

[== (equality)](#equality)   
[!= (inequality)](#inequality)   
[&& (logical AND)](#logical_AND)   
[! (logical NOT)](#logical_NOT)   
[|| (logical OR)](#logical_OR)   
[=== (strict equality)](#strict_equality)

" string delimiter| operator|   
---|---|---  
  
Usage | 
    
    
     "text"   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
When used before and after characters, indicates that the characters have a literal value and are considered a string, not a variable, numerical value, or other ActionScript element.

Operands | `text:[String](String.html)` — A sequence of zero or more characters.   
---|---  
  
Example   

See also

[String class](String.html)   
[String() function](package.html#String\(\))

\- subtraction| operator|   
---|---|---  
  
Usage | 
    
    
    **-** expression
    
    
     expression1 **-** expression2  
  
---|---  
  
**Runtime version:**|   
---|---  
  
Used for negating or subtracting. 

Usage 1: When used for negating, the operator reverses the sign of a numerical expression.

Usage 2: When used for subtracting, the operator performs an arithmetic subtraction on two numerical expressions, subtracting `expression2` from `expression1`. When both expressions are integers, the difference is an integer. When either or both expressions are floating-point numbers, the difference is a floating-point number.

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[Number](Number.html)` — An integer or floating-point number.  
---|---  
  
Example   

-= subtraction assignment| operator|   
---|---|---  
  
Usage | `expression1 -= expression2`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Assigns `expression1` the value of `expression1 - expression2`. For example, the following two statements are equivalent: 
    
    
    x -= y ;
    x = x - y;

String expressions must be converted to numbers; otherwise, the result is `NaN` (not a number).

Operands | `expression1:[Number](Number.html)` — A number or expression that evaluates to a number.   
---|---  
| `expression2:[Number](Number.html)` — A number or expression that evaluates to a number.   
  
Result | `[Number](Number.html)` — The result of the arithmetic operation.  
---|---  
  
Example   

See also

[\- (subtraction)](#subtraction)

: type| operator|   
---|---|---  
  
Usage | 
    
    
    [modifiers] var variableName:type
    
    
    function functionName():type { ... }
    
    
    function functionName(parameter1:type, ..., parameterN:type) [:type]{ ... }   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Used for assigning a data type; this operator specifies the variable type, function return type, or function parameter type. When used in a variable declaration or assignment, this operator specifies the variable's type; when used in a function declaration or definition, this operator specifies the function's return type; when used with a function parameter in a function definition, this operator specifies the variable type expected for that parameter. 

Type checking always occurs at run time. However, when the compiler is set to strict mode, all types are also checked at compile time, and errors are generated when there is a mismatch. Mismatches can occur during assignment operations, function calls, and class member dereferencing using the dot (`.`) operator.

Types that you can use include all native object types, classes and interfaces that you define, and `void`. The recognized native types are Boolean, Number, int, uint, and String. All built-in classes are also supported as native types.

If you do not assign a data type, the variable, function return value, or function parameter is considered untyped, which means that the value can be of any data type. If you wish to make clear your intent to use an untyped value, you can use the asterisk (*) character as the type annotation. When used as a type annotation, the asterisk character is equivalent to leaving a variable, function return type, or function parameter untyped.

Operands | `variableName:[*](specialTypes.html#*)` — An identifier for a variable.   
---|---  
| `type:[*](specialTypes.html#*)` — A native data type, class name that you have defined, or interface name.   
| `functionName:[Function](Function.html)` — An identifier for a function.   
| `parameter:[*](specialTypes.html#*)` — An identifier for a function parameter.   
  
Example   

See also

[function statement](statements.html#function)   
[var statement](statements.html#var)

typeof| operator|   
---|---|---  
  
Usage | `typeof expression`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates `expression` and returns a string specifying the expression's data type. The result is limited to six possible string values: `boolean`, `function`, `number`, `object`, `string`, and `xml`. If you apply this operator to an instance of a user-defined class, the result is the string `object`. The `typeof` operator is included for backward compatibility. Use the `is` operator to check type compatibility. 

Operands | `expression:[Object](Object.html)` — An object to evaluate.   
---|---  
  
Result | `[String](String.html)` — A string representation of the type of `expression`. The following table shows the results of the `typeof` operator on each type of expression.  | Expression Type | Result  
---|---  
Array  |  `object`  
Boolean  |  `boolean`  
Function  |  `function`  
int  |  `number`  
Number  |  `number`  
Object  |  `object`  
String  |  `string`  
uint  |  `number`  
XML  |  `xml`  
XMLList  |  `xml`  
*  |  `undefined`  
  
Example   

See also

[as](#as)   
[instanceof](#instanceof)   
[is](#is)

void| operator|   
---|---|---  
  
Usage | `void expression`  
---|---  
  
**Runtime version:**|   
---|---  
  
Evaluates an expression and then discards its value, returning `undefined`. The `void` operator is often used in comparisons that use the `==` operator to test for undefined values.

Operands | `expression:[Object](Object.html)` — An expression to be evaluated.   
---|---  
  
Result | `[*](specialTypes.html#*)` — The value `undefined`.  
---|---  
  
< > XML literal tag delimiter| operator|   
---|---|---  
  
Usage | 
    
    
     myXML= <{tagName} {attributeName} = {attributeValue}>{content}</{tagName}>  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines an XML tag in an XML literal. Use the forward slash / to define the closing tag. 

Operands | `myXML:[*](specialTypes.html#*)` — An XML or XMLList object.   
---|---  
| `tagName:[*](specialTypes.html#*)` — An expression that evaluates to the name of an XML tag.   
| `attributeName:[*](specialTypes.html#*)` — An expression that evaluates to the name of an XML attribute.   
| `attributeValue:[*](specialTypes.html#*)` — An expression that evaluates to the value of an XML attribute.   
| `content:[*](specialTypes.html#*)` — An expression that evaluates to the contents of an XML tag.   
  
Example   

See also

[XML class](XML.html)   
[XMLList class](XMLList.html)

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Jul 3 2024, 9:16 AM GMT+01:00\) : Operators)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Jul 3 2024, 9:16 AM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)