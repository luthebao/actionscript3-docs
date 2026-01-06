# Updater

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public final class Updater  
Inheritance| Updater ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The Updater class is used to update the currently running application with a different version. To use it, instantiate an Updater object and then call its `update()` method. 

The Updater class is only supported in the desktop profile. It is not supported for extended desktop applications (applications installed with a native installer), and it is not supported on the AIR mobile profile or AIR for TV profiles. Check the `Updater.isSupported` property.

Extended desktop application (applications installed with a native installer) can download a new version of the native installer and launch it using the `File.openWithDefaultApplication()` method.

See also

[air.update.ApplicationUpdater](../../air/update/ApplicationUpdater.html)   
[air.update.ApplicationUpdaterUI](../../air/update/ApplicationUpdaterUI.html)

  

* * *