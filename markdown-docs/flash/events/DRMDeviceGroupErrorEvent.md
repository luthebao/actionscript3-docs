# Drmdevicegrouperrorevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class DRMDeviceGroupErrorEvent  
Inheritance| DRMDeviceGroupErrorEvent ![Inheritance](../../images/inherit-arrow.gif) [ErrorEvent](ErrorEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [TextEvent](TextEvent.html) ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.0   
---|---  
  
Issued by the DRMManager when any error occurs during any device group related calls.

It is the application's responsibility to explicitly handle the error events.These events include cases where the user inputs valid credentials, but the voucher protecting the encrypted content restricts the access to the content. For example, an authenticated user cannot access content if the rights have not been paid for. This error can also occur when two registered members of the same publisher attempt to share content that only one of them has paid for.

  

* * *