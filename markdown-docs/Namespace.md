# Namespace

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class Namespace  
Inheritance| Namespace ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Namespace class contains methods and properties for defining and working with namespaces. There are three scenarios for using namespaces: 

  * **Namespaces of XML objects** Namespaces associate a namespace prefix with a Uniform Resource Identifier (URI) that identifies the namespace. The prefix is a string used to reference the namespace within an XML object. If the prefix is undefined, when the XML is converted to a string, a prefix is automatically generated. 
  * **Namespace to differentiate methods** Namespaces can differentiate methods with the same name to perform different tasks. If two methods have the same name but separate namespaces, they can perform different tasks. 
  * **Namespaces for access control** Namespaces can be used to control access to a group of properties and methods in a class. If you place the properties and methods into a private namespace, they are inaccessible to any code that does not have access to that namespace. You can grant access to the group of properties and methods by passing the namespace to other classes, methods or functions. 

This class shows two forms of the constructor method because each form accepts different parameters.

This class (along with the XML, XMLList, and QName classes) implements powerful XML-handling standards defined in ECMAScript for XML (E4X) specification (ECMA-357 edition 2).

[View the examples.](#includeExamplesSummary)

See also

[XML](XML.html)   
[XMLList](XMLList.html)   
[QName](QName.html)   
[ECMAScript for XML (E4X) specification (ECMA-357 edition 2)](http://www.ecma-international.org/publications/standards/Ecma-357.htm)

  

* * *