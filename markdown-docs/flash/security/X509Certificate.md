# X509Certificate

Package| [flash.security](package-detail.html)  
---|---  
Class| public class X509Certificate  
Inheritance| X509Certificate ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The X509Certificate class represents an X.509 certificate. This class defines X.509 properties specified in [RFC2459](http://tools.ietf.org/rfc/rfc2459). After you make a successful call to `SecureSocket.connect()`, the server's certificate data is stored as an X509Certificate instance in the `SecureSocket.serverCertificate` property. 

Use this class to examine a server certificate after establishing a secure socket connection. The properties in this class provide access to the most used attributes of an X.509 certificate. If you must access other parts of a server certificate (for example, its extensions), the complete certificate is available in the `encoded` property. The certificate stored in the `encoded` property is DER-encoded. 

See also

[SecureSocket class](../net/SecureSocket.html)

  

* * *