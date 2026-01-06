# Package

These functions can be used for debugging and profiling ActionScript code.

Public Functions

| Function| Defined by  
---|---|---  
|  |  [showRedrawRegions](#showRedrawRegions\(\))(on:[Boolean](../../Boolean.html), color:[uint](../../uint.html) = 0xFF0000):[void](../../specialTypes.html#void) Shows or hides redraw regions. | flash.profiler  
  
Function detail

showRedrawRegions| ()| function  
---|---|---  
  
`public function showRedrawRegions(on:[Boolean](../../Boolean.html), color:[uint](../../uint.html) = 0xFF0000):[void](../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Shows or hides redraw regions. Enables the debugger version of Flash® Player to outline the regions of the screen that are being redrawn (that is regions that are being updated). 

Parameters | `on:[Boolean](../../Boolean.html)` — Specifies whether to show or hide redraw regions. When set to `true`, the redraw rectangles are shown. When set to `false`, the redraw rectangles are hidden.   
---|---  
| `color:[uint](../../uint.html)` (default = `0xFF0000`)`` — Sets the color of the rectangles. If you do not specify this parameter, 0xFF0000 is used.   
  
[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:12 PM GMT+01:00\) : Package flash.profiler)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)