# Sqlschema

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLSchema  
Inheritance| SQLSchema ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [SQLIndexSchema](../data/SQLIndexSchema.html), [SQLTableSchema](../data/SQLTableSchema.html), [SQLTriggerSchema](../data/SQLTriggerSchema.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The SQLSchema class is the base class for schema information for database objects such as tables, views, and indices. 

To obtain schema information for a database, use the `SQLConnection.loadSchema()` method to load the schema information. The resulting SQLSchemaResult instance contains arrays of instances representing the objects in the database.

Generally, developer code does not construct SQLSchema instances directly.

See also

[flash.data.SQLConnection.loadSchema()](../data/SQLConnection.html#loadSchema\(\))

  

* * *