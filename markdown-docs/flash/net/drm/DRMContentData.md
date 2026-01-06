# Drmcontentdata

Package| [flash.net.drm](package-detail.html)  
---|---  
Class| public class DRMContentData  
Inheritance| DRMContentData ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The DRMContentData class provides the information required to obtain the voucher necessary to view DRM-protected content. 

(AIR only) A DRMContentData object can be obtained from a NetStream instance by calling the NetStream `preloadEmbeddedContent()` method and providing an `onDRMContentData` callback function on the NetStream client object. Use the DRMContentData object passed to the callback function as a parameter for the DRMManager `loadVoucher()` method.

When you package content with Flash Access, you have the option of saving the content's metadata as a separate file. To create a new DRMContentData object, get this metadata with a URLLoader object and pass it to the DRMContentData constructor.

See also

[flash.net.NetStream](../../net/NetStream.html)   
[flash.net.drm.DRMManager](../drm/DRMManager.html)   
[flash.net.drm.DRMVoucher](../drm/DRMVoucher.html)

  

* * *