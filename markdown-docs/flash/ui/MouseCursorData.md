# Mousecursordata

Package| [flash.ui](package-detail.html)  
---|---  
Class| public final class MouseCursorData  
Inheritance| MouseCursorData ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.6   
---|---  
  
The MouseCursorData class lets you define the appearance of a "native" mouse cursor. 

To display the cursor, use the `Mouse.registerCursor()` function. To return control of the cursor image to the operating system, call `Mouse.unregisterCursor()`. Call `Mouse.supportsNativeCursor` to test whether native cursors are supported on the current computer.

The maximum cursor size is 32x32 pixels.Transparency is supported on most operating systems.

A native mouse cursor is implemented directly through the operating system cursor mechanism and is a more efficient means for displaying a custom cursor image than using a display object. You can animate the cursor by supplying more than one image in the `data` property and setting the frame rate. 

The cursor is only displayed within the bounds of the stage. Outside the stage, control of the cursor image returns to the operating system

[View the examples.](#includeExamplesSummary)

See also

[flash.ui.Mouse.cursor](../ui/Mouse.html#cursor)   
[AIR Cookbook: Native Mouse cursor for Flash Player 10.2+](http://cookbooks.adobe.com/post_Native_Mouse_cursor_for_Flash_Player_10_2_-18576.html)

  

* * *