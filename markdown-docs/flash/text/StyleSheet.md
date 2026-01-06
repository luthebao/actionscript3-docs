# Stylesheet

Package| [flash.text](package-detail.html)  
---|---  
Class| public dynamic class StyleSheet  
Inheritance| StyleSheet ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The StyleSheet class lets you create a StyleSheet object that contains text formatting rules for font size, color, and other styles. You can then apply styles defined by a style sheet to a TextField object that contains HTML- or XML-formatted text. The text in the TextField object is automatically formatted according to the tag styles defined by the StyleSheet object. You can use text styles to define new formatting tags, redefine built-in HTML tags, or create style classes that you can apply to certain HTML tags. 

To apply styles to a TextField object, assign the StyleSheet object to a TextField object's `styleSheet` property.

**Note:** A text field with a style sheet is not editable. In other words, a text field with the `type` property set to `TextFieldType.INPUT` applies the StyleSheet to the default text for the text field, but the content will no longer be editable by the user. Consider using the TextFormat class to assign styles to input text fields.

Flash Player supports a subset of properties in the original CSS1 specification ([www.w3.org/TR/REC-CSS1](http://www.w3.org/TR/REC-CSS1)). The following table shows the supported Cascading Style Sheet (CSS) properties and values, as well as their corresponding ActionScript property names. (Each ActionScript property name is derived from the corresponding CSS property name; if the name contains a hyphen, the hyphen is omitted and the subsequent character is capitalized.)

CSS property | ActionScript property | Usage and supported values  
---|---|---  
`color` | `color` | Only hexadecimal color values are supported. Named colors (such as `blue`) are not supported. Colors are written in the following format: `#FF0000`.  
`display` | `display` | Supported values are `inline`, `block`, and `none`.  
`font-family` | `fontFamily` | A comma-separated list of fonts to use, in descending order of desirability. Any font family name can be used. If you specify a generic font name, it is converted to an appropriate device font. The following font conversions are available: `mono` is converted to `_typewriter`, `sans-serif` is converted to `_sans`, and `serif` is converted to `_serif`.  
`font-size` | `fontSize` | Only the numeric part of the value is used. Units (px, pt) are not parsed; pixels and points are equivalent.  
`font-style` | `fontStyle` | Recognized values are `normal` and `italic`.  
`font-weight` | `fontWeight` | Recognized values are `normal` and `bold`.  
`kerning` | `kerning` | Recognized values are `true` and `false`. Kerning is supported for embedded fonts only. Certain fonts, such as Courier New, do not support kerning. The kerning property is only supported in SWF files created in Windows, not in SWF files created on the Macintosh. However, these SWF files can be played in non-Windows versions of Flash Player and the kerning still applies.  
`leading` | `leading` | The amount of space that is uniformly distributed between lines. The value specifies the number of pixels that are added after each line. A negative value condenses the space between lines. Only the numeric part of the value is used. Units (px, pt) are not parsed; pixels and points are equivalent.  
`letter-spacing` | `letterSpacing` | The amount of space that is uniformly distributed between characters. The value specifies the number of pixels that are added after each character. A negative value condenses the space between characters. Only the numeric part of the value is used. Units (px, pt) are not parsed; pixels and points are equivalent.  
`margin-left` | `marginLeft` | Only the numeric part of the value is used. Units (px, pt) are not parsed; pixels and points are equivalent.   
`margin-right` | `marginRight` | Only the numeric part of the value is used. Units (px, pt) are not parsed; pixels and points are equivalent.  
`text-align` | `textAlign` | Recognized values are `left`, `center`, `right`, and `justify`.  
`text-decoration` | `textDecoration` | Recognized values are `none` and `underline`.  
`text-indent` | `textIndent` | Only the numeric part of the value is used. Units (px, pt) are not parsed; pixels and points are equivalent.   
  
You can use the StyleSheet class to perform low-level text rendering. However, in Flex, you typically use the Label, Text, TextArea, and TextInput controls to process text.

[View the examples.](#includeExamplesSummary)

See also

[flash.text.TextField](../text/TextField.html)

  

* * *