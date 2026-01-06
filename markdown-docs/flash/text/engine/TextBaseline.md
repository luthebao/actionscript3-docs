# Textbaseline

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public final class TextBaseline  
Inheritance| TextBaseline ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5  
---|---  
  
The TextBaseline class is an enumeration of constant values to use in setting the `dominantBaseline` and `alignmentBaseline` properties of the ElementFormat class. You can also use it in the `baselineZero` property of the TextBlock class. Consider this situation: 

![Text baseline alignment](../../../images/textBaselines.gif)

The line consists of four `TextElement` objects, containing 'a', 'b', 'cccccccc', and 'X' respectively. The element containing 'X' determines the line baselines because it is the largest element in the line. The roman baseline of the 'X' element is aligned with the roman baseline of the line. The ideographic top of the 'a' element is aligned with the ideographic top of the line. The ideographic bottom of the 'b' element is aligned with the ideographic bottom of the line. The ideographic center of the 'cccccccc' element is aligned with the ideographic center of the line.

See also

[ElementFormat.dominantBaseline](ElementFormat.html#dominantBaseline)   
[ElementFormat.alignmentBaseline](ElementFormat.html#alignmentBaseline)   
[TextBlock.baselineZero](TextBlock.html#baselineZero)

  

* * *