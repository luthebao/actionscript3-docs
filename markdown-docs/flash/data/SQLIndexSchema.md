# Sqlindexschema

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLIndexSchema  
Inheritance| SQLIndexSchema ![Inheritance](../../images/inherit-arrow.gif) [SQLSchema](SQLSchema.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLIndexSchema instance provides information describing a specific index in a database. The available information includes the name of the associated table (the `table` property), the SQL statement used to create the index (the `sql` property), and the name of the index (the `name` property). 

To obtain index schema information for a database, use the `SQLConnection.loadSchema()` method to load the schema information, making certain to use `null` or `SQLIndexSchema` for the `type` argument's value. In the resulting SQLSchemaResult instance, the `indices` property contains an array of SQLIndexSchema instances representing the indices in the database.

Generally, developer code does not construct SQLIndexSchema instances directly.

See also

[flash.data.SQLConnection.loadSchema()](../data/SQLConnection.html#loadSchema\(\))

  

* * *