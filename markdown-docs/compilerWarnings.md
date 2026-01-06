# Compilerwarnings

Compiler warning messages identify code that is valid and compiles successfully, but may not be what the author intended. To enable detecting these possible problems, compile ActionScript projects in warning mode. 

Some of these warnings (for example, "Missing type declaration.") are coding style choices that you have the option whether to enforce. Others (for example, "Impossible assignment to null.") point out statements that are valid, but are unlikely to behave as the user expects. A third class of warnings covers issues you may encounter when porting ActionScript 2.0 code to ActionScript 3.0.

See also

[Compiler Errors](compilerErrors.html)   
[Run-Time Errors](runtimeErrors.html)

  
| Code| Message| Description  
---|---|---|---  
| **1009**|  _ '_' has no type declaration. |  Not declaring a data type is a coding style preference. A function return type, parameter, or variable has no type declaration. However, using type declarations enables the compiler to write more efficient code, as well as detect more errors at compile time. Enable this warning if you want to be reminded when you fail to use a type declaration.   
| **1013**|  Variables of type _ cannot be undefined. The value undefined will be type coerced to _ before comparison. |  Only variables of type * can be undefined. With a few exceptions, uninitialized variables have a default value of `null` rather than `undefined`. The exceptions include: Boolean variables, which have a default value of `false`. Number variables, which have a default value of `NaN`, and int or uint variables, which have a default value of `0`.   
| **1031**|  Migration issue: Result of new _ will be the return value of _, rather than a new instance of that function. |  This is a code migration warning. The detected code behaves differently in ActionScript 3.0 than in ActionScript 2.0, as shown in the following example: 
    
    
    function f(){
       this.b = 22;
       this.a = new Array(2);Â  
       this.a[0] = 33;
       this.a[1] = 44;
       return a; 
       } 
       // returns a new instance of f in ActionScript 2.0 and a new 2 element array in ActionScript 3.0
       var d = new f();Â  // Warning here
       trace(d.a);       // undefined in ActionScript 3.0, [33,44] in ActionScript 2.0.
      
  
| **1035**|  Use of Boolean() with no arguments. |  This is a code migration warning. The `Boolean()` function returns `false` in ActionScript 3.0, but `undefined` in ActionScript 2.0.   
| **1039**|  Migration issue: When the Number('') function is called with an empty string argument it returns 0 in ActionScript 3.0, and NaN in ActionScript 2.0. |  This is a code migration warning. The `Number()` method called with a String argument skips over all white space in the string and return a default value of 0 if no digits are detected. In ActionScript 2.0, any white space in the string causes the result to be NaN.   
| **1045**|  Migration issue: Array.toString() handling of null and undefined elements has changed. |  This is a code migration warning. In ActionScript 2.0, `null` array elements convert to `null` and `undefined` elements convert to `undefined`. In ActionScript 3.0, both `null` and `undefined` elements convert to the empty string ''. If you have code that parses the `toString()` output from an Array, you may need to adjust your code for this difference.   
| **1059**|  Migration issue: The property _ is no longer supported. _. |  This is a code migration warning. The property you are attempting to use does not exist in ActionScript 3.0.   
| **1061**|  Migration issue: The method _ is no longer supported. _. |  This is a code migration warning. The method you are attempting to use does not exist in ActionScript 3.0.   
| **1066**|  __resolve is no longer supported.|   
| **1067**|  Migration issue: __resolve is no longer supported. Use the new Proxy class for similar functionality. |  This is a code migration warning. See Proxy in this language reference for more information on the replacement for `__resolve`.   
| **1071**|  Migration issue: _level is no longer supported. For more information, see the flash.display package. |  This is a code migration warning. The property you are attempting to use does not exist in ActionScript 3.0.   
| **1073**|  Migration issue: _ is not a dynamic class. Instances cannot have members added to them dynamically. |  This is a code migration warning. In ActionScript 2.0, many classes such as Number are dynamic, which means that new properties can be added to instances of those classes at run time. This warning results from code that tries to add a property to an instance of a non-dynamic class.   
| **1083**|  Migration issue: Method _ will behave differently in ActionScript 3.0 due to the change in scoping for the this keyword. See the entry for warning 1083 for additional information. |  This is a code migration warning. This warning is generated when a method of an object is used as a value, usually as a callback function. In ActionScript 2.0, functions are executed in the context they are called from. In ActionScript 3.0, functions are always executed in the context where they were defined. Thus, variable and method names are resolved to the class that the callback is part of, rather than relative to the context it is called from, as in the following example: 
    
    
    class a 
    { 
       var x; 
       function a() { x = 1; } 
       function b() { trace(x); } 
    }
    
    var A:a = new a();
    var f:Function = a.b; // warning triggered here
    var x = 22;
    f(); // prints 1 in ActionScript 3.0, 22 in ActionScript 2.0  
  
