# Serversocketconnectevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class ServerSocketConnectEvent  
Inheritance| ServerSocketConnectEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
A ServerSocket object dispatches a ServerSocketConnectEvent object when a client attempts to connect to the server socket. 

The `socket` property of the ServerSocketConnectEvent object provides the Socket object to use for subsequent communication between the server and the client. To deny the connection, call the Socket `close()` method.

See also

[ServerSocket class](../net/ServerSocket.html)

  

* * *