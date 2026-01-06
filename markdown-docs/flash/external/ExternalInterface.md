# Externalinterface

Package| [flash.external](package-detail.html)  
---|---  
Class| public final class ExternalInterface  
Inheritance| ExternalInterface ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The ExternalInterface class is an application programming interface that enables straightforward communication between ActionScript and the SWF container– for example, an HTML page with JavaScript or a desktop application that uses Flash Player to display a SWF file. 

Using the ExternalInterface class, you can call an ActionScript function in the Flash runtime, using JavaScript in the HTML page. The ActionScript function can return a value, and JavaScript receives it immediately as the return value of the call.

This functionality replaces the `fscommand()` method.

Use the ExternalInterface class in the following combinations of browser and operating system:

Browser | Operating System | Operating System  
---|---|---  
Internet Explorer 5.0 and later |  Windows  |   
Netscape 8.0 and later |  Windows  |  MacOS   
Mozilla 1.7.5 and later |  Windows  |  MacOS   
Firefox 1.0 and later |  Windows  |  MacOS   
Safari 1.3 and later |  |  MacOS   
  
Flash Player for Linux version 9.0.31.0 and later supports the ExternalInterface class in the following browsers:

Browser  
---  
Mozilla 1.7.x and later  
Firefox 1.5.0.7 and later  
SeaMonkey 1.0.5 and later   
  
The ExternalInterface class requires the user's web browser to support either ActiveX® or the NPRuntime API that is exposed by some browsers for plug-in scripting. Even if a browser and operating system combination are not listed above, they should support the ExternalInterface class if they support the NPRuntime API. See <http://www.mozilla.org/projects/plugins/npruntime.html>.

**Note:** When embedding SWF files within an HTML page, make sure that the `id` attribute is set and the `id` and `name` attributes of the `object` and `embed` tags do not include the following characters:
    
    
     . - + * / \
     

**Note for Flash Player applications:** Flash Player version 9.0.115.0 and later allows the `.` (period) character within the `id` and `name` attributes.

**Note for Flash Player applications:** In Flash Player 10 and later running in a browser, using this class programmatically to open a pop-up window may not be successful. Various browsers (and browser configurations) may block pop-up windows at any time; it is not possible to guarantee any pop-up window will appear. However, for the best chance of success, use this class to open a pop-up window only in code that executes as a direct result of a user action (for example, in an event handler for a mouse click or key-press event.)

From ActionScript, you can do the following on the HTML page: 

  * Call any JavaScript function.
  * Pass any number of arguments, with any names.
  * Pass various data types (Boolean, Number, String, and so on).
  * Receive a return value from the JavaScript function.

From JavaScript on the HTML page, you can: 

  * Call an ActionScript function.
  * Pass arguments using standard function call notation.
  * Return a value to the JavaScript function.

**Note for Flash Player applications:** Flash Player does not currently support SWF files embedded within HTML forms.

**Note for AIR applications:** In Adobe AIR, the ExternalInterface class can be used to communicate between JavaScript in an HTML page loaded in the HTMLLoader control and ActionScript in SWF content embedded in that HTML page.

[View the examples.](#includeExamplesSummary)

See also

[fscommand()](../../flash/system/package.html#fscommand\(\))

  

* * *