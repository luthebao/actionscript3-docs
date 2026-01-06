# Serversocket

Package| [flash.net](package-detail.html)  
---|---  
Class| public class ServerSocket  
Inheritance| ServerSocket ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The ServerSocket class allows code to act as a server for Transport Control Protocol (TCP) connections. 

_AIR profile support:_ This feature is supported on all desktop operating systems, on iOS (starting with AIR 3.8), and on Android (starting with AIR 3.8). This feature is not supported on AIR for TV devices. You can test for support at run time using the `ServerSocket.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

A TCP server listens for incoming connections from remote clients. When a client attempts to connect, the ServerSocket dispatches a `connect` event. The ServerSocketConnectEvent object dispatched for the event provides a Socket object representing the TCP connection between the server and the client. Use this Socket object for subsequent communication with the connected client. You can get the client address and port from the Socket object, if needed.

**Note:** Your application is responsible for maintaining a reference to the client Socket object. If you don't, the object is eligible for garbage collection and may be destroyed by the runtime without warning.

To put a ServerSocket object into the listening state, call the `listen()` method. In the listening state, the server socket object dispatches `connect` events whenever a client using the TCP protocol attempts to connect to the bound address and port. The ServerSocket object continues to listen for additional connections until you call the `close()` method.

TCP connections are persistent — they exist until one side of the connection closes it (or a serious network failure occurs). Any data sent over the connection is broken into transmittable packets and reassembled on the other end. All packets are guaranteed to arrive (within reason) — any lost packets are retransmitted. In general, the TCP protocol manages the available network bandwidth better than the UDP protocol. Most AIR applications that require socket communications should use the ServerSocket and Socket classes rather than the DatagramSocket class.

The ServerSocket class can only be used in Adobe AIR applications and only in the application security sandbox.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

[View the examples.](#includeExamplesSummary)

See also

[ServerSocketConnectEvent class](../events/ServerSocketConnectEvent.html)   
[Socket class](../net/Socket.html)   
[XMLSocket class](../net/XMLSocket.html)   
[DatagramSocket class](../net/DatagramSocket.html)

  

* * *