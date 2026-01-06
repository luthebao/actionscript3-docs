# Textrenderer

Package| [flash.text](package-detail.html)  
---|---  
Class| public final class TextRenderer  
Inheritance| TextRenderer ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The TextRenderer class provides functionality for the advanced anti-aliasing capability of embedded fonts. Advanced anti-aliasing allows font faces to render at very high quality at small sizes. Use advanced anti-aliasing with applications that have a lot of small text. Adobe does not recommend using advanced anti-aliasing for very large fonts (larger than 48 points). Advanced anti-aliasing is available in Flash Player 8 and later only. 

To set advanced anti-aliasing on a text field, set the `antiAliasType` property of the TextField instance.

Advanced anti-aliasing provides continuous stroke modulation (CSM), which is continuous modulation of both stroke weight and edge sharpness. As an advanced feature, you can use the `setAdvancedAntiAliasingTable()` method to define settings for specific typefaces and font sizes.

[View the examples.](#includeExamplesSummary)

See also

[flash.text.TextField.antiAliasType](../text/TextField.html#antiAliasType)

  

* * *