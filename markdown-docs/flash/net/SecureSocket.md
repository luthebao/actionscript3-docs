# Securesocket

Package| [flash.net](package-detail.html)  
---|---  
Class| public class SecureSocket  
Inheritance| SecureSocket ![Inheritance](../../images/inherit-arrow.gif) [Socket](Socket.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The SecureSocket class enables code to make socket connections using the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols. 

_AIR profile support:_ This feature is supported on all desktop operating systems, but is not supported on all AIR for TV devices. On mobile devices, it is supported on Android and also supported on iOS starting from AIR 20. You can test for support at run time using the `SecureSocket.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

The SSL/TLS protocols provide a mechanism to handle both aspects of a secure socket connection: 

  1. Encryption of data communication over the socket
  2. Authentication of the host's identity via its certificate

The supported encryption protocols are SSL 3.1 and higher, and TLS 1.0 and higher. (TLS is the successor protocol for SSL. TLS 1.0 equals SSL 3.1, TLS 1.1 equals SSL 3.2, and so on.) SSL versions 3.0 or lower are not supported.

Validation of the server certificate is performed using the trust store and certificate validation support of the client platform. In addition you can add your own certificates programmatically with the `addBinaryChainBuildingCertificate()` method.This API isn't supported on iOS currently. Using this API on iOS would throw an exception - "ArgumentError: Error #2004"

The SecureSocket class only connects to servers with valid, trusted certificates. You cannot choose to connect to a server in spite of a problem with its certificate. For example, there is no way to connect to a server with an expired certificate. The same is true for a certificate that doesn't chain to a trusted anchor certificate. The connection will not be made, even though the certificate would be valid otherwise.

The SecureSocket class is useful for performing encrypted communication to a trusted server. In other respects, a SecureSocket object behaves like a regular Socket object.

To use the SecureSocket class, create a SecureSocket object (`new SecureSocket()`). Next, set up your listeners, and then run `SecureSocket.connect(host, port)`. When you successfully connect to the server, the socket dispatches a `connect` event. A successful connection is one in which the server's security protocols are supported and its certificate is valid and trusted. If the certificate cannot be validated, the Socket dispatches an `IOError` event.

**Important:** The Online Certificate Status Protocol (OCSP) is not supported by all operating systems. Users can also disable OCSP checking on individual computers. If OCSP is not supported or is disabled and a certificate does not contain the information necessary to check revocation using a Certificate Revocation List (CRL), then certificate revocation is not checked. The certificate is accepted if otherwise valid. This scenario could allow a server to use a revoked certificate.

[View the examples.](#includeExamplesSummary)

See also

[Socket class](../net/Socket.html)

  

* * *