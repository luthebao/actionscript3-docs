# Interactiveicon

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public class InteractiveIcon  
Inheritance| InteractiveIcon ![Inheritance](../../images/inherit-arrow.gif) [Icon](Icon.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [DockIcon](../desktop/DockIcon.html), [SystemTrayIcon](../desktop/SystemTrayIcon.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The InteractiveIcon class is the base class for the operating system icons associated with applications. 

Use the `icon` property of the NativeApplication object to get an instance of the application icon. The icon type will be one of the subclasses of InteractiveIcon, either DockIcon on Mac OS X® or SystemTrayIcon on Windows® and Linux.

You cannot instantiate the InteractiveIcon class directly. Calls to the `new InteractiveIcon()` constructor will throw an ArgumentError exception.

See also

[flash.desktop.NativeApplication.icon](../desktop/NativeApplication.html#icon)   
[flash.desktop.NativeApplication.supportsDockIcon](../desktop/NativeApplication.html#supportsDockIcon)   
[flash.desktop.NativeApplication.supportsSystemTrayIcon](../desktop/NativeApplication.html#supportsSystemTrayIcon)

  

* * *