| **1085**|  _ will be scoped to the default namespace: _ internal. It will not be visible outside of this package. |  Not declaring a namespace is a coding style preference. Enable this warning if you want to be reminded when you forget to declare a namespace or access specifier for a definition. Without one, the definition is not visible to code located outside of this file. To make it visible to code outside this file, declare it with the access specifier `public` or with a namespace declaration. To keep the definition local to this file and avoid this warning, declare the definition as `private`.   
| **1087**|  Migration issue: ActionScript 3.0 iterates over an object's properties within a "for x in target" statement in random order. |  This is a code migration warning. In ActionScript 2.0, the order in which the properties of an object were processed was always the same. In ActionScript 3.0, the order is random and can change from machine to machine. If unexpected ordering behavior occurs, inspect this loop to determine if this change in behavior may affect your code.   
| **1089**|  Error code: _. |  This is due to either a corrupt source file or a bug in the compiler code. Please contact Adobe, Inc. to file a bug.   
| **1091**|  Migration issue: _ |  This is a code migration warning. In ActionScript 2.0 declaring a method by a special name (such as `onMouseDown`) would cause Flash to call that method when a certain event occurred. In ActionScript 3.0, you must call `addEventListener()` with a method in order to register it to receive that event. See `addEventListener` in this language reference for details.   
| **1093**|  Negative value used where a uint (non-negative) value is expected. |  Assigning a negative value to a uint data type results in an extremely large positive value. `var x:uint = -1; trace(x); // 4294967295`.   
| **1097**|  Illogical comparison with null. Variables of type _ cannot be null. |  Instances of Boolean, int, uint, and Number cannot be `null`. The comparison operator type converts `null` to `false` before comparing it to a Boolean, or to 0 before comparing it with a Number, int, or uint data type.   
| **1099**|  Illogical comparison with NaN. This statement always evaluates to false. |  `NaN` has the unique mathematical property that any comparison involving it evaluates to `false`. Use the global `isNaN()` function to detect a NaN value instead, as in the following example: 
    
    
    trace(NaN == NaN); // false!
    trace(NaN != NaN); // false again!
    trace(isNaN(NaN)); // true
      
  
| **1101**|  Assignment within conditional. Did you mean == instead of =? |  The result of an = assignment statement is the value of the right-hand side of the = statement. You can use an assignment statement as a conditional test, but it is not recommended. It usually is the result of a typo where a == equality test was intended, as the following example shows: 
    
    
    var x:Boolean = false;
    var y:Boolean = true;
    // it is hard to determine if the line below intentionally sets x's value to y's or if its a typo
    if (x = y) { trace("x is assigned y's value of true, making the conditional test evaluate as true."); }
      
  
| **1103**|  null used where a _ value was expected. |  Boolean, Number, int, and uint variables cannot be assigned `null` as a value. The `null` value is implicitly cast to `false` when assigned to a Boolean, and to `0` when assigned to an int, uint, or Number.   
| **1105**|  No constructor function was specified for class _. |  Not specifying a constructor function is a coding style preference. Enable this warning if you want to always declare constructors for classes. This warning is intended to help find cases where a class name is changed but its constructor's name is not. Conditions such as this are not flagged as a problem without this warning, the former constructor appears to be a normal function.   
| **1107**|  Empty statement found where block of code expected. Did you type ';' accidentally? |  It is common to accidentally type ; before block of code. 
    
    
     if (x == y);
    {
    	trace("This code will be executed no matter what are the x and y values.")
    }
      
  
