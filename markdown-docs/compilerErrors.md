# Compilererrors

The following is a list of compilation errors that the compiler generates when it encounters invalid code. A subset of these errors is detected only when compiling code in strict mode. Strict mode adds three constraints not found in the standard language: 

  * Expressions have static types and type errors are verification errors.
  * Additional verification rules catch common programming errors.
  * Verification errors are reported ahead of time. These are the verification errors that occur only in strict mode:
    * Function call signature matching, which checks the number of parameters supplied and their types.
    * Duplicate definition conflicts.
    * Unbound references, which occur when accessing methods or properties that are not defined at compile time.
    * Dynamically adding properties on sealed objects.
    * Writing to constant variables.
    * Deleting fixed properties.
    * Comparison expressions that use incompatible types.
    * Unfound packages.

See also

[Compiler Warnings](compilerWarnings.html)   
[Run-Time Errors](runtimeErrors.html)

  
| Code| Message| Description  
---|---|---|---  
| **1000**|  Ambiguous reference to _. |  A reference might be to more than one item. For example, the following uses the namespaces `rss` and `xml`, each of which defines a different value for the `hello()` function. The `trace(hello())` statement returns this error because it cannot determine which namespace to use. 
    
    
    private namespace rss;
    private namespace xml;
        
    public function ErrorExamples() {
      	use namespace rss;
       	use namespace xml;
    	trace(hello());
    }
        
    rss function hello():String {
          	return "hola";
        }
        
        xml function hello():String {
            return "foo";
        }

Correct an ambiguous reference by making the reference specific. The following example uses the form _namespace_ ::_function_ to specify which namespace to use:
    
    
    public function ErrorExamples() {
        
        trace(rss::hello());
        trace(xml::hello());
    }  
  
| **1003**|  Access specifiers are not allowed with namespace attributes. | You can not use both an access specifier (such as private or public) and a namespace attribute on a definition.  
| **1004**|  Namespace was not found or is not a compile-time constant. |  The namespace is either unknown or is an expression that could have different values at run time. Check that you are spelling the namespace correctly and that its definition is imported correctly.  
| **1006**|  A super expression can be used only inside class instance methods.|   
| **1007**|  A super statement can be used only inside class instance constructors. |  You cannot use the `super` statement within static members. You can use the `super` statement only within class instances.   
| **1008**|  Attribute is invalid.|   
| **1010**|  The override attribute may be used only on class property definitions. |  You cannot use the `override` keyword within a function block.   
| **1011**|  The virtual attribute may be used only on class property definitions. |  You cannot use the `virtual` attribute when you declare a property that does not belong to a class (for example, when you declare a variable within a function block).   
| **1012**|  The static attribute may be used only on definitions inside a class.|   
| **1013**|  The private attribute may be used only on class property definitions.|   
| **1014**|  The intrinsic attribute is no longer supported. |  ActionScript 3.0 does not support the intrinsic keyword.   
| **1016**|  Base class is final. |  The superclass cannot be extended because it is marked as `final`.   
| **1017**|  The definition of base class _ was not found.|   
| **1018**|  Duplicate class definition: _.|   
| **1020**|  Method marked override must override another method.|   
| **1021**|  Duplicate function definition. |  You cannot declare more than one function with the same identifier name within the same scope.   
| **1022**|  Cannot override a final accessor.|   
| **1023**|  Incompatible override. |  A function marked override must exactly match the parameter and return type declaration of the function it is overriding. It must have the same number of parameters, each of the same type, and declare the same return type. If any of the parameters are optional, that must match as well. Both functions must use the same access specifier (public, private, and so on) or namespace attribute as well.  
| **1024**|  Overriding a function that is not marked for override. |  If a method in a class overrides a method in a base class, you must explicitly declare it by using the `override` attribute, as this example shows: 
    
    
    public override function foo():void{};  
  
