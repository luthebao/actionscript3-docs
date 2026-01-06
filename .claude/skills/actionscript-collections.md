# ActionScript 3.0 Collections and Data Structures

## Overview
This skill covers arrays, vectors, dictionaries, and other collection types in ActionScript 3.0.

## Arrays

### Creating Arrays
```actionscript
// Array literal
var fruits:Array = ["apple", "banana", "orange"];

// Constructor
var numbers:Array = new Array(1, 2, 3, 4, 5);

// Empty array with size
var empty:Array = new Array(10);  // Length 10, all undefined
```

### Array Operations
```actionscript
var arr:Array = [1, 2, 3];

// Add elements
arr.push(4);           // Add to end: [1, 2, 3, 4]
arr.unshift(0);        // Add to start: [0, 1, 2, 3, 4]
arr.splice(2, 0, 1.5); // Insert at index: [0, 1, 1.5, 2, 3, 4]

// Remove elements
var last:* = arr.pop();      // Remove from end
var first:* = arr.shift();   // Remove from start
arr.splice(2, 1);            // Remove 1 element at index 2

// Access elements
var item:* = arr[0];         // First element
var length:int = arr.length; // Array length

// Search
var index:int = arr.indexOf(3);        // Find index
var hasItem:Boolean = arr.includes(3);  // Check existence
```

### Array Methods
```actionscript
var numbers:Array = [1, 2, 3, 4, 5];

// forEach - iterate
numbers.forEach(function(item:*, index:int, array:Array):void {
    trace(index + ": " + item);
});

// map - transform
var doubled:Array = numbers.map(function(n:Number):Number {
    return n * 2;
});

// filter - select subset
var evens:Array = numbers.filter(function(n:Number):Boolean {
    return n % 2 == 0;
});

// reduce - accumulate
var sum:Number = numbers.reduce(function(acc:Number, n:Number):Number {
    return acc + n;
}, 0);

// every - test all
var allPositive:Boolean = numbers.every(function(n:Number):Boolean {
    return n > 0;
});

// some - test any
var hasEven:Boolean = numbers.some(function(n:Number):Boolean {
    return n % 2 == 0;
});
```

### Array Sorting
```actionscript
var names:Array = ["Charlie", "Alice", "Bob"];

// Simple sort
names.sort();  // ["Alice", "Bob", "Charlie"]

// Numeric sort
var nums:Array = [10, 2, 30, 1];
nums.sort(Array.NUMERIC);  // [1, 2, 10, 30]

// Custom sort
nums.sort(function(a:Number, b:Number):int {
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
});

// Sort options
arr.sort(Array.NUMERIC | Array.DESCENDING);
arr.sort(Array.CASEINSENSITIVE);
```

## Vectors (Typed Arrays)

### Creating Vectors
```actionscript
// Type-safe collections
var intVec:Vector.<int> = new Vector.<int>();
var strVec:Vector.<String> = new <String>["a", "b", "c"];

// Fixed-length vector
var fixed:Vector.<Number> = new Vector.<Number>(5, true);
```

### Vector Operations
```actionscript
var vec:Vector.<int> = new <int>[1, 2, 3];

// Add elements
vec.push(4);
vec.unshift(0);

// Access elements
var item:int = vec[0];
var length:uint = vec.length;

// Vector methods (similar to Array)
vec.forEach(callback);
vec.map(callback);
vec.filter(callback);
vec.indexOf(value);
vec.slice(start, end);
vec.splice(start, deleteCount, ...items);
```

### Vector vs Array
```actionscript
// Vector advantages:
// 1. Type safety - compile-time type checking
// 2. Better performance
// 3. Fixed-length option
// 4. Memory efficient

var typed:Vector.<Number> = new Vector.<Number>();
// typed.push("string");  // Compile error!

var untyped:Array = new Array();
untyped.push("string");  // No error, but risky
```

## Dictionaries

