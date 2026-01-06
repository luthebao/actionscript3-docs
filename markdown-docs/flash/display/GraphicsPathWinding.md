# Graphicspathwinding

Package| [flash.display](package-detail.html)  
---|---  
Class| public final class GraphicsPathWinding  
Inheritance| GraphicsPathWinding ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 1.5  
---|---  
  
The GraphicsPathWinding class provides values for the `flash.display.GraphicsPath.winding` property and the `flash.display.Graphics.drawPath()` method to determine the direction to draw a path. A clockwise path is positively wound, and a counter-clockwise path is negatively wound: 

![positive and negative winding directions](../../images/winding_positive_negative.gif)

When paths intersect or overlap, the winding direction determines the rules for filling the areas created by the intersection or overlap:

![a comparison of even-odd and non-zero winding rules](../../images/winding_rules_evenodd_nonzero.gif)

See also

[flash.display.GraphicsPath.winding](../display/GraphicsPath.html#winding)   
[flash.display.Graphics.drawPath()](../display/Graphics.html#drawPath\(\))

  

* * *