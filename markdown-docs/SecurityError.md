# Securityerror

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class SecurityError  
Inheritance| SecurityError ![Inheritance](images/inherit-arrow.gif) [Error](Error.html) ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The `SecurityError` exception is thrown when some type of security violation takes place. 

Examples of security errors:

  * An unauthorized property access or method call is made across a security sandbox boundary.
  * An attempt was made to access a URL not permitted by the security sandbox.
  * A socket connection was attempted to an unauthorized port number, e.g. a port above 65535.
  * An attempt was made to access the user's camera or microphone, and the request to access the device was denied by the user.

[View the examples.](#includeExamplesSummary)

  

* * *