| **1025**|  Cannot redefine a final method. |  The method cannot be extended because it is marked as `final` in the base class.   
| **1026**|  Constructor functions must be instance methods.|   
| **1027**|  Functions cannot be both static and override.|   
| **1028**|  Functions cannot be both static and virtual.|   
| **1029**|  Functions cannot be both final and virtual.|   
| **1030**|  Must specify name of variable arguments array. |  The ...(rest) parameter definition specifies that all values supplied after ...(rest) are collected into any array. You must specify a name for the array, as in the expression `function foo(x,...(rest))`.   
| **1033**|  Virtual variables are not supported.|   
| **1034**|  Variables cannot be native.|   
| **1035**|  Variables cannot be both final and virtual.|   
| **1037**|  Packages cannot be nested.|   
| **1038**|  Target of break statement was not found.|   
| **1039**|  Target of continue statement was not found.|   
| **1040**|  Duplicate label definition.|   
| **1041**|  Attributes are not callable.|   
| **1042**|  The this keyword can not be used in static methods. It can only be used in instance methods, function closures, and global code. |  You cannot use the `this` keyword within a static member, because `this` would have no context.   
| **1043**|  Undefined namespace.|   
| **1044**|  Interface method _ in namespace _ not implemented by class _.|   
| **1045**|  Interface _ was not found.|   
| **1046**|  Type was not found or was not a compile-time constant: _. |  The class used as a type declaration is either unknown or is an expression that could have different values at run time. Check that you are importing the correct class and that its package location has not changed. Also, check that the package that contains the code (not the imported class) is defined correctly (for example, make sure to use proper ActionScript 3.0 package syntax, and not ActionScript 2.0 syntax). The error can also occur if the class being referenced is not defined in a namespace that is in use or is not defined as public:
    
    
    public class Foo{}

If you are using Flex™ Builder™ 2 and the class is in a library, make sure to set the class path for the project.  
| **1047**|  Parameter initializer unknown or is not a compile-time constant. |  The value used as the default value for the parameter is either undefined or could have different values at run time. Check that the initializer is spelled correctly, and that the initializer value isn't an expression that could result in different possible values at run time.   
| **1048**|  Method cannot be used as a constructor. |  It is not possible to create an instance of a method of a class. Only global functions can be used in `new` expressions. 
    
    
    class D { function xx() { return 22; } }
    var d:D = new D();
    var x = new d.xx(); // error, method cannot be used as constructor
    function yy() { this.a = 22; }
    var z = new yy(); // no error, global functions can be used as constructors.  
  
| **1049**|  Illegal assignment to a variable specified as constant.|   
| **1050**|  Cannot assign to a non-reference value.|   
| **1051**|  Return value must be undefined. |  You are attempting to use the `return` statement within a method that has a declared return type `void`.   
| **1052**|  Constant initializer unknown or is not a compile-time constant. |  The value used to initialize the constant is either undefined or could have different values at run time. Check that the initializer is spelled correctly, and that the initializer value isn't an expression that could result in different possible values at run time.   
| **1053**|  Accessor types must match.|   
| **1054**|  Return type of a setter definition must be unspecified or void. |  You cannot specify a return value for a setter function. For example, the following is invalid: 
    
    
    public function set gamma(g:Number):Number;

The following _is_ valid:
    
    
    public function set gamma(g:Number):void;  
  
| **1058**|  Property is write-only.|   
| **1059**|  Property is read-only. |  This property is defined through a getter function, which allows you to retrieve that property's value. There is no setter function defined for this property, however, so it is read-only. In the following example, line 3 generates an error because there is no setter function defined for `xx`:
    
    
    class D { function get xx() { return 22; } }
    var d:D = new D();
    d.xx = 44; // error, property is read-only  
  
