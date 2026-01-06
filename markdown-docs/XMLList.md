# Xmllist

Package| [Top Level](package-detail.html)  
---|---  
Class| public final dynamic class XMLList  
Inheritance| XMLList ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The XMLList class contains methods for working with one or more XML elements. An XMLList object can represent one or more XML objects or elements (including multiple nodes or attributes), so you can call methods on the elements as a group or on the individual elements in the collection. 

If an XMLList object has only one XML element, you can use the XML class methods on the XMLList object directly. In the following example, `example.two` is an XMLList object of length 1, so you can call any XML method on it.
    
    
    
     var example2 = <example><two>2</two></example>;

If you attempt to use XML class methods with an XMLList object containing more than one XML object, an exception is thrown; instead, iterate over the XMLList collection (using a `for each..in` statement, for example) and apply the methods to each XML object in the collection.

[View the examples.](#includeExamplesSummary)

See also

[XML](XML.html)   
[for each..in](statements.html#for_each..in)   
[Namespace](Namespace.html)   
[QName](QName.html)

  

* * *