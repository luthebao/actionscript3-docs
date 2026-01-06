# Drmdevicegroupevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class DRMDeviceGroupEvent  
Inheritance| DRMDeviceGroupEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.0   
---|---  
  
Issued by the DRMManager when a device group related call successfully completes. Multiple devices can be registered to a device group using the `DRMManager.addToDeviceGroup()` method. If there is a device with a valid domain-bound voucher for a given content, the application can then extract the serialized DRM vouchers using the `DRMVoucher.toByteArray()` method.

If the content metadata specifies that domain registration is required, the application can invoke an API to join the device group. This action triggers a domain registration request to be sent to the domain server. Once a license is issued to a device group, the license can be exported and shared with other devices that have joined the device group.

  

* * *