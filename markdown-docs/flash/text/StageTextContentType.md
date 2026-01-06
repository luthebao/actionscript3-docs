# Stagetextcontenttype

Package| [flash.text](package-detail.html)  
---|---  
Class| public final class StageTextContentType  
Inheritance| StageTextContentType ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 51.0   
---|---  
  
The StageTextContentType class defines the content type/hint that is provided to mobile operating systems when using a StageText text input control. The behaviour will be different on the different platforms - for example on Android this is primarily used as a hint to an auto-fill service, whereas on iPhoneOS this can change the type/behaviour of the keyboard. One of the key uses is the `SMS_OTP` value which can be used to bring a one-time password from a text message into the text field. The appropriate value here should be set on the `StageText.contentType` property. 

  

* * *