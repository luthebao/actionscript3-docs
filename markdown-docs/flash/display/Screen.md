# Screen

Package| [flash.display](package-detail.html)  
---|---  
Class| public final class Screen  
Inheritance| Screen ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The Screen class provides information about the display screens available to this application. 

Screens are independent desktop areas within a possibly larger "virtual desktop." The origin of the virtual desktop is the top-left corner of the operating-system-designated main screen. Thus, the coordinates for the bounds of an individual display screen may be negative. There may also be areas of the virtual desktop that are not within any of the display screens.

The Screen class includes static class members for accessing the available screen objects and instance members for accessing the properties of an individual screen. Screen information should not be cached since it can be changed by a user at any time.

Note that there is not necessarily a one-to-one correspondance between screens and the physical monitors attached to a computer. For example, two monitors may display the same screen.

You cannot instantiate the Screen class directly. Calls to the `new Screen()` constructor throw an `ArgumentError` exception.

[View the examples.](#includeExamplesSummary)

  

* * *