# Htmlhost

Package| [flash.html](package-detail.html)  
---|---  
Class| public class HTMLHost  
Inheritance| HTMLHost ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Runtime version:**|  AIR 1.0   
---|---  
  
An HTMLHost object defines behaviors of an HTMLLoader object for user interface elements that can be controlled by setting various properties or by calling various methods of the `window` object of the HTML page. These methods and properties are: 

  * `window.blur()`
  * `window.focus()`
  * `window.moveBy()`
  * `window.moveTo()`
  * `window.location`
  * `window.close()`
  * `window.open()`
  * `window.resizeBy()`
  * `window.resizeTo()`
  * `window.status`
  * `window.document.title`

The methods in the HTMLHost class provide ways of handling changes in each of these `window` settings. To use this class, create a new class (a subclass) that extends the HTMLHost class and that overrides the methods for which you want to define behaviors. The methods of the HTMLHost class handle JavaScript properties and methods as follows:

JavaScript property or method | HTMLHost method  
---|---  
`window.blur()` | `windowBlur()`  
`window.focus()` | `windowFocus`  
`window.location` | `updateLocation`  
`window.close()` | `windowClose`  
`window.open()` | `createWindow`  
`window.status` | `updateStatus`  
`window.document.title` | `updateTitle`  
  
To respond to changes in the `window.moveBy()`, `window.moveTo()`, `window.resizeBy()`, and `window.resizeTo()` methods, override the `set windowRect()` method in the subclass of HTMLHost.

Each HTMLHost object can be associated with at most one HTMLLoader object. Assigning an HTMLHost instance to the `htmlHost` property of the HTMLLoader object establishes this relationship. Assigning `null` to the `htmlHost` property of the HTMLLoader object or setting the HTMLHost object as the `htmlHost` property of another HTMLLoader object removes the HTMLHost from the first HTMLLoader object.

[View the examples.](#includeExamplesSummary)

See also

[HTMLLoader](HTMLLoader.html)   
[HTMLWindowCreateOptions](HTMLWindowCreateOptions.html)

  

* * *