# Bytearray

Package| [flash.utils](package-detail.html)  
---|---  
Class| public class ByteArray  
Inheritance| ByteArray ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The ByteArray class provides methods and properties to optimize reading, writing, and working with binary data. 

_Note:_ The ByteArray class is for advanced developers who need to access data on the byte level.

In-memory data is a packed array (the most compact representation for the data type) of bytes, but an instance of the ByteArray class can be manipulated with the standard `[]` (array access) operators. It also can be read and written to as an in-memory file, using methods similar to those in the URLStream and Socket classes.

In addition, zlib and lzma compression and decompression are supported, as well as Action Message Format (AMF) object serialization.

Possible uses of the ByteArray class include the following: 

  * Creating a custom protocol to connect to a server.
  * Writing your own URLEncoder/URLDecoder.
  * Writing your own AMF/Remoting packet.
  * Optimizing the size of your data by using data types.
  * Working with binary data loaded from a file in Adobe® AIR®.

[View the examples.](#includeExamplesSummary)

See also

[[] (array access)](../../operators.html#array_access)   
[Socket class](../net/Socket.html)   
[URLStream class](../net/URLStream.html)

  

* * *