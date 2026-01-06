# Package

The flash.utils package contains a variety of package-level functions for timing code execution, retrieving information about classes and objects, and converting escape characters.

Public Functions

| Function| Defined by  
---|---|---  
|  |  [clearInterval](#clearInterval\(\))(id:[uint](../../uint.html)):[void](../../specialTypes.html#void) Cancels a specified `setInterval()` call. | flash.utils  
|  |  [clearTimeout](#clearTimeout\(\))(id:[uint](../../uint.html)):[void](../../specialTypes.html#void) Cancels a specified `setTimeout()` call. | flash.utils  
|  |  [describeType](#describeType\(\))(value:[*](../../specialTypes.html#*)):[XML](../../XML.html) Produces an XML object that describes the ActionScript object named as the parameter of the method. | flash.utils  
|  |  [escapeMultiByte](#escapeMultiByte\(\))(value:[String](../../String.html)):[String](../../String.html) Returns an escaped copy of the input string encoded as either UTF-8 or system code page, depending on the value of System.useCodePage. | flash.utils  
|  |  [getDefinitionByName](#getDefinitionByName\(\))(name:[String](../../String.html)):[Object](../../Object.html) Returns a reference to the class object of the class specified by the `name` parameter. | flash.utils  
|  |  [getQualifiedClassName](#getQualifiedClassName\(\))(value:[*](../../specialTypes.html#*)):[String](../../String.html) Returns the fully qualified class name of an object. | flash.utils  
|  |  [getQualifiedSuperclassName](#getQualifiedSuperclassName\(\))(value:[*](../../specialTypes.html#*)):[String](../../String.html) Returns the fully qualified class name of the base class of the object specified by the `value` parameter. | flash.utils  
|  |  [getTimer](#getTimer\(\))():[int](../../int.html) Used to compute relative time. | flash.utils  
|  |  [setInterval](#setInterval\(\))(closure:[Function](../../Function.html), delay:[Number](../../Number.html), [...](../../statements.html#..._\(rest\)_parameter) arguments):[uint](../../uint.html) Runs a function at a specified interval (in milliseconds). | flash.utils  
|  |  [setTimeout](#setTimeout\(\))(closure:[Function](../../Function.html), delay:[Number](../../Number.html), [...](../../statements.html#..._\(rest\)_parameter) arguments):[uint](../../uint.html) Runs a specified function after a specified delay (in milliseconds). | flash.utils  
|  |  [unescapeMultiByte](#unescapeMultiByte\(\))(value:[String](../../String.html)):[String](../../String.html) Returns an unescaped copy of the input string, which is decoded from either system code page page or UTF-8 depending on the value of System.useCodePage. | flash.utils  
  
Function detail

clearInterval| ()| function  
---|---|---  
  
`public function clearInterval(id:[uint](../../uint.html)):[void](../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Cancels a specified `setInterval()` call. 

Parameters | `id:[uint](../../uint.html)` — The ID of the `setInterval()` call, which you set to a variable, as in the following:   
---|---  
  
See also

[setInterval()](package.html#setInterval\(\))

  
Example   
The following example uses the `setInterval()` method to create a timed interval, calling the `myRepeatingFunction()` method after regular intervals of one second. 

Each call of the `myRepeatingFunction` method increments the `counter` property, and when it equals the `stopCount` property, the `clearInterval() ` method is called with the property `intervalId` which is a reference id to the interval that was created earlier.
    
    
    package {
        import flash.display.Sprite;
        import flash.utils.*;
    
        public class ClearIntervalExample extends Sprite {
    		private var intervalDuration:Number = 1000; // duration between intervals, in milliseconds
    		private var intervalId:uint;
    		private var counter:uint 	= 0;
    		private var stopCount:uint 	= 3;
    		
            public function ClearIntervalExample() {
    			intervalId = setInterval(myRepeatingFunction, intervalDuration, "Hello", "World");
            }
    
            public function myRepeatingFunction():void {
                trace(arguments[0] + " " + arguments[1]);
    
    			counter++;
    			if(counter == stopCount) {
    				trace("Clearing Interval");
    				clearInterval(intervalId);	
    			}
            }
        }
    }

clearTimeout| ()| function|   
---|---|---|---  
  
`public function clearTimeout(id:[uint](../../uint.html)):[void](../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Cancels a specified `setTimeout()` call. 

Parameters | `id:[uint](../../uint.html)` — The ID of the `setTimeout()` call, which you set to a variable, as in the following:   
---|---  
  
See also

[setTimeout()](package.html#setTimeout\(\))

  
Example   
The following example uses the `setTimeout()` method to call another method following a specified delay period. 

A loop is created to count to one million. If the system can process this request faster than a second can expire, `clearTimeout()` will remove the `setTimeout()` request, and `myDelayedFunction()` will not be called.
    
    
    package {
        import flash.display.Sprite;
        import flash.utils.*;
    
        public class ClearTimeoutExample extends Sprite {
    		private var delay:Number = 1000; // delay before calling myDelayedFunction
    		private var intervalId:uint;
    		private var count:uint = 1000000;
    		
            public function ClearTimeoutExample() {
    			intervalId = setTimeout(myDelayedFunction, delay);
    			startCounting();
            }
    
    		public function startCounting():void {
    			var i:uint = 0;
    			do {
    				if(i == count-1) {
    					clearTimeout(intervalId);
    					trace("Your computer can count to " + count + " in less than " + delay/1000 + " seconds.");	
    				}
    				i++;
    			} while(i < count)			
    		}
    		
            public function myDelayedFunction():void {
    			trace("Time expired.");
    		}
        }
    }

describeType| ()| function|   
---|---|---|---  
  
`public function describeType(value:[*](../../specialTypes.html#*)):[XML](../../XML.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Produces an XML object that describes the ActionScript object named as the parameter of the method. This method implements the programming concept of _reflection_ for the ActionScript language. 

If the `value` parameter is an instance of a type, the returned XML object includes all the instance properties of that type, but does not include any static properties. You can check for this condition when you parse the XML object by examining the value of the `<type>` tag's `isStatic` attribute, which is `false` when the `value` parameter is an instance of a type.

To obtain the static properties of a type, pass the type itself for the `value` parameter. The returned XML object includes not only the type's static properties, but also all of its instance properties. The instance properties are nested inside a tag named `<factory>` to distinguish them from the static properties. In this case, the `isStatic` attribute of the `<type>` tag is `true`.

**Note:** If you need only to traverse an object's inheritance hierarchy and do not need the other information provided by `describeType()`, use the `getQualifiedClassName()` and `getQualifiedSuperclassName()` functions instead.

The following table describes some of the tags and attributes of the XML object generated by `describeType()` (all class and interface names returned are in fully qualified format):

Tag| Attribute| Description  
---|---|---  
`<type>`|  | The root tag of the XML object.  
| name| The name of the ActionScript object's data type.  
| base| The immediate superclass of the ActionScript object's defining class. If the ActionScript object is a class object, the value is `Class`.  
| isDynamic| `true` if the ActionScript object's defining class is dynamic; `false` otherwise. If the ActionScript object is a class object, the value is `true` because the Class class is dynamic.  
| isFinal| `true` if the ActionScript object's defining class is final; `false` otherwise.  
| isStatic| `true` if the ActionScript object is a class object or constructor function; `false` otherwise. This attribute is named `isStatic` because if it is `true`, any tags that are not nested inside the `factory` tag are static.  
`<extendsClass>`|  | There is a separate `extendsClass` tag for each superclass of the ActionScript object's defining class.  
| type| The name of a superclass that the ActionScript object's defining class extends.  
`<implementsInterface>`|  | There is a separate `implementsInterface` tag for each interface implemented by the ActionScript object's defining class or any of its superclasses.  
| type| The name of an interface that the ActionScript object's defining class implements.  
`<accessor>`|  | An accessor is a property defined by getter and setter functions.  
| name| The name of the accessor.  
| access| The access rights of the property. Possible values include `readonly`, `writeonly`, and `readwrite`.  
| type| The data type of the property.  
| declaredBy| The class that contains the associated getter or setter functions.  
`<constant>`|  | A constant is a property defined with the `const` statement.  
| name| The name of the constant.  
| type| The data type of the constant.  
`<method>`|  | A method is a function declared as part of a class definition.  
| name| The name of the method.  
| declaredBy| The class that contains the method definition.  
| returnType| The data type of the method's return value.  
`<parameter>`|  | There is a separate `parameter` tag for each parameter that a method defines. This tag is always nested inside a `<method>` tag.  
| index| A number corresponding to the order in which the parameter appears in the method's parameter list. The first parameter has a value of 1.  
| type| The data type of the parameter.  
| optional| `true` if the parameter is optional; `false` otherwise.  
`<variable>`|  | A variable is a property defined with the `var` statement.  
| name| The name of the variable.  
| type| The data type of the variable.  
`<factory>`|  | If the ActionScript object is a class object or constructor function, all instance properties and methods are nested inside this tag. If the `isStatic` attribute of the `<type>` tag is `true`, all properties and methods that are not nested within the `<factory>` tag are static. This tag appears only if the ActionScript object is a class object or constructor function.  
Parameters | `value:[*](../../specialTypes.html#*)` — The object for which a type description is desired. Any ActionScript value may be passed to this method including all available ActionScript types, object instances, primitive types such as uint, and class objects.   
---|---  
  
Returns | `[XML](../../XML.html)` — An XML object containing details about the object that was passed in as a parameter. It provides the following information about the object: 

  * The class of the object
  * The attributes of the class
  * The inheritance tree from the class to its base classes
  * The interfaces implemented by the class
  * The declared instance properties of the class
  * The declared static properties of the class
  * The instance methods of the class
  * The static methods of the class 
  * For each method of the class, the name, number of parameters, return type, and parameter types 

**Note:** `describeType()` only shows public properties and methods, and will not show properties and methods that are private, package internal or in custom namespaces.   
---|---  
  
See also

[getQualifiedClassName()](package.html#getQualifiedClassName\(\))   
[getQualifiedSuperclassName()](package.html#getQualifiedSuperclassName\(\))

  
Example   

    
    
    package {
        import flash.display.Sprite;
    	import flash.utils.describeType;
    	
    	public class DescribeTypeExample extends Sprite {
    		public function DescribeTypeExample() {
    			var child:Sprite = new Sprite();
    			var description:XML = describeType(child);
    			trace(description..accessor.@name.toXMLString());
    		}
    	}
    }

escapeMultiByte| ()| function|   
---|---|---|---  
  
`public function escapeMultiByte(value:[String](../../String.html)):[String](../../String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Returns an escaped copy of the input string encoded as either UTF-8 or system code page, depending on the value of System.useCodePage. Use of System.useCodePage allows legacy content encoded in local code pages to be accessed by the runtime, but only on systems using that legacy code page. For example, Japanese data encoded as `Shift-JIS` will only be escaped and unescaped properly on an OS using a Japanese default code page. 

Parameters | `value:[String](../../String.html)` — The string to be escaped.   
---|---  
  
Returns | `[String](../../String.html)` — An escaped copy of the input string. If System.useCodePage is `true`, the escaped string is encoded in the system code page. If System.useCodePage is `false`, the escaped string is encoded in UTF-8. For example, the input string "Crüe" will be escaped as "Cr%C3%BCe" on all systems if System.useCodePage is `false`. If system.useCodePage is `true`, and the system uses a Latin code page, "Crüe" will be escaped as "Cr%FCe". If the system uses a non Latin code page that does not contain the letter 'ü' the result will probably be "Cr?e". Unescaping "Cr%C3%BCe" with System.useCodePage set to `true` will produce different undesired results on different systems, such as "Crüe" on a Latin system. Similarly, unescaping "Cr%FCe" with System.useCodePage set to `false` could produce "Cre" or "Cr?e" or other variations depending on the code page of the system.   
---|---  
  
getDefinitionByName| ()| function|   
---|---|---|---  
  
`public function getDefinitionByName(name:[String](../../String.html)):[Object](../../Object.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Returns a reference to the class object of the class specified by the `name` parameter. 

Parameters | `name:[String](../../String.html)` — The name of a class.   
---|---  
  
Returns | `[Object](../../Object.html)` — Returns a reference to the class object of the class specified by the `name` parameter.   
---|---  
  
Throws | `[ReferenceError](../../ReferenceError.html) ` — No public definition exists with the specified name.   
---|---  
  
Example   
The following example uses the class `GetDefinitionByNameExample` to create an orange square on the stage. This is accomplished using the following steps: 

  1. Variables for the background color of orange and size of 80 pixels are declared, which will later be used in drawing the square.
  2. Within the constructor, a variable `ClassReference` of type Class is assigned to Sprite.
  3. An instance of ClassReference called `instance` is instantiated.
  4. Since `instance` is, by reference, a Sprite object, a square can be drawn and added to the display list using the methods available to Sprite.

    
    
    package {
    	import flash.display.DisplayObject;
    	import flash.display.Sprite;
    	import flash.utils.getDefinitionByName;
    
    	public class GetDefinitionByNameExample extends Sprite {
    		private var bgColor:uint = 0xFFCC00;
    		private var size:uint = 80;
    
    		public function GetDefinitionByNameExample() {
    			var ClassReference:Class = getDefinitionByName("flash.display.Sprite") as Class;
    			var instance:Object = new ClassReference();
    			instance.graphics.beginFill(bgColor);
    			instance.graphics.drawRect(0, 0, size, size);
    			instance.graphics.endFill();
    			addChild(DisplayObject(instance));
    		}
    	}
    }

getQualifiedClassName| ()| function|   
---|---|---|---  
  
`public function getQualifiedClassName(value:[*](../../specialTypes.html#*)):[String](../../String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Returns the fully qualified class name of an object. 

Parameters | `value:[*](../../specialTypes.html#*)` — The object for which a fully qualified class name is desired. Any ActionScript value may be passed to this method including all available ActionScript types, object instances, primitive types such as uint, and class objects.   
---|---  
  
Returns | `[String](../../String.html)` — A string containing the fully qualified class name.   
---|---  
  
See also

[describeType()](package.html#describeType\(\))   
[getQualifiedSuperclassName()](package.html#getQualifiedSuperclassName\(\))

getQualifiedSuperclassName| ()| function|   
---|---|---|---  
  
`public function getQualifiedSuperclassName(value:[*](../../specialTypes.html#*)):[String](../../String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Returns the fully qualified class name of the base class of the object specified by the `value` parameter. This function provides a quicker way of retrieving the base class name than `describeType()`, but also doesn't provide all the information `describeType()` does. 

After you retrieve the name of a class with this function, you can convert the class name to a class reference with the `getDefinitionByName()` function.

**Note:** This function restricts itself to instance hierarchies, whereas the `describeType()` function uses class object hierarchies if the `value` parameter is a data type. Calling `describeType()` on a data type returns the superclass based on the class object hierarchy, in which all class objects inherit from Class. The `getQualifiedSuperclassName()` function, however, ignores the class object hierarchy and returns the superclass based on the more familiar instance hierarchy. For example, calling `getQualifiedSuperclassName(String)` returns `Object` although technically the String class object inherits from Class. In other words, the results are the same whether you use an instance of a type or the type itself.

Parameters | `value:[*](../../specialTypes.html#*)` — Any value.   
---|---  
  
Returns | `[String](../../String.html)` — A fully qualified base class name, or `null` if none exists.   
---|---  
  
See also

[describeType()](package.html#describeType\(\))   
[getDefinitionByName()](package.html#getDefinitionByName\(\))   
[getQualifiedClassName()](package.html#getQualifiedClassName\(\))

getTimer| ()| function|   
---|---|---|---  
  
`public function getTimer():[int](../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Used to compute relative time. For a Flash runtime processing ActionScript 3.0, this method returns the number of milliseconds that have elapsed since the Flash runtime virtual machine for ActionScript 3.0 (AVM2) started. For a Flash runtime processing ActionScript 2.0, this method returns the number of milliseconds since the Flash runtime began initialization. Flash runtimes use two virtual machines to process ActionScript. AVM1 is the ActionScript virtual machine used to run ActionScript 1.0 and 2.0. AVM2 is the ActionScript virtual machine used to run ActionScript 3.0. The `getTimer()` method behavior for AVM1 is different than the behavior for AVM2. 

For a calendar date (timestamp), see the Date object.

Returns | `[int](../../int.html)` — The number of milliseconds since the runtime was initialized (while processing ActionScript 2.0), or since the virtual machine started (while processing ActionScript 3.0). If the runtime starts playing one SWF file, and another SWF file is loaded later, the return value is relative to when the first SWF file was loaded.   
---|---  
  
See also

[flash.display.AVM1Movie](../display/AVM1Movie.html)   
[Date class](../../Date.html)

  
Example   
The following example uses the class `GetTimerExample` to get and print the number of milliseconds since the runtime initialized. 
    
    
    package {
        import flash.utils.getTimer;
    	import flash.display.Sprite;
    
    	public class GetTimerExample extends Sprite {
    		public function GetTimerExample() {
    			var duration:uint = getTimer();
    			trace("duration: " + duration);
    		}
    	}
    }

setInterval| ()| function|   
---|---|---|---  
  
`public function setInterval(closure:[Function](../../Function.html), delay:[Number](../../Number.html), [...](../../statements.html#..._\(rest\)_parameter) arguments):[uint](../../uint.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Runs a function at a specified interval (in milliseconds). 

Instead of using the `setInterval()` method, consider creating a Timer object, with the specified interval, using 0 as the `repeatCount` parameter (which sets the timer to repeat indefinitely).

If you intend to use the `clearInterval()` method to cancel the `setInterval()` call, be sure to assign the `setInterval()` call to a variable (which the `clearInterval()` function will later reference). If you do not call the `clearInterval()` function to cancel the `setInterval()` call, the object containing the set timeout closure function will not be garbage collected. 

Parameters | `closure:[Function](../../Function.html)` — The name of the function to execute. Do not include quotation marks or parentheses, and do not specify parameters of the function to call. For example, use `functionName`, not `functionName()` or `functionName(param)`.   
---|---  
| `delay:[Number](../../Number.html)` — The interval, in milliseconds.   
| `[...](../../statements.html#..._\(rest\)_parameter) arguments` — An optional list of arguments that are passed to the closure function.   
  
Returns | `[uint](../../uint.html)` — Unique numeric identifier for the timed process. Use this identifier to cancel the process, by calling the `clearInterval()` method.   
---|---  
  
See also

[clearInterval()](package.html#clearInterval\(\))

  
Example   
The following example uses the `setInterval()` method to create a timed interval, calling the `myRepeatingFunction()` method after regular intervals of one second. 
    
    
    package {
        import flash.display.Sprite;
        import flash.utils.*;
    
        public class SetIntervalExample extends Sprite {
    		private var intervalDuration:Number = 1000; // duration between intervals, in milliseconds
    		
            public function SetIntervalExample() {
    			var intervalId:uint = setInterval(myRepeatingFunction, intervalDuration, "Hello", "World");
            }
    
            public function myRepeatingFunction():void {
                trace(arguments[0] + " " + arguments[1]);
            }
        }
    }

setTimeout| ()| function|   
---|---|---|---  
  
`public function setTimeout(closure:[Function](../../Function.html), delay:[Number](../../Number.html), [...](../../statements.html#..._\(rest\)_parameter) arguments):[uint](../../uint.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Runs a specified function after a specified delay (in milliseconds). 

Instead of using this method, consider creating a Timer object, with the specified interval, using 1 as the `repeatCount` parameter (which sets the timer to run only once).

If you intend to use the `clearTimeout()` method to cancel the `setTimeout()` call, be sure to assign the `setTimeout()` call to a variable (which the `clearTimeout()` function will later reference). If you do not call the `clearTimeout()` function to cancel the `setTimeout()` call, the object containing the set timeout closure function will not be garbage collected. 

Parameters | `closure:[Function](../../Function.html)` — The name of the function to execute. Do not include quotation marks or parentheses, and do not specify parameters of the function to call. For example, use `functionName`, not `functionName()` or `functionName(param)`.   
---|---  
| `delay:[Number](../../Number.html)` — The delay, in milliseconds, until the function is executed.   
| `[...](../../statements.html#..._\(rest\)_parameter) arguments` — An optional list of arguments that are passed to the closure function.   
  
Returns | `[uint](../../uint.html)` — Unique numeric identifier for the timed process. Use this identifier to cancel the process, by calling the `clearTimeout()` method.   
---|---  
  
See also

[clearTimeout()](package.html#clearTimeout\(\))

  
Example   
The following example uses the `setTimeout()` method to call another method following a specified delay period. 
    
    
    package {
        import flash.display.Sprite;
        import flash.utils.*;
    
        public class SetTimeoutExample extends Sprite {
    		private var delay:Number = 1000; // delay before calling myDelayedFunction
    		
            public function SetTimeoutExample() {
    			var intervalId:uint = setTimeout(myDelayedFunction, delay, "Hello", "World");
            }
    
            public function myDelayedFunction():void {
                trace(arguments[0] + " " + arguments[1]);
            }
        }
    }

unescapeMultiByte| ()| function|   
---|---|---|---  
  
`public function unescapeMultiByte(value:[String](../../String.html)):[String](../../String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Returns an unescaped copy of the input string, which is decoded from either system code page page or UTF-8 depending on the value of System.useCodePage. Use of System.useCodePage allows legacy content encoded in local code pages to be accessed by the runtime, but only on systems using that legacy code page. For example, Japanese data encoded as `Shift-JIS` will only be escaped and unescaped properly on an OS using a Japanese default code page. 

Parameters | `value:[String](../../String.html)` — The escaped string to be unescaped.   
---|---  
  
Returns | `[String](../../String.html)` — An unescaped copy of the input string. If System.useCodePage is `true`, the escaped string is decoded from the system code page. If System.useCodePage is `false`, the escaped string is decoded from UTF-8. For example, if the input string is "Crüe" and System.useCodePage is `false`, the result will be "Crüe" on all systems. If System.useCodePage is `true` and the input string is "Cr%FCe", and the system uses a Latin code page, the result will also be "Crüe". Unescaping "Cr%C3%BCe" with System.useCodePage set to `true` will produce different undesired results on different systems, such as "CrÃ¼e" on a Latin system. Similarly, unescaping "Cr%FCe" with System.useCodePage set to `false` could produce "Cre" or "Cr?e" or other variations depending on the code page of the system.   
---|---  
  
[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:12 PM GMT+01:00\) : Package flash.utils)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)