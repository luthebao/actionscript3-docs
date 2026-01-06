# Keyboardevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class KeyboardEvent  
Inheritance| KeyboardEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
A KeyboardEvent object id dispatched in response to user input through a keyboard. There are two types of keyboard events: `KeyboardEvent.KEY_DOWN` and `KeyboardEvent.KEY_UP`

Because mappings between keys and specific characters vary by device and operating system, use the TextEvent event type for processing character input.

To listen globally for key events, listen on the Stage for the capture and target or bubble phase.

[View the examples.](#includeExamplesSummary)

See also

[KEY_DOWN](../events/KeyboardEvent.html#KEY_DOWN)   
[KEY_UP](../events/KeyboardEvent.html#KEY_UP)   
[KeyLocation](../ui/KeyLocation.html)

  

* * *