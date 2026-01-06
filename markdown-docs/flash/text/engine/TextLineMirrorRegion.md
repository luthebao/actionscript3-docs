# Textlinemirrorregion

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public final class TextLineMirrorRegion  
Inheritance| TextLineMirrorRegion ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The TextLineMirrorRegion class represents a portion of a text line wherein events are mirrored to another event dispatcher. 

After normal event-dispatching for a text line finishes, if the line is valid and event propagation has not been stopped, events are re dispatched to the mirror regions of the line.

Mirroring of mouse events is a special case. Because mirror regions aren't actually display objects, `mouseOver` and `mouseOut` events are simulated for them. The `rollOver` and `rollOut` events are not simulated. All naturally occuring `mouseOver`, `mouseOut`, `rollOver` and `rollOut` events (whether targetted at the text line or at children of the text line) are ignored - they are not mirrored.

You cannot create a TextLineMirrorRegion object directly from ActionScript code. If you call `new TextLineMirrorRegion()`, an exception is thrown. A TextLineMirrorRegion is created and associated with a text line when that text line is created from a ContentElement object with an event mirror set.

The TextLineMirrorRegion class is final; it cannot be subclassed.

[View the examples.](#includeExamplesSummary)

See also

[ContentElement.eventMirror](ContentElement.html#eventMirror)   
[TextBlock.createTextLine()](TextBlock.html#createTextLine\(\))   
[TextLine.mirrorRegions](TextLine.html#mirrorRegions)

  

* * *