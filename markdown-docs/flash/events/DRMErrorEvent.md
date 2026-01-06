# Drmerrorevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class DRMErrorEvent  
Inheritance| DRMErrorEvent ![Inheritance](../../images/inherit-arrow.gif) [ErrorEvent](ErrorEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [TextEvent](TextEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The DRMErrorEvent class provides information about errors that occur when playing digital rights management (DRM) encrypted files. 

The runtime dispatches a DRMErrorEvent object when a NetStream object, trying to play a digital rights management (DRM) encrypted file, encounters a DRM-related error. For example, a DRMErrorEvent object is dispatched when the content provider does not support the viewing application, or when the user authorization fails, possibly because the user has not purchased the content.

In the case of invalid user credentials, the DRMAuthenticateEvent object handles the error by repeatedly dispatching until the user enters valid credentials, or the application denies further attempts. The application should listen to any other DRM error events in order to detect, identify, and handle the DRM-related errors. 

This class provides properties containing the object throwing the exception, the error code, and, where applicable, a suberror code and text message containing information related to the error. For a description of DRM-related error codes, see the [Runtime error codes](../../runtimeErrors.html). The DRM-related error codes start at error 3300. 

[View the examples.](#includeExamplesSummary)

See also

[flash.net.NetStream](../net/NetStream.html)   
[DRMErrorEvent.DRM_ERROR](DRMErrorEvent.html#DRM_ERROR)   
[Runtime error codes](../../runtimeErrors.html)

  

* * *