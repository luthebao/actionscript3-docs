# Sqlschemaresult

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLSchemaResult  
Inheritance| SQLSchemaResult ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLSchemaResult instance contains the information resulting from a call to the `SQLConnection.loadSchema()` method. It contains four Array properties that hold the requested schema data, based on the argument values used when calling `SQLConnection.loadSchema()`. 

To retrieve the SQLSchemaResult instance for a `SQLConnection.loadSchema()` call, call the SQLConnection instance's `getSchemaResult()` method. Generally, developer code does not create SQLSchemaResult instances directly.

See also

[flash.data.SQLConnection.loadSchema()](../data/SQLConnection.html#loadSchema\(\))   
[flash.data.SQLConnection.getSchemaResult()](../data/SQLConnection.html#getSchemaResult\(\))

  

* * *