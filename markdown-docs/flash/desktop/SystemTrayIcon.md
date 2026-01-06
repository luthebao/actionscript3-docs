# Systemtrayicon

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public class SystemTrayIcon  
Inheritance| SystemTrayIcon ![Inheritance](../../images/inherit-arrow.gif) [InteractiveIcon](InteractiveIcon.html) ![Inheritance](../../images/inherit-arrow.gif) [Icon](Icon.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The SystemTrayIcon class represents the Windows® taskbar notification area (system tray)-style icon. 

_AIR profile support:_ This feature is supported on desktop operating systems, but it is not supported on mobile devices or AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

Not all desktop operating systems have system tray icons. Check `NativeApplication.supportsSystemTrayIcon` to determine whether system tray icons are supported on the current system.

An instance of the SystemTrayIcon class cannot be created. Get the object representing the system tray icon from the `icon` property of the "global" NativeApplication object. 

When system tray icons are supported, the icon will be of type _SystemTrayIcon_. Otherwise, the type of `icon` will be another subclass of InteractiveIcon, typically DockIcon.

**Important:** Attempting to call a SystemTrayIcon class method on the `NativeApplication.icon` object on an operating system for which AIR does not support system tray icons will generate a run-time exception.

See also

[flash.desktop.NativeApplication.icon](../desktop/NativeApplication.html#icon)   
[flash.desktop.NativeApplication.supportsSystemTrayIcon](../desktop/NativeApplication.html#supportsSystemTrayIcon)   
[flash.desktop.DockIcon](../desktop/DockIcon.html)

  

* * *