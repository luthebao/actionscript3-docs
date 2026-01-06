# Dockicon

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public class DockIcon  
Inheritance| DockIcon ![Inheritance](../../images/inherit-arrow.gif) [InteractiveIcon](InteractiveIcon.html) ![Inheritance](../../images/inherit-arrow.gif) [Icon](Icon.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The DockIcon class represents the Mac OS X®-style dock icon. 

_AIR profile support:_ This feature is supported on all desktop operating systems, but it is not supported on mobile devices or AIR for TV devices. You can test for support at run time using the `NativeApplication.supportsDockIcon` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

You can use the DockIcon class to change the appearance of the standard icon; for example, to animate the icon or add informational graphics. You can also add items to the dock icon menu. The menu items that you add are displayed above the standard menu items.

An instance of the DockIcon class cannot be created. Get the object representing the operating system dock icon from `NativeApplication.icon`. 

Not all operating systems have dock icons. Check `NativeApplication.supportsDockIcon` to determine whether dock icons are supported on the current system. If dock icons are supported, the `NativeApplication.icon` property is of type DockIcon. Otherwise, the type of `NativeApplication.icon` is another subclass of InteractiveIcon, typically SystemTrayIcon.

**Important:** Attempting to call a DockIcon class method on the `NativeApplication.icon` object on an operating system for which AIR does not support dock icons generates a run-time exception.

[View the examples.](#includeExamplesSummary)

See also

[flash.desktop.NativeApplication.icon](../desktop/NativeApplication.html#icon)   
[flash.desktop.NativeApplication.supportsDockIcon](../desktop/NativeApplication.html#supportsDockIcon)   
[flash.desktop.SystemTrayIcon](../desktop/SystemTrayIcon.html)

  

* * *