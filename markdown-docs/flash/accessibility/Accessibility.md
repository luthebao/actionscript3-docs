# Accessibility

Package| [flash.accessibility](package-detail.html)  
---|---  
Class| public final class Accessibility  
Inheritance| Accessibility ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Accessibility class manages communication with screen readers. Screen readers are a type of assistive technology for visually impaired users that provides an audio version of screen content. The methods of the Accessibility class are static—that is, you don't have to create an instance of the class to use its methods. 

**Mobile Browser Support:** This class is not supported in mobile browsers.

_AIR profile support:_ This feature is supported on all desktop operating systems, but is not supported on mobile devices or on AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

To get and set accessible properties for a specific object, such as a button, movie clip, or text field, use the `DisplayObject.accessibilityProperties` property. To determine whether the player or runtime is running in an environment that supports accessibility aids, use the `Capabilities.hasAccessibility` property. 

**Note:** AIR 2 supports the JAWS 11 (or higher) screen reader software. For additional information, please see http://www.adobe.com/accessibility/.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.DisplayObject.accessibilityProperties](../display/DisplayObject.html#accessibilityProperties)   
[flash.system.Capabilities.hasAccessibility](../system/Capabilities.html#hasAccessibility)   
[Socket](../net/Socket.html)   
<http://www.adobe.com/accessibility/>

  

* * *