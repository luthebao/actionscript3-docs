# Accessibilityimplementation

Package| [flash.accessibility](package-detail.html)  
---|---  
Class| public class AccessibilityImplementation  
Inheritance| AccessibilityImplementation ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Runtime version:**|  AIR 2   
---|---  
  
The AccessibilityImplementation class is the base class in Flash Player that allows for the implementation of accessibility in components. This class enables communication between a component and a screen reader. Screen readers are used to translate screen content into synthesized speech or braille for visually impaired users. 

The AccessibilityImplementation class provides a set of methods that allow a component developer to make information about system roles, object based events, and states available to assistive technology.

Adobe Flash Player uses Microsoft Active Accessibility (MSAA), which provides a descriptive and standardized way for applications and screen readers to communicate. For more information on how the Flash Player works with MSAA, see the accessibility chapter in _Using Flex SDK_.

The methods of the AccessibilityImplementation class are a subset of the [IAccessible](http://msdn.microsoft.com/en-us/library/ms696097\(VS.85\).aspx) interface for a component instance.

The way that an AccessibilityImplementation implements the IAccessible interface, and the events that it sends, depend on the kind of component being implemented.

Do not directly instantiate AccessibilityImplementation by calling its constructor. Instead, create new accessibility implementations by extending the AccImpl class for each new component. In Flash, see the fl.accessibility package. In Flex, see the mx.accessibility package and the accessibility chapter in _Using Flex SDK_.

**Note:** The AccessibilityImplementation class is not supported in AIR runtime versions before AIR 2. The class is available for compilation in AIR versions before AIR 2, but is not supported in the runtime until AIR 2.

  

* * *