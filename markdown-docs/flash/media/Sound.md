# Sound

Package| [flash.media](package-detail.html)  
---|---  
Class| public class Sound  
Inheritance| Sound ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Sound class lets you work with sound in an application. The Sound class lets you create a Sound object, load and play an external MP3 file into that object, close the sound stream, and access data about the sound, such as information about the number of bytes in the stream and ID3 metadata. More detailed control of the sound is performed through the sound source — the SoundChannel or Microphone object for the sound — and through the properties in the SoundTransform class that control the output of the sound to the computer's speakers. 

In Flash Player 10 and later and AIR 1.5 and later, you can also use this class to work with sound that is generated dynamically. In this case, the Sound object uses the function you assign to a `sampleData` event handler to poll for sound data. The sound is played as it is retrieved from a ByteArray object that you populate with sound data. You can use `Sound.extract()` to extract sound data from a Sound object, after which you can manipulate it before writing it back to the stream for playback.

To control sounds that are embedded in a SWF file, use the properties in the SoundMixer class.

**Note** : The ActionScript 3.0 Sound API differs from ActionScript 2.0. In ActionScript 3.0, you cannot take sound objects and arrange them in a hierarchy to control their properties.

When you use this class, consider the following security model: 

  * Loading and playing a sound is not allowed if the calling file is in a network sandbox and the sound file to be loaded is local.
  * By default, loading and playing a sound is not allowed if the calling file is local and tries to load and play a remote sound. A user must grant explicit permission to allow this type of access.
  * Certain operations dealing with sound are restricted. The data in a loaded sound cannot be accessed by a file in a different domain unless you implement a cross-domain policy file. Sound-related APIs that fall under this restriction are `Sound.id3`, `SoundMixer.computeSpectrum()`, `SoundMixer.bufferTime`, and the `SoundTransform` class.

However, in Adobe AIR, content in the `application` security sandbox (content installed with the AIR application) are not restricted by these security limitations.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

[View the examples.](#includeExamplesSummary)

See also

[flash.net.NetStream](../net/NetStream.html)   
[Microphone](Microphone.html)   
[SoundChannel](SoundChannel.html)   
[SoundMixer](SoundMixer.html)   
[SoundTransform](SoundTransform.html)

  

* * *