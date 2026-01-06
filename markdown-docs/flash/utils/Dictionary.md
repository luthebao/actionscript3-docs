# Dictionary

Package| [flash.utils](package-detail.html)  
---|---  
Class| public dynamic class Dictionary  
Inheritance| Dictionary ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Dictionary class lets you create a dynamic collection of properties, which uses strict equality (`===`) for key comparison. When an object is used as a key, the object's identity is used to look up the object, and not the value returned from calling `toString()` on it. 

The following statements show the relationship between a Dictionary object and a key object:
    
    
    
     var dict = new Dictionary();
    
     var obj = new Object();
    
     var key:Object = new Object();
    
     key.toString = function() { return "key" }
    
     
     dict[key] = "Letters";
    
     obj["key"] = "Letters";
    
     
     dict[key] == "Letters"; // true
    
     obj["key"] == "Letters"; // true
    
     obj[key] == "Letters"; // true because key == "key" is true b/c key.toString == "key"
    
     dict["key"] == "Letters"; // false because "key" === key is false
    
     delete dict[key]; //removes the key
    
     

See also

[=== (strict equality)](../../operators.html#strict_equality)

  

* * *