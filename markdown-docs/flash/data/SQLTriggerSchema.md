# Sqltriggerschema

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLTriggerSchema  
Inheritance| SQLTriggerSchema ![Inheritance](../../images/inherit-arrow.gif) [SQLSchema](SQLSchema.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLTriggerSchema instance provides information describing a specific trigger in a database. It contains the name of the trigger (the `name` property), the name of the associated table (the `table` property), and the SQL statement used to create the trigger (the `sql` property). 

To obtain trigger schema information for a database, use the `SQLConnection.loadSchema()` method to load the schema information, making certain to use `null` or `SQLTriggerSchema` for the `type` argument's value. In the resulting SQLSchemaResult instance, the `triggers` property contains an array of SQLTriggerSchema instances representing the triggers in the database.

Generally, developer code does not construct SQLTriggerSchema instances directly.

See also

[flash.data.SQLConnection.loadSchema()](../data/SQLConnection.html#loadSchema\(\))

  

* * *