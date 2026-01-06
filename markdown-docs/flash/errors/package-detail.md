# Package Detail

The flash.error package contains error classes that are part of the Flash Player Application Programming Interface (API), rather than part of the ActionScript core language. 

The ActionScript core language is the part of the language that complies with the ECMAScript standard. The Flash Player API is the part of the language that is specific to ActionScript. The flash.error package relates to Flash Player specific functionality (Flash Player API). 

The error classes that are not part of the flash.error package are top level core classes that are based on the ECMAScript standard. 

**Note** : In ActionScript 3.0, exceptions are the primary mechanism for reporting runtime errors. Error events are a secondary mechanism that are used when errors are encountered during an asynchronous operation, such as a call to the `Loader.load()` method.

  

* * *

Classes

| Class| Description  
---|---|---  
| [DRMManagerError](DRMManagerError.html)|  The DRMManager dispatches a DRMManagerError event to report errors.  
| [InvalidSWFError](InvalidSWFError.html)|  The Flash runtimes throw this exception when they encounter a corrupted SWF file.  
| [PermissionError](PermissionError.html)|  Permission error is dispatched when the application tries to access a resource without requesting appropriate permissions.  
| [ScriptTimeoutError](ScriptTimeoutError.html)|  The ScriptTimeoutError exception is thrown when the script timeout interval is reached.  
| [SQLError](SQLError.html)|  A SQLError instance provides detailed information about a failed operation.  
| [SQLErrorOperation](SQLErrorOperation.html)|  This class contains the constants that represent the possible values for the `SQLError.operation` property.  
| [StackOverflowError](StackOverflowError.html)|  ActionScript throws a StackOverflowError exception when the stack available to the script is exhausted.  
  
© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Jul 3 2024, 9:16 AM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)