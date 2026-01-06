# Nativewindow

Package| [flash.display](package-detail.html)  
---|---  
Class| public class NativeWindow  
Inheritance| NativeWindow ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The NativeWindow class provides an interface for creating and controlling native desktop windows. 

_AIR profile support:_ This feature is supported fully on desktop operating systems, has some limited (single-window) support on mobile devices, and is not supported on AIR for TV devices. You can test for support at run time on desktop devices using the `NativeWindow.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

On desktop operating systems, a reference to a new NativeWindow instance is returned by the window constructor. On mobile operating systems, attempting to create a new NativeWindow instance will throw an error - the only NativeWindow that exists is the initial application window with properties set via the application descriptor file, and accessed from the stage. The reference to the initial NativeWindow instance for an application can be accessed using the `stage.nativeWindow` property of any display object on that window's stage:
    
    
    var window:NativeWindow = displayObject.stage.nativeWindow;

On mobile operating systems, the window object cannot be modified, but can be used to listen for resize events (for example, on screen orientation changes) and for focus (activate/deactive) events. These can be separate from the `NativeApplication` events that describe the foreground/background mode of the application itself, and can be used to determine when other elements are hiding part of the window's display.

The properties of a NativeWindow instance can only be accessed by application content. If non-application content attempts to access the NativeWindow object, a security error will be thrown.

Content can be added to a window using the DisplayObjectContainer methods of the Stage object such as `addChild()`.

You cannot not add Flex components directly to the display list of a NativeWindow instance. Instead, use the Flex mx:WindowedApplication and mx:Window components to create your windows and add the other Flex components as children of those objects. You can add Flex-based SWF content directly to a NativeWindow window as long as the SWF file is loaded into its own application domain and is application content. 

The following operations on NativeWindow objects are asynchronous: `close()`, `maximize()`, `minimize()`, `restore()`, and `bounds` changes. An application can detect when these operations have completed by listening for the appropriate events. 

If the `NativeApplication.autoExit` property is `true`, which is the default, the application will close when its last window is closed (and all `close` event handlers have returned). If `autoExit` is `false`, then `NativeApplication.nativeApplication.exit()` must be called to terminate the application. 

NativeWindow objects will not be garbage collected after the window constructor has been called and before `close()` has been called. It is the responsibility of the application to close its own windows. 

See also

[flash.display.Stage.nativeWindow](../display/Stage.html#nativeWindow)   
[flash.display.NativeWindowInitOptions](../display/NativeWindowInitOptions.html)   
[flash.desktop.NativeApplication](../desktop/NativeApplication.html)   
[flash.system.ApplicationDomain](../system/ApplicationDomain.html)

  

* * *