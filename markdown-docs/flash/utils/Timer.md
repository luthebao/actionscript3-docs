# Timer

Package| [flash.utils](package-detail.html)  
---|---  
Class| public class Timer  
Inheritance| Timer ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Timer class is the interface to timers, which let you run code on a specified time sequence. Use the `start()` method to start a timer. Add an event listener for the `timer` event to set up code to be run on the timer interval. 

You can create Timer objects to run once or repeat at specified intervals to execute code on a schedule. Depending on the SWF file's framerate or the runtime environment (available memory and other factors), the runtime may dispatch events at slightly offset intervals. For example, if a SWF file is set to play at 10 frames per second (fps), which is 100 millisecond intervals, but your timer is set to fire an event at 80 milliseconds, the event will be dispatched close to the 100 millisecond interval. Applications may dispatch events at slightly offset intervals based on the internal frame rate of the application. Memory-intensive scripts may also offset the events.

[View the examples.](#includeExamplesSummary)

  

* * *