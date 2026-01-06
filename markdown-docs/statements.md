# Statements

Statements are language elements that perform or specify an action at runtime. For example, the `return` statement returns a result value for the function in which it executes. The `if` statement evaluates a condition to determine the next action that should be taken. The `switch` statement creates a branching structure for ActionScript statements. 

Attribute keywords alter the meaning of definitions, and can be applied to class, variable, function, and namespace definitions. Definition keywords are used to define entities such as variables, functions, classes, and interfaces. Primary expression keywords represent literal values. For a list of reserved words, see [Learning ActionScript 3.0](http://www.adobe.com/go/learn_as3_reservedwords_en).

Directives include statements and definitions and can have an effect at compile time or runtime. Directives that are neither statements nor definitions are labeled as directives in the following table.

  
| Statement summary  
---|---  
| [break](#break)| Appears within a loop (`for`, `for..in`, `for each..in`, `do..while`, or `while`) or within a block of statements associated with a particular case within a `switch` statement.  
| [case](#case)| Defines a jump target for the `switch` statement.  
| [continue](#continue)| Jumps past all remaining statements in the innermost loop and starts the next iteration of the loop as if control had passed through to the end of the loop normally.  
| [default](#default)| Defines the default case for a `switch` statement.  
| [do..while](#do..while)| Similar to a `while` loop, except that the statements are executed once before the initial evaluation of the condition.  
| [else](#else)| Specifies the statements to run if the condition in the `if` statement returns `false`.  
| [for](#for)| Evaluates the `init` (initialize) expression once and then starts a looping sequence.  
| [for..in](#for..in)| Iterates over the dynamic properties of an object or elements in an array and executes `statement` for each property or element.  
| [for each..in](#for_each..in)| Iterates over the items of a collection and executes `statement` for each item.  
| [if](#if)| Evaluates a condition to determine the next statement to execute.  
| [label](#label)| Associates a statement with an identifier that can be referenced by `break` or `continue`.  
| [return](#return)| Causes execution to return immediately to the calling function.  
| [super](#super)| Invokes the superclass or parent version of a method or constructor.  
| [switch](#switch)| Causes control to transfer to one of several statements, depending on the value of an expression.  
| [throw](#throw)| Generates, or _throws_ , an error that can be handled, or _caught_ , by a `catch` code block.  
| [try..catch..finally](#try..catch..finally)| Encloses a block of code in which an error can occur, and then responds to the error.  
| [while](#while)| Evaluates a condition and if the condition evaluates to `true`, executes one or more statements before looping back to evaluate the condition again.  
| [with](#with)| Establishes a default object to be used for the execution of a statement or statements, potentially reducing the amount of code that needs to be written.  
| Attribute keyword summary  
| [dynamic](#dynamic)| Specifies that instances of a class may possess dynamic properties added at runtime.  
| [final](#final)| Specifies that a method cannot be overridden or that a class cannot be extended.  
| [internal](#internal)| Specifies that a class, variable, constant or function is available to any caller within the same package.  
| [native](#native)| Specifies that a function or method is implemented by Flash Player in native code.  
| [override](#override)| Specifies that a method replaces an inherited method.  
| [private](#private)| Specifies that a variable, constant, method or namespace is available only to the class that defines it.  
| [protected](#protected)| Specifies that a variable, constant, method, or namespace is available only to the class that defines it and to any subclasses of that class.  
| [public](#public)| Specifies that a class, variable, constant or method is available to any caller.  
| [static](#static)| Specifies that a variable, constant, or method belongs to the class, rather than to instances of the class.  
| Definition keyword summary  
| [... (rest) parameter](#..._\(rest\)_parameter)| Specifies that a function will accept any number of comma-delimited arguments.  
| [class](#class)| Defines a class, which lets you instantiate objects that share methods and properties that you define.  
| [const](#const)| Specifies a constant, which is a variable that can be assigned a value only once.  
| [extends](#extends)| Defines a class that is a subclass of another class.  
| [function](#function)| Comprises a set of statements that you define to perform a certain task.  
| [get](#get)| Defines a getter, which is a method that can be read like a property.  
| [implements](#implements)| Specifies that a class implements one or more interfaces.  
| [interface](#interface)| Defines an interface.  
| [namespace](#namespace)| Allows you to control the visibility of definitions.  
| [package](#package)| Allows you to organize your code into discrete groups that can be imported by other scripts.  
| [set](#set)| Defines a setter, which is a method that appears in the public interface as a property.  
| [var](#var)| Specifies a variable.  
| Directive summary  
| [default xml namespace](#default_xml_namespace)|  The `default xml namespace` directive sets the default namespace to use for XML objects.   
| [import](#import)| Makes externally defined classes and packages available to your code.  
| [include](#include)| Includes the contents of the specified file, as if the commands in the file are part of the calling script.  
| [use namespace](#use_namespace)| Causes the specified namespaces to be added to the set of open namespaces.  
| Namespace summary  
| [AS3](#AS3)| Defines methods and properties of the core ActionScript classes that are fixed properties instead of prototype properties.  
| [flash_proxy](#flash_proxy)| Defines methods of the Proxy class.  
| [object_proxy](#object_proxy)| Defines methods of the ObjectProxy class.  
| Primary expression keyword summary  
| [false](#false)| A Boolean value representing false.  
| [null](#null)| A special value that can be assigned to variables or returned by a function if no data was provided.  
| [this](#this)| A reference to a method's containing object.  
| [true](#true)| A Boolean value representing true.  
  
Statement, Keyword & Directive detail

... (rest) parameter| definition keyword  
---|---  
  
Usage | 
    
    
    function functionName(parameter0, parameter1, ...rest){ 
    	// statement(s) 
    }   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a function will accept any number of comma-delimited arguments. The list of arguments becomes an array that is available throughout the function body. The name of the array is specified after the `...` characters in the parameter declaration. The parameter can have any name that is not a reserved word. 

If used with other parameters, the `...` (rest) parameter declaration must be the last parameter specified. The `...` (rest) parameter array is populated only if the number of arguments passed to the function exceeds the number of other parameters.

Each argument in the comma-delimited list of arguments is placed into an element of the array. If you pass an instance of the Array class, the entire array is placed into a single element of the `...` (rest) parameter array.

Use of this parameter makes the `arguments` object unavailable. Although the `...` (rest) parameter gives you the same functionality as the `arguments` array and `arguments.length` property, it does not provide functionality similar to that provided by `arguments.callee`. Make sure you do not need to use `arguments.callee` before using the `...` (rest) parameter.

Parameters | `rest:[*](specialTypes.html#*)` — An identifier that represents the name of the array of arguments passed in to the function. The parameter does not need to be called `rest`; it can have any name that is not a keyword. You can specify the data type of the `...` (rest) parameter as Array, but this could cause confusion because the parameter accepts a comma-delimited list of values, which is not identical to an instance of the Array class.   
---|---  
  
Example   

See also

[arguments object](arguments.html)

AS3| namespace|   
---|---|---  
  
Defines methods and properties of the core ActionScript classes that are fixed properties instead of prototype properties. When you set the "-as3" compiler option to `true` (which is the default setting in Flex Builder 2), the AS3 namespace is automatically opened for all the core classes. This means that an instance of a core class will use fixed properties and methods instead of the versions of those same properties and methods that are attached to the class's prototype object. The use of fixed properties usually provides better performance, but at the cost of backward compatibility with the ECMAScript edition 3 language specification (ECMA-262).

See also

[Object class](Object.html)

break| statement|   
---|---|---  
  
Usage | `break [label]`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Appears within a loop (`for`, `for..in`, `for each..in`, `do..while`, or `while`) or within a block of statements associated with a particular case in a `switch` statement. When used in a loop, the `break` statement instructs Flash to skip the rest of the loop body, stop the looping action, and execute the statement following the loop statement. When used in a `switch`, the `break` statement instructs Flash to skip the rest of the statements in that `case` block and jump to the first statement that follows the enclosing `switch` statement. 

In nested loops, `break` only skips the rest of the immediate loop and does not break out of the entire series of nested loops. To break out of an entire series of nested loops, use `label` or `try..catch..finally`.

The `break` statement can have an optional label that must match an outer labeled statement. Use of a label that does not match the label of an outer statement is a syntax error. Labeled `break` statements can be used to break out of multiple levels of nested loop statements, `switch` statements, or `block` statements. For an example, see the entry for the `label` statement.

Parameters | `label:[*](specialTypes.html#*)` — The name of a label associated with a statement.   
---|---  
  
Example   

See also

[do..while](#do..while)   
[for](#for)   
[for..in](#for..in)   
[for each..in](#for_each..in)   
[label](#label)   
[while](#while)

case| statement|   
---|---|---  
  
Usage | 
    
    
    case jumpTarget: statements  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines a jump target for the `switch` statement. If the `jumpTarget` parameter equals the `expression` parameter of the `switch` statement using strict equality (`===`), Flash Player executes the statements in the `statements` parameter until it encounters a `break` statement or the end of the `switch` statement. 

If you use the `case` statement outside a `switch` statement, it produces an error and the script doesn't compile.

**Note:** Always end the `statements` parameter with a `break` statement. If you omit the `break` statement from the `statements` parameter, it continues executing with the next `case` statement instead of exiting the `switch` statement.

Parameters | `jumpTarget:[*](specialTypes.html#*)` — Any expression.   
---|---  
| `statements:[*](specialTypes.html#*)` — Statements to execute if `jumpTarget` matches the conditional expression in the `switch` statement.   
  
Example   

See also

[break](#break)   
[switch](#switch)

class| definition keyword|   
---|---|---  
  
Usage | 
    
    
    [dynamic] [public | internal] [final] class className [ extends superClass ] [ implements interfaceName[, interfaceName... ] ] { 
    	// class definition here
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines a class, which lets you instantiate objects that share methods and properties that you define. For example, if you are developing an invoice-tracking system, you could create an Invoice class that defines all the methods and properties that each invoice should have. You would then use the `new Invoice()` command to create Invoice objects. 

Each ActionScript source file can contain only one class that is visible to other source files or scripts. The externally visible class can be a public or internal class, and must be defined inside a package statement. If you include other classes in the same file, the classes must be placed outside of the package statement and at the end of the file. 

The name of the externally visible class must match the name of the ActionScript source file that contains the class. The name of the source file must be the name of the class with the file extension .as appended. For example, if you name a class Student, the file that defines the class must be named Student.as.

You cannot nest class definitions; that is, you cannot define additional classes within a class definition.

You can define a constructor method, which is a method that is executed whenever a new instance of the class is created. The name of the constructor method must match the name of the class. If you do not define a constructor method, a default constructor is created for you.

To indicate that objects can add and access dynamic properties at runtime, precede the class statement with the `dynamic` keyword. To declare that a class implements an interface, use the `implements` keyword. To create subclasses of a class, use the `extends` keyword. (A class can extend only one class, but can implement several interfaces.) You can use `implements` and `extends` in a single statement. The following examples show typical uses of the `implements` and `extends` keywords:
    
    
    class C implements Interface_i, Interface_j // OK 
    class C extends Class_d implements Interface_i, Interface_j // OK 
    class C extends Class_d, Class_e // not OK 

Parameters | `className:[Class](Class.html)` — The fully qualified name of the class.   
---|---  
  
Example   

See also

[dynamic](#dynamic)   
[extends](#extends)   
[final](#final)   
[internal](#internal)   
[public](#public)

const| definition keyword|   
---|---|---  
  
Usage | 
    
    
    const identifier = value   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies a constant, which is a variable that can be assigned a value only once. 

You can strictly type a constant by appending a colon (:) character followed by the data type.

Parameters | `identifier:[*](specialTypes.html#*)` — An identifier for the constant.   
---|---  
  
Example   

See also

[var](#var)

continue| statement|   
---|---|---  
  
Usage | 
    
    
    continue [label]  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Jumps past all remaining statements in the innermost loop and starts the next iteration of the loop as if control had passed to the end of the loop normally. The `continue` statement has no effect outside a loop. In nested loops, use the optional `label` parameter to skip more than just the innermost loop. 

The `continue` statement can have an optional label that must match an outer labeled statement. Use of a label that does not match the label of an outer statement is a syntax error. Labeled `continue` statements can be used to skip multiple levels of nested loop statements.

  
Example   

See also

[do..while](#do..while)   
[for](#for)   
[for..in](#for..in)   
[for each..in](#for_each..in)   
[label](#label)   
[while](#while)

default| statement|   
---|---|---  
  
Usage | 
    
    
    default: statements   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines the default case for a `switch` statement. The statements execute if the `expression` parameter of the `switch` statement doesn't equal (using the strict equality [`===`] operation) any of the `expression` parameters that follow the `case` keywords for a given `switch` statement. 

A `switch` statement does not require a `default` case statement. A `default` case statement does not have to be last in the list. If you use a `default` statement outside a `switch` statement, it produces an error and the script doesn't compile.

Parameters | `statements:[*](specialTypes.html#*)` — Any statements.   
---|---  
  
Example   

See also

[switch](#switch)

default xml namespace| directive|   
---|---|---  
  
Usage | `default xml namespace = ns`  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
The `default xml namespace` directive sets the default namespace to use for XML objects. 

If you do not set `default xml namespace`, the default namespace is the unnamed namespace (with the URI set to an empty string). The scope of a `default xml namespace` declaration is within a function block, like the scope of a variable. 

  
Example   

See also

[namespace](#namespace)   
[Namespace Class](Namespace.html)   
[use namespace](#use_namespace)   
[XML](XML.html)

do..while| statement|   
---|---|---  
  
Usage | 
    
    
    do { statement(s) } while (condition)  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Similar to a `while` loop, except that the statements are executed once before the initial evaluation of the condition. Subsequently, the statements are executed only if the condition evaluates to `true`. 

A `do..while` loop ensures that the code inside the loop executes at least once. Although you can also do this with a `while` loop by placing a copy of the statements to be executed before the `while` loop begins, many programmers believe that `do..while` loops are easier to read.

If the condition always evaluates to `true`, the `do..while` loop is infinite. If you enter an infinite loop, you encounter problems with Flash Player and eventually get a warning message or crash the player. Whenever possible, use a `for` loop if you know the number of times you want to loop. Although `for` loops are easy to read and debug, they cannot replace `do..while` loops in all circumstances.

Parameters | `condition:[Boolean](Boolean.html)` — The condition to evaluate. The `statement(s)` within the `do` block of code will execute as long as the `condition` parameter evaluates to `true` .   
---|---  
  
Example   

See also

[break](#break)   
[continue](#continue)   
[while](#while)

dynamic| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    dynamic class className { // class definition here }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that instances of a class may possess dynamic properties added at runtime. If you use the `dynamic` attribute on a class, you can add properties to instances of that class at runtime. Classes that are not marked as `dynamic` are considered _sealed_ , which means that properties cannot be added to instances of the class. 

If a class is sealed (not dynamic), attempts to get or set properties on class instances result in an error. If you have your compiler set to strict mode and you specify the data type when you create instances, attempts to add properties to sealed objects generate a compiler error; otherwise, a runtime error occurs.

The `dynamic` attribute is not inherited by subclasses. If you extend a dynamic class, the subclass is dynamic only if you declare the subclass with the `dynamic` attribute.

**Note:** This keyword is supported only when used in external script files, not in scripts written in the Actions panel.

  
Example   

See also

[class](#class)

else| statement|   
---|---|---  
  
Usage | 
    
    
    if (condition) { 
    	// statement(s)
    } 
    else {
    	// statement(s)
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies the statements to run if the condition in the `if` statement returns `false`. The curly braces (`{}`) that enclose the statements to be executed by the `else` statement are not necessary if only one statement will execute.

Parameters | `condition:[Boolean](Boolean.html)` — An expression that evaluates to `true` or `false`.   
---|---  
  
Example   

See also

[if](#if)

extends| definition keyword|   
---|---|---  
  
Usage | 
    
    
    class className extends otherClassName {}
    interface interfaceName extends otherInterfaceName {}   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines a class that is a subclass of another class. The subclass inherits all the methods, properties, functions, and so on that are defined in the superclass. Classes that are marked as `final` cannot be extended. 

You can also use the `extends` keyword to extend an interface. An interface that extends another interface includes all the original interface's method declarations.

**Note:** To use this keyword, you must specify ActionScript 2.0 and Flash Player 6 or later in the Flash tab of your FLA file's Publish Settings dialog box. This keyword is supported only when used in external script files, not in scripts written in the Actions panel.

Parameters | `className:[Class](Class.html)` — The name of the class you are defining.   
---|---  
  
Example   

See also

[class](#class)   
[final](#final)   
[interface](#interface)

false| primary expression keyword|   
---|---|---  
  
Usage | 
    
    
    false  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
A Boolean value representing false. A Boolean value is either `true` or `false`; the opposite of `false` is `true`. 

When automatic data typing converts `false` to a number, it becomes `0`; when it converts `false` to a string, it becomes `"false"`.

**Note:** The string `"false"` converts to the Boolean value `true`.

  
Example   

See also

[Boolean class](Boolean.html)   
[true](#true)

final| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    final function methodName() { 
    	// your statements here 
    }
    final class className {}  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a method cannot be overridden or that a class cannot be extended. An attempt to override a method, or extend a class, marked as `final` results in an error.

Parameters | `methodName:[Function](Function.html)` — The name of the method that cannot be overridden.   
---|---  
| `className:[Class](Class.html)` — The name of the class that cannot be extended.   
  
See also

[override](#override)   
[extends](#extends)

flash_proxy| namespace|   
---|---|---  
  
Defines methods of the Proxy class. The Proxy class methods are in their own namespace to avoid name conflicts in situations where your Proxy subclass contains instance method names that match any of the Proxy class method names.

See also

[Proxy class](flash/utils/Proxy.html)

for| statement|   
---|---|---  
  
Usage | 
    
    
    for ([init]; [condition]; [next]) { 
    	// statement(s)
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates the `init` (initialize) expression once and then starts a looping sequence. The looping sequence begins by evaluating the `condition` expression. If the `condition` expression evaluates to `true`, `statement` is executed and `next` is evaluated. The looping sequence then begins again with the evaluation of the `condition` expression. 

The curly braces (`{}`) that enclose the block of statements to be executed by the `for` statement are not necessary if only one statement will execute.

Parameters | `init` — An optional expression to evaluate before beginning the looping sequence; usually an assignment expression. A `var` statement is also permitted for this parameter.   
---|---  
| `condition` — An optional expression to evaluate before beginning the looping sequence; usually a comparison expression. If the expression evaluates to `true`, the statements associated with the `for` statement are executed.   
| `next` — An optional expression to evaluate after the looping sequence; usually an increment or decrement expression.   
  
Example   

See also

[++ (increment)](operators.html#increment)

for..in| statement|   
---|---|---  
  
Usage | 
    
    
    for (variableIterant:String in object){ 
    	// statement(s)
    }   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Iterates over the dynamic properties of an object or elements in an array and executes `statement` for each property or element. Object properties are not kept in any particular order, so properties may appear in a seemingly random order. Fixed properties, such as variables and methods defined in a class, are not enumerated by the `for..in` statement. To get a list of fixed properties, use the `describeType()` function, which is in the flash.utils package. 

Parameters | `variableIterant:[String](String.html)` — The name of a variable to act as the iterant, referencing each property of an object or element in an array.   
---|---  
  
Example   

See also

[describeType()](flash/utils/package.html#describeType\(\))

for each..in| statement|   
---|---|---  
  
Usage | 
    
    
    for each (variableIterant in object){ 
    	// statement(s)
    }   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Iterates over the items of a collection and executes `statement` for each item. Introduced as a part of the E4X language extensions, the `for each..in` statement can be used not only for XML objects, but also for objects and arrays. The `for each..in` statement iterates only through the dynamic properties of an object, not the fixed properties. A fixed property is a property that is defined as part of a class definition. To use the `for each..in` statement with an instance of a user-defined class, you must declare the class with the `dynamic` attribute. 

Unlike the `for..in` statement, the `for each..in` statement iterates over the values of an object's properties, rather than the property names.

Parameters | `variableIterant:[*](specialTypes.html#*)` — The name of a variable to act as the iterant, referencing the item in a collection.   
---|---  
| `object:[Object](Object.html)` — The name of a collection over which to iterate. The collection can be an XML object, a generic object, or an array.   
  
Example   

function| definition keyword|   
---|---|---  
  
Usage | 
    
    
    function functionName([parameter0, parameter1,...parameterN]) : returnType{ 
    	// statement(s) 
    } 
    var functionName:Function = function ([parameter0, parameter1,...parameterN]) : returnType{ 
    	// statement(s) 
    }   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Comprises a set of statements that you define to perform a certain task. You can define a function in one location and invoke, or _call_ , it from different scripts in a SWF file. When you define a function, you can also specify parameters for the function. Parameters are placeholders for values on which the function operates. You can pass different parameters to a function each time you call it so you can reuse the function in different situations. 

Use the `return` statement in a function's `statement(s)` block to cause a function to generate, or _return_ , a value.

Usage 1: You can use the `function` keyword to define a function with the specified function name, parameters, and statements. When a script calls a function, the statements in the function's definition are executed. Forward referencing is permitted; within the same script, a function may be declared after it is called. A function definition replaces any prior definition of the same function. You can use this syntax wherever a statement is permitted. 

Usage 2: You can also use `function` to create an anonymous function and return a reference to it. This syntax is used in expressions and is particularly useful for installing methods in objects.

For additional functionality, you can use the `arguments` object in your function definition. The `arguments` object is commonly used to create a function that accepts a variable number of parameters and to create a recursive anonymous function.

Parameters | `functionName:[Function](Function.html)` — The name of the new function.   
---|---  
| `returnType:[*](specialTypes.html#*)` — The data type of the return value.   
  
Example   

See also

[arguments object](arguments.html)   
[return](#return)

get| definition keyword|   
---|---|---  
  
Usage | 
    
    
    function get property() : returnType{ 
    	// your statements here 
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines a getter, which is a method that can be read like a property. A getter is a special function that returns the value of a property declared with the `var` or `const` keyword. Unlike other methods, a getter is called without parentheses (`()`), which makes the getter appear to be a variable. 

Getters allow you to apply the principle of information hiding by letting you create a public interface for a private property. The advantage of information hiding is that the public interface remains the same even if the underlying implementation of the private property changes.

Another advantage of getters is that they can be overridden in subclasses, whereas properties declared with `var` or `const` cannot.

A getter can be combined with a setter to create a read-write property. To create a read-only property, create a getter without a corresponding setter. To create a write-only property, create a setter without a corresponding getter.

**Note:** To use this keyword, you must specify ActionScript 2.0 and Flash Player 6 or later in the Flash tab of your FLA file's Publish Settings dialog box. This keyword is supported only when used in external script files, not in scripts written in the Actions panel.

Parameters | `property:[*](specialTypes.html#*)` — The identifier for the property that `get` accesses; this value must be the same as the value used in the corresponding `set` command.   
---|---  
| `returnType:[*](specialTypes.html#*)` — The data type of the return value.   
  
Example   

See also

[set](#set)

if| statement|   
---|---|---  
  
Usage | 
    
    
    if (condition) {
    	// statement(s)
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates a condition to determine the next statement to execute. If the condition is `true`, Flash Player runs the statements that follow the condition inside curly braces (`{}`). If the condition is `false`, Flash Player skips the statements inside the curly braces and runs the statements following the curly braces. Use the `if` statement along with the `else` statement to create branching logic in your scripts. 

The curly braces (`{}`) that enclose the statements to be executed by the `if` statement are not necessary if only one statement will execute.

Parameters | `condition:[Boolean](Boolean.html)` — An expression that evaluates to `true` or `false`.   
---|---  
  
See also

[else](#else)

implements| definition keyword|   
---|---|---  
  
Usage | 
    
    
    myClass implements interface01 [, interface02 , ...]   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a class implements one or more interfaces. When a class implements an interface, the class must define all the methods declared in the interface. Any instance of a class that implements an interface is considered a member of the data type defined by the interface. As a result, the `is` operator returns `true` when the class instance is the first operand and the interface is the second; in addition, type coercions to and from the data type defined by the interface work. 

**Note:** To use this keyword, you must specify ActionScript 2.0 and Flash Player 6 or later in the Flash tab of your FLA file's Publish Settings dialog box. This keyword is supported only when used in external script files, not in scripts written in the Actions panel.

See also

[class](#class)   
[interface](#interface)

import| directive|   
---|---|---  
  
Usage | 
    
    
    import packageName.className 
    import packageName.*  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Makes externally defined classes and packages available to your code. For example, if you want to use the flash.display.Sprite class in a script, you must import it. This requirement is different from previous versions of ActionScript, in which the `import` directive was optional. 

After using the `import` directive, you can use the full class name, which includes the package name, or just the name of the class.
    
    
     
    import flash.display.Sprite; 
    
    // name of class only
    var mySprite:Sprite = new Sprite();
    
    // full class name
    var mySprite:flash.display.Sprite = new flash.display.Sprite();
    

If there are several classes in the package that you want to access, you can import them all in a single statement, as shown in the following example:
    
    
    import flash.display.*;

The `import` directive imports only the classes, functions, and variables that reside at the top level of the imported package. Nested packages must be explicitly imported.

If you import a class but do not use it in your script, the class is not exported as part of the SWF file. This means you can import large packages without being concerned about the size of the SWF file; the bytecode associated with a class is included in a SWF file only if that class is actually used. One disadvantage of importing classes that you do not need is that you increase the likelihood of name collisions.

The `import` directive applies to the whole timeline in which it's called. For example, suppose on Frame 1 of a Flash document you import all the classes in the adobe.example package. On that frame, or any subsequent frames in the timeline, you can reference classes in that package by their simple names:
    
    
    // On Frame 1 of a FLA: 
    import adobe.example.*; 
    var myFoo:foo = new foo();

Parameters | `packageName:[*](specialTypes.html#*)` — The name of a package you have defined in a separate class file.   
---|---  
| `className:[Class](Class.html)` — The name of a class you have defined in a separate class file.   
  
include| directive|   
---|---|---  
  
Usage | 
    
    
    include "[path]filename.as"  
  
---|---  
  
Includes the contents of the specified file, as if the commands in the file are part of the calling script. The `include` directive is invoked at compile time. Therefore, if you make any changes to an included file, you must save the file and recompile any SWF files that use it. 

interface| definition keyword|   
---|---|---  
  
Usage | 
    
    
     interface InterfaceName [extends InterfaceName ] {}  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines an interface. Interfaces are data types that define a set of methods; the methods must be defined by any class that implements the interface. 

An interface is similar to a class, with the following important differences:

  * Interfaces contain only declarations of methods, not their implementation. That is, every class that implements an interface must provide an implementation for each method declared in the interface.
  * Interface method definitions cannot have any attribute such as `public` or `private`, but implemented methods must be marked as `public` in the definition of the class that implements the interface.
  * Multiple interfaces can be inherited by an interface by means of the `extends` statement, or by a class through the `implements` statement.

Unlike ActionScript 2.0, ActionScript 3.0 allows the use of getter and setter methods in interface definitions.

**Note:** To use this keyword, you must specify ActionScript 2.0 and Flash Player 6 or later in the Flash tab of your FLA file's Publish Settings dialog box. This keyword is supported only when used in external script files, not in scripts written in the Actions panel.

See also

[class](#class)   
[implements](#implements)

internal| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    [internal] var varName
    [internal] const kName
    [internal] function functionName()  { 
    	// your statements here 
    }
    [internal] class className{
    	// your statements here 
    }
    [internal] namespace nsName
      
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a class, variable, constant, or function is available to any caller within the same package. Classes, properties, and methods belong to the `internal` namespace by default.

Parameters | `className:[Class](Class.html)` — The name of the class that you want to specify as internal.   
---|---  
| `varName:[*](specialTypes.html#*)` — The name of the variable that you want to specify as internal. You can apply the `internal` attribute whether the variable is part of a class or not.   
| `kName:[*](specialTypes.html#*)` — The name of the constant that you want to specify as internal. You can apply the `internal` attribute whether the constant is part of a class or not.   
| `functionName:[Function](Function.html)` — The name of the function or method that you want to specify as internal. You can apply the `internal` attribute whether the function is part of a class or not.   
| `nsName:[Namespace](Namespace.html)` — The name of the namespace that you want to specify as internal. You can apply the `internal` attribute whether the namespace is part of a class or not.   
  
See also

[package](#package)   
[private](#private)   
[protected](#protected)   
[public](#public)

label| statement|   
---|---|---  
  
Usage | 
    
    
    label: statement
    label: {
        statements
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Associates a statement with an identifier that can be referenced by `break` or `continue`. In nested loops, a `break` or `continue` statement that does not reference a label can skip only the rest of the immediate loop and does not skip the entire series of loops. However, if the statement that defines the entire series of loops has an associated label, a `break` or `continue` statement can skip the entire series of loops by referring to that label. 

Labels also allow you to break out of a block statement. You cannot place a `break` statement that does not reference a label inside a block statement unless the block statement is part of a loop. If the block statement has an associated label, you can place a `break` statement that refers to that label inside the block statement.

Parameters | `label:[*](specialTypes.html#*)` — A valid identifier to associate with a statement.   
---|---  
| `statements:[*](specialTypes.html#*)` — Statement to associate with the label.   
  
Example   

See also

[break](#break)   
[continue](#continue)

namespace| definition keyword|   
---|---|---  
  
Usage | 
    
    
    namespace name [= uri]  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Allows you to control the visibility of definitions. Predefined namespaces include `public`, `private`, `protected`, and `internal`. 

The following steps show how to create, apply, and reference a namespace:

  * First, define the custom namespace using the `namespace` keyword. For example, the code `namespace version1` creates a namespace called `version1`.
  * Second, apply the namespace to a property or method by using your custom namespace in the property or method declaration. For example, the code `version1 myProperty:String` creates a property named `myProperty` that belongs to the `version1` namespace
  * Third, reference the namespace by using the `use` keyword or by prefixing an identifier with the namespace. For example, the code `use namespace version1;` references the `version1` namespace for subsequent lines of code, and the code `version1::myProperty` references the `version1` namespace for the `myProperty` property.

Parameters | `name:[Namespace](Namespace.html)` — The name of the namespace, which can be any legal identifier.   
---|---  
| `uri:[String](String.html)` — The Uniform Resource Identifier (URI) of the namespace. This is an optional parameter.   
  
See also

[class](#class)   
[internal](#internal)   
[package](#package)   
[private](#private)   
[protected](#protected)   
[public](#public)

native| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    native function functionName();
    class className { 
    	native function methodName();
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a function or method is implemented by Flash Player in native code. Flash Player uses the `native` keyword internally to declare functions and methods in the ActionScript application programming interface (API). This keyword cannot be used in your own code. 

null| primary expression keyword|   
---|---|---  
  
Usage | 
    
    
    null  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
A special value that can be assigned to variables or returned by a function if no data was provided. You can use `null` to represent values that are missing or that do not have a defined data type. 

The value `null` should not be confused with the special value `undefined`. When `null` and `undefined` are compared with the equality (`==`) operator, they compare as equal. However, when `null` and `undefined` are compared with the strict equality (`===`) operator, they compare as not equal.

  
Example   

See also

[undefined](package.html#undefined)

object_proxy| namespace|   
---|---|---  
  
Defines methods of the ObjectProxy class. The ObjectProxy class methods are in their own namespace to avoid name conflicts in situations where a Proxy subclass contains instance method names that match any of the Proxy class method names.

override| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    override function name() { 
    	// your statements here 
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a method replaces an inherited method. To override an inherited method, you must use the `override` attribute and ensure that the name, class property attribute, number and type of parameters, and the return type match exactly. It is an error to attempt to override a method without using the `override` attribute. Likewise, it is an error to use the `override` attribute if the method does not have a matching inherited method. 

You cannot use the `override` attribute on any of the following:

  * Variables
  * Constants
  * Static methods
  * Methods that are not inherited
  * Methods that implement an interface method
  * Inherited methods that are marked as `final` in the superclass

Although you cannot override a property declared with `var` or `const`, you can achieve similar functionality by making the base class property a getter-setter and overriding the methods defined with `get` and `set`.

Parameters | `name:[Function](Function.html)` — The name of the method to override.   
---|---  
  
See also

[final](#final)   
[get](#get)   
[set](#set)

package| definition keyword|   
---|---|---  
  
Usage | 
    
    
    package packageName {
        class someClassName { 
        } 
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Allows you to organize your code into discrete groups that can be imported by other scripts. You must use the `package` keyword to indicate that a class is a member of a package.

Parameters | `packageName:[*](specialTypes.html#*)` — The name of the package.   
---|---  
  
See also

[internal](#internal)   
[public](#public)   
[class](#class)

private| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    class className{ 
    	private var varName;
    	private const kName;
    	private function methodName() { 
    		// your statements here 
    	}
    	private namespace nsName;
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a variable, constant, or method is available only to the class that declares or defines it. Unlike in ActionScript 2.0, in ActionScript 3.0 `private` no longer provides access to subclasses. Moreover, `private` restricts access at both compile time and runtime. By default, a variable or function is available to any caller in the same package. Use this keyword if you want to restrict access to a variable or function. 

You can use this keyword only in class definitions, not in interface definitions. You cannot apply `private` to a class or to any other package-level definitions.

Parameters | `varName:[*](specialTypes.html#*)` — The name of the variable that you want to specify as private. You can apply the `private` attribute only if the variable is inside a class.   
---|---  
| `kName:[*](specialTypes.html#*)` — The name of the constant that you want to specify as private. You can apply the `private` attribute only if the constant is inside a class.   
| `methodName:[Function](Function.html)` — The name of the method that you want to specify as private. You can apply the `private` attribute only if the method is inside a class.   
| `nsName:[Namespace](Namespace.html)` — The name of the namespace that you want to specify as private. You can apply the `private` attribute only if the namespace is inside a class.   
  
Example   

See also

[internal](#internal)   
[protected](#protected)   
[public](#public)

protected| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    class className{ 
    	protected var varName;
    	protected const kName;
    	protected function methodName() { 
    		// your statements here 
    	}
    	protected namespace nsName;
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a variable, constant, method, or namespace is available only to the class that defines it and to any subclasses of that class. The definition of `protected` in ActionScript 3.0 is similar to the definition of the ActionScript 2.0 version of `private`, except that `protected` restricts access at both compile time and runtime. By default, a variable or function is available to any caller within the same package. Use this keyword if you want to restrict access to a variable or function. 

You can use this keyword only in class definitions, not in interface definitions. You cannot apply `private` to a class, or to any other package-level definitions.

The definition of `protected` in ActionScript 3.0 is more restrictive than that of `protected` in the Java programming language. In ActionScript 3.0 `protected` limits access strictly to subclasses, whereas in Java `protected` also allows access to any class in the same package. For example, if a class named `Base` contains a property marked as `protected`, in ActionScript 3.0 only classes that extend Base can access the protected property. In Java, any class in the same package as Base has access to the protected property even if the class is not a subclass of Base.

Parameters | `varName:[*](specialTypes.html#*)` — The name of the variable that you want to specify as protected. You can apply the `protected` attribute only if the variable is inside a class.   
---|---  
| `kName:[*](specialTypes.html#*)` — The name of the constant that you want to specify as protected. You can apply the `protected` attribute only if the constant is inside a class.   
| `methodName:[Function](Function.html)` — The name of the method that you want to specify as protected. You can apply the `protected` attribute only if the method is inside a class.   
| `nsName:[Namespace](Namespace.html)` — The name of the namespace that you want to specify as protected. You can apply the `protected` attribute only if the namespace is inside a class.   
  
Example   

See also

[internal](#internal)   
[private](#private)   
[public](#public)

public| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    public var varName
    public const kName
    public function functionName()  { 
    	// your statements here 
    }
    public class className {
    	// your statements here 
    }
    public namespace nsName
      
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a class, variable, constant, or method is available to any caller. Classes, variables, and methods are internal by default, which means that they are visible only within the current package. To make a class, variable, or method visible to all callers, you must use the `public` attribute.

Parameters | `className:[Class](Class.html)` — The name of the class that you want to specify as public.   
---|---  
| `varName:[*](specialTypes.html#*)` — The name of the variable that you want to specify as public. You can apply the `public` attribute whether the variable is part of a class or not.   
| `kName:[*](specialTypes.html#*)` — The name of the constant that you want to specify as public. You can apply the `public` attribute whether the constant is part of a class or not.   
| `functionName:[Function](Function.html)` — The name of the function or method that you want to specify as public. You can apply the `public` attribute whether the function is part of a class or not.   
| `nsName:[Namespace](Namespace.html)` — The name of the namespace that you want to specify as public. You can apply the `public` attribute whether the namespace is part of a class or not.   
  
Example   

See also

[class](#class)   
[internal](#internal)   
[private](#private)   
[protected](#protected)

return| statement|   
---|---|---  
  
Usage | 
    
    
    function functionName () {
    	return [expression]
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Causes execution to return immediately to the calling function. If the `return` statement is followed by an expression, the expression is evaluated and the result is returned. 

If a function definition includes a return type, the `return` statement must be followed by an expression. If no return type is specified and the `return` statement is used alone, it returns `undefined`.

You cannot return multiple values. If you try to do so, only the last value is returned. In the following example, `c` is returned:
    
    
    return a, b, c ;

If you need to return multiple values, use an array or object instead.

Parameters | `expression:[*](specialTypes.html#*)` — An expression to evaluate and return as a value of the function. This parameter is optional.   
---|---  
  
Result | `[*](specialTypes.html#*)` — The evaluated `expression` parameter, if provided.  
---|---  
  
Example   

See also

[function](#function)

set| definition keyword|   
---|---|---  
  
Usage | 
    
    
    function set property(newValue:*) : void{ 
    	// your statements here 
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Defines a setter, which is a method that appears in the public interface as a property. A setter is a special method that sets the value of a property declared with the `var` keyword. Unlike other methods, a setter is called without parentheses (`()`), which makes the setter appear to be a variable. 

Setters allow you to apply the principle of information hiding by letting you create a public interface for a private property. The advantage of information hiding is that the public interface remains the same even if the underlying implementation of the private property changes.

Another advantage of setters is that they can be overridden in subclasses, whereas properties declared with `var` cannot.

The return type of a setter must be either `void` or not specified.

A setter can be combined with a getter to create a read-write property. To create a read-only property, create a getter without a corresponding setter. To create a write-only property, create a setter without a corresponding getter.

**Note:** This keyword is supported only when used in external script files, not in scripts written in the Actions panel.

Parameters | `property:[*](specialTypes.html#*)` — The identifier for the property that `set` modifies; this value must be the same as the value used in the corresponding `get` command.   
---|---  
| `newValue:[*](specialTypes.html#*)` — The new value to assign.   
  
Example   

See also

[get](#get)

static| attribute keyword|   
---|---|---  
  
Usage | 
    
    
    class someClassName{ 
    	static var varName; 
    	static const kName;
    	static function methodName() { 
    		// your statements here
    	} 
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies that a variable, constant, or method belongs to the class, rather than to instances of the class. 

To access a static class member, use the name of the class instead of the name of an instance. For example, the Date class has a static method named `parse()`, which can only be called using the following syntax:
    
    
    Date.parse()

The `parse()` method cannot be called on an instance of the Date class. For example, the following code generates an error:
    
    
    var myDate:Date = new Date();
    			myDate.parse("Jan 01 00:00:00 2006"); // error

You can use `static` in class definitions only, not in interface definitions.

Static class members are not inherited. You cannot refer to a static class member using the name of a subclass, as you can in Java or C++. You can, however, refer to a static variable or method within a class or subclass, without using any qualifier. See the example below.

You cannot use the `super` statement or the `this` keyword inside a static method.

**Note:** This keyword is supported only when used in external script files, not in scripts written in the Actions panel.

Parameters | `varName:[*](specialTypes.html#*)` — The name of the variable that you want to specify as static.   
---|---  
| `kName:[*](specialTypes.html#*)` — The name of the constant that you want to specify as static.   
| `methodName:[Function](Function.html)` — The name of the method that you want to specify as static.   
  
Example   

super| statement|   
---|---|---  
  
Usage | 
    
    
    super([arg1, ..., argN])
    super.method([arg1, ..., argN])  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Invokes the superclass or parent version of a method or constructor. When used within the body of a class constructor, the `super()` statement invokes the superclass version of the constructor. The call to the superclass constructor must have the correct number of arguments. Note that the superclass constructor is always called, whether or not you call it explicitly. If you do not explicitly call it, a call with no arguments is automatically inserted before the first statement in the subclass constructor body. This means that if you define a constructor function in a subclass, and the superclass constructor takes one or more arguments, you must explicitly call the superclass constructor with the correct number of arguments or an error will occur. The call to the superclass constructor, however, does not need to be the first statement in your subclass constructor, as was required in ActionScript 2.0. 

When used in the body of an instance method, `super` can be used with the dot (.) operator to invoke the superclass version of a method and can optionally pass arguments `(arg1 ... argN)` to the superclass method. This is useful for creating subclass methods that not only add additional behavior to superclass methods, but also invoke the superclass methods to perform their original behavior.

You cannot use the `super` statement in a static method.

Parameters | `method:[Function](Function.html)` — The method to invoke in the superclass.   
---|---  
| `argN:[*](specialTypes.html#*)` — Optional parameters that are passed to the superclass version of the method or to the constructor function of the superclass.   
  
See also

[class](#class)   
[extends](#extends)

switch| statement|   
---|---|---  
  
Usage | 
    
    
    switch (expression) {
    	caseClause: 
    	[defaultClause:] 
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Causes control to transfer to one of several statements, depending on the value of an expression. All `switch` statements should include a default case that will execute if none of the `case` statements match the expression. Each `case` statement should end with a `break` statement, which prevents a fall-through error. When a case falls through, it executes the code in the next `case` statement, even though that case may not match the test expression.

Parameters | `expression:[*](specialTypes.html#*)` — Any expression.   
---|---  
  
Example   

See also

[=== (strict equality)](operators.html#strict_equality)   
[case](#case)   
[default](#default)

this| primary expression keyword|   
---|---|---  
  
Usage | 
    
    
    this  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
A reference to a method's containing object. When a script executes, the `this` keyword references the object that contains the script. Inside a method body, the `this` keyword references the class instance that contains the called method.

  
Example   

throw| statement|   
---|---|---  
  
Usage | 
    
    
    throw expression   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Generates, or _throws_ , an error that can be handled, or _caught_ , by a `catch` code block. If an exception is not caught by a `catch` block, the string representation of the thrown value is sent to the Output panel. If an exception is not caught by a `catch` or `finally` block, the string representation of the thrown value is sent to the log file.

Typically, you throw instances of the Error class or its subclasses (see the Example section).

Parameters | `expression:[*](specialTypes.html#*)` — An ActionScript expression or object.   
---|---  
  
Example   

See also

[Error class](Error.html)   
[try..catch..finally](#try..catch..finally)

true| primary expression keyword|   
---|---|---  
  
Usage | 
    
    
    true  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
A Boolean value representing true. A Boolean value is either `true` or `false`; the opposite of `true` is `false`. When automatic data typing converts `true` to a number, it becomes 1; when it converts `true` to a string, it becomes `"true"`. 

  
Example   

See also

[Boolean class](Boolean.html)   
[false](#false)

try..catch..finally| statement|   
---|---|---  
  
Usage | 
    
    
    try { 
        // try block 
    } finally { 
        // finally block  
    } 
    
    try { 
        // try block 
    } catch(error[:ErrorType1]) {
        // catch block 
    } [catch(error[:ErrorTypeN]) { 
        // catch block 
    }] [finally {
        // finally block 
    }]  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Encloses a block of code in which an error can occur, and then responds to the error. Exception handling, which is implemented using the `try..catch..finally` statements, is the primary mechanism for handling runtime error conditions in ActionScript 3.0. When a runtime error occurs, Flash Player throws an exception, which means that Flash Player suspends normal execution and creates a special object of type `Error`. Flash Player then passes, or _throws_ , the error object to the first available `catch` block. If no `catch` blocks are available, the exception is considered to be an uncaught exception. Uncaught exceptions cause the script to terminate. 

You can use the `throw` statement to explicitly throw exceptions in your code. You can throw any value, but the best practice is to throw an object because it provides flexibility and matches the behavior of Flash Player.

To catch an exception, whether it is thrown by Flash Player or by your own code, place the code that may throw the exception in a `try` block. If any code in the `try` block throws an exception, control passes to the `catch` block, if one exists, and then to the `finally` block, if one exists. The `finally` block always executes, regardless of whether an exception was thrown. If code within the `try` block does not throw an exception (that is, if the `try` block completes normally), the code in the `catch` block is ignored, but the code in the `finally` block is still executed. The `finally` block executes even if the `try` block exits using a `return` statement. 

A `try` block must be followed by a `catch` block, a `finally` block, or both. A single `try` block can have multiple `catch` blocks but only one `finally` block. You can nest `try` blocks as many levels deep as desired.

The `error` parameter specified in a `catch` handler must be a simple identifier such as `e` or `theException` or `x`. The parameter can also be typed. When used with multiple `catch` blocks, typed parameters let you catch multiple types of error objects thrown from a single `try` block.

If the exception thrown is an object, the type will match if the thrown object is a subclass of the specified type. If an error of a specific type is thrown, the `catch` block that handles the corresponding error is executed. If an exception that is not of the specified type is thrown, the `catch` block does not execute and the exception is automatically thrown out of the `try` block to a `catch` handler that matches it. 

If an error is thrown within a function, and the function does not include a `catch` handler, Flash Player exits that function, as well as any caller functions, until a `catch` block is found. During this process, `finally` handlers are called at all levels.

Note: If in a try block, there is an event dispatcher that calls its event handler, the catch block doesn't catch the error if thrown in event handler. Any error thrown thereafter can be caught by listening to `LoaderInfo.uncaughtErrorEvents`.

Parameters | `error:[*](specialTypes.html#*)` — The expression thrown from a `throw` statement, typically an instance of the Error class or one of its subclasses.   
---|---  
  
Example   

See also

[Error class](Error.html)   
[throw](#throw)

use namespace| directive|   
---|---|---  
  
Usage | 
    
    
    use namespace ns1[, ns2, ...nsN]  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Causes the specified namespaces to be added to the set of open namespaces. The specified namespaces are removed from the set of open namespaces when the current code block is exited. The `use namespace` directive can appear at the top level of a program, package definition, or class definition.

Parameters | `nsN:[Namespace](Namespace.html)` — One or more namespaces to add to the set of open namespaces.   
---|---  
  
See also

[default xml namespace](#default_xml_namespace)   
[namespace](#namespace)   
[XML class](XML.html)

var| definition keyword|   
---|---|---  
  
Usage | 
    
    
    var variableName [= value1][...,variableNameN[=valueN]]   
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Specifies a variable. If you declare variables inside a function, the variables are local. They are defined for the function and expire at the end of the function call. 

If you declare variables outside a function, the variables are available throughout the timeline containing the statement.

You cannot declare a variable that is in the scope of another object as a local variable.
    
    
    my_array.length = 25; // ok 
    var my_array.length = 25; // syntax error 

You can assign a data type to a variable by appending a colon character followed by the data type.

You can declare multiple variables in one statement, separating the declarations with commas (although this syntax may reduce clarity in your code):
    
    
    var first:String = "Bart", middle:String = "J.", last:String = "Bartleby";

Parameters | `variableName:[*](specialTypes.html#*)` — An identifier.   
---|---  
  
Example   

See also

[const](#const)

while| statement|   
---|---|---  
  
Usage | 
    
    
    while (condition) { 
    	// statement(s)
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Evaluates a condition and if the condition evaluates to `true`, executes one or more statements before looping back to evaluate the condition again. After the condition evaluates to `false`, the statements are skipped and the loop ends. 

The `while` statement performs the following series of steps. Each repetition of steps 1 through 4 is called an _iteration_ of the loop. The condition is tested at the beginning of each iteration, as shown in the following steps:

  1. The expression `condition` is evaluated.
  2. If `condition` evaluates to `true` or a value that converts to the Boolean value `true`, such as a nonzero number, go to step 3. Otherwise, the `while` statement is completed and execution resumes at the next statement after the `while` loop.
  3. Run the statement block `statement(s)`. If a `continue` statement is encountered, skip the remaining statements and go to step 1. If a `break` statement is encountered, the `while` statement is completed and execution resumes at the next statement after the `while` loop.
  4. Go to step 1.

Looping is commonly used to perform an action while a counter variable is less than a specified value. At the end of each loop, the counter is incremented until the specified value is reached. At that point, the `condition` is no longer `true`, and the loop ends.

The curly braces (`{}`) that enclose the statements to be executed by the `while` statement are not necessary if only one statement will execute.

Parameters | `condition:[Boolean](Boolean.html)` — An expression that evaluates to `true` or `false`.   
---|---  
  
Example   

See also

[break](#break)   
[continue](#continue)   
[do..while](#do..while)

with| statement|   
---|---|---  
  
Usage | 
    
    
    with (object:Object) { 
    	// statement(s)
    }  
  
---|---  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
Establishes a default object to be used for the execution of a statement or statements, potentially reducing the amount of code that needs to be written. 

The `object` parameter becomes the context in which the properties, variables, and functions in the `statement(s)` parameter are read. For example, if `object` is `my_array`, and two of the properties specified are `length` and `concat`, those properties are automatically read as `my_array.length` and `my_array.concat`. In another example, if `object` is `state.california`, any actions or statements inside the `with` statement are called from inside the `california` instance.

To find the value of an identifier in the `statement(s)` parameter, ActionScript starts at the beginning of the scope chain specified by `object` and searches for the identifier at each level of the scope chain, in a specific order. 

The scope chain used by the `with` statement to resolve identifiers starts with the first item in the following list and continues to the last item:

  * The object specified in the `object` parameter in the innermost `with` statement
  * The object specified in the `object` parameter in the outermost `with` statement
  * The Activation object (a temporary object that is automatically created when the script calls a function that holds the local variables called in the function)
  * The object that contains the currently executing script
  * The Global object (built-in objects such as Math and String)

To set a variable inside a `with` statement, you must have declared the variable outside the `with` statement, or you must enter the full path to the Timeline on which you want the variable to live. If you set a variable in a `with` statement without declaring it, the `with` statement will look for the value according to the scope chain. If the variable doesn't already exist, the new value will be set on the Timeline from which the `with` statement was called.

Parameters | `object:[Object](Object.html)` — An instance of an ActionScript object or movie clip.   
---|---  
  
Example   

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:12 PM GMT+01:00\) : Statements)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)