# Textfield

Package| [flash.text](package-detail.html)  
---|---  
Class| public class TextField  
Inheritance| TextField ![Inheritance](../../images/inherit-arrow.gif) [InteractiveObject](../display/InteractiveObject.html) ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](../display/DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The TextField class is used to create display objects for text display and input. You can use the TextField class to perform low-level text rendering. However, in Flex, you typically use the Label, Text, TextArea, and TextInput controls to process text. You can give a text field an instance name in the Property inspector and use the methods and properties of the TextField class to manipulate it with ActionScript. TextField instance names are displayed in the Movie Explorer and in the Insert Target Path dialog box in the Actions panel.

To create a text field dynamically, use the `TextField()` constructor.

The methods of the TextField class let you set, select, and manipulate text in a dynamic or input text field that you create during authoring or at runtime. 

ActionScript provides several ways to format your text at runtime. The TextFormat class lets you set character and paragraph formatting for TextField objects. You can apply Cascading Style Sheets (CSS) styles to text fields by using the `TextField.styleSheet` property and the StyleSheet class. You can use CSS to style built-in HTML tags, define new formatting tags, or apply styles. You can assign HTML formatted text, which optionally uses CSS styles, directly to a text field. HTML text that you assign to a text field can contain embedded media (movie clips, SWF files, GIF files, PNG files, and JPEG files). The text wraps around the embedded media in the same way that a web browser wraps text around media embedded in an HTML document. 

Flash Player supports a subset of HTML tags that you can use to format text. See the list of supported HTML tags in the description of the `htmlText` property.

[View the examples.](#includeExamplesSummary)

See also

[flash.text.TextFormat](../text/TextFormat.html)   
[flash.text.StyleSheet](../text/StyleSheet.html)   
[htmlText](../text/TextField.html#htmlText)

  

* * *