# Qname

Package| [Top Level](package-detail.html)  
---|---  
Class| public final class QName  
Inheritance| QName ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
QName objects represent qualified names of XML elements and attributes. Each QName object has a local name and a namespace Uniform Resource Identifier (URI). When the value of the namespace URI is `null`, the QName object matches any namespace. Use the QName constructor to create a new QName object that is either a copy of another QName object or a new QName object with a `uri` from a Namespace object and a `localName` from a QName object. 

Methods specific to E4X can use QName objects interchangeably with strings. E4X methods are in the QName, Namespace, XML, and XMLList classes. These E4X methods, which take a string, can also take a QName object. This interchangeability is how namespace support works with, for example, the `XML.child()` method. 

The QName class (along with the XML, XMLList, and Namespace classes) implements powerful XML-handling standards defined in ECMAScript for XML (E4X) specification (ECMA-357 edition 2).

A qualified identifier evaluates to a QName object. If the QName object of an XML element is specified without identifying a namespace, the `uri` property of the associated QName object is set to the global default namespace. If the QName object of an XML attribute is specified without identifying a namespace, the `uri` property is set to an empty string.

[View the examples.](#includeExamplesSummary)

See also

[XML](XML.html)   
[XMLList](XMLList.html)   
[Namespace](Namespace.html)   
[ECMAScript for XML (E4X) specification (ECMA-357 edition 2)](http://www.ecma-international.org/publications/standards/Ecma-357.htm)

  

* * *