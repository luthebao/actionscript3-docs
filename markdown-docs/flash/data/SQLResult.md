# Sqlresult

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLResult  
Inheritance| SQLResult ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The SQLResult class provides access to data returned in response to the execution of a SQL statement (a SQLStatement instance). 

The SQLResult instance for a SQL statement is accessed by calling the `SQLStatement.getResult()` method or as an argument passed to the result handler of a Responder instance specified in a call to `SQLStatement.execute()` or `SQLStatement.next()`. Generally, developer code does not construct SQLResult instances directly.

You use a SQLResult object to access the rows of data returned from a `SELECT` statement (using the `data` property), to get row identifier information for an `INSERT` statement (using the `lastInsertRowID` property), to determine the number of rows affected by an `INSERT`, `UPDATE`, or `DELETE` statement (using the `rowsAffected` property), or to determine whether there are additional `SELECT` result rows that haven't been retrieved (using the `complete` property).

See also

[flash.data.SQLStatement.getResult()](../data/SQLStatement.html#getResult\(\))   
[flash.data.SQLStatement.execute()](../data/SQLStatement.html#execute\(\))   
[flash.data.SQLStatement.next()](../data/SQLStatement.html#next\(\))

  

* * *