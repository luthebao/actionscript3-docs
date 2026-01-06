# ActionScript 3.0 Basics

## Overview
ActionScript 3.0 is an object-oriented programming language for Adobe Flash, AIR, and related platforms. This skill provides core ActionScript concepts and patterns.

## Language Fundamentals

### Variable Declaration
```actionscript
// Typed variables (preferred)
var myString:String = "Hello";
var myNumber:Number = 42;
var myInt:int = 10;
var myUint:uint = 20;
var myBoolean:Boolean = true;

// Untyped (avoid in production)
var myVar:* = "anything";
```

### Data Types
- **String**: Text data, immutable
- **Number**: Double-precision floating point
- **int**: 32-bit signed integer (-2,147,483,648 to 2,147,483,647)
- **uint**: 32-bit unsigned integer (0 to 4,294,967,295)
- **Boolean**: true or false
- **Array**: Indexed collection (zero-based)
- **Object**: Key-value pairs (associative array)
- **Vector**: Typed array (Vector.<Type>)

### Constants
```actionscript
const MAX_SIZE:int = 100;
const API_KEY:String = "abc123";
```

### Functions
```actionscript
// Function declaration
function greet(name:String):String {
    return "Hello, " + name;
}

// Function with default parameters
function calculate(x:int, y:int = 10):int {
    return x + y;
}

// Rest parameters
function sum(...numbers):Number {
    var total:Number = 0;
    for each (var num:Number in numbers) {
        total += num;
    }
    return total;
}
```

## Object-Oriented Programming

### Class Definition
```actionscript
package com.example {
    public class Person {
        // Properties
        private var _name:String;
        private var _age:int;
        
        // Constructor
        public function Person(name:String, age:int) {
            _name = name;
            _age = age;
        }
        
        // Getter
        public function get name():String {
            return _name;
        }
        
        // Setter
        public function set name(value:String):void {
            _name = value;
        }
        
        // Method
        public function introduce():String {
            return "I'm " + _name + ", " + _age + " years old";
        }
    }
}
```

### Inheritance
```actionscript
package com.example {
    public class Employee extends Person {
        private var _employeeId:String;
        
        public function Employee(name:String, age:int, id:String) {
            super(name, age);
            _employeeId = id;
        }
        
        override public function introduce():String {
            return super.introduce() + ", ID: " + _employeeId;
        }
    }
}
```

### Interfaces
```actionscript
package com.example {
    public interface IDrawable {
        function draw():void;
        function get color():uint;
        function set color(value:uint):void;
    }
}

// Implementation
public class Circle implements IDrawable {
    private var _color:uint;
    
    public function draw():void {
        // Drawing logic
    }
    
    public function get color():uint {
        return _color;
    }
    
    public function set color(value:uint):void {
        _color = value;
    }
}
```

## Common Patterns

### Event Handling
```actionscript
import flash.events.Event;
import flash.events.EventDispatcher;

// Add event listener
button.addEventListener(MouseEvent.CLICK, onButtonClick);

function onButtonClick(event:MouseEvent):void {
    trace("Button clicked!");
}

// Remove event listener
button.removeEventListener(MouseEvent.CLICK, onButtonClick);
```

### Error Handling
```actionscript
try {
    // Code that might throw an error
    var result:Number = riskyOperation();
} catch (error:TypeError) {
    trace("Type error:", error.message);
} catch (error:Error) {
    trace("General error:", error.message);
} finally {
    // Always executes
    cleanup();
}
```

### Null Safety
```actionscript
// Check for null/undefined
if (myObject != null) {
    myObject.doSomething();
}

// Default values
var value:String = input || "default";
```

## Best Practices

1. **Always use type annotations** - Catches errors at compile time
2. **Use const for constants** - Prevents accidental reassignment
3. **Prefer Vector over Array** - Better performance for typed collections
4. **Use strict equality** - `===` and `!==` for comparisons
5. **Avoid using Object for associative arrays** - Use Dictionary instead
6. **Make properties private with getters/setters** - Better encapsulation
7. **Use package structure** - Organize code logically
8. **Dispose of event listeners** - Prevent memory leaks
9. **Use meaningful variable names** - camelCase for variables, PascalCase for classes
10. **Comment complex logic** - But prefer self-documenting code

## Common Gotchas

1. **Array assignment is by reference**
   ```actionscript
   var arr1:Array = [1, 2, 3];
   var arr2:Array = arr1;  // Same reference!
   arr2[0] = 99;
   trace(arr1[0]);  // 99
   ```

2. **Strings starting with 0 are decimal in parseInt()**
   ```actionscript
   parseInt("010");      // 10, not 8
   parseInt("010", 8);   // 8 (specify octal)
   ```

3. **undefined vs null**
   ```actionscript
   var s:String = undefined;  // Actually becomes null
   var obj:* = undefined;     // Can be undefined
   ```

4. **Dynamic class properties**
   ```actionscript
   public dynamic class MyClass {
       // Can add properties at runtime
   }
   ```
