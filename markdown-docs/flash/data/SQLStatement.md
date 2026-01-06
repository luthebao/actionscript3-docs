# Sqlstatement

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLStatement  
Inheritance| SQLStatement ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLStatement instance is used to execute a SQL statement against a local SQL database that is open through a SQLConnection instance. 

A SQLStatement instance is linked to a SQLConnection instance by setting the SQLConnection instance as the value of the SQLStatement instance's `sqlConnection` property. The `text` property is populated with the actual text of the SQL statement to execute. If necessary, SQL statement parameter values are specified using the `parameters` property, and the statement is carried out by calling the `execute()` method.

For a complete description of the SQL dialect supported in local SQL databases, see the appendix [SQL support in local databases](http://adobe.com/go/learn_as3_sqlsupportdb_en).

In asynchronous execution mode, the `execute()` and `next()` methods are executed in the background, and the runtime dispatches events to registered event listeners or to a specified Responder instance when the operations complete or fail. In synchronous mode, the methods are executed on the main application thread, meaning that no other code executes until the database operations are completed. In addition, in synchronous mode if the methods fail the runtime throws an exception rather than dispatching an error event.

See also

[flash.data.SQLConnection](../data/SQLConnection.html)

  

* * *