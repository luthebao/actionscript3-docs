# Endian

Package| [flash.utils](package-detail.html)  
---|---  
Class| public final class Endian  
Inheritance| Endian ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Endian class contains values that denote the byte order used to represent multibyte numbers. The byte order is either bigEndian (most significant byte first) or littleEndian (least significant byte first). 

Content in Flash Player or Adobe® AIR™ can interface with a server by using the binary protocol of that server, directly. Some servers use the bigEndian byte order and some servers use the littleEndian byte order. Most servers on the Internet use the bigEndian byte order because "network byte order" is bigEndian. The littleEndian byte order is popular because the Intel x86 architecture uses it. Use the endian byte order that matches the protocol of the server that is sending or receiving data.

See also

[flash.utils.ByteArray.endian](../utils/ByteArray.html#endian)   
[flash.filesystem.FileStream.endian](../filesystem/FileStream.html#endian)   
[flash.utils.IDataInput.endian](../utils/IDataInput.html#endian)   
[flash.utils.IDataOutput.endian](../utils/IDataOutput.html#endian)   
[flash.net.Socket.endian](../net/Socket.html#endian)   
[flash.net.URLStream.endian](../net/URLStream.html#endian)

  

* * *