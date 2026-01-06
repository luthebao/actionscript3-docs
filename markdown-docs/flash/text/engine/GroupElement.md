# Groupelement

Package| [flash.text.engine](package-detail.html)  
---|---  
Class| public final class GroupElement  
Inheritance| GroupElement ![Inheritance](../../../images/inherit-arrow.gif) [ContentElement](ContentElement.html) ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
A GroupElement object groups a collection of TextElement, GraphicElement, or other GroupElement objects that you can assign as a unit to the `content` property of a TextBlock object. A GroupElement object can also simply share common formatting within another GroupElement object. 

When a GroupElement contains another GroupElement, the inner GroupElement retains its own formatting (ElementFormat settings). It does not inherit the formatting of the outer GroupElement.

On a GroupElement, most of the format properties have no impact. For this reason, it is legal to create a text line for a GroupElement object that has a null `elementFormat` parameter. A few format properties such as `kerning` and `ligature` do affect formatting where intersections occur between members of the group. If the group has a null format, the format of the preceding element determines the formatting where intersections occur between members of the group.

[View the examples.](#includeExamplesSummary)

See also

[ContentElement](ContentElement.html)   
[GraphicElement](GraphicElement.html)   
[TextBlock](TextBlock.html)   
[TextElement](TextElement.html)

  

* * *