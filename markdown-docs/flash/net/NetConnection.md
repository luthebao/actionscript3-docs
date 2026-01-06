# Netconnection

Package| [flash.net](package-detail.html)  
---|---  
Class| public class NetConnection  
Inheritance| NetConnection ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The NetConnection class creates a two-way connection between a client and a server. The client can be a Flash Player or AIR an AIR application. The server can be a web server, Flash Media Server, an application server running Flash Remoting, or the [Adobe Stratus](http://labs.adobe.com/technologies/stratus/) service. Call `NetConnection.connect()` to establish the connection. Use the NetStream class to send streams of media and data over the connection. 

For security information about loading content and data into Flash Player and AIR, see the following:

  * To load content and data into Flash Player from a web server or from a local location, see [Flash Player Developer Center: Security](http://www.adobe.com/go/devnet_security_en).
  * To load content and data into Flash Player and AIR from Flash Media Server, see the [Flash Media Server documentation](http://www.adobe.com/support/flashmediaserver).
  * To load content and data into AIR, see the [Adobe AIR Developer Center](http://www.adobe.com/devnet/air/).

To write callback methods for this class, extend the class and define the callback methods in the subclass, or assign the `client` property to an object and define the callback methods on that object.

[View the examples.](#includeExamplesSummary)

See also

[client](../net/NetConnection.html#client)   
[NetStream](NetStream.html)   
[connect()](../net/NetConnection.html#connect\(\))   
[flash.net.Responder](../net/Responder.html)

  

* * *