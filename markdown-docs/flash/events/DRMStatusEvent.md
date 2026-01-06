# Drmstatusevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class DRMStatusEvent  
Inheritance| DRMStatusEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A NetStream object dispatches a DRMStatusEvent object when the content protected using digital rights management (DRM) begins playing successfully (when the voucher is verified, and when the user is authenticated and authorized to view the content). The DRMStatusEvent object contains information related to the voucher, such as whether the content can be made available offline or when the voucher will expire and the content can no longer be viewed. The application can use this data to inform the user of the status of her policy and permissions. 

See also

[flash.net.NetStream](../net/NetStream.html)   
[DRMStatusEvent.DRM_STATUS](DRMStatusEvent.html#DRM_STATUS)   
[flash.net.drm.DRMManager](../net/drm/DRMManager.html)   
[flash.net.drm.DRMVoucher](../net/drm/DRMVoucher.html)

  

* * *