| **1061**|  Call to a possibly undefined method _ through a reference with static type _. |  You are calling a method that is not defined.   
| **1063**|  Unable to open file: _.|   
| **1064**|  Invalid metadata. |  This metadata is unrecognized.   
| **1065**|  Metadata attributes cannot have more than one element.|   
| **1067**|  Implicit coercion of a value of type _ to an unrelated type _. |  You are attempting to cast an object to a type to which it cannot be converted. This can happen if the class you are casting to is not in the inheritance chain of the object being cast. This error appears only when the compiler is running in strict mode.   
| **1068**|  Unable to open included file: _.|   
| **1069**|  Syntax error: definition or directive expected. |  Check the syntax in the line.   
| **1071**|  Syntax error: expected a definition keyword (such as function) after attribute _, not _. |  This error will occur if the author forgets to use the "var" or "function" keyword in a declaration. 
    
    
    public int z;// should be 'public var z:int;'

This error might also occur when the compiler encounters an unexpected character. For example, the following use of the `trace()` function is invalid, because of the missing parentheses (the correct syntax is `trace("hello")`): 
    
    
    trace "hello"
      
  
| **1072**|  Syntax error: expecting xml before namespace. |  The correct statement syntax is `default xml namespace = ` _ns_. Either the keyword `xml` (note the lowercase) is missing or an incorrect keyword was used. For more information, see the [default xml namespace](statements.html#default_xml_namespace) directive.   
| **1073**|  Syntax error: expecting a catch or a finally clause.|   
| **1075**|  Syntax error: the 'each' keyword is not allowed without an 'in' operator.|   
| **1076**|  Syntax error: expecting left parenthesis before the identifier.|   
| **1077**|  Expecting CaseLabel. |  The compiler expected a `case` statement at this point in the switch block. The following switch block incorrectly includes a call to `print` before the first `case` statement: 
    
    
    switch(x)
    {
    trace(2);
    case 0:  trace(0); 
    break
    }  
  
| **1078**|  Label must be a simple identifier.|   
| **1079**|  A super expression must have one operand.|   
| **1080**|  Expecting increment or decrement operator.|   
| **1082**|  Expecting a single expression within parentheses.|   
| **1083**|  Syntax error: _ is unexpected. |  The line of code is missing some information. In the following example, some expression (such as another number) needs to be included after the final plus sign: 
    
    
    var sum:int = 1 + 2 + ;  
  
| **1084**|  Syntax error: expecting _ before _. |  The expression was unexpected at this point. If the error says "Expecting right brace before end of program," a block of code is missing a closing brace (}). If the error says "Expecting left parenthesis before _," you may have omitted a parenthesis from a conditional expression, as shown in the following example, which is intentionally incorrect: 
    
    
    var fact:int = 1 * 2 * 3;
    if fact > 2 {
    	var bigger:Boolean = true;
    }  
  
