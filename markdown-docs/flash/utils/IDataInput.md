# Idatainput

Package| [flash.utils](package-detail.html)  
---|---  
Interface| public interface IDataInput  
Implementors| [ByteArray](../utils/ByteArray.html), [FileStream](../filesystem/FileStream.html), [Socket](../net/Socket.html), [URLStream](../net/URLStream.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The IDataInput interface provides a set of methods for reading binary data. This interface is the I/O counterpart to the IDataOutput interface, which writes binary data. 

All IDataInput and IDataOutput operations are "bigEndian" by default (the most significant byte in the sequence is stored at the lowest or first storage address), and are nonblocking. If insufficient data is available, an `EOFError` exception is thrown. Use the `IDataInput.bytesAvailable` property to determine how much data is available to read.

Sign extension matters only when you read data, not when you write it. Therefore you do not need separate write methods to work with `IDataInput.readUnsignedByte()` and `IDataInput.readUnsignedShort()`. In other words:

  * Use `IDataOutput.writeByte()` with `IDataInput.readUnsignedByte()` and `IDataInput.readByte()`.
  * Use `IDataOutput.writeShort()` with `IDataInput.readUnsignedShort()` and `IDataInput.readShort()`.

[View the examples.](#includeExamplesSummary)

See also

[IDataOutput interface](../utils/IDataOutput.html)   
[endian](../utils/IDataInput.html#endian)   
[FileStream class](../filesystem/FileStream.html)   
[Socket class](../net/Socket.html)   
[URLStream class](../net/URLStream.html)   
[ByteArray class](../utils/ByteArray.html)   
EOFError class

  

* * *