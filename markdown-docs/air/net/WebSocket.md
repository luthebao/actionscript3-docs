# Websocket

Package| [air.net](package-detail.html)  
---|---  
Class| public class WebSocket  
Inheritance| WebSocket ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../../flash/events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 51.0   
---|---  
  
The WebSocket class is a utility that encapsulates a normal `Socket` object and implements the WebSocket protocol (RFC 6455). 

This can be used in conjunction with a `ServerSocket` object to allow web pages to connect to and communicate with an AIR application - once a connection is received, create a new `WebSocket` instance and call `startServer()` to handle the protocol handshake.

To initiate an outgoing WebSocket connection to a server, use the `connect()` method, passing in the URL string in format `"ws://some.example.com/ws/demo"` ('wss' can be used for secure WebSocket over TLS connections). An optional set of protocols can be passed in, that will be passed to the server, and the chosen protocol can then be accessed via the `protocol` property.

If a `PING` message is received by a WebSocket object, it will automatically response with the appropriate `PONG` message. It is up to the developer to implement any outgoing `PING` messages (or unsolicited `PONGs`) should those be desired.

Note: messages are limited to 4GB in size, due to the restrictions of the ByteArray class.

  

* * *