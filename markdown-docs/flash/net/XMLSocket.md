# Xmlsocket

Package| [flash.net](package-detail.html)  
---|---  
Class| public class XMLSocket  
Inheritance| XMLSocket ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The XMLSocket class implements client sockets that let the Flash Player or AIR application communicate with a server computer identified by an IP address or domain name. The XMLSocket class is useful for client-server applications that require low latency, such as real-time chat systems. A traditional HTTP-based chat solution frequently polls the server and downloads new messages using an HTTP request. In contrast, an XMLSocket chat solution maintains an open connection to the server, which lets the server immediately send incoming messages without a request from the client. To use the XMLSocket class, the server computer must run a daemon that understands the protocol used by the XMLSocket class. The protocol is described in the following list: 

  * XML messages are sent over a full-duplex TCP/IP stream socket connection.
  * Each XML message is a complete XML document, terminated by a zero (0) byte.
  * An unlimited number of XML messages can be sent and received over a single XMLSocket connection.

Setting up a server to communicate with the XMLSocket object can be challenging. If your application does not require real-time interactivity, use the URLLoader class instead of the XMLSocket class. 

To use the methods of the XMLSocket class, first use the constructor, `new XMLSocket`, to create an XMLSocket object.

SWF files in the local-with-filesystem sandbox may not use sockets.

_Socket policy files_ on the target host specify the hosts from which SWF files can make socket connections, and the ports to which those connections can be made. The security requirements with regard to socket policy files have become more stringent in the last several releases of Flash Player. In all versions of Flash Player, Adobe recommends the use of a socket policy file; in some circumstances, a socket policy file is required. Therefore, if you are using XMLSocket objects, make sure that the target host provides a socket policy file if necessary. 

The following list summarizes the requirements for socket policy files in different versions of Flash Player:

  * In Flash Player 9.0.124.0 and later, a socket policy file is required for any XMLSocket connection. That is, a socket policy file on the target host is required no matter what port you are connecting to, and is required even if you are connecting to a port on the same host that is serving the SWF file. 
  * In Flash Player versions 9.0.115.0 and earlier, if you want to connect to a port number below 1024, or if you want to connect to a host other than the one serving the SWF file, a socket policy file on the target host is required. 
  * In Flash Player 9.0.115.0, even if a socket policy file isn't required, a warning is displayed when using the Flash Debug Player if the target host doesn't serve a socket policy file. 

However, in Adobe AIR, content in the `application` security sandbox (content installed with the AIR application) are not restricted by these security limitations.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

[View the examples.](#includeExamplesSummary)

See also

[flash.net.URLLoader.load()](../net/URLLoader.html#load\(\))   
[flash.net.URLLoader](../net/URLLoader.html)

  

* * *