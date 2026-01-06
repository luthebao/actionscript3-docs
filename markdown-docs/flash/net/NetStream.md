# Netstream

Package| [flash.net](package-detail.html)  
---|---  
Class| public class NetStream  
Inheritance| NetStream ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The NetStream class opens a one-way streaming channel over a NetConnection. 

Use the NetStream class to do the following:

  * Call `NetStream.play()` to play a media file from a local disk, a web server, or Flash Media Server.
  * Call `NetStream.publish()` to publish a video, audio, and data stream to Flash Media Server.
  * Call `NetStream.send()` to send data messages to all subscribed clients.
  * Call `NetStream.send()` to add metadata to a live stream.
  * Call `NetStream.appendBytes()` to pass ByteArray data into the NetStream.

**Note:** You cannot play and publish a stream over the same NetStream object.

Adobe AIR and Flash Player 9.0.115.0 and later versions support files derived from the standard MPEG-4 container format. These files include F4V, MP4, M4A, MOV, MP4V, 3GP, and 3G2 if they contain H.264 video, HEAAC v2 encoded audio, or both. H.264 delivers higher quality video at lower bit rates when compared to the same encoding profile in Sorenson or On2. AAC is a standard audio format defined in the MPEG-4 video standard. HE-AAC v2 is an extension of AAC that uses Spectral Band Replication (SBR) and Parametric Stereo (PS) techniques to increase coding efficiency at low bit rates.

For information about supported codecs and file formats, see the following:

  * [Flash Media Server documentation](http://www.adobe.com/go/learn_fms_fileformats_en)
  * [Exploring Flash Player support for high-definition H.264 video and AAC audio](http://www.adobe.com/go/hardware_scaling_en)
  * [FLV/F4V open specification documents](http://www.adobe.com/go/video_file_format)

**Receiving data from a Flash Media Server stream, progressive F4V file, or progressive FLV file**

Flash Media Server, F4V files, and FLV files can send event objects containing data at specific data points during streaming or playback. You can handle data from a stream or FLV file during playback in two ways:

  * Associate a client property with an event handler to receive the data object. Use the `NetStream.client` property to assign an object to call specific data handling functions. The object assigned to the `NetStream.client` property can listen for the following data points: `onCuePoint()`, `onImageData()`, `onMetaData()`, `onPlayStatus()`, `onSeekPoint()`, `onTextData()`, and `onXMPData()`. Write procedures within those functions to handle the data object returned from the stream during playback. See the `NetStream.client` property for more information. 
  * Associate a client property with a subclass of the NetStream class, then write an event handler to receive the data object. NetStream is a sealed class, which means that properties or methods cannot be added to a NetStream object at runtime. However, you can create a subclass of NetStream and define your event handler in the subclass. You can also make the subclass dynamic and add the event handler to an instance of the subclass. 

Wait to receive a `NetGroup.Neighbor.Connect` event before you use the object replication, direct routing, or posting APIs.

**Note:** To send data through an audio file, like an mp3 file, use the Sound class to associate the audio file with a Sound object. Then, use the `Sound.id3` property to read metadata from the sound file.

**Support for H.264 encoded video in AIR for iOS**

For H.264 video, AIR 3.0 (and later) for iOS supports a subset of the full NetStream API. The following table lists NetStream members for playback that are not supported in AIR for iOS:

Unsupported properties| Unsupported methods| Unsupported events  
---|---|---  
bufferTime| appendBytes()| onCuePoint (works only with FLV files)  
bufferLength| appendBytesAction()| onImageData  
backBufferTime| step()| onSeekPoint  
backBufferLength| | onTextData  
bufferTimeMax| | onXMPData  
bytesLoaded| | drmError  
currentFPS| | drmStatus  
inBufferSeek| | onDRMContentData  
info| | drmAuthenticate  
liveDelay| | DRM.encryptedFLV status event code  
maxPauseBufferTime| |   
soundTransform| |   
All properties describing RTMFP connections| |   
  
For additional information on using AIR for iOS, see the `NetStream.play()` method. 

[View the examples.](#includeExamplesSummary)

See also

[flash.media.Video](../media/Video.html)   
[flash.net.NetConnection](../net/NetConnection.html)   
[appendBytes()](../net/NetStream.html#appendBytes\(\))   
[play()](../net/NetStream.html#play\(\))   
[publish()](../net/NetStream.html#publish\(\))   
[send()](../net/NetStream.html#send\(\))   
[onImageData](../net/NetStream.html#event:onImageData)   
[onMetaData](../net/NetStream.html#event:onMetaData)

  

* * *