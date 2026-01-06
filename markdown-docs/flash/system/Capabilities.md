# Capabilities

Package| [flash.system](package-detail.html)  
---|---  
Class| public final class Capabilities  
Inheritance| Capabilities ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0  
---|---  
  
The Capabilities class provides properties that describe the system and runtime that are hosting the application. For example, a mobile phone's screen might be 100 square pixels, black and white, whereas a PC screen might be 1000 square pixels, color. By using the Capabilities class to determine what capabilities the client has, you can provide appropriate content to as many users as possible. When you know the device's capabilities, you can tell the server to send the appropriate SWF files or tell the SWF file to alter its presentation. The Capabilities class provides properties that describe the system and runtime that are hosting HTML (and SWF) content. By using the Capabilities class to determine what capabilities the client has, you can provide appropriate content to as many users as possible. When you know the device's capabilities, you can load appropriate content or use code to alter its presentation.

However, some capabilities of Adobe AIR are not listed as properties in the Capabilities class. They are properties of other classes:

Property | Description  
---|---  
`NativeApplication.supportsDockIcon` | Whether the operating system supports application doc icons.  
`NativeApplication.supportsMenu` | Whether the operating system supports a global application menu bar.  
`NativeApplication.supportsSystemTrayIcon` | Whether the operating system supports system tray icons.  
`NativeWindow.supportsMenu` | Whether the operating system supports window menus.  
`NativeWindow.supportsTransparency` | Whether the operating system supports transparent windows.  
  
Do _not_ use `Capabilities.os` or `Capabilities.manufacturer` to determine a capability based on the operating system. Basing a capability on the operating system is a bad idea, since it can lead to problems if an application does not consider all potential target operating systems. Instead, use the property corresponding to the capability for which you are testing.

You can send capabilities information, which is stored in the `Capabilities.serverString` property as a URL-encoded string, using the `GET` or `POST` HTTP method. The following example shows a server string for a computer that has MP3 support and 1600 x 1200 pixel resolution, that is running Windows XP with an input method editor (IME) installed, and does not have support for multichannel audio:
    
    
    A=t&SA=t&SV=t&EV=t&MP3=t&AE=t&VE=t&ACC=f&PR=t&SP=t&
         SB=f&DEB=t&V=WIN%209%2C0%2C0%2C0&M=Adobe%20Windows&
         R=1600x1200&DP=72&COL=color&AR=1.0&OS=Windows%20XP&
         L=en&PT=External&AVD=f&LFD=f&WD=f&IME=t&DD=f&
         DDP=f&DTS=f&DTE=f&DTH=f&DTM=f

The following table lists the properties of the Capabilities class and corresponding server strings. It also lists the server strings for the multichannel audio types.  Capabilities class property | Server string  
---|---  
`avHardwareDisable` | `AVD`  
`hasAccessibility` | `ACC`  
`hasAudio` | `A`  
`hasAudioEncoder` | `AE`  
`hasEmbeddedVideo` | `EV`  
`hasIME` | `IME`  
`hasMP3` | `MP3`  
`hasPrinting` | `PR`  
`hasScreenBroadcast` | `SB`  
`hasScreenPlayback` | `SP`  
`hasStreamingAudio` | `SA`  
`hasStreamingVideo` | `SV`  
`hasTLS` | `TLS`  
`hasVideoEncoder` | `VE`  
`isDebugger` | `DEB`  
`language` | `L`  
`localFileReadDisable` | `LFD`  
`manufacturer` | `M`  
`maxLevelIDC` | `ML`  
`os` | `OS`  
`pixelAspectRatio` | `AR`  
`playerType` | `PT`  
`screenColor` | `COL`  
`screenDPI` | `DP`  
`screenResolutionX` | `R`  
`screenResolutionY` | `R`  
`version` | `V`  
`supports Dolby Digital audio` | `DD`  
`supports Dolby Digital Plus audio` | `DDP`  
`supports DTS audio` | `DTS`  
`supports DTS Express audio` | `DTE`  
`supports DTS-HD High Resolution Audio` | `DTH`  
`supports DTS-HD Master Audio` | `DTM`  
  
There is also a `WD` server string that specifies whether windowless mode is disabled. Windowless mode can be disabled in Flash Player due to incompatibility with the web browser or to a user setting in the mms.cfg file. There is no corresponding Capabilities property.

All properties of the Capabilities class are read-only.

[View the examples.](#includeExamplesSummary)

  

* * *