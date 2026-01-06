# Contextmenu

Package| [flash.ui](package-detail.html)  
---|---  
Class| public final class ContextMenu  
Inheritance| ContextMenu ![Inheritance](../../images/inherit-arrow.gif) [NativeMenu](../display/NativeMenu.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The ContextMenu class provides control over the items displayed in context menus. 

**Mobile Browser Support:** This class is not supported in mobile browsers.

_AIR profile support:_ This feature is not supported on mobile devices or AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

In Flash Player, users open the context menu by right-clicking (Windows or Linux) or Control-clicking (Macintosh) Flash Player. You can use the methods and properties of the ContextMenu class to add custom menu items, control the display of the built-in context menu items (for example, Zoom In, and Print), or create copies of menus. In AIR, there are no built-in items and no standard context menu.

In Flash Professional, you can attach a ContextMenu object to a specific button, movie clip, or text field object, or to an entire movie level. You use the `contextMenu` property of the InteractiveObject class to do this.

In Flex or Flash Builder, only top-level components in the application can have context menus. For example, if a DataGrid control is a child of a TabNavigator or VBox container, the DataGrid control cannot have its own context menu.

To add new items to a ContextMenu object, you create a ContextMenuItem object, and then add that object to the `ContextMenu.customItems` array. For more information about creating context menu items, see the ContextMenuItem class entry.

Flash Player has three types of context menus: the standard menu (which appears when you right-click in Flash Player), the edit menu (which appears when you right-click a selectable or editable text field), and an error menu (which appears when a SWF file has failed to load into Flash Player). Only the standard and edit menus can be modified with the ContextMenu class. Only the edit menu appears in AIR.

Custom menu items always appear at the top of the Flash Player context menu, above any visible built-in menu items; a separator bar distinguishes built-in and custom menu items. You cannot remove the Settings menu item from the context menu. The Settings menu item is required in Flash so that users can access the settings that affect privacy and storage on their computers. You also cannot remove the About menu item, which is required so that users can find out what version of Flash Player they are using. (In AIR, the built-in Settings and About menu items are not used.)

You can add no more than 15 custom items to a context menu in Flash Player. In AIR, there is no explicit limit imposed on the number of items in a context menu.

You must use the `ContextMenu()` constructor to create a ContextMenu object before calling its methods.

[View the examples.](#includeExamplesSummary)

See also

[ContextMenuItem class](ContextMenuItem.html)   
[flash.display.InteractiveObject.contextMenu](../display/InteractiveObject.html#contextMenu)

  

* * *