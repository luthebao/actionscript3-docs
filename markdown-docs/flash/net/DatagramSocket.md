# Datagramsocket

Package| [flash.net](package-detail.html)  
---|---  
Class| public class DatagramSocket  
Inheritance| DatagramSocket ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The DatagramSocket class enables code to send and receive Universal Datagram Protocol (UDP) packets. 

_AIR profile support:_ This feature is supported on all desktop operating systems, on iOS (starting with AIR 3.8), and on Android (starting with AIR 3.8). This feature is not supported on AIR for TV devices. You can test for support at run time using the `DatagramSocket.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

Datagram packets are individually transmitted between the source and destination. Packets can arrive in a different order than they were sent. Packets lost in transmission are not retransmitted, or even detected.

Data sent using a datagram socket is not automatically broken up into packets of transmittable size. If you send a UDP packet that exceeds the maximum transmission unit (MTU) size, network discards the packet (without warning). The limiting MTU is the smallest MTU of any interface, switch, or router in the transmission path. You can use the NetworkInterface class to determine the MTU of the local interface, but other nodes in the network can have different MTU values.

The Socket class uses TCP which provides guaranteed packet delivery and automatically divides and reassembles large packets. TCP also provides better network bandwidth management. These features mean that data sent using a TCP socket incurs higher latency, but for most uses, the benefits of TCP far outweigh the costs. Most network communication should use the Socket class rather than the DatagramSocket class.

The DatagramSocket class is useful for working with applications where a small transmission latency is important and packet loss is tolerable. For example, network operations in voice-over-IP (VoIP) applications and real-time, multiplayer games can often benefit from UDP. The DatagramSocket class is also useful for some server-side applications. Since UDP is a stateless protocol, a server can handle more requests from more clients than it can with TCP.

The DatagramSocket class can only be used in Adobe AIR applications and only in the application security sandbox.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

[View the examples.](#includeExamplesSummary)

See also

[RFC 768](http://tools.ietf.org/html/rfc768)   
[Socket class](../net/Socket.html)   
[XMLSocket class](../net/XMLSocket.html)   
[ServerSocket class](../net/ServerSocket.html)

  

* * *