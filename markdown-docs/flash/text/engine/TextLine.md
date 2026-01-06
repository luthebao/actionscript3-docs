# Textline

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public final class TextLine  
Inheritance| TextLine ![Inheritance](../../../images/inherit-arrow.gif) [DisplayObjectContainer](../../display/DisplayObjectContainer.html) ![Inheritance](../../../images/inherit-arrow.gif) [InteractiveObject](../../display/InteractiveObject.html) ![Inheritance](../../../images/inherit-arrow.gif) [DisplayObject](../../display/DisplayObject.html) ![Inheritance](../../../images/inherit-arrow.gif) [EventDispatcher](../../events/EventDispatcher.html) ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The TextLine class is used to display text on the display list. 

You cannot create a TextLine object directly from ActionScript code. If you call `new TextLine()`, an exception is thrown. To create a TextLine object, call the `createTextLine()` method of a TextBlock.

The TextLine encapsulates the minimum information necessary to render its contents and to provide interactivity through some methods that describe the properties of the atoms of the line. The term atom refers to both graphic elements and characters (including groups of combining characters), the indivisible entities that make up a text line.

After normal event-dispatching for a text line finishes, if the line is valid, events are mirrored to the event dispatchers that are specified in the `eventMirror` properties of the content element objects that contributed to the text line. These objects are recorded in the `TextLine.mirrorRegions` property. The events are not mirrored if event propagation failed or was stopped, or if the text line is not valid.

Mirroring of mouse events is a special case. Because mirror regions aren't actually display objects, `mouseOver` and `mouseOut` events are simulated for them. `rollOver` and `rollOut` events are not simulated. All naturally occurring `mouseOver`, `mouseOut`, `rollOver` and `rollOut` events (whether targeted at the text line or at children of the text line) are ignored - they are not mirrored.

The origin of a text line object is the beginning of the baseline. If you don't set the vertical position (`y` property) of a line that contains Latin text on a Roman baseline, only the descenders of the text appear below the top of the Sprite to which you add the text line. See the following diagram:

![Text baselines](../../../images/TextLine.gif)

The TextLine class has several ancestor classes — DisplayObjectContainer, InteractiveObject, DisplayObject, and EventDispatcher — from which it inherits properties and methods. The following inherited properties are inapplicable to TextLine objects: 

  * `contextMenu`
  * `focusRect`
  * `tabChildren`
  * `tabEnabled`
  * `tabIndex`

If you try to set these properties, the text engine throws the error: IllegalOperationError. You can read these properties, but they always contain default values.

[View the examples.](#includeExamplesSummary)

See also

[ContentElement.eventMirror](ContentElement.html#eventMirror)   
[TextBlock.createTextLine()](TextBlock.html#createTextLine\(\))   
[TextLineValidity](TextLineValidity.html)

  

* * *