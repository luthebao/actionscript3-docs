# Graphicspath

Package| [flash.display](package-detail.html)  
---|---  
Class| public final class GraphicsPath  
Inheritance| GraphicsPath ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IGraphicsData](IGraphicsData.html), [IGraphicsPath](IGraphicsPath.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
A collection of drawing commands and the coordinate parameters for those commands. 

Use a GraphicsPath object with the `Graphics.drawGraphicsData()` method. Drawing a GraphicsPath object is the equivalent of calling the `Graphics.drawPath()` method. 

The GraphicsPath class also has its own set of methods (`curveTo()`, `lineTo()`, `moveTo()` `wideLineTo()` and `wideMoveTo()`) similar to those in the Graphics class for making adjustments to the `GraphicsPath.commands` and `GraphicsPath.data` vector arrays.

See also

[flash.display.Graphics.drawGraphicsData()](../display/Graphics.html#drawGraphicsData\(\))   
[flash.display.Graphics.drawPath()](../display/Graphics.html#drawPath\(\))

  

* * *