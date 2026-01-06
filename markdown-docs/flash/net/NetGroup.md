# Netgroup

Package| [flash.net](package-detail.html)  
---|---  
Class| public class NetGroup  
Inheritance| NetGroup ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 2  
---|---  
  
Instances of the NetGroup class represent membership in an RTMFP group. Use this class to do the following: 

  * **Monitor Quality of Service**. The `info` property contains a NetGroupInfo object whose properties provide QoS statistics for this group.
  * **Posting**. Call `post()` to broadcast ActionScript messages to all members of a group.
  * **Direct routing**. Call `sendToNearest()`, `sendToNeighbor()`, and `sendToAllNeighbors()` to send a short data message to a specific member of a peer-to-peer group. The source and the destination do not need to have a direct connection.
  * **Object replication**. Call `addHaveObjects()`, `removeHaveObjects()`, `addWantObjects()`, `removeWantObjects()`, `writeRequestedObject()`, and `denyRequestedObject()` to break up large data into pieces and replicate it to all nodes in a peer-to-peer group.

In the client-side NetGroup class, the NetConnection dispatches the following events:

  * NetGroup.Connect.Success
  * NetGroup.Connect.Failed
  * NetGroup.Connect.Rejected

The `info.group` property of the event object contains a reference to the event source (the NetGroup). The NetGroup dispatches all other events. In the server-side NetGroup class, the NetGroup dispatches all events.

For information about using groups with peer-assisted networking, see [Social Media Experiences with Flash Media and RTMFP](http://tv.adobe.com/watch/adobe-at-nab-2010/social-media-experiences-with-adobe-flash-media-server-and-rtmfp/), also by Tom Krcha.

For information about the technical details behind peer-assisted networking, see [P2P on the Flash Platform with RTMFP](http://tv.adobe.com/watch/fitc/playertoplayer-communications-with-rtmfp/) by Adobe Computer Scientist Matthew Kaufman.

See also

[flash.net.GroupSpecifier](../net/GroupSpecifier.html)   
[flash.net.NetStream](../net/NetStream.html)   
[flash.events.NetStatusEvent info.code values starting with "NetGroup."](../events/NetStatusEvent.html#info)

  

* * *