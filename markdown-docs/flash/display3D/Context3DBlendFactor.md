# Context3Dblendfactor

Package| [flash.display3D](package-detail.html)  
---|---  
Class| public final class Context3DBlendFactor  
Inheritance| Context3DBlendFactor ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
Defines the values to use for specifying the source and destination blend factors. 

A blend factor represents a particular four-value vector that is multiplied with the source or destination color in the blending formula. The blending formula is:

`result = source * sourceFactor + destination * destinationFactor`

In the formuls, the source color is the output color of the pixel shader program. The destination color is the color that currently exists in the color buffer, as set by previous clear and draw operations.

For example, if the source color is (.6, .6, .6, .4) and the source blend factor is `Context3DBlendFactor.ONE_MINUS_SOURCE_ALPHA`, then the source part of the blending equation is calculated as:

`(.6, .6, .6, .4) * (1-0.4, 1-0.4, 1-0.4, 1-0.4) = (.36, .36, .36, .24)`

The final calculation is clamped to the range [0,1].

**Examples**

The following examples demonstrate the blending math using source color = (.6,.4,.2,.4), destination color = (.8,.8,.8,.5), and various blend factors.

Purpose| Source factor| Destination factor| Blend formula| Result  
---|---|---|---|---  
No blending| ONE| ZERO | (.6,.4,.2,.4) * ( 1, 1, 1, 1) + (.8,.8,.8,.5) * ( 0, 0, 0, 0)| ( .6, .4, .2, .4)  
Alpha| SOURCE_ALPHA| ONE_MINUS_SOURCE_ALPHA| (.6,.4,.2,.4) * (.4,.4,.4,.4) + (.8,.8,.8,.5) * (.6,.6,.6,.6)| (.72,.64,.56,.46)  
Additive| ONE| ONE | (.6,.4,.2,.4) * ( 1, 1, 1, 1) + (.8,.8,.8,.5) * ( 1, 1, 1, 1)| ( 1, 1, 1, .9)  
Multiply| DESTINATION_COLOR| ZERO | (.6,.4,.2,.4) * (.8,.8,.8,.5) + (.8,.8,.8,.5) * ( 0, 0, 0, 0)| (.48,.32,.16, .2)  
Screen| ONE| ONE_MINUS_SOURCE_COLOR | (.6,.4,.2,.4) * ( 1, 1, 1, 1) + (.8,.8,.8,.5) * (.4,.6,.8,.6)| (.92,.88,.68, .7)  
  
Note that not all combinations of blend factors are useful and that you can sometimes achieve the same effect in different ways.

See also

[Context3D.setBlendFactors()](Context3D.html#setBlendFactors\(\))

  

* * *