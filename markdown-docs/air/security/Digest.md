# Digest

Package| [air.security](package-detail.html)  
---|---  
Class| public class Digest  
Inheritance| Digest ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IDataOutput](../../flash/utils/IDataOutput.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 50   
---|---  
  
The Digest class is used to generate a digest, or hash, of some data. It can be used to generate a fixed-length, one-way hash value based on arbitrary-sized data, to create a checksum and to attempt to quickly detect changes in data for validation purposes. 

This class is similar to the Java `java.security.MessageDigest` implementation, and can be used in two ways:

  1. By creating an instance of the Digest class with a particular algorith, and then feeding data into the object using repeated calls to one of the `IDataOutput` methods, and finally then calling the `digest` method in order to calculate the hash value.
  2. By calling the static `hash` method with a `ByteArray` to perform the whole operation in a single call.

The supported algorithms are `"SHA-1"`, `"SHA-256"`, and `"MD5"`. 

  

* * *