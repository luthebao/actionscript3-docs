# Package Detail

The flash.net package contains classes for sending and receiving from the network, such as URL downloading and Flash Remoting.

  

* * *

Functions

| Function| Description  
---|---|---  
| [getClassByAlias](package.html#getClassByAlias\(\))|  Looks up a class that previously had an alias registered through a call to the `registerClassAlias()` method.  
| [navigateToURL](package.html#navigateToURL\(\))|  Opens or replaces a window in the application that contains the Flash Player container (usually a browser).  
| [registerClassAlias](package.html#registerClassAlias\(\))|  Preserves the class (type) of an object when the object is encoded in Action Message Format (AMF).  
| [sendToURL](package.html#sendToURL\(\))|  Sends a URL request to a server, but ignores any response.  
  
Interfaces

| Interface| Description  
---|---|---  
|  _[IDynamicPropertyOutput](IDynamicPropertyOutput.html)_|  This interface controls the serialization of dynamic properties of dynamic objects.  
|  _[IDynamicPropertyWriter](IDynamicPropertyWriter.html)_|  This interface is used with the IDynamicPropertyOutput interface to control the serialization of dynamic properties of dynamic objects.  
  
Classes

| Class| Description  
---|---|---  
| [DatagramSocket](DatagramSocket.html)|  The DatagramSocket class enables code to send and receive Universal Datagram Protocol (UDP) packets.  
| [FileFilter](FileFilter.html)|  The FileFilter class is used to indicate what files on the user's system are shown in the file-browsing dialog box that is displayed when the `FileReference.browse()` method, the `FileReferenceList.browse()` method is called or a browse method of a File, FileReference, or FileReferenceList object is called.  
| [FileReference](FileReference.html)|  The FileReference class provides a means to upload and download files between a user's computer and a server.  
| [FileReferenceList](FileReferenceList.html)|  The FileReferenceList class provides a means to let users select one or more files for uploading.  
| [GroupSpecifier](GroupSpecifier.html)|  The GroupSpecifier class is used to construct the opaque `groupspec` strings that can be passed to NetStream and NetGroup constructors.  
| [InterfaceAddress](InterfaceAddress.html)|  The InterfaceAddress class reports the properties of a network interface address.  
| [IPVersion](IPVersion.html)|  The IPVersion class defines constants representing the different families of IP addresses.  
| [LocalConnection](LocalConnection.html)|  The LocalConnection class lets you create a LocalConnection object that can invoke a method in another LocalConnection object.  
| [NetConnection](NetConnection.html)|  The NetConnection class creates a two-way connection between a client and a server.  
| [NetGroup](NetGroup.html)|  Instances of the NetGroup class represent membership in an RTMFP group.  
| [NetGroupInfo](NetGroupInfo.html)|  The NetGroupInfo class specifies various Quality of Service (QoS) statistics related to a NetGroup object's underlying RTMFP Peer-to-Peer data transport.  
| [NetGroupReceiveMode](NetGroupReceiveMode.html)|  The NetGroupReceiveMode class is an enumeration of constant values used for the `receiveMode` property of the NetGroup class.  
| [NetGroupReplicationStrategy](NetGroupReplicationStrategy.html)|  The NetGroupReplicationStrategy class is an enumeration of constant values used in setting the `replicationStrategy` property of the `NetGroup` class.  
| [NetGroupSendMode](NetGroupSendMode.html)|  The NetGroupSendMode class is an enumeration of constant values used for the `sendMode` parameter of the `NetGroup.sendToNeighbor()` method.  
| [NetGroupSendResult](NetGroupSendResult.html)|  The NetGroupSendResult class is an enumeration of constant values used for the return value of the Directed Routing methods associated with a NetGroup instance.  
| [NetMonitor](NetMonitor.html)|  The NetMonitor class maintains a list of NetStream objects.  
| [NetStream](NetStream.html)|  The NetStream class opens a one-way streaming channel over a NetConnection.  
| [NetStreamAppendBytesAction](NetStreamAppendBytesAction.html)|  The NetStreamAppendBytesAction class is an enumeration of the constants you can pass to the `NetStream.appendBytesAction()` method.  
| [NetStreamInfo](NetStreamInfo.html)|  The NetStreamInfo class specifies the various Quality of Service (QOS) statistics and other information related to a NetStream object and the underlying streaming buffer for audio, video, and data.  
| [NetStreamMulticastInfo](NetStreamMulticastInfo.html)|  The NetStreamMulticastInfo class specifies various Quality of Service (QoS) statistics related to a NetStream object's underlying RTMFP Peer-to-Peer and IP Multicast stream transport.  
| [NetStreamPlayOptions](NetStreamPlayOptions.html)|  The NetStreamPlayOptions class specifies the various options that can be passed to the `NetStream.play2()` method.  
| [NetStreamPlayTransitions](NetStreamPlayTransitions.html)|  The NetStreamPlayTransitions class specifies the valid strings that you can use with the `NetStreamPlayOptions.transition` property.  
| [NetworkInfo](NetworkInfo.html)|  The NetworkInfo class provides information about the network interfaces on a computer.  
| [NetworkInterface](NetworkInterface.html)|  The NetworkInterface class describes a network interface.  
| [ObjectEncoding](ObjectEncoding.html)|  The ObjectEncoding class is used in defining serialization settings in classes that serialize objects (such as FileStream, NetStream, NetConnection, SharedObject, and ByteArray) to work with prior versions of ActionScript.  
| [Responder](Responder.html)|  The Responder class provides an object that is used in `NetConnection.call()` to handle return values from the server related to the success or failure of specific operations.  
| [SecureSocket](SecureSocket.html)|  The SecureSocket class enables code to make socket connections using the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols.  
| [ServerSocket](ServerSocket.html)|  The ServerSocket class allows code to act as a server for Transport Control Protocol (TCP) connections.  
| [SharedObject](SharedObject.html)|  The SharedObject class is used to read and store limited amounts of data on a user's computer or on a server.  
| [SharedObjectFlushStatus](SharedObjectFlushStatus.html)|  The SharedObjectFlushStatus class provides values for the code returned from a call to the `SharedObject.flush()` method.  
| [Socket](Socket.html)|  The Socket class enables code to establish Transport Control Protocol (TCP) socket connections for sending and receiving binary data.  
| [URLLoader](URLLoader.html)|  The URLLoader class downloads data from a URL as text, binary data, or URL-encoded variables.  
| [URLLoaderDataFormat](URLLoaderDataFormat.html)|  The URLLoaderDataFormat class provides values that specify how downloaded data is received.  
| [URLRequest](URLRequest.html)|  The URLRequest class captures all of the information in a single HTTP request.  
| [URLRequestDefaults](URLRequestDefaults.html)|  The URLRequestDefaults class includes static properties that you can set to define default values for the properties of the URLRequest class.  
| [URLRequestHeader](URLRequestHeader.html)|  A URLRequestHeader object encapsulates a single HTTP request header and consists of a name/value pair.  
| [URLRequestMethod](URLRequestMethod.html)|  The URLRequestMethod class provides values that specify whether the URLRequest object should use the `POST` method or the `GET` method when sending data to a server.  
| [URLStream](URLStream.html)|  The URLStream class provides low-level access to downloading URLs.  
| [URLVariables](URLVariables.html)|  The URLVariables class allows you to transfer variables between an application and a server.  
| [XMLSocket](XMLSocket.html)|  The XMLSocket class implements client sockets that let the Flash Player or AIR application communicate with a server computer identified by an IP address or domain name.  
  
© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)