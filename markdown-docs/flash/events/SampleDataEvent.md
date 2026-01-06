# Sampledataevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class SampleDataEvent  
Inheritance| SampleDataEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
Dispatched when a Sound object requests new audio data or when a Microphone object has new audio data to provide. 

This event has two uses:

  * To provide dynamically generated audio data for a Sound object
  * To get audio data for a Microphone object

**Dynamically generating audio using the Sound object** Use the `sampleData` event to play dynamically generated audio. In this environment, the Sound object doesn't actually contain sound data. Instead, it acts as a socket for sound data that is being streamed to it through the use of the function you assign as the handler for the `sampleData` event. 

In your function, you use the `ByteArray.writeFloat()` method to write to the event's `data`) property, which contains the sampled data you want to play.

If a Sound object has not loaded an MP3 file, when you call its `play()` method the object starts dispatching `sampleData` events, requesting sound samples. The Sound object continues to send events as the sound plays back until you stop providing data, or until the `stop()` method of the SoundChannel object is called.

Thes latency of the event varies from platform to platform, and it could change in future versions of Flash Player or AIR. Don't depend on a specific latency. Instead calculate it using `((SampleDataEvent.position/44.1) - SoundChannelObject.position)`.

Provide between 2048 and 8192 samples to the `data` property of the SampleDataEvent object. For best performance, provide as many samples as possible. The fewer samples you provide, the more likely it is that clicks and pops will occur during playback. This behavior can differ on various platforms and can occur in various situations - for example, when resizing the browser. You might write code that works on one platform when you provide only 2048 samples, but that same code might not work as well when run on a different platform. If you require the lowest latency possible, consider making the amount of data user-selectable.

If you provide fewer than 2048 samples, tha Sound object plays the remaining samples and then stops the sound as if the end of a sound file was reached, generating a `complete` event.

You can use the `extract()` method of a Sound object to extract its sound data, which you can then write to the dynamic stream for playback.

When you use the `sampleData` event with a Sound object, the only Sound methods that are enabled are `extract()` and `play()`. Calling any other methods or properties results in an "invalid call" exception. All methods and properties of the SoundChannel object are still enabled.

**Capturing Microphone audio** Use the `sampleData` event to capture audio data from a microphone. When you add an event listener for the `sampleData` event, the Microphone dispatches the event as audio samples become available.

In the event handler function, use the `ByteArray.readFloat()` method to read the event's `data`) property, which contains the sampled data. The event will contain multiple samples, so you should use a `while` loop to read the available data:
    
    
    var soundBytes:ByteArray = new ByteArray();
     while(event.data.bytesAvailable)
     {
          var sample:Number = event.data.readFloat();
          soundBytes.writeFloat(sample);
     }

[View the examples.](#includeExamplesSummary)

See also

[flash.media.Sound](../media/Sound.html)

  

* * *