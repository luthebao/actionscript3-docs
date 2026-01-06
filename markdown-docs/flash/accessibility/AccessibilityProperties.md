# Accessibilityproperties

Package| [flash.accessibility](package-detail.html)  
---|---  
Class| public class AccessibilityProperties  
Inheritance| AccessibilityProperties ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|   
---|---  
  
The AccessibilityProperties class lets you control the presentation of Flash objects to accessibility aids, such as screen readers. 

You can attach an AccessibilityProperties object to any display object, but Flash Player will read your AccessibilityProperties object only for certain kinds of objects: entire SWF files (as represented by `DisplayObject.root`), container objects (`DisplayObjectContainer` and subclasses), buttons (`SimpleButton` and subclasses), and text (`TextField` and subclasses).

The `name` property of these objects is the most important property to specify because accessibility aids provide the names of objects to users as a basic means of navigation. Do not confuse `AccessibilityProperties.name` with `DisplayObject.name`; these are separate and unrelated. The `AccessibilityProperties.name` property is a name that is read aloud by the accessibility aids, whereas `DisplayObject.name` is essentially a variable name visible only to ActionScript code.

In Flash Professional, the properties of `AccessibilityProperties` objects override the corresponding settings available in the Accessibility panel during authoring.

To determine whether Flash Player is running in an environment that supports accessibility aids, use the `Capabilities.hasAccessibility` property. If you modify AccessibilityProperties objects, you need to call the `Accessibility.updateProperties()` method for the changes to take effect.

[View the examples.](#includeExamplesSummary)

See also

[flash.accessibility.Accessibility.updateProperties()](../accessibility/Accessibility.html#updateProperties\(\))   
[flash.display.DisplayObject.accessibilityProperties](../display/DisplayObject.html#accessibilityProperties)   
[flash.display.InteractiveObject.tabIndex](../display/InteractiveObject.html#tabIndex)   
[flash.system.Capabilities.hasAccessibility](../system/Capabilities.html#hasAccessibility)

  

* * *