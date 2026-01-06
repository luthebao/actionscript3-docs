# Elementformat

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public final class ElementFormat  
Inheritance| ElementFormat ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The ElementFormat class represents formatting information which can be applied to a ContentElement. Use the ElementFormat class to create specific text formatting for the various subclasses of ContentElement. The properties of the ElementFormat class apply to device and embedded fonts. 

An ElementFormat object that is applied to a ContentElement in a TextBlock does not invalidate the TextBlock. Once an ElementFormat has been applied to a ContentElement, its `locked` property is set to `true`. The properties of a locked ElementFormat object cannot be changed. Instead, use the `clone()` method to create an unlocked copy of the object, which can be modified and assigned to the ContentElement.

[View the examples.](#includeExamplesSummary)

See also

[ContentElement.elementFormat](ContentElement.html#elementFormat)

  

* * *