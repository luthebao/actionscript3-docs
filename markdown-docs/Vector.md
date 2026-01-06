# Vector

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class Vector  
Inheritance| Vector ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The Vector class lets you access and manipulate a vector — an array whose elements all have the same data type. The data type of a Vector's elements is known as the Vector's _base type_. The base type can be any class, including built in classes and custom classes. The base type is specified when declaring a Vector variable as well as when creating an instance by calling the class constructor. 

As with an Array, you can use the array access operator (`[]`) to set or retrieve the value of a Vector element. Several Vector methods also provide mechanisms for setting and retrieving element values. These include `push()`, `pop()`, `shift()`, `unshift()`, and others. The properties and methods of a Vector object are similar — in most cases identical — to the properties and methods of an Array. In most cases where you would use an Array in which all the elements have the same data type, a Vector instance is preferable. However, Vector instances are dense arrays, meaning it must have a value (or `null`) in each index. Array instances don't have this same restriction.

The Vector's base type is specified using postfix type parameter syntax. Type parameter syntax is a sequence consisting of a dot (`.`), left angle bracket (`<`), class name, then a right angle bracket (`>`), as shown in this example:

In the first line of the example, the variable `v` is declared as a Vector.<String> instance. In other words, it represents a Vector (an array) that can only hold String instances and from which only String instances can be retrieved. The second line constructs an instance of the same Vector type (that is, a Vector whose elements are all String objects) and assigns it to `v`.
    
    
     var v:Vector.<String>;
     v = new Vector.<String>();
     

Use brackets to define a vector's base type when calling the Vector constructor function. The string included in the brackets is a sequence consisting of a left angle bracket (`<`), the base class name, then a right angle bracket (`>`), as shown in this example:
    
    
     var v = new air.Vector["<String>"]();
     

To add items to a Vector, you can use the `push()` method. For example, the following code adds content to a Vector of String objects:
    
    
     var v = new air.Vector["<String>"]();
     v.push("a", "b", "c");
     

In this API reference for AIR HTML developers, properties that are defined as Vector types are listed using `Vector.<T>` syntax. In this syntax, `T` represents the data type of the elements in the Vector. For example, the NativeProcessStartupInfo class includes an `arguments` property. The API reference lists this property as having the type `Vector.<String>`, meaning that the property is a Vector containing String objects. Other references to Vector objects in this documentation also uses this syntax, which is used in ActionScript 3.0.

A variable declared with the Vector.<T> data type can only store a Vector instance that is constructed with the same base type `T`. For example, a Vector that's constructed by calling `new Vector.<String>()` can't be assigned to a variable that's declared with the Vector.<int> data type. The base types must match exactly. For example, the following code doesn't compile because the object's base type isn't the same as the variable's declared base type (even though Sprite is a subclass of DisplayObject):
    
    
     // This code doesn't compile even though Sprite is a DisplayObject subclass
     var v:Vector.<DisplayObject> = new Vector.<Sprite>();
     

To convert a Vector with base type `T` to a Vector of a superclass of `T`, use the `Vector()` global function.

In addition to the data type restriction, the Vector class has other restrictions that distinguish it from the Array class:

  * A Vector is a dense array. Unlike an Array, which may have values in indices 0 and 7 even if there are no values in positions 1 through 6, a Vector must have a value (or `null`) in each index.
  * A Vector can optionally be fixed-length, meaning the number of elements it contains can't change.
  * Access to a Vector's elements is bounds-checked. You can never read a value from an index greater than the final element (`length - 1`). You can never set a value with an index more than one beyond the current final index (in other words, you can only set a value at an existing index or at index `[length]`).

As a result of its restrictions, a Vector has three primary benefits over an Array instance whose elements are all instances of a single class:

  * Performance: array element access and iteration are much faster when using a Vector instance than they are when using an Array.
  * Type safety: in strict mode the compiler can identify data type errors. Examples of data type errors include assigning a value of the incorrect data type to a Vector or expecting the wrong data type when reading a value from a Vector. Note, however, that when using the `push()` method or `unshift()` method to add values to a Vector, the arguments' data types are not checked at compile time. Instead, they are checked at run time.
  * Reliability: runtime range checking (or fixed-length checking) increases reliability significantly over Arrays.

See also

[[] array access](operators.html#array_access)   
[Vector() global function](package.html#Vector\(\))   
[Array class](Array.html)

  

* * *