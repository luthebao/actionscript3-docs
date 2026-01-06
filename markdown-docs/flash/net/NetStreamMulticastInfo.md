# Netstreammulticastinfo

Package| [flash.net](package-detail.html)  
---|---  
Class| public final class NetStreamMulticastInfo  
Inheritance| NetStreamMulticastInfo ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 2  
---|---  
  
The NetStreamMulticastInfo class specifies various Quality of Service (QoS) statistics related to a NetStream object's underlying RTMFP Peer-to-Peer and IP Multicast stream transport. A NetStreamMulticastInfo object is returned by the `NetStream.multicastInfo` property. 

Properties that return numbers represent totals computed from the beginning of the multicast stream. These types of properties include the number of media bytes sent or the number of media fragment messages received. Properties that are rates represent a snapshot of the current rate averaged over a few seconds. These types of properties include the rate at which a local node is receiving data. 

To see a list of values contained in the NetStreamMulticastInfo object, use the `NetStreamMulticastInfo.toString()` method.

See also

[toString()](../net/NetStreamMulticastInfo.html#toString\(\))   
[flash.net.NetStream.multicastInfo](../net/NetStream.html#multicastInfo)

  

* * *