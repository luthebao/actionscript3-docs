# Sqltableschema

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLTableSchema  
Inheritance| SQLTableSchema ![Inheritance](../../images/inherit-arrow.gif) [SQLSchema](SQLSchema.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [SQLViewSchema](../data/SQLViewSchema.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLTableSchema instance provides information describing a specific table in a database. It contains the name of the table (the `name` property), the SQL statement used to create the table (the `sql` property), and information about the table's columns (the `columns` property). 

To obtain table schema information for a database, use the `SQLConnection.loadSchema()` method to load the schema information, making certain to use `null` or `SQLTableSchema` for the `type` argument's value. In the resulting SQLSchemaResult instance, the `tables` property contains an array of SQLTableSchema instances representing the tables in the database.

Generally, developer code does not construct SQLTableSchema instances directly.

See also

[flash.data.SQLConnection.loadSchema()](../data/SQLConnection.html#loadSchema\(\))   
[flash.data.SQLColumnSchema](../data/SQLColumnSchema.html)

  

* * *