# Runtimeerrors

The following errors can occur at run time. Run-time type checking occurs in ActionScript 3.0 whether you compile in strict mode or warning mode.

See also

[Compiler Errors](compilerErrors.html)   
[Compiler Warnings](compilerWarnings.html)

  
| Code| Message| Description  
---|---|---|---  
| **1000**|  The system is out of memory. |  Flash Player needs more memory to compile your code than your system has available. Close some of the applications or processes running on your system.   
| **1001**|  The method _ is not implemented.|   
| **1002**|  Number.toPrecision has a range of 1 to 21. Number.toFixed and Number.toExponential have a range of 0 to 20. Specified value is not within expected range. |  You specified a value that is not within the expected range of the `precision` argument. Number.toPrecision has a range of 1 to 21. Number.toFixed and Number.toExponential have a range of 0 to 20.   
| **1003**|  The radix argument must be between 2 and 36; got _. |  You passed a value less than 2 or greater than 36 for the `radix` argument of a method or property. Pass a value between 2 and 36 as a `radix` argument.   
| **1004**|  Method _ was invoked on an incompatible object. |  You tried to call a method that is not available to the specified object. This error occurs when you have copied a prototype function from one object to another, and then invoked it, but the target object is not the same type as the original object. Ensure that the target object and original object are the same type. See the ECMAScript Language Specification, 3rd Edition, Chapter 15 for more details.   
| **1005**|  Array index is not a positive integer (_). |  You tried to access a member of an array using an index value that is not a positive integer. Pass only positive integers as index values for arrays.   
| **1006**|  _ is not a function. |  This error occurs when you attempt to call a function that does not exist. Make sure you are calling the correct function, and that the API has not changed from ActionScript 2.0. Also, make sure you are using the correct object. For example, you will see this error when you use the following code (because the last line mistakenly calls the variable `big` instead of `blg`): 
    
    
    var blg:String = "foo";
    var big:Sprite = new Sprite();
    var error:int = big.length();   
  
| **1007**|  Instantiation attempted on a non-constructor.|   
| **1008**|  _ is ambiguous; Found more than one matching binding.|   
| **1009**|  Cannot access a property or method of a null object reference. |  An object that evaluates to `null` can have no properties. This error can occur in some unexpected (though valid) situations. For example, consider the following code, which creates a Sprite object. Because this Sprite object is never added to the display list (through the `addChild()` method of a DisplayObjectContainer object), its `stage` property is set to `null`. Thus, the example generates this error because Sprite object's `stage` property cannot have any properties: 
    
    
    import flash.display.Sprite;
    var sprite1:Sprite = new Sprite();
    var q:String = sprite1.stage.quality;  
  
| **1010**|  A term is undefined and has no properties. |  This error can occur if you try to access a property of an object that does not exist. For example: 
    
    
    var obj:Object = new Object();
    obj.a = "foo";
    trace(obj.b.prop);

You can also see this error because of a misspelling, for example in the following, where `mc` represents a MovieClip object in the display list, and the `stage` property is misspelled with a capital S (it should be `stage`):
    
    
    trace(mc.Stage.quality);  
  
