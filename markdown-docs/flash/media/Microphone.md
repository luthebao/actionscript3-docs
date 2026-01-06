# Microphone

Package| [flash.media](package-detail.html)  
---|---  
Class| public final class Microphone  
Inheritance| Microphone ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Use the Microphone class to monitor or capture audio from a microphone. 

To get access to the device microphone, you can use `Microphone.getMicrophone()` method. However, this method returns a simple microphone, which does not have the ability to eliminate acoustic echo. In order to eliminate acoustic echo, you need to get an instance of microphone using `Microphone.getEnhancedMicrophone()` method. This method returns a device microphone that has the acoustic echo cancellation feature enabled for mobile. Use acoustic echo cancellation to create real-time audio/video applications that don't require headsets. 

**Create a real-time chat application**

To create a real-time chat application, capture audio and send it to Flash Media Server. Use the NetConnection and NetStream classes to send the audio stream to Flash Media Server. Flash Media Server can broadcast the audio to other clients. To create a chat application that doesn't require headsets, use acoustic echo cancellation. Acoustic echo cancellation prevents the feedback loop that occurs when audio enters a microphone, travels out the speakers, and enters the microphone again. To use acoustic echo cancellation, call the `Microphone.getEnhancedMicrophone()` method to get a reference to a Microphone instance. Set `Microphone.enhancedOptions` to an instance of the `MicrophoneEnhancedOptions` class to configure settings.

**Play microphone audio locally**

Call the Microphone `setLoopback()` method to route the microphone audio directly to the local computer or device audio output. Uncontrolled audio feedback is an inherent danger and is likely to occur whenever the audio output can be picked up by the microphone input. The `setUseEchoSuppression()` method can reduce, but not eliminate, the risk of feedback amplification.

**Capture microphone audio for local recording or processing**

To capture microphone audio, listen for the `sampleData` events dispatched by a Microphone instance. The SampleDataEvent object dispatched for this event contains the audio data.

For information about capturing video, see the Camera class.

**Runtime microphone support**

The Microphone class is not supported in Flash Player running in a mobile browser.

_AIR profile support:_ The Microphone class is supported on desktop operating systems, and iOS and Android mobile devices. It is not supported on AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

You can test for support at run time using the `Microphone.isSupported` property. Note that for AIR for TV devices, `Microphone.isSupported` is `true` but `Microphone.getMicrophone()` always returns `null`.

**Privacy controls**

Flash Player displays a Privacy dialog box that lets the user choose whether to allow or deny access to the microphone. Your application window size must be at least 215 x 138 pixels, the minimum size required to display the dialog box, or access is denied automatically. 

Content running in the AIR application sandbox does not need permission to access the microphone and no dialog is displayed. AIR content running outside the application sandbox does require permission and the Privacy dialog is displayed.

[View the examples.](#includeExamplesSummary)

See also

[flash.media.Camera](../media/Camera.html)   
[flash.media.MicrophoneEnhancedMode](../media/MicrophoneEnhancedMode.html)   
[flash.media.MicrophoneEnhancedOptions](../media/MicrophoneEnhancedOptions.html)   
[aYo Binitie: Implementing Acoustic Echo Suppression in Flash/Flex applications](http://mrbinitie.blogspot.com/2011/03/implementing-acoustic-echo-suppression.html)   
[Cristophe Coenraets: Voice Notes for Android](http://coenraets.org/blog/air-for-android-samples/voice-notes-for-android/)   
[Michael Chaize: AIR, Android, and the Microphone](http://www.riagora.com/2010/08/air-android-and-the-microphone/)

  

* * *