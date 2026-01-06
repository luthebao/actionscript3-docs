# Sqlerror

Package| [flash.errors](package-detail.html)  
---|---  
Class| public class SQLError  
Inheritance| SQLError ![Inheritance](../../images/inherit-arrow.gif) [Error](../../Error.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLError instance provides detailed information about a failed operation. 

In asynchronous execution mode, when an error occurs with a SQL database operation the SQLConnection or SQLStatement instance dispatches a SQLErrorEvent object. Information about the error in the form of a SQLError instance can be accessed from the SQLErrorEvent object's `error` property.

In synchronous execution mode, when an error occurs with a SQL database operation the SQLConnection or SQLStatement instance throws a SQLError exception, which can be handled by enclosing the error-throwing code in a `try..catch` block.

This class provides properties containing the error details (specifying the specific type of error that occured), a text message containing the details of the error, and the operation that caused the error to occur.

See also

[flash.events.SQLErrorEvent](../events/SQLErrorEvent.html)   
[flash.data.SQLConnection](../data/SQLConnection.html)   
[flash.data.SQLStatement](../data/SQLStatement.html)

  

* * *