| **1011**|  Method _ contained illegal opcode _ at offset _. |  See the [note](#note) at the bottom of this table.*   
| **1012**|  The last instruction exceeded code size. |  See the [note](#note) at the bottom of this table.*   
| **1013**|  Cannot call OP_findproperty when scopeDepth is 0. |  See the [note](#note) at the bottom of this table.*   
| **1014**|  Class _ could not be found.|   
| **1015**|  Method _ cannot set default xml namespace |  See the [note](#note) at the bottom of this table.*   
| **1016**|  Descendants operator (..) not supported on type _.|   
| **1017**|  Scope stack overflow occurred. |  See the [note](#note) at the bottom of this table.*   
| **1018**|  Scope stack underflow occurred. |  See the [note](#note) at the bottom of this table.*   
| **1019**|  Getscopeobject _ is out of bounds. |  See the [note](#note) at the bottom of this table.*   
| **1020**|  Code cannot fall off the end of a method. |  See the [note](#note) at the bottom of this table.*   
| **1021**|  At least one branch target was not on a valid instruction in the method. |  See the [note](#note) at the bottom of this table.*   
| **1022**|  Type void may only be used as a function return type. |  See the [note](#note) at the bottom of this table.*   
| **1023**|  Stack overflow occurred. |  See the [note](#note) at the bottom of this table.*   
| **1024**|  Stack underflow occurred. |  See the [note](#note) at the bottom of this table.*   
| **1025**|  An invalid register _ was accessed. |  See the [note](#note) at the bottom of this table.*   
| **1026**|  Slot _ exceeds slotCount=_ of _. |  See the [note](#note) at the bottom of this table.*   
| **1027**|  Method_info _ exceeds method_count=_. |  See the [note](#note) at the bottom of this table.*   
| **1028**|  Disp_id _ exceeds max_disp_id=_ of _. |  See the [note](#note) at the bottom of this table.*   
| **1029**|  Disp_id _ is undefined on _. |  See the [note](#note) at the bottom of this table.*   
| **1030**|  Stack depth is unbalanced. _ != _. |  See the [note](#note) at the bottom of this table.*   
| **1031**|  Scope depth is unbalanced. _ != _. |  See the [note](#note) at the bottom of this table.*   
| **1032**|  Cpool index _ is out of range _. |  See the [note](#note) at the bottom of this table.*   
| **1033**|  Cpool entry _ is wrong type. |  See the [note](#note) at the bottom of this table.*   
| **1034**|  Type Coercion failed: cannot convert _ to _.|   
| **1035**|  Illegal super expression found in method _. |  See the [note](#note) at the bottom of this table.*   
| **1037**|  Cannot assign to a method _ on _. |  See the [note](#note) at the bottom of this table.*   
| **1038**|  _ is already defined. |  You cannot declare a variable or function with the same identifier name more than once within the same scope. In ActionScript 3.0, different code blocks (such as those used in two `for` loops in the same `function` definition) are considered to be in the same scope. See the [note](#note) at the bottom of this table.*   
| **1039**|  Cannot verify method until it is referenced. |  See the [note](#note) at the bottom of this table.*   
| **1040**|  The right-hand side of instanceof must be a class or function. |  The expression on the right side of the `instanceof` operator must be a class or function.   
| **1041**|  The right-hand side of operator must be a class. |  The expression on the right side of the `is` operator must be a class.   
| **1042**|  Not an ABC file. major_version=_ minor_version=_. |  You are attempting to use an invalid file with the player: the tool that generates the SWF may be out of date or the SWF itself may be corrupt.   
| **1043**|  Invalid code_length=_. |  See the [note](#note) at the bottom of this table.*   
| **1044**|  MethodInfo-_ unsupported flags=_. |  See the [note](#note) at the bottom of this table.*   
| **1045**|  Unsupported traits kind=_. |  See the [note](#note) at the bottom of this table.*   
| **1046**|  MethodInfo-_ referenced before definition. |  See the [note](#note) at the bottom of this table.*   
| **1047**|  No entry point was found. |  See the [note](#note) at the bottom of this table.*   
| **1049**|  Prototype objects must be vanilla Objects. |  See the [note](#note) at the bottom of this table.*   
| **1050**|  Cannot convert _ to primitive. |  See the [note](#note) at the bottom of this table.*   
| **1051**|  Illegal early binding access to _. |  See the [note](#note) at the bottom of this table.*   
| **1052**|  Invalid URI passed to _ function. |  See the [note](#note) at the bottom of this table.*   
| **1053**|  Illegal override of _ in _. |  See the [note](#note) at the bottom of this table.*   
| **1054**|  Illegal range or target offsets in exception handler. |  See the [note](#note) at the bottom of this table.*   
| **1056**|  Cannot create property _ on _. |  You are trying to assign a value to a nonexistent property on an instance of a non-dynamic class. This is only possible for instances of dynamic classes  
| **1057**|  _ can only contain methods. |  See the [note](#note) at the bottom of this table.*   
| **1058**|  Illegal operand type: _ must be _. |  See the [note](#note) at the bottom of this table.*   
| **1059**|  ClassInfo-_ is referenced before definition. |  See the [note](#note) at the bottom of this table.*   
| **1060**|  ClassInfo _ exceeds class_count=_. |  See the [note](#note) at the bottom of this table.*   
| **1061**|  The value _ cannot be converted to _ without losing precision. |  This error appears if you attempt to assign a decimal number to a property that has data type int. This error also appears for out-of-range assignments, such as the following:
    
    
    var m0:int = 2147483648; // int.MAX_VALUE == 2147483647

You can also see this error when using the bitwise left shift operator (<<). For example, consider the following code:
    
    
    var m0:uint = 0xFF;
    var m1:uint = m0<&lt24

The result of left shift operator (<<) is interpreted as a 32-bit two's complement number with sign. In the example, the result is a negative value, which causes the error when assigned to the uint typed property. A workaround is the following:
    
    
    var m0:uint = 0xFF;
    var m1:uint = uint(m0<<24);  
  
| **1063**|  Argument count mismatch on _. Expected _, got _.|   
| **1064**|  Cannot call method _ as constructor. |  Extracted methods are permanently bound to the object they are extracted from. Therefore, they can not later be called as a constructor. For example, the following creates function `f()` in Class A: 
    
    
    class A {
           function f() {}
        }

In the following code, extracting the function causes no error. However, creating a new instance of the function causes an error. 
    
    
    var a = new A()
        var m = a.f // extract f, don't call it
        m() // same as a.f()
        new m() // causes this error  
  
| **1065**|  Variable _ is not defined. |  You are using an undefined lexical reference. For example, in the following statements, the statement `trace(x)` generates an error because `x` is undefined. However, the statement `trace(y)` doesn't generate an error because `y` is defined: 
    
    
    trace("hello world")
        trace(x) // x is undefined
        var y
        trace(y) // No error, y is defined.  
  
| **1066**|  The form function('function body') is not supported. |  Unlike JavaScript, Flash does not compile code on-the-fly using `eval()` and `function()`. Thus, calling these as a constructor in ActionScript 3.0 generates this error.   
| **1067**|  Native method _ has illegal method body. |  See the [note](#note) at the bottom of this table.*   
| **1068**|  _ and _ cannot be reconciled. |  See the [note](#note) at the bottom of this table.*   
| **1069**|  Property _ not found on _ and there is no default value. |  You are referencing an undefined property on a non-dynamic class instance. For example, the following generates this error when it references property `x`, which is not defined and cannot be created dynamically: 
    
    
    class A {} // sealed class, not dynamic
        trace(new A().x) // no property x defined on A, and A is not dynamic  
  
| **1070**|  Method _ not found on _ |  You are using a `super` statement to call a function, but the function doesn't exist in the super class. For example, the following code generates the error: 
    
    
    class A() {}
    class B extends A {
      function f() { trace(super.f()); } // error 1070, there is no f on A
    }  
  
| **1071**|  Function _ has already been bound to _.|   
| **1072**|  Disp_id 0 is illegal. |  See the [note](#note) at the bottom of this table.*   
| **1073**|  Non-override method _ replaced because of duplicate disp_id _. |  See the [note](#note) at the bottom of this table.*   
| **1074**|  Illegal write to read-only property _ on _.|   
| **1075**|  Math is not a function. |  You are trying to call `math()` as a function, but the Math class is a class with static methods.   
| **1076**|  Math is not a constructor. |  You can not instantiate the Math class.   
| **1077**|  Illegal read of write-only property _ on _.|   
| **1078**|  Illegal opcode/multiname combination: _<_>. |  See the [note](#note) at the bottom of this table.*   
| **1079**|  Native methods are not allowed in loaded code. |  See the [note](#note) at the bottom of this table.*   
| **1080**|  Illegal value for namespace. |  See the [note](#note) at the bottom of this table.*   
| **1081**|  Property _ not found on _ and there is no default value.|   
| **1082**|  No default namespace has been set. |  See the [note](#note) at the bottom of this table.*   
| **1083**|  The prefix "_" for element "_" is not bound. |  An attribute name or element name has a prefix but no matching namespace was found. This statement generates an error because there is no `foo` namespace to match `foo:x`:

<foo:x xmlns:clowns='http://circuscenter.org'>  
| **1084**|  Element or attribute ("_") does not match QName production: QName::=(NCName':')?NCName. |  You have `foo: ` or `:foo` as an element or attribute name, but there is nothing on the other side of the colon.   
| **1085**|  The element type "_" must be terminated by the matching end-tag "</_>".|   
| **1086**|  The _ method only works on lists containing one item. |  The XMLList class propagates the XML-specific functions to one child if it has only one item in its list. If more than one item is in the list, the routines fail with this error. This happens for the following XMLList functions that mimic XML functions: `addNamespace`, `appendChild`, `childIndex`, `inScopeNamespaces`, `insertChildAfter`, `insertChildBefore`, `name`, `namespace`, `localName`, `namespaceDeclarations`, `nodeKind`, `prependChild`, `removeNamespace`, `replace`, `setChildren`, `setLocalName`, `setName`, and `setNamespace. `  
| **1087**|  Assignment to indexed XML is not allowed.|   
| **1088**|  The markup in the document following the root element must be well-formed. |  These are possible causes of this error: 

  * Parsing an XMLList style object as XML
  * Misbalanced strings

  
| **1089**|  Assignment to lists with more than one item is not supported.|   
| **1090**|  XML parser failure: element is malformed. |  An element name is malformed. This example of an element name is malformed because a trailing right angle bracket `>` is missing: 
    
    
    <a/><b></b  
  
| **1091**|  XML parser failure: Unterminated CDATA section.|   
| **1092**|  XML parser failure: Unterminated XML declaration.|   
| **1093**|  XML parser failure: Unterminated DOCTYPE declaration.|   
| **1094**|  XML parser failure: Unterminated comment.|   
| **1095**|  XML parser failure: Unterminated attribute.|   
| **1096**|  XML parser failure: Unterminated element.|   
| **1097**|  XML parser failure: Unterminated processing instruction.|   
| **1098**|  Illegal prefix _ for no namespace. |  The namespace constructor throws this error if you try to pass in an empty URI with a non-empty prefix as in this example: 
    
    
    ns = new Namespace ("prefix", "");
          
  
| **1100**|  Cannot supply flags when constructing one RegExp from another. |  Creating a new regular expression from an existing one also copies its flags. To create a regular expression with different flags, use the `new` operator and set the flags as desired. For example, this statement creates a regular expression and specifies flag settings: 
    
    
    var re:RegExp = new RegExp("ali", /s)

Alternatively, this statement creates a regular expression that has the same flags as re: 
    
    
    var re2:RegExp = new RegExp(re, ...)  
  
| **1101**|  Cannot verify method _ with unknown scope. |  See the [note](#note) at the bottom of this table.*   
| **1102**|  Illegal default value for type _. |  See the [note](#note) at the bottom of this table.*   
| **1103**|  Class _ cannot extend final base class. |  See the [note](#note) at the bottom of this table.*   
| **1104**|  Attribute "_" was already specified for element "_".|   
| **1107**|  The ABC data is corrupt, attempt to read out of bounds. |  See the [note](#note) at the bottom of this table.*   
| **1108**|  The OP_newclass opcode was used with the incorrect base class. |  See the [note](#note) at the bottom of this table.*   
| **1109**|  Attempt to directly call unbound function _ from method _. |  See the [note](#note) at the bottom of this table.*   
| **1110**|  _ cannot extend _. |  See the [note](#note) at the bottom of this table.*   
| **1111**|  _ cannot implement _. |  See the [note](#note) at the bottom of this table.*   
| **1112**|  Argument count mismatch on class coercion. Expected 1, got _.|   
| **1113**|  OP_newactivation used in method without NEED_ACTIVATION flag. |  See the [note](#note) at the bottom of this table.*   
| **1114**|  OP_getglobalslot or OP_setglobalslot used with no global scope. |  See the [note](#note) at the bottom of this table.*   
| **1115**|  _ is not a constructor.|   
| **1116**|  second argument to Function.prototype.apply must be an array.|   
| **1117**|  Invalid XML name: _.|   
| **1118**|  Illegal cyclical loop between nodes.|   
| **1119**|  Delete operator is not supported with operand of type _.|   
| **1120**|  Cannot delete property _ on _.|   
| **1121**|  Method _ has a duplicate method body.|   
| **1122**|  Interface method _ has illegal method body.|   
| **1123**|  Filter operator not supported on type _.|   
| **1124**|  OP_hasnext2 requires object and index to be distinct registers.|   
| **1125**|  The index _ is out of range _.|   
| **1126**|  Cannot change the length of a fixed Vector.|   
| **1127**|  Type application attempted on a non-parameterized type.|   
| **1128**|  Incorrect number of type parameters for _. Expected _, got _.|   
| **1129**|  Cyclic structure cannot be converted to JSON string.|   
| **1131**|  Replacer argument to JSON stringifier must be an array or a two parameter function.|   
| **1132**|  Invalid JSON parse input.|   
| **1502**|  A script has executed for longer than the default timeout period of 15 seconds. |  A script executed after the timeout period. (The default timeout period is 15 seconds.) After this error occurs, the script can continue to execute for 15 seconds more, after which the script terminates and throws run-time error number 1503 (A script failed to exit after 30 seconds and was terminated.)   
| **1503**|  A script failed to exit after 30 seconds and was terminated. |  The script was still executing after 30 seconds. Flash Player first throws run-time error number 1502 (A script has executed for longer than the default timeout period of 15 seconds.) if the script executed more than 15 seconds, which is the default timeout period. This error occurs 15 seconds after Error 1502 occurs.   
| **1507**|  Argument _ cannot be null.|   
| **1508**|  The value specified for argument _ is invalid. |  You are possibly trying to pass the wrong data type. For example, the code 
    
    
    public function doSomething(const:int):void {
        }
        this ["doSomething"] ("str")

generates an error at runtime because `doSomething` is cast as an int data type.   
| **1510**|  When the callback argument is a method of a class, the optional this argument must be null.|   
| **1511**|  Worker is already started.|   
| **1512**|  Starting a worker that already failed is not supported.|   
| **1513**|  Worker has terminated."|   
| **1514**|  unlock() with no preceding matching lock().|   
| **1515**|  Invalid condition timeout value: _.|   
| **1516**|  Condition cannot notify if associated mutex is not owned.|   
| **1517**|  Condition cannot notifyAll if associated mutex is not owned.|   
| **1518**|  Condition cannot wait if associated mutex is not owned.|   
| **1519**|  Condition cannot be initialized.|   
| **1520**|  Mutex cannot be initialized.|   
| **1521**|  Only the worker's parent may call start.|   
| **2004**|  One of the parameters is invalid.|   
| **2006**|  The supplied index is out of bounds.|   
| **2007**|  Parameter _ must be non-null.|   
| **2008**|  Parameter _ must be one of the accepted values.|   
| **2012**|  _ class cannot be instantiated.|   
| **2030**|  End of file was encountered.|   
| **2058**|  There was an error decompressing the data.|   
| **2085**|  Parameter _ must be non-empty string.|   
| **2088**|  The Proxy class does not implement getProperty. It must be overridden by a subclass.|   
| **2089**|  The Proxy class does not implement setProperty. It must be overridden by a subclass.|   
| **2090**|  The Proxy class does not implement callProperty. It must be overridden by a subclass.|   
| **2091**|  The Proxy class does not implement hasProperty. It must be overridden by a subclass.|   
| **2092**|  The Proxy class does not implement deleteProperty. It must be overridden by a subclass.|   
| **2093**|  The Proxy class does not implement getDescendants. It must be overridden by a subclass.|   
| **2105**|  The Proxy class does not implement nextNameIndex. It must be overridden by a subclass.|   
| **2106**|  The Proxy class does not implement nextName. It must be overridden by a subclass.|   
| **2107**|  The Proxy class does not implement nextValue. It must be overridden by a subclass.|   
| **2108**|  The value _ is not a valid Array length.|   
| **2173**|  Unable to read object in stream. The class _ does not implement flash.utils.IExternalizable but is aliased to an externalizable class.|   
| **3735**|  This API cannot accept shared ByteArrays.|   
| **3806**|  ByteArray.shareable is no longer supported. Learn more at https://www.adobe.com/go/fp-spectre|   
| **3807**|  Worker.start has been disabled by the user. Learn more at https://www.adobe.com/go/fp-spectre|   
| **2000**|  No active security context.|   
| **2001**|  Too few arguments were specified; got _, _ expected.|   
| **2002**|  Operation attempted on invalid socket.|   
| **2003**|  Invalid socket port number specified. |  The valid range is 0 to 65535. For more information, see Socket Connections in this language reference.   
| **2005**|  Parameter _ is of the incorrect type. Should be type _.|   
| **2007**|  Parameter _ must be non-null. |  Possible symbol clash in multiple SWFs; abcenv must be non-null.   
| **2009**|  This method cannot be used on a text field with a style sheet.|   
| **2010**|  Local-with-filesystem SWF files are not permitted to use sockets.|   
| **2011**|  Socket connection failed to _:_. |  There is a network problem. Possibly a DNS name is not resolving or a TCP socket is not connecting.   
| **2013**|  Feature can only be used in Flash Authoring.|   
| **2014**|  Feature is not available at this time. |  The feature is not supported on this system.   
| **2015**|  Invalid BitmapData.|   
| **2017**|  Only trusted local files may cause the Flash Player to exit.|   
| **2018**|  System.exit is only available in the standalone Flash Player.|   
| **2019**|  Depth specified is invalid.|   
| **2020**|  MovieClips objects with different parents cannot be swapped.|   
| **2021**|  Object creation failed.|   
| **2022**|  Class _ must inherit from DisplayObject to link to a symbol.|   
| **2023**|  Class _ must inherit from Sprite to link to the root.|   
| **2024**|  An object cannot be added as a child of itself.|   
| **2025**|  The supplied DisplayObject must be a child of the caller.|   
| **2026**|  An error occurred navigating to the URL _. |  Possibly the URL does not exist, the network connection has a problem, or the URL is outside the security sandbox.   
| **2027**|  Parameter _ must be a non-negative number; got _.|   
| **2028**|  Local-with-filesystem SWF file _ cannot access Internet URL _.|   
| **2029**|  This URLStream object does not have a stream opened.|   
| **2031**|  Socket Error. |  A socket error occurred. For more information, see Socket Connections in this language reference.   
| **2032**|  Stream Error.|   
| **2033**|  Key Generation Failed.|   
| **2034**|  An invalid digest was supplied.|   
| **2035**|  URL Not Found.|   
| **2036**|  Load Never Completed.|   
| **2037**|  Functions called in incorrect sequence, or earlier call was unsuccessful.|   
| **2038**|  File I/O Error.|   
| **2039**|  Invalid remote URL protocol. The remote URL protocol must be HTTP or HTTPS.|   
| **2041**|  Only one file browsing session may be performed at a time.|   
| **2042**|  The digest property is not supported by this load operation.|   
| **2044**|  Unhandled _:.|   
| **2046**|  The loaded file did not have a valid signature.|   
| **2047**|  Security sandbox violation: _: _ cannot access _.|   
| **2048**|  Security sandbox violation: _ cannot load data from _.|   
| **2049**|  Security sandbox violation: _ cannot upload data to _.|   
| **2051**|  Security sandbox violation: _ cannot evaluate scripting URLs within _ (allowScriptAccess is _). Attempted URL was _.|   
| **2052**|  Only String arguments are permitted for allowDomain and allowInsecureDomain.|   
| **2053**|  Security sandbox violation: _ cannot clear an interval timer set by _.|   
| **2054**|  The value of Security.exactSettings cannot be changed after it has been used.|   
| **2055**|  The print job could not be started.|   
| **2056**|  The print job could not be sent to the printer.|   
| **2057**|  The page could not be added to the print job. |  The `addPage()` method is not used correctly. See the addPage() entry in this language reference.   
| **2059**|  Security sandbox violation: _ cannot overwrite an ExternalInterface callback added by _.|   
| **2060**|  Security sandbox violation: ExternalInterface caller _ cannot access _.|   
| **2061**|  No ExternalInterface callback _ registered.|   
| **2062**|  Children of Event must override clone() {return new MyEventClass (...);}.|   
| **2063**|  Error attempting to execute IME command. |  One of the IME services has failed. 

  * If you are using the `setConversionMode()` or `setEnabled()` method, ActionScript 3.0 replaces these methods with the `access` property.
  * If you are using the `doConversion()` or `setComposition()` method, these methods are not supported for Macintosh OSX.

  
| **2065**|  The focus cannot be set for this target.|   
| **2066**|  The Timer delay specified is out of range.|   
| **2067**|  The ExternalInterface is not available in this container. ExternalInterface requires Internet Explorer ActiveX, Firefox, Mozilla 1.7.5 and greater, or other browsers that support NPRuntime.|   
| **2068**|  Invalid sound.|   
| **2069**|  The Loader class does not implement this method.|   
| **2070**|  Security sandbox violation: caller _ cannot access Stage owned by _.|   
| **2071**|  The Stage class does not implement this property or method.|   
| **2074**|  The stage is too small to fit the download ui.|   
| **2075**|  The downloaded file is invalid. |  Possibly the file decompression failed, the file format is invalid, or the signature validation failed.   
| **2077**|  This filter operation cannot be performed with the specified input parameters.|   
| **2078**|  The name property of a Timeline-placed object cannot be modified.|   
| **2079**|  Classes derived from Bitmap can only be associated with defineBits characters (bitmaps).|   
| **2082**|  Connect failed because the object is already connected.|   
| **2083**|  Close failed because the object is not connected.|   
| **2084**|  The AMF encoding of the arguments cannot exceed 40K.|   
| **2086**|  A setting in the mms.cfg file prohibits this FileReference request.|   
| **2087**|  The FileReference.download() file name contains prohibited characters. |  The filename cannot contain spaces or any of the following characters: /, \, :, *, ?, ", <, >, |, %, or the ASCII control characters 0 through 31 (0x00 through 0X1F). Also, filenames longer than 256 characters may fail on some browsers or servers.   
| **2094**|  Event dispatch recursion overflow. |  The recursion exceeds the maximum recursion depth. (The default maximum is 256.)   
| **2095**|  _ was unable to invoke callback _.|   
| **2096**|  The HTTP request header _ cannot be set via ActionScript. |  You are adding a disallowed HTTP header to an HTTP request. See the [flash.net.URLRequestHeader](flash/net/URLRequestHeader.html) class for a complete list of disallowed HTTP request headers.   
| **2097**|  The FileFilter Array is not in the correct format. |  There are two valid formats: 

  * A description with Windows file extensions only
  * A description with Windows file extensions and Macintosh file formats.

The two file formats and not interchangeable; you must use one or the other. For more information, see the FileFilter class in this language reference.  
| **2098**|  The loading object is not a .swf file, you cannot request SWF properties from it.|   
| **2099**|  The loading object is not sufficiently loaded to provide this information.|   
| **2100**|  The ByteArray parameter in Loader.loadBytes() must have length greater than 0.|   
| **2101**|  The String passed to URLVariables.decode() must be a URL-encoded query string containing name/value pairs.|   
| **2102**|  The before XMLNode parameter must be a child of the caller.|   
| **2103**|  XML recursion failure: new child would create infinite loop. |  Possibly you are trying to make objects child objects of each other. For example, the following code generates this error because a and b both try to add the other as a child object. 
    
    
    a.addChild(b);
    b.addChild(a);  
  
| **2108**|  Scene _ was not found.|   
| **2109**|  Frame label _ not found in scene _.|   
| **2110**|  The value of Security.disableAVM1Loading cannot be set unless the caller can access the stage and is in an ActionScript 3.0 SWF file.|   
| **2111**|  Security.disableAVM1Loading is true so the current load of the ActionScript 1.0/2.0 SWF file has been blocked.|   
| **2112**|  Provided parameter LoaderContext.ApplicationDomain is from a disallowed domain.|   
| **2113**|  Provided parameter LoaderContext.SecurityDomain is from a disallowed domain.|   
| **2114**|  Parameter _ must be null.|   
| **2115**|  Parameter _ must be false.|   
| **2116**|  Parameter _ must be true.|   
| **2118**|  The LoaderInfo class does not implement this method.|   
| **2119**|  Security sandbox violation: caller _ cannot access LoaderInfo.applicationDomain owned by _.|   
| **2121**|  Security sandbox violation: _: _ cannot access _. This may be worked around by calling Security.allowDomain.|   
| **2122**|  Security sandbox violation: _: _ cannot access _. A policy file is required, but the checkPolicyFile flag was not set when this media was loaded.|   
| **2123**|  Security sandbox violation: _: _ cannot access _. No policy files granted access.|   
| **2124**|  Loaded file is an unknown type.|   
| **2125**|  Security sandbox violation: _ cannot use Runtime Shared Library _ because crossing the boundary between ActionScript 3.0 and ActionScript 1.0/2.0 objects is not allowed.|   
| **2126**|  NetConnection object must be connected.|   
| **2127**|  FileReference POST data cannot be type ByteArray.|   
| **2128**|  Certificate error in secure connection.|   
| **2129**|  Connection to _ failed.|   
| **2130**|  Unable to flush SharedObject.|   
| **2131**|  Definition _ cannot be found.|   
| **2132**|  NetConnection.connect cannot be called from a netStatus event handler.|   
| **2133**|  Callback _ is not registered.|   
| **2134**|  Cannot create SharedObject.|   
| **2136**|  The SWF file _ contains invalid data.|   
| **2137**|  Security sandbox violation: _ cannot navigate window _ within _ (allowScriptAccess is _). Attempted URL was _.|   
| **2138**|  Rich text XML could not be parsed.|   
| **2139**|  SharedObject could not connect.|   
| **2140**|  Security sandbox violation: _ cannot load _. Local-with-filesystem and local-with-networking SWF files cannot load each other.|   
| **2141**|  Only one PrintJob may be in use at a time.|   
| **2142**|  Security sandbox violation: local SWF files cannot use the LoaderContext.securityDomain property. _ was attempting to load _.|   
| **2143**|  AccessibilityImplementation.get_accRole() must be overridden from its default.|   
| **2144**|  AccessibilityImplementation.get_accState() must be overridden from its default.|   
| **2145**|  Cumulative length of requestHeaders must be less than 8192 characters.|   
| **2146**|  Security sandbox violation: _ cannot call _ because the HTML/container parameter allowNetworking has the value _.|   
| **2147**|  Forbidden protocol in URL _.|   
| **2148**|  SWF file _ cannot access local resource _. Only local-with-filesystem and trusted local SWF files may access local resources.|   
| **2149**|  Security sandbox violation: _ cannot make fscommand calls to _ (allowScriptAccess is _).|   
| **2150**|  An object cannot be added as a child to one of it's children (or children's children, etc.).|   
| **2151**|  You cannot enter full screen mode when the settings dialog is visible.|   
| **2152**|  Full screen mode is not allowed.|   
| **2153**|  The URLRequest.requestHeaders array must contain only non-NULL URLRequestHeader objects.|   
| **2154**|  The NetStream Object is invalid. This may be due to a failed NetConnection.|   
| **2155**|  The ExternalInterface.call functionName parameter is invalid. Only alphanumeric characters are supported.|   
| **2156**|  Port _ may not be accessed using protocol _. Calling SWF was _.|   
| **2157**|  Rejecting URL _ because the 'asfunction:' protocol may only be used for link targets, not for networking APIs.|   
| **2158**|  The NetConnection Object is invalid. This may be due to a dropped NetConnection.|   
| **2159**|  The SharedObject Object is invalid.|   
| **2160**|  The TextLine is INVALID and cannot be used to access the current state of the TextBlock.|   
| **2161**|  An internal error occured while laying out the text.|   
| **2162**|  The Shader output type is not compatible for this operation.|   
| **2163**|  The Shader input type _ is not compatible for this operation.|   
| **2164**|  The Shader input _ is missing or an unsupported type.|   
| **2165**|  The Shader input _ does not have enough data.|   
| **2166**|  The Shader input _ lacks valid dimensions.|   
| **2167**|  The Shader does not have the required number of inputs for this operation.|   
| **2168**|  Static text lines have no atoms and no reference to a text block.|   
| **2169**|  The method _ may not be used for browser scripting. The URL _ requested by _ is being ignored. If you intend to call browser script, use navigateToURL instead.|   
| **2170**|  Security sandbox violation: _ cannot send HTTP headers to _.|   
| **2171**|  The Shader object contains no byte code to execute.|   
| **2172**|  The ShaderJob is already running or finished.|   
| **2174**|  Only one download, upload, load or save operation can be active at a time on each FileReference.|   
| **2175**|  One or more elements of the content of the TextBlock has a null ElementFormat.|   
| **2176**|  Certain actions, such as those that display a pop-up window, may only be invoked upon user interaction, for example by a mouse click or button press.|   
| **2177**|  The Shader input _ is too large.|   
| **2178**|  The Clipboard.generalClipboard object must be used instead of creating a new Clipboard.|   
| **2179**|  The Clipboard.generalClipboard object may only be read while processing a flash.events.Event.PASTE event.|   
| **2180**|  It is illegal to move AVM1 content (AS1 or AS2) to a different part of the displayList when it has been loaded into AVM2 (AS3) content.|   
| **2181**|  The TextLine class does not implement this property or method.|   
| **2182**|  Invalid fieldOfView value. The value must be greater than 0 and less than 180.|   
| **2183**|  Scale values must not be zero.|   
| **2184**|  The ElementFormat object is locked and cannot be modified.|   
| **2185**|  The FontDescription object is locked and cannot be modified.|   
| **2186**|  Invalid focalLength _.|   
| **2187**|  Invalid orientation style _. Value must be one of 'Orientation3D.EULER_ANGLES', 'Orientation3D.AXIS_ANGLE', or 'Orientation3D.QUATERNION'.|   
| **2188**|  Invalid raw matrix. Matrix must be invertible.|   
| **2189**|  A Matrix3D can not be assigned to more than one DisplayObject.|   
| **2190**|  The attempted load of _ failed as it had a Content-Disposition of attachment set.|   
| **2191**|  The Clipboard.generalClipboard object may only be written to as the result of user interaction, for example by a mouse click or button press.|   
| **2192**|  An unpaired Unicode surrogate was encountered in the input.|   
| **2193**|  Security sandbox violation: _: _ cannot access _. |   
| **2194**|  Parameter _ cannot be a Loader. |   
| **2195**|  Error thrown as Loader called _.|   
| **2196**|  Parameter _ must be an Object with only String values. |   
| **2200**|  The SystemUpdater class is not supported by this player.|   
| **2201**|  The requested update type is not supported on this operating system.|   
| **2202**|  Only one SystemUpdater action is allowed at a time.|   
| **2203**|  The requested SystemUpdater action cannot be completed.|   
| **2204**|  This operation cannot be canceled because it is waiting for user interaction.|   
| **2205**|  Invalid update type _.|   
| **2500**|  An error occurred decrypting the signed swf file. The swf will not be loaded.|   
| **2501**|  This property can only be accessed during screen sharing.|   
| **2502**|  This property can only be accessed if sharing the entire screen.|   
| **3000**|  Illegal path name.|   
| **3001**|  File or directory access denied.|   
| **3002**|  File or directory exists.|   
| **3003**|  File or directory does not exist.|   
| **3004**|  Insufficient file space.|   
| **3005**|  Insufficient system resources.|   
| **3006**|  Not a file.|   
| **3007**|  Not a directory.|   
| **3008**|  Read-only or write-protected media.|   
| **3009**|  Cannot move file or directory to a different device.|   
| **3010**|  Directory is not empty.|   
| **3011**|  Move or copy destination already exists.|   
| **3012**|  Cannot delete file or directory.|   
| **3013**|  File or directory is in use.|   
| **3014**|  Cannot copy or move a file or directory to overwrite a containing directory.|   
| **3015**|  Loader.loadBytes() is not permitted to load content with executable code.|   
| **3016**|  No application was found that can open this file.|   
| **3100**|  A SQLConnection cannot be closed while statements are still executing.|   
| **3101**|  Database connection is already open.|   
| **3102**|  Name argument specified was invalid. It must not be null or empty.|   
| **3103**|  Operation cannot be performed while there is an open transaction on this connection.|   
| **3104**|  A SQLConnection must be open to perform this operation.|   
| **3105**|  Operation is only allowed if a connection has an open transaction.|   
| **3106**|  Property cannot be changed while SQLStatement.executing is true.|   
| **3107**|  _ may not be called unless SQLResult.complete is false.|   
| **3108**|  Operation is not permitted when the SQLStatement.text property is not set.|   
| **3109**|  Operation is not permitted when the SQLStatement.sqlConnection property is not set.|   
| **3110**|  Operation cannot be performed while SQLStatement.executing is true.|   
| **3111**|  An invalid schema type was specified. |  Valid values are: 

  * SQLIndexSchema
  * SQLTableSchema
  * SQLTriggerSchema
  * SQLViewSchema

  
| **3112**|  An invalid transaction lock type was specified. |  Valid values are: 

  * SQLTransactionLockType.DEFERRED
  * SQLTransactionLockType.IMMEDIATE
  * SQLTransactionLockType.EXCLUSIVE

  
| **3113**|  Reference specified is not of type File.|   
| **3114**|  An invalid open mode was specified. |  Valid values are: 

  * SQLMode.READ
  * SQLMode.UPDATE
  * SQLMode.CREATE

  
| **3115**|  SQL Error.|   
| **3116**|  An internal logic error occurred.|   
| **3117**|  Access permission denied. |  Indicates that the operation failed because a SQL statement attempted to perform an operation that it didn't have permission to perform, such as specifying an `INSERT` operation to be performed on a view.   
| **3118**|  Operation aborted. |  Indicates that a SQL statement execution failed because execution was aborted. This error occurs when code in a trigger cancels the operation using the SQL `RAISE()` function, or if the `SQLConnection.cancel()` or `SQLStatement.cancel()` methods are called when a statement is executed using `SQLStatement.execute()` or `SQLStatement.next()` with a prefetch argument specified, and not all of the results have been returned.   
| **3119**|  Database file is currently locked.|   
| **3120**|  Table is locked. |  Indicates that an operation could not be completed because another AIR application was holding a lock on a table involved in the operation. This can occur when a statement executing through a SQLConnection attempts to write to a table when another SQLConnection (in the same application or a different application) has an open transaction and is writing to the table, or if a SQLConnection attempts to read from or write to a table while another SQLConnection has an exclusive-locked transaction.   
| **3121**|  Out of memory.|   
| **3122**|  Attempt to write a readonly database. |  Indicates that an operation could not be completed because the database is read only. This can occur if the database file is designated as read only in the operating system, if the database is opened in read-only mode, or if an older version of Adobe AIR accesses a database file created with a newer version of the runtime.   
| **3123**|  Database disk image is malformed. |  Indicates that the operation failed because the specified file is a database file whose data has become corrupted. This can happen when the application is force quit while in a transaction or any other time that a database file is left in the state of having an open transaction that can't be rolled back when reopening the file.   
| **3124**|  Insertion failed because database is full.|   
| **3125**|  Unable to open the database file. |  Indicates that the connection could not be completed because the database file could not be opened. This can happen if `SQLConnection.open()` or `SQLConnection.openAsync()`is called with the `openMode` parameter set to `SQLMode.UPDATE` and the database file doesn't exist. It can also happen if the operating system returns an error when the runtime attempts to access the database file.   
| **3126**|  Database lock protocol error.|   
| **3127**|  Database is empty.|   
| **3128**|  Disk I/O error occurred. |  Indicates that an operation could not be completed because of a disk I/O error. This can happen if the runtime is attempting to delete a temporary file and another program (such as a virus protection application) is holding a lock on the file. This can also happen if the runtime is attempting to write data to a file and the data can't be written.   
| **3129**|  The database schema changed. |  Indicates that the operation could not be completed because of a schema error. This occurs when the schema of the database changes after a statement is prepared but before it finishes executing, such as if two SQLConnection instances are connected to the same database, and one instance changes the schema while another one is reading it.   
| **3130**|  Too much data for one row of a table.|   
| **3131**|  Abort due to constraint violation. |  Indicates that the operation could not be completed because the statement caused a violation of one or more data integrity constraints. These are constraints that are defined in the table structure when it is created. For more information, see the [CREATE TABLE](http://www.adobe.com/go/learn_as3_sqlsupportdb_en#createTable) section in the appendix [SQL support in local databases](http://www.adobe.com/go/learn_as3_sqlsupportdb_en).   
| **3132**|  Data type mismatch. |  Indicates that the operation could not be completed because of a data type mismatch error. This occurs when the data type of a value doesn't match the expected or required type. For more information, see the [Data type support](http://www.adobe.com/go/learn_as3_sqlsupportdb_en#dataTypes) section in the appendix [SQL support in local databases](http://www.adobe.com/go/learn_as3_sqlsupportdb_en).   
| **3133**|  An internal error occurred.|   
| **3134**|  Feature not supported on this operating system.|   
| **3135**|  Authorization denied.|   
| **3136**|  Auxiliary database format error.|   
| **3137**|  An index specified for a parameter was out of range. |  Indicates that the operation could not be completed because a parameter index was not valid, such as if a parameter is specified with an index less than 0, or if a parameter is specified with index 7 but the statement text only includes five parameters.   
| **3138**|  File opened is not a database file.|   
| **3139**|  The page size specified was not valid for this operation.|   
| **3140**|  The encryption key size specified was not valid for this operation. Keys must be exactly 16 bytes in length|   
| **3141**|  The requested database configuration is not supported.|   
| **3143**|  Unencrypted databases may not be reencrypted.|   
| **3200**|  Cannot perform operation on closed window.|   
| **3201**|  Adobe Reader cannot be found.|   
| **3202**|  Adobe Reader 8.1 or later cannot be found.|   
| **3203**|  Default Adobe Reader must be version 8.1 or later.|   
| **3204**|  An error ocurred trying to load Adobe Reader.|   
| **3205**|  Only application-sandbox content can access this feature.|   
| **3206**|  Caller _ cannot set LoaderInfo property _.|   
| **3207**|  Application-sandbox content cannot access this feature.|   
| **3208**|  Attempt to access invalid clipboard.|   
| **3209**|  Attempt to access dead clipboard.|   
| **3210**|  The application attempted to reference a JavaScript object in a HTML page that is no longer loaded.|   
| **3211**|  Drag and Drop File Promise error: _|   
| **3212**|  Cannot perform operation on a NativeProcess that is not running.|   
| **3213**|  Cannot perform operation on a NativeProcess that is already running.|   
| **3214**|  NativeProcessStartupInfo.executable does not specify a valid executable file.|   
| **3215**|  NativeProcessStartupInfo.workingDirectory does not specify a valid directory.|   
| **3216**|  Error while reading data from NativeProcess.standardOutput.|   
| **3217**|  Error while reading data from NativeProcess.standardError.|   
| **3218**|  Error while writing data to NativeProcess.standardInput.|   
| **3219**|  The NativeProcess could not be started. '_'|   
| **3220**|  Action '_' not allowed in current security context '_'.|   
| **3221**|  Adobe Flash Player cannot be found.|   
| **3222**|  The installed version of Adobe Flash Player is too old.|   
| **3223**|  DNS lookup error: platform error _|   
| **3224**|  Socket message too long|   
| **3225**|  Cannot send data to a location when connected.|   
| **3226**|  Cannot import a SWF file when LoaderContext.allowCodeImport is false.|   
| **3227**|  Cannot launch another application from background.|   
| **3228**|  StageWebView encountered an error during the load operation.|   
| **3229**|  The protocol is not supported.: |   
| **3230**|  The browse operation is unsupported.|   
| **3300**|  Voucher is invalid. |  Reacquire the voucher from the server.   
| **3301**|  User authentication failed. |  Ask user to re-enter credentials.   
| **3302**|  Flash Access server does not support SSL. |  SSL must be enabled on the license server when playing content packaged using Flash Media Right Management Server.   
| **3303**|  Content expired. |  Reacquire voucher from the server.   
| **3304**|  User authorization failed (for example, the user has not purchased the content). |  The current user is not authorized to view the content.   
| **3305**|  Can't connect to the server. |  Check the network connection.   
| **3306**|  Client update required (Flash Access server requires new client). |  Both the runtime (Flash Player or AIR) and the Flash Access module need to be updated.   
| **3307**|  Generic internal Flash Access failure.|   
| **3308**|  Wrong voucher key. |  Reacquire the voucher from the server.   
| **3309**|  Video content is corrupted. |  Try downloading the content again.   
| **3310**|  The AIR application or Flash Player SWF does not match the one specified in the DRM policy.|   
| **3311**|  The version of the application does not match the one specified in the DRM policy.|   
| **3312**|  Verification of voucher failed. |  Reacquire the voucher from the server.   
| **3313**|  Write to the file system failed.|   
| **3314**|  Verification of FLV/F4V header file failed. |  Try downloading the DRMContentData object again. If DRMContentData was extracted from FLV/F4V try downloading the content again.   
| **3315**|  The current security context does not allow this operation. |  This error can occur when the remote SWF loaded by AIR isn't allowed access to Flash Access functionality. This error can also occur if a security error occurs during network access. Other possible security errors include errors due to a crossdomain.xml file, which restricts client access based on domain, or if crossdomain.xml is not accessible.   
| **3316**|  The value of LocalConnection.isPerUser cannot be changed because it has already been locked by a call to LocalConnection.connect, .send, or .close.|   
| **3317**|  Failed to load Flash Access module. |  If this error occurs in AIR, reinstall AIR. If this error occurs in Flash Player, download the Flash Access module again.   
| **3318**|  Incompatible version of Flash Access module found. |  If this error occurs in AIR, reinstall AIR. If this error occurs in Flash Player, download the Flash Access module again.   
| **3319**|  Missing Flash Access module API entry point. |  If this error occurs in AIR, reinstall AIR. If this error occurs in Flash Player, download the Flash Access module again.   
| **3320**|  Generic internal Flash Access failure.|   
| **3321**|  Individualization failed. |  There was a problem with the Adobe server (e.g. could be busy). Retry the operation.   
| **3322**|  Device binding failed. |  Undo any device changes or reset the license (voucher) files. The Flash Access module will then reindividualize. In AIR, voucher reset can be done by invoking the resetDRMVouchers() on DRMManager, whereas in Flash Player, the user needs to reset the license files in the Flash Player Settings Manager.   
| **3323**|  The internal stores are corrupted. |  Retry the operation. If the error persists, reset the license files in the Flash Player Settings Manager. The Flash Access module will then reindividualize.   
| **3324**|  Reset license files and the client will fetch a new machine token. |  Reset the license files in the Flash Player Settings Manager and the client will fetch a new machine token.   
| **3325**|  Internal stores are corrupt. |  Internal stores are corrupt and has been deleted. Retry the operation.   
| **3326**|  Call customer support. |  Tampering has been detected. Options are to call customer support, or reset the license files in the Flash Player Settings Manager.   
| **3327**|  Clock tampering detected. |  Options are to reacquire the voucher or to fix the clock.   
| **3328**|  Server error; retry the request. |  This error is a server error. Retry the request. The sub error gives the error returned by the server.   
| **3329**|  Error in application-specific namespace. |  The server has returned an error in an application-specific namespace. Check the application for details.   
| **3330**|  Need to authenticate the user and reacquire the voucher. |  Try authenticating the user and acquiring the voucher again.   
| **3331**|  Content is not yet valid. |  The voucher is not yet valid. Try again at a later date.   
| **3332**|  Cached voucher has expired. Reacquire the voucher from the server. |  The voucher cached on the local computer has expired. Reacquire the voucher from the server.   
| **3333**|  The playback window for this policy has expired. |  The playback window for this policy has expired. The user can no longer play this content under this policy.   
| **3334**|  This platform is not allowed to play this content. |  This platform is not allowed to play this media.   
| **3335**|  Invalid version of Flash Access module. Upgrade AIR or Flash Access module for the Flash Player. |  In AIR, update to the latest version of AIR. In Flash Player, upgrade to the latest version of the Flash Access module and try playing content again.   
| **3336**|  This platform is not allowed to play this content. |  This operating system is not allowed to play this media.   
| **3337**|  Upgrade Flash Player or AIR and retry playback. |  Upgrade to the latest version of AIR or Flash Player, and try playing content again.   
| **3338**|  Unknown connection type. |  Flash Player or AIR cannot detect the connection type. Try connecting the device to a different connection.   
| **3339**|  Can't play back on analog device. Connect to a digital device. |  Cannot play media on an analog device. Connect to a digital device and try again.   
| **3340**|  Can't play back because connected analog device doesn't have the correct capabilities. |  Cannot play media because the connected analog device doesn't have the correct capabilities (for example, it doesn't have Macrovision or ACP).   
| **3341**|  Can't play back on digital device. |  The policy does not allow play back on digital devices.   
| **3342**|  The connected digital device doesn't have the correct capabilities. |  The connected digital device doesn't have the correct capabilities, for example, it doesn't support HDCP.   
| **3343**|  Internal Error. |  If this error occurs in AIR, reinstall AIR. If this error occurs in Flash Player, you may need to update the Adobe Access module by calling `SystemUpdater.update(flash.system.SystemUpdaterType.DRM)` For more information, see the [SystemUpdater](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/system/SystemUpdater.html) page.   
| **3344**|  Missing Flash Access module. |  If this error occurs in AIR, reinstall AIR. If this error occurs in Flash Player, you may need to update the Adobe Access module by calling `SystemUpdater.update(flash.system.SystemUpdaterType.DRM)` For more information, see the [SystemUpdater](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/system/SystemUpdater.html) page.   
| **3345**|  This operation is not permitted with content protected using Flash Access.|   
| **3346**|  Failed migrating local DRM data, all locally cached DRM vouchers are lost. |   
| **3347**|  The device does not meet the Flash Access server's playback device constraints. |   
| **3348**|  This protected content is expired. |   
| **3349**|  The Flash Access server is running at a version that's higher than the max supported by this runtime.|   
| **3350**|  The Flash Access server is running at a version that's lower than the min supported by this runtime.|   
| **3351**|  Device Group registration token is corrupted, please refresh the token by registering again to the DRMDeviceGroup. |   
| **3352**|  The server is using a newer version of the registration token for this Device Group. Please refresh the token by registering again to the DRMDeviceGroup. |   
| **3353**|  the server is using an older version of the registration token for this Device Group. |   
| **3354**|  Device Group registration is expired, please refresh the token by registering again to the DRMDeviceGroup. |   
| **3355**|  The server denied this Device Group registration request.|   
| **3356**|  The root voucher for this content's DRMVoucher was not found. |   
| **3357**|  The DRMContentData provides no valid embedded voucher and no Flash Access server url to acquire the voucher from. |   
| **3358**|  ACP protection is not available on the device but required to playback the content. |   
| **3359**|  CGMSA protection is not available on the device but required to playback the content. |   
| **3360**|  Device Group registration is required before doing this operation. |   
| **3361**|  The device is not registered to this Device Group. |   
| **3362**|  Asynchronous operation took longer than maxOperationTimeout.|   
| **3363**|  The M3U8 playlist passed in had unsupported content.|   
| **3364**|  The framework requested the device ID, but the returned value was empty.|   
| **3365**|  This browser/platform combination does not allow DRM protected playback when in incognito mode.|   
| **3366**|  The host runtime called the Access library with a bad parameter.|   
| **3367**|  M3U8 manifest signing failed.|   
| **3368**|  The user cancelled the operation, or has entered settings that disallow access to the system.|   
| **3369**|  A required browser interface is not available.|   
| **3370**|  The user has disabled the "Allow identifiers for protected content" setting.|   
| **3400**|  An error occured while executing JavaScript code.|   
| **3401**|  Security sandbox violation: An object with this name has already been registered from another security domain.|   
| **3402**|  Security sandbox violation: Bridge caller _ cannot access _.|   
| **3500**|  The extension context does not have a method with the name _.|   
| **3501**|  The extension context has already been disposed.|   
| **3502**|  The extension returned an invalid value.|   
| **3503**|  The extension was left in an invalid state.|   
| **3600**|  No valid program set.|   
| **3601**|  No valid index buffer set.|   
| **3602**|  Sanity check on parameters failed, _ triangles and _ index offset.|   
| **3603**|  Not enough indices in this buffer. _ triangles at offset _, but there are only _ indices in buffer.|   
| **3604**|  Sampler _ binds a texture that is also bound for render to texture.|   
| **3605**|  Sampler _ binds an invalid texture.|   
| **3606**|  Sampler _ format does not match texture format.|   
| **3607**|  Stream _ is set but not used by the current vertex program.|   
| **3608**|  Stream _ is invalid.|   
| **3609**|  Stream _ does not have enough vertices.|   
| **3610**|  Stream _ vertex offset is out of bounds|   
| **3611**|  Stream _ is read by the current vertex program but not set.|   
| **3612**|  Programs must be in little endian format.|   
| **3613**|  The native shader compilation failed.|   
| **3614**|  The native shader compilation failed.\nOpenGL specific: _|   
| **3615**|  AGAL validation failed: Program size below minimum length for _ program.|   
| **3616**|  AGAL validation failed: Not an AGAL program. Wrong magic byte for _ program.|   
| **3617**|  AGAL validation failed: Bad AGAL version for _ program. Current version is _.|   
| **3618**|  AGAL validation failed: Bad AGAL program type identifier for _ program.|   
| **3619**|  AGAL validation failed: Shader type must be either fragment or vertex for _ program.|   
| **3620**|  AGAL validation failed: Invalid opcode, value out of range: _ at token _ of _ program.|   
| **3621**|  AGAL validation failed: Invalid opcode, _ is not implemented in this version at token _ of _ program.|   
| **3622**|  AGAL validation failed: Opcode _ only allowed in fragment programs at token _ of _ program.|   
| **3623**|  AGAL validation failed: Block nesting underflow - EIF without opening IF condition. At token _ of _ program.|   
| **3624**|  AGAL validation failed: Block nesting overflow. Too many nested IF blocks. At token _ of _ program.|   
| **3625**|  AGAL validation failed: Bad AGAL source operands. Both are constants (this must be precomputed) at token _ of _ program.|   
| **3626**|  AGAL validation failed: Opcode _, both operands are indirect reads at token _ of _ program.|   
| **3627**|  AGAL validation failed: Opcode _ destination operand must be all zero at token _ of _ program.|   
| **3628**|  AGAL validation failed: The destination operand for the _ instruction must mask w (use .xyz or less) at token _ of _ program.|   
| **3629**|  AGAL validation failed: Too many tokens (_) for _ program.|   
| **3630**|  Fragment shader type is not fragment.|   
| **3631**|  Vertex shader type is not vertex.|   
| **3632**|  AGAL linkage: Varying _ is read in the fragment shader but not written to by the vertex shader.|   
| **3633**|  AGAL linkage: Varying _ is only partially written to. Must write all four components.|   
| **3634**|  AGAL linkage: Fragment output needs to write to all components.|   
| **3635**|  AGAL linkage: Vertex output needs to write to all components.|   
| **3636**|  AGAL validation failed: Unused operand is not set to zero for _ at token _ of _ program.|   
| **3637**|  AGAL validation failed: Sampler registers only allowed in fragment programs for _ at token _ of _ program.|   
| **3638**|  AGAL validation failed: Sampler register only allowed as second operand in texture instructions for _ at token _ of _ program.|   
| **3639**|  AGAL validation failed: Indirect addressing only allowed in vertex programs for _ at token _ of _ program.|   
| **3640**|  AGAL validation failed: Indirect addressing only allowed into constant registers for _ at token _ of _ program.|   
| **3641**|  AGAL validation failed: Indirect addressing not allowed for this operand in this instruction for _ at token _ of _ program.|   
| **3642**|  AGAL validation failed: Indirect source type must be attribute, constant or temporary for _ at token _ of _ program.|   
| **3643**|  AGAL validation failed: Indirect addressing fields must be zero for direct addressing for _ at token _ of _ program.|   
| **3644**|  AGAL validation failed: Varying registers can only be read in fragment programs for _ at token _ of _ program.|   
| **3645**|  AGAL validation failed: Attribute registers can only be read in vertex programs for _ at token _ of _ program.|   
| **3646**|  AGAL validation failed: Can not read from output register for _ at token _ of _ program.|   
| **3647**|  AGAL validation failed: Temporary register read without being written to for _ at token _ of _ program.|   
| **3648**|  AGAL validation failed: Temporary register component read without being written to for _ at token _ of _ program.|   
| **3649**|  AGAL validation failed: Sampler registers can not be written to for _ at token _ of _ program.|   
| **3650**|  AGAL validation failed: Varying registers can only be written in vertex programs for _ at token _ of _ program.|   
| **3651**|  AGAL validation failed: Attribute registers can not be written to for _ at token _ of _ program.|   
| **3652**|  AGAL validation failed: Constant registers can not be written to for _ at token _ of _ program.|   
| **3653**|  AGAL validation failed: Destination writemask is zero for _ at token _ of _ program.|   
| **3654**|  AGAL validation failed: Reserve bits should be zero for _ at token _ of _ program.|   
| **3655**|  AGAL validation failed: Unknown register type for _ at token _ of _ program.|   
| **3656**|  AGAL validation failed: Sampler register index out of bounds for _ at token _ of _ program.|   
| **3657**|  AGAL validation failed: Varying register index out of bounds for _ at token _ of _ program.|   
| **3658**|  AGAL validation failed: Attribute register index out of bounds for _ at token _ of _ program.|   
| **3659**|  AGAL validation failed: Constant register index out of bounds for _ at token _ of _ program.|   
| **3660**|  AGAL validation failed: Output register index out of bounds for _ at token _ of _ program.|   
| **3661**|  AGAL validation failed: Temporary register index out of bounds for _ at token _ of _ program.|   
| **3662**|  AGAL validation failed: Cube map samplers must set wrapping to clamp mode for _ at token _ of _ program.|   
| **3663**|  Sampler _ binds an undefined texture.|   
| **3664**|  AGAL validation failed: Unknown sampler dimension _ for _ at token _ of _ program.|   
| **3665**|  AGAL validation failed: Unknown filter mode in sampler: _ for _ at token _ of _ program.|   
| **3666**|  AGAL validation failed: Unknown mipmap mode in sampler: _ for _ at token _ of _ program.|   
| **3667**|  AGAL validation failed: Unknown wrapping mode in sampler: _ for _ at token _ of _ program.|   
| **3668**|  AGAL validation failed: Unknown special flag used in sampler: _ for _ at token _ of _ program.|   
| **3669**|  Bad input size.|   
| **3670**|  Buffer too big.|   
| **3671**|  Buffer has zero size.|   
| **3672**|  Buffer creation failed. Internal error.|   
| **3673**|  Cube side must be [0..5].|   
| **3674**|  Miplevel too large.|   
| **3675**|  Texture format mismatch.|   
| **3676**|  Platform does not support desired texture format.|   
| **3677**|  Texture decoding failed. Internal error.|   
| **3678**|  Texture needs to be square.|   
| **3679**|  Texture size does not match.|   
| **3680**|  Depth texture not implemented yet.|   
| **3681**|  Texture size is zero.|   
| **3682**|  Texture size not a power of two.|   
| **3683**|  Texture too big (max is _x_).|   
| **3684**|  Texture creation failed. Internal error.|   
| **3685**|  Could not create renderer.|   
| **3686**|  'disabled' format only valid with a null vertex buffer.|   
| **3687**|  Null vertex buffers require the 'disabled' format.|   
| **3688**|  You must add an event listener for the context3DCreate event before requesting a new Context3D.|   
| **3689**|  You can not swizzle second operand for _ at token _ of _ program.|   
| **3690**|  Too many draw calls before calling present.|   
| **3691**|  Resource limit for this resource type exceeded.|   
| **3692**|  All buffers need to be cleared every frame before drawing.|   
| **3693**|  AGAL validation failed: Sampler register must be used for second operand in texture instructions for _ at token _ of _ program.|   
| **3694**|  The object was disposed by an earlier call of dispose() on it.|   
| **3695**|  A texture can only be bound to multiple samplers if the samplers also have the exact same properties. Mismatch at samplers _ and _.|   
| **3696**|  AGAL validation failed: Second use of sampler register needs to specify the exact same properties. At token _ of _ program.|   
| **3697**|  A texture is bound on sampler _ but not used by the fragment program.|   
| **3698**|  The back buffer is not configured.|   
| **3699**|  Requested Operation failed to complete|   
| **3700**|  A texture sampler binds an incomplete texture. Make sure to upload(). All miplevels are required when mipmapping is enabled.|   
| **3701**|  The output color register can not use a write mask. All components must be written.|   
| **3702**|  Context3D not available.|   
| **3703**|  AGAL validation failed: Source swizzle must be scalar (one of: xxxx, yyyy, zzzz, wwww) for _ at token _ of _ program.|   
| **3704**|  AGAL validation failed: Cube map samplers must enable mipmapping for _ at token _ of _ program.|   
| **3705**|  Cubemap texture too big (max is 1024x1024).|   
| **3706**|  Scissor rectangle is set but does not intersect the framebuffer.|   
| **3707**|  Property can not be set in non full screen mode.|   
| **3708**|  Feature not available on this platform.|   
| **3709**|  The depthAndStencil flag in the application descriptor must match the enableDepthAndStencil Boolean passed to configureBackBuffer on the Context3D object.|   
| **3710**|  Requested Stage3D Operation failed to complete.|   
| **3711**|  The streaming levels is too large.|   
| **3712**|  Rendering to streaming textures is not allowed.|   
| **3713**|  Incomplete streaming texture (base level not uploaded) used with no mip sampling.|   
| **3714**|  ApplicationDomain.domainMemory is not available.|   
| **3715**|  Too many instructions used in native shader. Detected _ but can only support _ for _ program.|   
| **3716**|  Too many ALU instructions in native shader. Detected _ but can only support _ for _ program.|   
| **3717**|  Too many texture instructions in native shader. Detected _ but can only support _ for _ program.|   
| **3718**|  Too many constants used in native shader. Detected _ but can only support _ for _ program.|   
| **3719**|  Too many temporary registers used in native shader. Detected _ but can only support _ for _ program.|   
| **3720**|  Too many varying registers used in native shader. Detected _ but can only support _ for _ program.|   
| **3721**|  Too many indirect texture reads in native shader. Detected _ but can only support _ for _ program.|   
| **3722**|  Event.FRAME_LABEL event can only be registered with FrameLabel object.|   
| **3723**|  Invalid Context3D bounds. Context3D instance bounds must be contained within Stage bounds in constrained mode. Requested Context3D bounds were (_,_,_,_), stage bounds are (_,_,_,_).|   
| **3724**|  This call requires a Context3D that is created with the extended profile.|   
| **3725**|  The requested AGAL version (_) is not valid under the Context3D profile. For example AGAL version 2 requires extended profile.|   
| **3726**|  AGAL validation failed: Opcode _ requires AGAL version to be at least 2, at token _ of _ program.|   
| **3727**|  Failed to obtain authorization token.|   
| **3728**|  When rendering to multiple textures slot 0 must be active. When rendering to the back buffer all render to texture slots must be disabled.|   
| **3729**|  When rendering to multiple textures all textures must have the same dimension and render settings.|   
| **3730**|  When rendering to multiple textures the same texture (or cube map face) may not be bound into multiple slots.|   
| **3731**|  This feature is not available within this context. |  This error occurs if a background worker attempts to access an API that is not available to it.   
| **3732**|  Worker.terminate is only available for background workers. |  This error occurs if Worker.terminate() is invoked on the primoridial worker.   
| **3735**|  This API cannot accept shared ByteArrays.|   
| **3736**|  MessageChannel is not a sender.|   
| **3737**|  MessageChannel is not a receiver.|   
| **3738**|  MessageChannel is closed.|   
| **3739**|  AGAL validation failed: Open conditional block at end of _ program.|   
| **3740**|  AGAL validation failed: Texture samplers used in the TED instruction can not specify a lod bias. At token _ of _ program.|   
| **3741**|  AGAL validation failed: TEX instructions in an if block can not use computed texture coordinates. Either use interpolated texture coordinates or use the TED instruction instead. At token _ of _ program.|   
| **3742**|  AGAL validation failed: DDX and DDY opcodes are not allowed inside conditional blocks. At token _ of _ program.|   
| **3743**|  AGAL validation failed: The TED opcode must enable mip mapping. At token _ of _ program.|   
| **3744**|  AGAL validation failed: Color output written to multiple times. At token _ of _ program.|   
| **3745**|  Compressed texture size is too small. The minimum size for compressed textures is 4x4.|   
| **3746**|  Rendering to compressed textures is not allowed.|   
| **3747**|  Multiple application domains are not supported on this operating system.|   
| **3748**|  AGAL validation failed: Empty conditional branch in AGAL of _ program.|   
| **3749**|  AGAL validation failed: Depth output register index out of bounds for _ at token _ of _ program.|   
| **3750**|  AGAL validation failed: Depth output register is only available in fragment programs.|   
| **3751**|  AGAL validation failed: Output registers can not be written inside conditionals.|   
| **3752**|  AGAL validation failed: Broken else chain.|   
| **3753**|  Rectangle or cube textures require textures sampling to be set to clamp.|   
| **3754**|  Texture sampler dimensions mismatch. The AGAL declaration has to match the texture used.|   
| **3755**|  Rectangle textures have to disable mip mapping and can not have a lod bias set.|   
| **3756**|  AGAL validation failed: Depth output must set only x as a write mask. At token _ of _ program.|   
| **3757**|  AGAL validation failed: Vertex and fragment program need to have the same version.|   
| **3758**|  AGAL validation failed: Conditional source are exactly the same, condition is constant. At token _ of _ program.|   
| **3759**|  The selected texture format is not valid in this profile.|   
| **3760**|  The color output index is out of range.|   
| **3761**|  The bit depth of all textures used for render to texture must be exactly the same.|   
| **3762**|  This texture format is not supported for rectangle textures.|   
| **3763**|  Sampler _ binds a texture that that does not match the read mode specified in AGAL. Reading compressed or single/dual channel textures must be explicitly declared.|   
| **3764**|  Reloading a SWF is not supported on this operating system.|   
| **3765**|  This call requires a Context3D that is created with the baseline or baselineExtended profile.|   
| **3766**|  RectangleTexture too big (max is the larger of _x_ or the size of the backbuffer).|   
| **3767**|  The argument samples is too big. More than 1800 seconds of audio data is not permitted in a single call of loadPCMFromByteArray.|   
| **3768**|  The Stage3D API may not be used during background execution on this operating system.|   
| **3769**|  Security sandbox violation: Only simple headers can be used with navigateToUrl() or sendToUrl().|   
| **3770**|  ColorOutputIndex must be in the range [0..3].|   
| **3771**|  2D textures need to have surfaceSelector = 0.|   
| **3772**|  Cube textures need to have surfaceSelector [0..5].|   
| **3773**|  Rectangle textures need to have surfaceSelector = 0.|   
| **3774**|  All the assigned render targets should match the outputs in the fragment program.|   
| **3775**|  AGAL validation failed: Non-consecutive slots are not allowed.|   
| **3776**|  Depth output in fragment program requires depthAndStencil = true.|   
| **3777**|  Buffers need to be cleared before first draw.|   
| **3778**|  Video textures have to disable mip mapping and can not have a LOD bias set.|   
| **3779**|  This call requires a Context3D that is created with the standard profile or above|   
| **3780**|  Requested width of backbuffer is not in allowed range _ to _.|   
| **3781**|  Requested height of backbuffer is not in allowed range _ to _.|   
| **3782**|  This call requires a Context3D that is created with the baseline profile or above.|   
| **3783**|  A Stage object cannot be added as the child of another object.|   
| **3784**|  The number of instances per element should be greater than 0.|   
| **3785**|  Vertex buffer stream _ does not contain enough elements for number of instances.|   
| **3786**|  AGAL validation failed: Instance id register can not be written to for _ at token _ of _ program.|   
| **3787**|  This call requires a Context3D that is created with the standard extended profile or above.|   
| **3788**|  Instance id register can only be read in the vertex shader.|   
| **3789**|  AGAL validation failed: Instance id register is supported in Agal version 3 and above.|   
| **3790**|  Texture upload failed.|   
| **3791**|  Asynchronous upload is available for miplevel 0 only.|   
| **3792**|  Vertex buffer stream _ for instances is improperly set at first index.|   
| **3800**|  This call requires _ permission.|   
| **3801**|  Another permission request is in progress.|   
| **3802**|  Offset outside stage coordinate bound.|   
| **3803**|  AGAL validation failed: Opcode _ only allowed in vertex programs at token _ of _ program.|   
| **3804**|  AGAL validation failed: Anistropic Filter is not allowed in Vertex Texture Sampler.|   
| **3805**|  AGAL validation failed: Vertex Texture Fetch is supported in Agal version 4 and above.|   
  
  

* Note: This error indicates that the ActionScript in the SWF is invalid. If you believe that the file has not been corrupted, please report the problem to Adobe.

  

[Compiler Errors](compilerErrors.html) | [Compiler Warnings](compilerWarnings.html)

[All Packages](package-summary.html) | [All Classes](class-summary.html) | [Language Elements](language-elements.html) | [Index](all-index-Symbols.html) | [Appendices](appendices.html) | [Conventions](conventions.html) | [Frames](index.html?runtimeErrors.html&all-classes.html)[No Frames]()

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Mon Jun 30 2025, 11:01 AM GMT+01:00\) : Run-Time Errors)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Mon Jun 30 2025, 11:01 AM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)