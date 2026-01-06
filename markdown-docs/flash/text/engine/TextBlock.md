# Textblock

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public final class TextBlock  
Inheritance| TextBlock ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The TextBlock class is a factory for the creation of TextLine objects, which you can render by placing them on the display list. 

The TextBlock class is intended to contain a single paragraph because the Unicode bidirectional and line-break algorithms operate on one paragraph at a time. For applications that compose multiple paragraphs of text, use a markup language, or text analysis to divide the text into paragraphs and create one TextBlock per paragraph.

The TextBlock object stores its content in the `content` property, which is an instance of the ContentElement class. Because you can't create an instance of the ContentElement class, set `content` to an instance of one of its subclasses: TextElement, GraphicElement, or GroupElement. Use TextElement for purely text content, GraphicElement for an image or graphic content, and GroupElement for content that contains a combination of TextElement, GraphicElement, and other GroupElement objects. See the ContentElement class and its subclasses for details on managing formatted runs of text, embedded sub-runs, and graphic elements.

After you create the TextBlock instance and set the `content` property, call the `createTextLine()` method to create lines of text, which are instances of the `TextLine` class. 

[View the examples.](#includeExamplesSummary)

See also

[ContentElement](ContentElement.html)   
[GraphicElement](GraphicElement.html)   
[GroupElement](GroupElement.html)   
[TextBaseline](TextBaseline.html)   
[TextElement](TextElement.html)   
[TextJustifier](TextJustifier.html)   
[TextLine](TextLine.html)   
[TextRotation](TextRotation.html)   
[TabStop](TabStop.html)

  

* * *