# X500Distinguishedname

Package| [flash.security](package-detail.html)  
---|---  
Class| public class X500DistinguishedName  
Inheritance| X500DistinguishedName ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The X500DistinguishedName class defines Distinguished Name (DN) properties for use in the X509Certificate class. The Distinguished Name protocol is specified in [RFC1779](http://tools.ietf.org/rfc/rfc1779). 

This class is useful for any code that needs to examine a server certificate's Subject and Issuer DN after a secure socket connection has been established. Subject and Issuer DN data is accessible in the X509Certificate class's `subject` and `issuer` properties. These properties are populated with X500DistinguishedName objects after `SecureSocket.connect()` establishes a connection with the server.

This class stores DN attributes as string properties. You can use the `toString()` method to get all of the individual DN properties in one string. Properties with no DN value are set to null.

Note: The X500DistinguishedName properties store only the first occurrence of each DN attribute, although the DN protocol allows for multiple attributes of the same type.

See also

[SecureSocket class](../net/SecureSocket.html)

  

* * *