| **1086**|  Syntax error: expecting semicolon before _.|   
| **1087**|  Syntax error: extra characters found after end of program.|   
| **1093**|  Syntax error.|   
| **1094**|  Syntax error: A string literal must be terminated before the line break.|   
| **1095**|  Syntax error: A string literal must be terminated before the line break.|   
| **1097**|  Syntax error: input ended before reaching the closing quotation mark for a string literal.|   
| **1099**|  Syntax error.|   
| **1100**|  Syntax error: XML does not have matching begin and end tags.|   
| **1102**|  Cannot delete super descendants.|   
| **1103**|  Duplicate namespace definition. |  You defined the namespace more than once. Delete or modify the duplicate definition.   
| **1105**|  Target of assignment must be a reference value. |  You can assign a value to a variable, but you cannot assign a value to another value.   
| **1106**|  Operand of increment must be a reference. |  The operand must be a variable, an element in an array, or a property of an object.   
| **1107**|  Increment operand is invalid. |  The operand must be a variable, an element in an array, or a property of an object.   
| **1108**|  Decrement operand is invalid. |  The operand must be a variable, an element in an array, or a property of an object.   
| **1109**|  Expecting an expression. |  An expression is missing in a part of the code. For example, the following produces this error (there is a condition missing from the `if` statement: 
    
    
    var x = (5 > 2) ? 
    trace(x)  
  
| **1110**|  Missing XML tag name.|   
| **1112**|  Possible infinite recursion due to this file include: _. |  A file that is included in the source being compiled contains other `include` statements that would cause an infinite loop. For example, the following files. a.as and b.as, generate this error because each file tries to include the other.  File a.as contains the following, which attempts to include the file b.as:
    
    
    import foo.bar.baz;
    include "b.as"
    trace(2);

File b.as contains the following, which attempts to include the file a.as:
    
    
    include "a.as"  
  
| **1113**|  Circular type reference was detected in _. |  A class is trying to extend a superclass. For example, class A cannot extend class B if B inherits from A: 
    
    
    class a extends b { }
    class b extends a { }  
  
| **1114**|  The public attribute can only be used inside a package.|   
| **1115**|  The internal attribute can only be used inside a package.|   
| **1116**|  A user-defined namespace attribute can only be used at the top level of a class definition.|   
| **1118**|  Implicit coercion of a value with static type _ to a possibly unrelated type _. | You are using a value that is not of the expected type and no implicit coercion exists to convert it to the expected type. Perhaps you are using a supertype where a subtype is expected. For example:
    
    
    class A {}
    var a:A = new A(); 
    class B extends A { function f() }
    var b : B = a // error

The last statement generates an error because it attempts to assign an object of type A to a variable of type B. Similarly, the following defines the `foo()` function, which takes a parameter of type B. The statement ` foo(a);` generates an error because it attempts to use a parameter of type A:
    
    
    function foo(x:B) { }
    foo(a);

Also, the following statement generates an error because the returned value for `foo2()` must be type B:
    
    
    function foo2():B { return new A(); }  
  
| **1119**|  Access of possibly undefined property _ through a reference with static type _. |  You are attempting to access a property that does not exist for the specified object. For example, the following code generates this error because an int object does not have a property named `assortment`: 
    
    
    var i:int = 44;
    var str:String = i.assortment;

This error appears only when the compiler is running in strict mode.   
| **1120**|  Access of undefined property _. |  You are attempting to access an undefined variable. For example, if the variable `huh` has not been defined, a call to it generates this error: 
    
    
    huh = 55;

This error can appear only when the compiler is running in strict mode.   
| **1121**|  A getter definition must have no parameters.|   
| **1122**|  A setter definition must have exactly one parameter.|   
| **1123**|  A setter definition cannot have optional parameters.|   
| **1124**|  Return type of a getter definition must not be void. |  A getter function simulates a variable. Because variables cannot be of type void, you cannot declare getter functions to return type void.   
| **1125**|  Methods defined in an interface must not have a body.|   
| **1126**|  Function does not have a body.|   
| **1127**|  Attribute _ was specified multiple times. |  You specified an attribute more than once in the same statement. For example, the statement `public static public var x;` generates this error because it specifies that the variable `x` is public twice. Delete duplicate declarations.   
| **1129**|  Duplicate interface definition: _. |  Change or delete the duplicate definitions.   
| **1130**|  A constructor cannot specify a return type.|   
| **1131**|  Classes must not be nested.|   
| **1132**|  The attribute final can only be used on a method defined in a class.|   
| **1133**|  The native attribute can only be used with function definitions.|   
| **1134**|  The dynamic attribute can only be used with class definitions.|   
| **1135**|  Syntax error: _ is not a valid type.|   
| **1136**|  Incorrect number of arguments. Expected _. |  The function expects a different number of arguments than those you provided. For example, the following defines function `goo`, which has two arguments: 
    
    
    class A { static function goo(x:int,y:int) 
    { return(x+y); } }

The following statement would generate an error because it provides three arguments:
    
    
    A.goo(1,2,3);  
  
| **1137**|  Incorrect number of arguments. Expected no more than _.|   
| **1138**|  Required parameters are not permitted after optional parameters.|   
| **1139**|  Variable declarations are not permitted in interfaces.|   
| **1140**|  Parameters specified after the ...rest parameter definition keyword can only be an Array data type.|   
| **1141**|  A class can only extend another class, not an interface.|   
| **1142**|  An interface can only extend other interfaces, but _ is a class. |  You are attempting to have the interface extend a class. An interface can only extend another interface.   
| **1143**|  The override attribute can only be used on a method defined in a class.|   
| **1144**|  Interface method _ in namespace _ is implemented with an incompatible signature in class _. |  Method signatures must match exactly.   
| **1145**|  Native methods cannot have a body. |  You cannot use `native` because it is a reserved keyword.   
| **1146**|  A constructor cannot be a getter or setter method.|   
| **1147**|  An AS source file was not specified.|   
| **1149**|  The return statement cannot be used in static initialization code.|   
| **1150**|  The protected attribute can only be used on class property definitions.|   
| **1151**|  A conflict exists with definition _ in namespace _. |  You cannot declare more than one variable with the same identifier name within the same scope unless all such variables are declared to be of the same type. In ActionScript 3.0, different code blocks (such as those used in two `for` loops in the same function definition) are considered to be in the same scope. The following code example correctly casts the variable `x` as the same type:
    
    
    function test()
    {
    	var x:int = 3;
    	for(var x:int = 33; x < 55; x++)
    	trace(x);
    	for(var x:int = 11; x < 33; x++)
    	trace(x)
    }

The following code example generates an error because the type casting in the variable declaration and the `for` loops are different:
    
    
    function test()
    {
    	var x:String = "The answer is";
    	for(var x:int = 33; x < 55; x++) // error
    	trace(x);
    	for(var x:unit = 11; x < 33; x++) // error
    	trace(x)
    }  
  
| **1152**|  A conflict exists with inherited definition _ in namespace _.|   
| **1153**|  A constructor can only be declared public.|   
| **1154**|  Only one of public, private, protected, or internal can be specified on a definition.|   
| **1155**|  Accessors cannot be nested inside other functions.|   
| **1156**|  Interfaces cannot be instantiated with the new operator.|   
| **1157**|  Interface members cannot be declared public, private, protected, or internal.|   
| **1158**|  Syntax error: missing left brace ({) before the function body.|   
| **1159**|  The return statement cannot be used in package initialization code.|   
| **1160**|  The native attribute cannot be used in interface definitions. |  You cannot use `native` because it is a reserved keyword.   
| **1162**|  Only one namespace attribute can be used per definition.|   
| **1163**|  Method _ conflicts with definition inherited from interface _.|   
| **1165**|  Interface attribute _ is invalid.|   
| **1166**|  Namespace declarations are not permitted in interfaces.|   
| **1167**|  Class _ implements interface _ multiple times. |  The class implements the same interface more than once. For example, the following generates this error because class C implements interface A twice: 
    
    
    interface A {  public function f();  };
    class C implements A,A {
    public function f() { trace("f"); }
    }

The correct implementing statement should be ` class C implements A {`.  
| **1168**|  Illegal assignment to function _. |  You are attempting to redefine a function. For example, the following defines the function `topLevel()` to print the word "top". The second statement generates an error because it assigns a different return value to the function: 
    
    
    function topLevel() { trace("top"); }
    topLevel = function() { trace("replacement works in ~");} // error  
  
| **1169**|  Namespace attributes are not permitted on interface methods.|   
| **1170**|  Function does not return a value. |  Every possible control flow in a function must return a value whenever the return type is something other than void. The following function `f(x)` does not generate an error because the `if..else` statement always returns a value: 
    
    
    function f(x):int
    {
    if (x)
        	return 2;
    else
        	return 3;
    } // no error

However, the function `g(x)` below generates the error because the `switch` statement does not always return a value.
    
    
    function g(x:int):int
    {
    switch(x)
    {
          	case 1: return 1;
          	case 2: return 2:
    }
    // return 2;//uncomment to remove the error
    }

This checking is enabled only when the function declares a return type other than void.   
| **1171**|  A namespace initializer must be either a literal string or another namespace.|   
| **1172**|  Definition _ could not be found.|   
| **1173**|  Label definition is invalid.|   
| **1176**|  Comparison between a value with static type _ and a possibly unrelated type _. | This error is enabled in strict mode.  
| **1177**|  The return statement cannot be used in global initialization code.|   
| **1178**|  Attempted access of inaccessible property _ through a reference with static type _.|   
| **1180**|  Call to a possibly undefined method _. | This error appears only when the compiler is running in strict mode.  
| **1181**|  Forward reference to base class _.|   
| **1182**|  Package cannot be used as a value: _.|   
| **1184**|  Incompatible default value of type _ where _ is expected.|   
| **1185**|  The switch has more than one default, but only one default is allowed.|   
| **1188**|  Illegal assignment to class _.|   
| **1189**|  Attempt to delete the fixed property _. Only dynamically defined properties can be deleted. | Delete removes dynamically defined properties from an object. Declared properties of a class can not be deleted. This error appears only when the compiler is running in strict mode.  
| **1190**|  Base class was not found or is not a compile-time constant.|   
| **1191**|  Interface was not found or is not a compile-time constant.|   
| **1192**|  The static attribute is not allowed on namespace definitions.|   
| **1193**|  Interface definitions must not be nested within class or other interface definitions.|   
| **1194**|  The prototype attribute is invalid.|   
| **1195**|  Attempted access of inaccessible method _ through a reference with static type _. | You are either calling a private method from another class, or calling a method defined in a namespace that is not in use. If you are calling a method defined in an unused namespace, add a `use` statement for the required namespace.   
| **1196**|  Syntax error: expecting an expression after the throw.|   
| **1197**|  The class _ cannot extend _ since both are associated with library symbols or the main timeline.|   
| **1198**|  Attributes are not allowed on package definition.|   
| **1199**|  Internal error: _.|   
| **1200**|  Syntax error: invalid for-in initializer, only 1 expression expected.|   
| **1201**|  A super statement cannot occur after a this, super, return, or throw statement.|   
| **1202**|  Access of undefined property _ in package _. |  You are attempting to access an undefined variable in a package. For example, if the variable `p.huh` has not been defined, a call to it generates this error: 
    
    
    p.huh = 55;

This error can only appear when the compiler is running in strict mode.   
| **1203**|  No default constructor found in base class _. | You must explicitly call the constructor of the base class with a super() statement if it has 1 or more required arguments.  
| **1204**|  /* found without matching */ . |  The characters '/*' where found, which indicate the beginning of a comment, but the corresponding characters, '*/', which indicate the end of the comment block, were not found.   
| **1205**|  Syntax Error: expecting a left brace({)or string literal("").|   
| **1206**|  A super statement can be used only as the last item in a constructor initializer list. |  You cannot use the `super` statement within a constructor. You can use the `super` statement only as the last item in the constructor initializer list.   
| **1207**|  The this keyword can not be used in property initializers. |  You cannot use the `this` keyword within a property initializer.   
| **1208**|  The initializer for a configuration value must be a compile time constant. |  The initializer of a configuration value must be a value known at compile time. The initializer may be a constant string, number, or boolean, or a reference to another previously defined configuration value.   
| **1209**|  A configuration variable may only be declared const. |  When defining a configuration variable, it must be declared as const.   
| **1210**|  A configuration value must be declared at the top level of a program or package. |  A configuration value must be declared at the top level of a program or package.   
| **1211**|  Namespace _ conflicts with a configuration namespace. |  A namespace may not have the same name as a configuration namespace.   
| **1212**|  Precision must be an integer between 1 and 34.|   
| **1214**|  Incompatible Version: can not reference definition _ introduced in version _ from code with version _.|   
| **1215**|  Invalid initialization: conversion to type _ loses data.|   
  
  

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Mon Jun 30 2025, 11:01 AM GMT+01:00\) : Compiler Errors)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Mon Jun 30 2025, 11:01 AM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)