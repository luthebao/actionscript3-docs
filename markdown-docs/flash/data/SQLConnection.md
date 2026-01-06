# Sqlconnection

Package| [flash.data](package-detail.html)  
---|---  
Class| public class SQLConnection  
Inheritance| SQLConnection ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A SQLConnection instance is used to manage the creation of and connection to local SQL database files (local databases). 

The functionality of the SQLConnection class falls into several categories:

  * A local SQL database file is created or opened by calling the `open()` method or the SQLConnection instance to the SQLStatement's `sqlConnection` property.

  * The SQLConnection class also provides state for SQL statements, including a mechanism for executing multiple statements in a transaction. Transactions are managed using the `begin()`, `commit()`, and `rollback()` methods. In addition, the `setSavepoint()`, `releaseSavepoint()`, and `rollbackToSavepoint()` methods allow code to define and manage savepoints. These are used to subdivide transactions into sets of operations.

  * The SQLConnection class provides access to database schema information for connected databases. A database's schema describes the definitions of its tables, columns, indices, and triggers. See the `loadSchema()` method for more information.

  * The SQLConnection class provides the ability to encrypt databases using AES with CCM. This provides both authentication and privacy for data. To encrypt a database, a 16 byte key (specified using a ByteArray) must be specified when the database is created. This key can later be changed using the `SQLConnection.reencrypt()` method. Encryption imposes a performance penalty on writes to and reads from the database. Encryption is applied to data stored on the disk, but not to a temporary data cache in memory. Encryption is _not_ supported for in-memory databases.

  * A SQLConnection instance can be used to receive database-level event notifications and provide configuration control for all aspects of a database, including cache page size, process canceling, and statement execution options.

A `SQLConnection` instance operates in one of two distinct execution modes: asynchronous and synchronous. To use synchronous execution, you use the `open()` method to connect to the main database for the SQLConnection instance. To use asynchronous execution, use the `openAsync()` method to connect to the main database for the instance.

When you're using asynchronous execution, you use event listeners or a Responder instance to determine when an operation completes or fails. The operations run in the background rather than in the main application thread, so the application continues to run and respond to user interaction even while the database operations are being performed. Each asynchronous SQLConnection instance executes SQL statements in its own thread.

In asynchronous execution mode, you begin a specific operation by calling the appropriate method, and you can detect the completion (or failure) of the operation by registering a listener for the appropriate event. Each operation has an associated event that is dispatched when the operation completes successfully; for example, when an `openAsync()` method call completes successfully (when the database connection is opened) the `open` event is dispatched. When any operation fails, an `error` event is dispatched. The SQLError instance in the SQLErrorEvent object's `error` property contains information about the specific error, including the operation that was being attempted and the reason the operation failed.

When you're using synchronous execution, you do not need to register event listeners to determine when an operation completes or fails. To identify errors, enclose the error-throwing statements in a `try..catch` block. Because synchronous operations execute in the main execution thread, all application functionality (including refreshing the screen and allowing mouse and keyboard interaction) is paused while the database operation or operations are performed. For long-running operations this can cause a noticeable pause in the application.

See also

[flash.data.SQLStatement](../data/SQLStatement.html)   
[flash.events.SQLEvent](../events/SQLEvent.html)   
[flash.events.SQLErrorEvent](../events/SQLErrorEvent.html)   
[flash.errors.SQLError](../errors/SQLError.html)   
[Quick Start: Working asynchronously with a local SQL database (Flex)](http://www.adobe.com/go/learn_air_qs_SQLasynch_en)   
[Quick Start: Working asynchronously with a local SQL database (Flash)](http://www.adobe.com/go/learn_air_qs_SQLasynch_flash_en)   
[Quick Start: Working asynchronously with a local SQL database (HTML)](http://www.adobe.com/go/learn_air_qs_SQLasynch_html_en)   
[Quick Start: Working synchronously with a local SQL database (Flex)](http://www.adobe.com/go/learn_air_qs_SQLsynch_en)   
[Quick Start: Working synchronously with a local SQL database (Flash)](http://www.adobe.com/go/learn_air_qs_SQLsynch_flash_en)   
[Quick Start: Working synchronously with a local SQL database (HTML)](http://www.adobe.com/go/learn_air_qs_SQLsynch_html_en)

  

* * *