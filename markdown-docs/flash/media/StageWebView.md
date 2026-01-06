# Stagewebview

Package| [flash.media](package-detail.html)  
---|---  
Class| public final class StageWebView  
Inheritance| StageWebView ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.5   
---|---  
  
The StageWebView class displays HTML content in a stage view port. 

The StageWebView class provides a simple means to display HTML content on devices where the HTMLLoader class is not supported. The class provides no interaction between ActionScript and the HTML content except through the methods and properties of the StageWebView class itself. There is, for example, no way to pass values or call functions between ActionScript and JavaScript.

_AIR profile support:_ This feature is supported on all desktop operating systems and mobile devices, but is not supported on AIR for TV devices. You can test for support at run time using the `StageWebView.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

On devices in the mobile and extended mobile profiles, the StageWebView class uses the system web control provided by the device operating system. Thus, the available features and rendering appearance may vary from device to device.

On android, inline HTML5 video is supported only if `<application android:hardwareAccelerated="true"/>` is included in the application descriptor.

On desktop computers (in the desktop and extended desktop profiles), the StageWebView class uses the system web control provided by the Flash Player plugin. The features available and rendering appearance are the same as those of the HTMLLoader class (without the close integration and script bridging between ActionScript and JavaScript provided by an HTMLLoader instance). Since the HTMLLoader class uses the internal AIR WebKit engine, concurrent use of StageWebView and HTMLLoader instances is strongly discouraged as it has undefined behavior and can possibly terminate the application.

The StageWebView class is NOT a display object and cannot be added to the Flash display list. Instead you display a StageWebView object by attaching it directly to a stage using the `stage` property. The StageWebView instance attached to a stage is displayed on top of any Flash display objects. You control the size and position of the rendering area with the `viewPort` property. There is no way to control the depth ordering of different StageWebView objects. Overlapping two instances is not recommended.

When the content within the StageWebView object has focus, the StageWebView object has the first opportunity to handle keyboard input. The stage to which the StageWebView object is attached dispatches any keyboard input that is not handled. The normal event capture/bubble cycle does not apply here since the StageWebView instance is not part of the display list.

In Android 3.0+, an application must enable hardware acceleration in the Android manifestAdditions element of the AIR application descriptor to display plug-in content in a StageWebView object.

[View the examples.](#includeExamplesSummary)

See also

[Enabling Flash Player and other plug-ins in a StageWebView object](http://help.adobe.com/en_US/air/build/WSfffb011ac560372f-5d0f4f25128cc9cd0cb-7ffe.html#WS365a66ad37c9f5102ec8a8ba12f2d91095a-8000)   
[HTMLLoader class](../../flash/html/HTMLLoader.html)

  

* * *