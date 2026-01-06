# Urlrequestdefaults

Package| [flash.net](package-detail.html)  
---|---  
Class| public class URLRequestDefaults  
Inheritance| URLRequestDefaults ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Runtime version:**|  AIR 1.0   
---|---  
  
The URLRequestDefaults class includes static properties that you can set to define default values for the properties of the URLRequest class. It also includes a static method, `URLRequestDefaults.setLoginCredentialsForHost()`, which lets you define default authentication credentials for requests. The URLRequest class defines the information to use in an HTTP request. 

Any properties set in a URLRequest object override those static properties set for the URLRequestDefaults class.

URLRequestDefault settings only apply to content in the caller's application domain, with one exception: settings made by calling `URLRequestDefaults.setLoginCredentialsForHost()` apply to all application domains in the currently running application.

Only Adobe® AIR® content running in the application security sandbox can use the URLRequestDefaults class. Other content will result in a SecurityError being thrown when accessing the members or properties of this class.

See also

[URLRequest](URLRequest.html)

  

* * *