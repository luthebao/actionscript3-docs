# Textformat

Package| [flash.text](package-detail.html)  
---|---  
Class| public class TextFormat  
Inheritance| TextFormat ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The TextFormat class represents character formatting information. Use the TextFormat class to create specific text formatting for text fields. You can apply text formatting to both static and dynamic text fields. The properties of the TextFormat class apply to device and embedded fonts. However, for embedded fonts, bold and italic text actually require specific fonts. If you want to display bold or italic text with an embedded font, you need to embed the bold and italic variations of that font. 

You must use the constructor `new TextFormat()` to create a TextFormat object before setting its properties. When you apply a TextFormat object to a text field using the `TextField.defaultTextFormat` property or the `TextField.setTextFormat()` method, only its defined properties are applied. Use the `TextField.defaultTextFormat` property to apply formatting BEFORE you add text to the `TextField`, and the `setTextFormat()` method to add formatting AFTER you add text to the `TextField`. The TextFormat properties are `null` by default because if you don't provide values for the properties, Flash Player uses its own default formatting. The default formatting that Flash Player uses for each property (if property's value is `null`) is as follows:

align = "left"  
---  
blockIndent = 0  
bold = false  
bullet = false  
color = 0x000000  
font = "Times New Roman" (default font is Times on Mac OS X)  
indent = 0  
italic = false  
kerning = false  
leading = 0  
leftMargin = 0  
letterSpacing = 0  
rightMargin = 0  
size = 12  
tabStops = [] (empty array)  
target = "" (empty string)  
underline = false  
url = "" (empty string)  
  
The default formatting for each property is also described in each property description.

[View the examples.](#includeExamplesSummary)

See also

[flash.text.TextField.setTextFormat()](../text/TextField.html#setTextFormat\(\))   
[flash.text.TextField.defaultTextFormat](../text/TextField.html#defaultTextFormat)   
[flash.text.TextField.getTextFormat()](../text/TextField.html#getTextFormat\(\))

  

* * *