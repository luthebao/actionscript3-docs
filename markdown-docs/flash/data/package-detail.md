# Package Detail

The flash.data package contains classes used for working with Adobe AIR local SQL databases. Adobe AIR includes a SQL database engine that supports the creation and use of local databases from within AIR applications. For information about SQL language and data type support in the runtime, see the appendix [SQL support in local databases](../../localDatabaseSQLSupport.html).

  

* * *

Classes

| Class| Description  
---|---|---  
| [EncryptedLocalStore](EncryptedLocalStore.html)|  The EncryptedLocalStore class (ELS) provides an encrypted local storage mechanism that can be used as a small cache for an application's private data.  
| [SQLCollationType](SQLCollationType.html)|  This class contains the constants that represent the possible values for the `defaultCollationType` parameter of the SQLColumnSchema constructor, as well as the `SQLColumnSchema.defaultCollationType` property.  
| [SQLColumnNameStyle](SQLColumnNameStyle.html)|  This class contains the constants that represent the possible values for the `SQLConnection.columnNameStyle` property.  
| [SQLColumnSchema](SQLColumnSchema.html)|  The SQLColumnSchema class provides information describing the characteristics of a specific column within a table in a database.  
| [SQLConnection](SQLConnection.html)|  A SQLConnection instance is used to manage the creation of and connection to local SQL database files (local databases).  
| [SQLIndexSchema](SQLIndexSchema.html)|  A SQLIndexSchema instance provides information describing a specific index in a database.  
| [SQLMode](SQLMode.html)|  This class contains the constants that represent the possible values for the `openMode` parameter of the `SQLConnection.open()` and `SQLConnection.openAsync()` methods.  
| [SQLResult](SQLResult.html)|  The SQLResult class provides access to data returned in response to the execution of a SQL statement (a SQLStatement instance).  
| [SQLSchema](SQLSchema.html)|  The SQLSchema class is the base class for schema information for database objects such as tables, views, and indices.  
| [SQLSchemaResult](SQLSchemaResult.html)|  A SQLSchemaResult instance contains the information resulting from a call to the `SQLConnection.loadSchema()` method.  
| [SQLStatement](SQLStatement.html)|  A SQLStatement instance is used to execute a SQL statement against a local SQL database that is open through a SQLConnection instance.  
| [SQLTableSchema](SQLTableSchema.html)|  A SQLTableSchema instance provides information describing a specific table in a database.  
| [SQLTransactionLockType](SQLTransactionLockType.html)|  This class contains the constants that represent the possible values for the `option` parameter of the `SQLConnection.begin()` method.  
| [SQLTriggerSchema](SQLTriggerSchema.html)|  A SQLTriggerSchema instance provides information describing a specific trigger in a database.  
| [SQLViewSchema](SQLViewSchema.html)|  A SQLViewSchema instance provides information describing a specific view in a database.  
  
© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)