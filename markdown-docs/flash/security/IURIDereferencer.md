# Iuridereferencer

Package| [flash.security](package-detail.html)  
---|---  
Interface| public interface IURIDereferencer  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
IURIDereferencer defines an interface for objects that resolve URIs in an XML signature. 

The IURIDereferencer implementation is responsible for resolving the URIs specified in the SignedInfo elements of an XML signature file and returning the referenced data in an object, such as a ByteArray, that implements the IDataInput interface. In order to use the IURIDereferencer interface, you must create an ActionScript class that implements the interface. In JavaScript, you can use a `script` tag to load a SWF file that contains that ActionScript class.

The interface has one method: `dereference()`. A typical implementation might also require a method for passing the XML signature object containing the URIs to be resolved to the dereferencer.

The IURIDereferencer interface is used with the XMLSignatureValidator class.

See also

[XMLSignatureValidator](XMLSignatureValidator.html)   
[XMLSignatureValidator.uriDereferencer](XMLSignatureValidator.html#uriDereferencer)

  

* * *