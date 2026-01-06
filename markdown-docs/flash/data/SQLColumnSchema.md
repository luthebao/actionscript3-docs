# Sqlcolumnschema

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLColumnSchema  
Inheritance| SQLColumnSchema ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The SQLColumnSchema class provides information describing the characteristics of a specific column within a table in a database. 

To obtain column schema information for one or more tables in a database, use the `SQLConnection.loadSchema()` method to load the schema information, making certain to use `true` for the `includeColumnSchema` argument's value. In the resulting SQLSchemaResult instance, each table and view definition includes a `columns` property — an array of SQLColumnSchema instances representing the columns in the table or view.

Generally, developer code does not construct SQLColumnSchema instances directly.

See also

[flash.data.SQLConnection.loadSchema()](../data/SQLConnection.html#loadSchema\(\))   
[flash.data.SQLTableSchema](../data/SQLTableSchema.html)   
[flash.data.SQLViewSchema](../data/SQLViewSchema.html)

  

* * *