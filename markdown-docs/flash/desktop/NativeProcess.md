# Nativeprocess

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public class NativeProcess  
Inheritance| NativeProcess ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The NativeProcess class provides command line integration and general launching capabilities. The NativeProcess class lets an AIR application execute native processes on the host operating system. The AIR applcation can monitor the standard input (stdin) and standard output (stdout) stream of the process as well as the process's standard error (stderr) stream. 

The NativeProcess class and its capabilities are only available to AIR applications installed with a native installer (extended desktop profile applications). When debugging, you can pass the `-profile extendedDesktop` argument to ADL to enable the NativeProcess functionality. At runtime, you can check the `NativeProcess.isSupported` property to to determine whether native process communication is supported. 

_AIR profile support:_ This feature is supported on applications that are deployed to desktop operating systems via native installers. The feature is not supported on mobile devices or on AIR for TV devices. You can test for support at run time using the `NativeProcess.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

AIR applications installed with a native installer (extended desktop profile applications) can also use the `File.openWithDefaultApplication` to open an application. However, the NativeProcess class provides direct access to the standard input, standard output, and standard error pipes.

**Note:** AIR for TV applications using the `extendedTV` profile can use native extensions to execute native processes. Similarly, mobile devices can use native extensions.

[View the examples.](#includeExamplesSummary)

See also

[flash.external.ExtensionContext](../external/ExtensionContext.html)

  

* * *