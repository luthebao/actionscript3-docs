# Nativemenuitem

Package| [flash.display](package-detail.html)  
---|---  
Class| public class NativeMenuItem  
Inheritance| NativeMenuItem ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [ContextMenuItem](../ui/ContextMenuItem.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The NativeMenuItem class represents a single item in a menu. 

A menu item can be a command, a submenu, or a separator line:

  * To create a command item, call the NativeMenuItem constructor, passing in a string for the label and `false` for the `isSeparator` parameter.
  * To create a submenu, create a command item for the parent menu and assign the NativeMenu object of the submenu to the item's `submenu` property. You can also call the `addSubmenu()` method of the parent NativeMenu object to create the item and set the `submenu` property at the same time.
  * To create a separator, call the NativeMenuItem constructor, passing in an empty string for the label and `true` for the `isSeparator` parameter.

Listen for `select` events on an item or a parent menu to detect when a menu command is selected. Neither submenus nor separators dispatch select events. Listen for `preparing` events to determine when a menu item is about to be displayed or activated through a key equivalent.

See also

[flash.display.NativeMenu](../display/NativeMenu.html)   
[flash.display.NativeMenu.addSubmenu()](../display/NativeMenu.html#addSubmenu\(\))

  

* * *