# Fontdescription

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public final class FontDescription  
Inheritance| FontDescription ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The FontDescription class represents the information necessary to describe a font. 

A FontDescription object is applied to an ElementFormat, which is in turn applied to a ContentElement in a TextBlock. Once a FontDescription has been applied to an ElementFormat, its `locked` property is set to `true`. The properties of a locked FontDescription object cannot be changed. Instead, use the `clone()` method to create an unlocked copy of the object, which can be modified and assigned to the ElementFormat.

**Note:** FTE (Flash Text Engine) does not support Type 1 fonts or bitmap fonts such as Type 3, ATC, sfnt-wrapped CID, or Naked CID.

[View the examples.](#includeExamplesSummary)

See also

[ElementFormat.fontDescription](ElementFormat.html#fontDescription)

  

* * *