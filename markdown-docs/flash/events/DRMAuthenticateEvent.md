# Drmauthenticateevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class DRMAuthenticateEvent  
Inheritance| DRMAuthenticateEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A NetStream object dispatchs a DRMAuthenticateEvent object when attempting to play digital rights management (DRM) encrypted content that requires a user credential for authentication. 

The DRMAuthenticateEvent handler is responsible for gathering the required credentials (such as the user name, password, and type) and passing the values to the `NetStream.setDRMAuthenticationCredentials()` method for authentication. Each AIR application must provide some mechanism for obtaining user credentials. For example, the application could provide a user with a simple user interface to enter the username and password values, and optionally the type value as well. 

If user authentication failed, the application will retry authentication and dispatch a new DRMAuthenticateEvent event for the NetStream object. 

[View the examples.](#includeExamplesSummary)

See also

[DRMAuthenticateEvent.DRM_AUTHENTICATE](DRMAuthenticateEvent.html#DRM_AUTHENTICATE)   
[flash.net.drm.DRMManager](../net/drm/DRMManager.html)

  

* * *