# Textjustifier

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public class TextJustifier  
Inheritance| TextJustifier ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
Subclasses| [EastAsianJustifier](../engine/EastAsianJustifier.html), [SpaceJustifier](../engine/SpaceJustifier.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The TextJustifier class is an abstract base class for the justifier types that you can apply to a TextBlock, specifically the EastAsianJustifier and SpaceJustifier classes. 

You cannot instantiate the TextJustifier class directly. Invoking `new TextJustifier()` throws an `ArgumentError` exception. Setting the properties of an EastAsianJustifier or SpaceJustifier object after you apply it to a TextBlock does not invalidate the TextBlock.

See also

[EastAsianJustifier](EastAsianJustifier.html)   
[SpaceJustifier](SpaceJustifier.html)   
[TextBlock.textJustifier](TextBlock.html#textJustifier)

  

* * *