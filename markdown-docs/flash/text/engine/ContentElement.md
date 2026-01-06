# Contentelement

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public class ContentElement  
Inheritance| ContentElement ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
Subclasses| [GraphicElement](../engine/GraphicElement.html), [GroupElement](../engine/GroupElement.html), [TextElement](../engine/TextElement.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The ContentElement class serves as a base class for the element types that can appear in a GroupElement, namely a GraphicElement, another GroupElement, or a TextElement. 

ContentElement is an abstract base class; therefore, you cannot instantiate ContentElement directly. Invoking `new ContentElement()` throws an `ArgumentError` exception. 

You can assign a ContentElement element to exactly one `GroupElement` or to the `content` property of exactly one text block.

See also

[ElementFormat](ElementFormat.html)   
[GraphicElement](GraphicElement.html)   
[GroupElement](GroupElement.html)   
[TextBlock.content](TextBlock.html#content)   
[TextElement](TextElement.html)   
[TextLineMirrorRegion](TextLineMirrorRegion.html)   
[TextRotation](TextRotation.html)

  

* * *