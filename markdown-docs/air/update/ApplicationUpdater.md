# Applicationupdater

Package| [air.update](package-detail.html)  
---|---  
Class| public class ApplicationUpdater  
Inheritance| ApplicationUpdater ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../../flash/events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The ApplicationUpdater class defines the basic functionality of the update framework for Adobe® AIR® applications, without providing any default user interface. (The ApplicationUpdaterUI class includes update functionality _and_ a default user interface.) 

This class is included in the applicationupdater_ui.swc file, included in the Adobe AIR SDK. The applicationupdater_ui.swc file is in the frameworks/libs/air directory of the AIR SDK.

Adobe® Flex™ Builder™ loads this class automatically when you create a project for Adobe AIR. You should include the SWC file when compiling the application using the Adobe® Flex™ SDK.

To use this class in JavaScript code, load the applicationupdater_ui.swf file. This file is provided in the frameworks/libs/air directory of the AIR SDK. The following code loads the SWF file:
    
    
    <script src="applicationupdater.swf" type="application/x-shockwave-flash">

Managing updates of applications can be complicated. The AIR update framework provides APIs to assist developers in providing good update capabilities in AIR applications. The functionality in the AIR update framework assists developers in the following:

  * Periodically checking for updates based on an interval or at the request of the user

  * Downloading AIR files (updates) from a web source

  * Alerting the user on the first run of the newly installed version

  * Confirming that the user wants to check for updates

  * Displaying information on the new update version to the user

  * Displaying download progress and error information to the user

The AIR update framework lets you store information about the update version of an AIR application in simple XML configuration files. For most applications, setting up these configuration files and including some basic code provides good update functionality to the end user.

Use the AIRUpdater class if you want to define your own user interface for use with the AIR update framework.

The update process includes a sequence of states. The `currentState` property of the updater object reflects the current state of the updater:

currentState value  |  Description   
---|---  
"UNINITIALIZED" | The updater has not been initialized.  
"INITIALIZING" | The updater is initializing.  
"READY" | The updater has been initialized  
"BEFORE_CHECKING" | The updater has not yet checked for the update descriptor file.  
"CHECKING" | The updater is checking for an update descriptor file.  
"AVAILABLE" | The update descriptor file is available.  
"DOWNLOADING" | The updater is downloading the AIR file.  
"DOWNLOADED" | The updater has downloaded the AIR file.  
"INSTALLING" | The updater is installing the AIR file.  
"PENDING_INSTALLING" | The updater has initialized and there are pending updates.  
  
When testing an application using the AIR Debug Launcher (ADL) application, attempting to update the application results in an IllegalOperationError exception.

The AIR update framework is only supported in the desktop profile. It is not supported for extended desktop applications (applications installed with a native installer), and it is not supported on the mobile profile (iPhone applications written with ActionScript 3.0). Check the `Updater.isSupported` property at runtime to see if the update framework is supported.

For details on using the AIR update framework, see the "Updating AIR Applications" chapter of [Building Adobe AIR Applications](http://help.adobe.com/en_US/air/build/index.html).

See also

[ApplicationUpdaterUI](ApplicationUpdaterUI.html)   
[flash.desktop.Updater](../../flash/desktop/Updater.html)

  

* * *