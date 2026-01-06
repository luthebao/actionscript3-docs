# Socket

Package| [flash.net](package-detail.html)  
---|---  
Class| public class Socket  
Inheritance| Socket ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IDataInput](../utils/IDataInput.html), [IDataOutput](../utils/IDataOutput.html)  
Subclasses| [SecureSocket](../net/SecureSocket.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Socket class enables code to establish Transport Control Protocol (TCP) socket connections for sending and receiving binary data. 

The Socket class is useful for working with servers that use binary protocols.

To use the methods of the Socket class, first use the constructor, `new Socket`, to create a Socket object.

A socket transmits and receives data asynchronously. 

On some operating systems, flush() is called automatically between execution frames, but on other operating systems, such as Windows, the data is never sent unless you call `flush()` explicitly. To ensure your application behaves reliably across all operating systems, it is a good practice to call the `flush()` method after writing each message (or related group of data) to the socket.

In Adobe AIR, Socket objects are also created when a listening ServerSocket receives a connection from an external process. The Socket representing the connection is dispatched in a ServerSocketConnectEvent. Your application is responsible for maintaining a reference to this Socket object. If you don't, the Socket object is eligible for garbage collection and may be destroyed by the runtime without warning.

SWF content running in the local-with-filesystem security sandbox cannot use sockets.

_Socket policy files_ on the target host specify the hosts from which SWF files can make socket connections, and the ports to which those connections can be made. The security requirements with regard to socket policy files have become more stringent in the last several releases of Flash Player. In all versions of Flash Player, Adobe recommends the use of a socket policy file; in some circumstances, a socket policy file is required. Therefore, if you are using Socket objects, make sure that the target host provides a socket policy file if necessary. 

The following list summarizes the requirements for socket policy files in different versions of Flash Player:

  * In Flash Player 9.0.124.0 and later, a socket policy file is required for any socket connection. That is, a socket policy file on the target host is required no matter what port you are connecting to, and is required even if you are connecting to a port on the same host that is serving the SWF file. 
  * In Flash Player versions 9.0.115.0 and earlier, if you want to connect to a port number below 1024, or if you want to connect to a host other than the one serving the SWF file, a socket policy file on the target host is required. 
  * In Flash Player 9.0.115.0, even if a socket policy file isn't required, a warning is displayed when using the Flash Debug Player if the target host doesn't serve a socket policy file. 
  * In AIR, a socket policy file is not required for content running in the application security sandbox. Socket policy files are required for any socket connection established by content running outside the AIR application security sandbox.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en)

[View the examples.](#includeExamplesSummary)

See also

[ServerSocket](../net/ServerSocket.html)   
[DatagramSocket](../net/DatagramSocket.html)

  

* * *