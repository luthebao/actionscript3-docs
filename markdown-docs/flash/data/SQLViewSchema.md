# Sqlviewschema

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLViewSchema  
Inheritance| SQLViewSchema ![Inheritance](../../images/inherit-arrow.gif) [SQLTableSchema](SQLTableSchema.html) ![Inheritance](../../images/inherit-arrow.gif) [SQLSchema](SQLSchema.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLViewSchema instance provides information describing a specific view in a database. It contains the name of the view (the `name` property), the SQL statement used to create the view (the `sql` property), and information about the view's columns (the `columns` property). 

To obtain view schema information for a database, use the `SQLConnection.loadSchema()` method to load the schema information, making certain to use `null` or `SQLViewSchema` for the `type` argument's value. In the resulting SQLSchemaResult instance, the `views` property contains an array of SQLViewSchema instances representing the views in the database.

Generally, developer code does not construct SQLViewSchema instances directly.

See also

[flash.data.SQLConnection.loadSchema()](../data/SQLConnection.html#loadSchema\(\))   
[flash.data.SQLColumnSchema](../data/SQLColumnSchema.html)

  

* * *