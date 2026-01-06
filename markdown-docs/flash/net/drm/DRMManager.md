# Drmmanager

Package| [flash.net.drm](package-detail.html)  
---|---  
Class| public class DRMManager  
Inheritance| DRMManager ![Inheritance](../../../images/inherit-arrow.gif) [EventDispatcher](../../events/EventDispatcher.html) ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The DRMManager manages the retrieval and storage of the vouchers needed to view DRM-protected content. With the static `DRMManager.getDRMManager()` method, you can access the existing DRMManager object to perform the following DRM-management tasks: 

  * Preload vouchers from a media rights server, using a DRMContentData object.
  * Query the local cache for an individual voucher, using a DRMContentData object.
  * Reset all vouchers (AIR only)

No method is provided for enumerating all the vouchers in the local cache.

Do not create an instance of the DRMManager class. Use the static `DRMManager.getDRMManager()` to access the existing DRMManager object.

_AIR profile support:_ This feature is supported on all desktop operating systems and AIR for TV devices, but it is not supported on mobile devices. You can test for support at run time using the `DRMManager.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

See also

[flash.net.NetStream](../../net/NetStream.html)   
[flash.net.drm.DRMVoucher](../drm/DRMVoucher.html)   
[flash.net.drm.DRMContentData](../drm/DRMContentData.html)

  

* * *