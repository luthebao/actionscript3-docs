# Array

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class Array  
Inheritance| Array ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Array class lets you access and manipulate arrays. Array indices are zero-based, which means that the first element in the array is `[0]`, the second element is `[1]`, and so on. To create an Array object, you use the `new Array()` constructor . `Array()` can also be invoked as a function. In addition, you can use the array access (`[]`) operator to initialize an array or access the elements of an array. 

You can store a wide variety of data types in an array element, including numbers, strings, objects, and even other arrays. You can create a _multidimensional_ array by creating an indexed array and assigning to each of its elements a different indexed array. Such an array is considered multidimensional because it can be used to represent data in a table.

Arrays are _sparse arrays_ , meaning there might be an element at index 0 and another at index 5, but nothing in the index positions between those two elements. In such a case, the elements in positions 1 through 4 are undefined, which indicates the absence of an element, not necessarily the presence of an element with the value `undefined`.

Array assignment is by reference rather than by value. When you assign one array variable to another array variable, both refer to the same array:
    
    
    
     var oneArray:Array = new Array("a", "b", "c");
    
     var twoArray:Array = oneArray; // Both array variables refer to the same array.
    
     twoArray[0] = "z";             
    
     trace(oneArray);               // Output: z,b,c.
    
     

Do not use the Array class to create _associative arrays_ (also called _hashes_), which are data structures that contain named elements instead of numbered elements. To create associative arrays, use the Object class. Although ActionScript permits you to create associative arrays using the Array class, you cannot use any of the Array class methods or properties with associative arrays. 

You can extend the Array class and override or add methods. However, you must specify the subclass as `dynamic` or you will lose the ability to store data in an array.

[View the examples.](#includeExamplesSummary)

See also

[[] (array access)](operators.html#array_access)   
[Object class](Object.html)

  

* * *