| **1111**|  The constant was not initialized.|   
| **1113**|  Array(x) behaves the same as new Array(x). To cast a value to type Array use the expression x as Array instead of Array(x).|   
| **1115**|  The super() statement will be executed prior to entering this constructor. Add a call to super() within the constructor if you want to explicitly control when it is executed. |  Adding a call to `super()` within the constructor is a coding style preference. Enable this warning if you want to always be explicit about when `super()` is called. This can help catch cases where you meant to call `super()` after some local initialization code and forgot to add it.   
| **3552**|  Appending text to a TextField using += is many times slower than using the TextField.appendText() method. |  See this language reference for the `appendText()` method of the TextField class for details on this significant text optimization.   
| **3554**|  Function value used where type _ was expected. Possibly the parentheses () are missing after this function reference. |  You can use functions themselves as values in ActionScript. The code in question is using a value of type Function where a type other than Function, Object, or * is expected. Usually, this indicates a typo where the parentheses `()` were omitted after the function name.   
| **3556**|  The instanceof operator is deprecated, use the is operator instead.|   
| **3574**|  Migration issue: The ActionScript 2.0 XML class has been renamed XMLDocument. |  This is a code migration warning. XML is a different class in ActionScript 3.0 than it was in ActionScript 2.0. In ActionScript 3.0, the XMLDocument class is the equivalent of the XML class in ActionScript 2.0. The ActionScript 3.0 XML class offers improved functionality with an easier and more powerful API. See XML in the ActionScript Language Reference for additional details.   
| **3576**|  Date(x) behaves the same as new Date().toString(). To cast a value to type Date use "x as Date" instead of Date(x).|   
| **3582**|  Importing a package by the same name as the current class will hide that class identifier in this scope.|   
| **3584**|  More than one argument named '_' specified. References to that argument will always resolve to the last one.|   
| **3590**|  Non-Boolean value used where a Boolean value was expected.|   
| **3591**|  _ used where a Boolean value was expected. The expression will be type coerced to Boolean.|   
| **3593**|  _ is not a recognized property of the dynamic class _. |  The strict compilation mode does not check for undefined properties on instances of dynamic classes. The types Date, RegExp, and Error are dynamic for backwards compatibility with ECMAScript. This warning finds usages of undefined properties on instances of those classes. A common problem is attempting to get or set a non-existent `year` property on a Date value. The correct property name is `fullYear`.   
| **3595**|  _ is not a recognized method of the dynamic class _. |  The strict compilation mode does not check for undefined methods on instances of dynamic classes. The types Date, RegExp, and Error are dynamic for backwards compatibility with ECMAScript. This warning finds usages of undefined methods on instances of those classes.   
| **3597**|  Duplicate variable definition. |  The compiler has detected a duplicate definition for a variable. This can lead to unexpected results. ActionScript does not support block level scoping of variables. All variables defined within a function body exist within the same scope, even if they are defined within an `if` statement, `while` statement, `for` statement, and so on: for example, the following code redeclares the variable x twice: 
    
    
    function test() {
    	var x:Number = 10;
    	if (true) {
    	    for (var x=0; x < 5; x++)  // warning here, this is the second defintion of x
    	    trace(x);
    	}
    	trace(x); // 5, not 10.  The last value set by the for loop above is the current value of x
    }  
  
| **3598**|  Definition name is the same as an imported package name. Unqualified references to that name will resolve to the package and not the definition.|   
| **3599**|  Definition name is the same as an imported package name. Unqualified references to that name will resolve to the package and not the definition. |  If a definition is named the same as a package that is in scope, then any unqualified references to that name will resolve to the package instead of the definition. This can result in unexpected errors when attempting to reference the variable. Any references to the definition need to be qualified to resolve to the definition and not the package.   
| **3600**|  Possible attempt to delete a fixed property.|   
| **3601**|  The declared property _ cannot be deleted. To free associated memory, set its value to null. | Delete removes dynamically defined properties from an object. Declared properties of a class can not be deleted, the operation merely fails silently. To free memory associated with this variable, set its value to null instead.  
| **3602**|  Use of deprecated definition.|   
| **3603**|  '_' has been deprecated. | This definition is deprecated and may be removed in the future.  
| **3604**|  Use of deprecated definition.|   
| **3605**|  _ |   
| **3606**|  Use of deprecated definition.|   
| **3607**|  '_' has been deprecated. Please use '_'. |   
| **3608**|  Use of deprecated definition.|   
| **3609**|  '_' has been deprecated since _. Please use '_'. |   
| **3610**|  Use of deprecated definition.|   
| **3611**|  '_' has been deprecated since _. |   
  
  

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:13 PM GMT+01:00\) : Compiler Warnings)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:13 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)