# Sqlerrorevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class SQLErrorEvent  
Inheritance| SQLErrorEvent ![Inheritance](../../images/inherit-arrow.gif) [ErrorEvent](ErrorEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [TextEvent](TextEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLErrorEvent instance is dispatched by a SQLConnection instance or SQLStatement instance when an error occurs while performing a database operation in asynchronous execution mode. The SQLErrorEvent instance that's passed as an event object to listeners provides access to information about the cause of the error and the operation that was being attempted. 

The specific details of the failure can be found on the SQLError object in the SQLErrorEvent instance's `error` property.

See also

[flash.errors.SQLError](../errors/SQLError.html)   
[flash.data.SQLConnection](../data/SQLConnection.html)   
[flash.data.SQLStatement](../data/SQLStatement.html)

  

* * *