# Json

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class JSON  
Inheritance| JSON ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.0   
---|---  
  
The JSON class lets applications import and export data using JavaScript Object Notation (JSON) format. JSON is an industry-standard data interchange format that is described at <http://www.json.org>. 

As a rule, the ActionScript JSON class adheres to the ECMA-262 specification. The following exceptions occur where ActionScript provides greater flexibility than ECMAScript:

  * Unlike ECMAScript, the ActionScript JSON class encodes the following primitives data types as well as the objects that wrap them:

Primitive type| Wrapper class  
---|---  
string| String  
number| Number  
boolean| Boolean  
  * **`parse()` method:** When the argument passed to the `reviver` parameter is not a function, ActionScript throws a TypeError with error ID `kJSONInvalidReviver`. It also posts a localized error message.

  * **`stringify()` method:** When the argument passed to the `replacer` parameter is neither an array or a function, ActionScript throws a TypeError with error ID `kJSONInvalidReplacer`. It also posts a localized error message.

  * **`stringify()` method:** When the argument passed to the `space` parameter is not a String or a Number, it is converted to a String. This string serves as the gap in the output. ECMA-262 requires the gap to be an empty string.

  * **`stringify()` method:** When the code encounters a cyclic structure, it throws a TypeError with error ID `kJSONCyclicStructure`. It also posts a localized error message.

  * ECMA-262 specifies that JSON stringification enumerates the "own properties" of an object, meaning the object's dynamic properties. Because ActionScript classes can also declare fixed properties, the ActionScript `stringify()` method enumerates both dynamic properties and public non-transient properties on ActionScript objects. These properties include properties accessed by getters as well as properties accessed directly.

For most ActionScript classes, the ActionScript `JSON.stringify()` method generates a default encoding. ActionScript classes can change this encoding by defining a `toJSON()` method in the class or its prototype. For a few ActionScript classes, the default JSON encoding is inappropriate. These classes provide a trivial, overridable implementation of `toJSON()` that returns the value described in the following table. You can override or redefine the `toJSON()` methods on these classes if you require a specific behavior. The following table describes these exceptions:

Class| Comments  
---|---  
ByteArray| Overridable `toJSON()` method returns the string "ByteArray".  
Dictionary| Overridable `toJSON()` method returns the string "Dictionary".  
Date| Overridable `toJSON()` method returns `Date.toString()`. This exception guarantees that the ActionScript Date constructor can parse the JSON string.  
XML| Overridable `toJSON()` method returns the string "XML".  
  
[View the examples.](#includeExamplesSummary)

  

* * *