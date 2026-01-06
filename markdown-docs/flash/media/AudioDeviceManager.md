# Audiodevicemanager

Package| [flash.media](package-detail.html)  
---|---  
Class| public final class AudioDeviceManager  
Inheritance| AudioDeviceManager ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 28  
---|---  
  
Use the AudioDeviceManager class to get audio device information of the system, and select a device for audio playback. User can change audio output device either through Flash Player's Settings UI, or the AudioDeviceManager API. Both of them are in sync with audio output settings. AudioDeviceManager API was enabled for Flash Player 27. It is now enabled for AIR Desktop from AIR 28. 

The audio device selected from one AIR application does not affect the audio from other AIR applications or Flash Player instances.

**Privacy Restriction**

AudioDeviceManager API is under User Invoked Action (UIA) restriction, that is, it can only be invoked with some user interaction. If this API is not invoked by user interaction, Flash Player throws runtime error IllegalOperationError with error code set to 2176. In case of AIR applications, the UIA check will be applied when we load an external SWF/HTML hosted over a network. If the externally loaded SWF/HTML tries to change the audio output device without any user invoked action, then AIR runtime throws an error IllegalOperationError with error code 2176. 

**Access AudioDeviceManager instance**

AudioDeviceManager instance is a singleton object, it is in sync with Flash Player's Audio Output Settings. Client should use `AudioDeviceManager.audioDeviceManager` to get a reference to this singleton object. 

**Get the current audio devices available on the system**

Use `AudioDeviceManager.deviceNames` to get all the available audio output devices in the system. 

**Get the current selected audio device**

Use `AudioDeviceManager.selectedDeviceIndex` to find the index of the current used audio output device. Use this index to find the device name the device list returned from `AudioDeviceManager.deviceNames`

**Select an audio output device**

Set `AudioDeviceManager.selectedDeviceIndex` to a different value can make that device to be the current selected audio playback device. 

**Monitor audio output device change**

Audio output device may change because of user selecting a different device from Flash Player's Settings UI, Content setting `AudioDeviceManager.selectedDeviceIndex`, audio device being added/removed from the system. Client application can register listener to event: `AudioOutputChangeEvent.AUDIO_OUTPUT_CHANGE` to receive notification when audio output device change happens. The `reason` property of the event object indicates how this change is triggered. There are 2 possible values for `reason` property: `AudioOutputChangeReason.USER_SELECTION` indicates that user selects a different audio output device through Flash Player's Settings UI, or Content sets `AudioDeviceManager.selectedDeviceIndex`. `AudioOutputChangeReason.DEVICE_CHANGE` indicates that audio output device has been added or removed from the system. 

  

* * *