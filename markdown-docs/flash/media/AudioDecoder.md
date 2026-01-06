# Audiodecoder

Package| [flash.media](package-detail.html)  
---|---  
Class| public final class AudioDecoder  
Inheritance| AudioDecoder ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The AudioDecoder class enumerates the types of multichannel audio that a system can support. 

Use one of the constants defined in this class as the parameter to the `hasMultiChannelAudio()` method of the Capabilities class.

_AIR profile support:_ Multichannel audio is supported only on AIR for TV devices. On all other devices, `hasMultiChannelAudio()` always returns `false`. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

See also

[Capabilities.hasMultiChannelAudio()](../system/Capabilities.html#hasMultiChannelAudio\(\))

  

* * *