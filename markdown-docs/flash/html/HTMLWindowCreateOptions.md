# Htmlwindowcreateoptions

Package| [flash.html](package-detail.html)  
---|---  
Class| public class HTMLWindowCreateOptions  
Inheritance| HTMLWindowCreateOptions ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Runtime version:**|  AIR 1.0   
---|---  
  
This class defines the options that can be specified when JavaScript running in an HTMLLoader object tries to create a new HTML window by calling the `window.open()` method. 

This class defines the properties and methods that correspond to options in the `features` parameter passed to the `window.open()` method in JavaScript.

For example, JavaScript in an HTML document (in an HTMLLoader object) can include the following call to `window.open()`, in which the `features` parameter (the third parameter) lists a number of options:
    
    
    window.open("http://www.adobe.com", "AdobeWindow", "scrollbars=1,menubar=1,location=0,status=0")

You use the HTMLWindowCreateOptions class in overriding the `createWindow()` method of a subclass of the HTMLHost class. The HTMLLoader object passes an HTMLWindowCreateOptions object as the `windowCreateOptions` parameter of the `createWindow()` method of the HTMLHost object.

See also

[HTMLHost#createWindow()](HTMLHost.html#createWindow\(\))

  

* * *