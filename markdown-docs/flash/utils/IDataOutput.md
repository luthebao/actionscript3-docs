# Idataoutput

Package| [flash.utils](package-detail.html)  
---|---  
Interface| public interface IDataOutput  
Implementors| [ByteArray](../utils/ByteArray.html), [Digest](../../air/security/Digest.html), [FileStream](../filesystem/FileStream.html), [Socket](../net/Socket.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The IDataOutput interface provides a set of methods for writing binary data. This interface is the I/O counterpart to the IDataInput interface, which reads binary data. The IDataOutput interface is implemented by the FileStream, Socket and ByteArray classes. 

All IDataInput and IDataOutput operations are "bigEndian" by default (the most significant byte in the sequence is stored at the lowest or first storage address), and are nonblocking. 

Sign extension matters only when you read data, not when you write it. Therefore, you do not need separate write methods to work with `IDataInput.readUnsignedByte()` and `IDataInput.readUnsignedShort()`. In other words:

  * Use `IDataOutput.writeByte()` with `IDataInput.readUnsignedByte()` and `IDataInput.readByte()`.
  * Use `IDataOutput.writeShort()` with `IDataInput.readUnsignedShort()` and `IDataInput.readShort()`.

[View the examples.](#includeExamplesSummary)

See also

[IDataInput interface](../utils/IDataInput.html)   
[endian](../utils/IDataOutput.html#endian)   
[FileStream class](../filesystem/FileStream.html)   
[Socket class](../net/Socket.html)   
[URLStream class](../net/URLStream.html)   
[ByteArray class](../utils/ByteArray.html)

  

* * *