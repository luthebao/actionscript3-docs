# Scripttimeouterror

Package| [flash.errors](package-detail.html)  
---|---  
Class| public dynamic class ScriptTimeoutError  
Inheritance| ScriptTimeoutError ![Inheritance](../../images/inherit-arrow.gif) [Error](../../Error.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The ScriptTimeoutError exception is thrown when the script timeout interval is reached. The script timeout interval is 15 seconds. There are two XML attributes that you can add to the `mx:Application` tag: `scriptTimeLimit` (the number of seconds until script timeout) and `scriptRecursionLimit` (the depth of recursive calls permitted). 

Two ScriptTimeoutError exceptions are thrown. The first exception you can catch and exit cleanly. If there is no exception handler, the uncaught exception terminates execution. The second exception is thrown but cannot be caught by user code; it goes to the uncaught exception handler. It is uncatchable to prevent the player from hanging indefinitely.

[View the examples.](#includeExamplesSummary)

  

* * *