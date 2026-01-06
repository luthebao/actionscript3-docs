# Permissionmanager

Package| [flash.permissions](package-detail.html)  
---|---  
Class| public final class PermissionManager  
Inheritance| PermissionManager ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 33.1   
---|---  
  
A PermissionManager object provides access to information about operating system permissions for a restricted resource such as camera or microphone. Due to changes in OS security and privacy, this is required to be tested/requested prior to the AIR runtime attempting to find out any information about the resource in question; so relevant classes will provide a PermissionManager as a static class member so that applications can use this without having to first create an instance of the class. Whether permissions has been granted (or isn't needed), or denied, can be checked using the permissionStatus property. If this is 'unknown' then use the requestPermission() method to trigger an OS-specific request to the user. Once the user has responded, a PermissionEvent will be dispatched. 

See also

[flash.media.Camera.permissionManager](../media/Camera.html#permissionManager)   
[flash.media.Microphone.permissionManager](../media/Microphone.html#permissionManager)

  

* * *