### Creating Dictionaries
```actionscript
import flash.utils.Dictionary;

// Standard dictionary
var dict:Dictionary = new Dictionary();

// Weak-key dictionary (for memory management)
var weakDict:Dictionary = new Dictionary(true);
```

### Dictionary Operations
```actionscript
var dict:Dictionary = new Dictionary();

// Add/update entries
dict[key] = value;
dict["name"] = "John";
dict[42] = "number key";

// Objects as keys
var obj:Object = {id: 1};
dict[obj] = "object key";

// Access values
var value:* = dict[key];

// Check existence
if (dict[key] !== undefined) {
    trace("Key exists");
}

// Delete entries
delete dict[key];

// Iterate
for (var key:* in dict) {
    trace(key + ": " + dict[key]);
}
```

## Object as Associative Array

### Basic Usage
```actionscript
var person:Object = {
    name: "John",
    age: 30,
    city: "New York"
};

// Access properties
trace(person.name);      // Dot notation
trace(person["age"]);    // Bracket notation

// Add properties
person.email = "john@example.com";
person["phone"] = "555-1234";

// Check property
if (person.hasOwnProperty("name")) {
    trace("Has name property");
}

// Delete property
delete person.age;

// Iterate
for (var key:String in person) {
    trace(key + ": " + person[key]);
}
```

## Best Practices

### 1. Choose the Right Collection
```actionscript
// Indexed, heterogeneous data → Array
var mixed:Array = [1, "two", {three: 3}];

// Indexed, homogeneous data → Vector
var numbers:Vector.<Number> = new <Number>[1, 2, 3];

// Key-value pairs, string keys → Object
var config:Object = {host: "localhost", port: 8080};

// Key-value pairs, object keys → Dictionary
var cache:Dictionary = new Dictionary();
cache[movieClip] = "cached data";
```

### 2. Array Performance
```actionscript
// Good: Pre-allocate when size is known
var arr:Array = new Array(1000);

// Good: Use Vector for better performance
var vec:Vector.<int> = new Vector.<int>(1000);

// Avoid: Growing array in tight loops
for (var i:int = 0; i < 10000; i++) {
    arr.push(i);  // Repeated reallocation
}
```

### 3. Memory Management
```actionscript
// Use weak dictionaries for caches
var cache:Dictionary = new Dictionary(true);  // Weak references

// Clear references when done
arr.length = 0;  // Clear array
dict = null;     // Clear dictionary
```

### 4. Copying Collections
```actionscript
// Shallow copy
var copy:Array = arr.slice();
var vecCopy:Vector.<int> = vec.slice();

// Deep copy (manual)
function deepCopy(arr:Array):Array {
    var result:Array = [];
    for each (var item:* in arr) {
        if (item is Array) {
            result.push(deepCopy(item));
        } else {
            result.push(item);
        }
    }
    return result;
}
```

### 5. Null Safety
```actionscript
// Check before accessing
if (arr != null && arr.length > 0) {
    var first:* = arr[0];
}

// Default empty collections
function getItems():Array {
    return items || [];  // Never return null
}
```

## Common Patterns

### Array Flattening
```actionscript
function flatten(arr:Array):Array {
    var result:Array = [];
    for each (var item:* in arr) {
        if (item is Array) {
            result = result.concat(flatten(item));
        } else {
            result.push(item);
        }
    }
    return result;
}
```

### Array Unique Values
```actionscript
function unique(arr:Array):Array {
    var dict:Dictionary = new Dictionary();
    var result:Array = [];
    for each (var item:* in arr) {
        if (!dict[item]) {
            dict[item] = true;
            result.push(item);
        }
    }
    return result;
}
```

### Array Grouping
```actionscript
function groupBy(arr:Array, keyFunc:Function):Object {
    var groups:Object = {};
    for each (var item:* in arr) {
        var key:String = keyFunc(item);
        if (!groups[key]) {
            groups[key] = [];
        }
        groups[key].push(item);
    }
    return groups;
}
```
