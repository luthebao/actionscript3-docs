# Hostobject

Package| [flash.external](package-detail.html)  
---|---  
Class| public dynamic class HostObject  
Inheritance| HostObject ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
The HostObject is the base class of all host objects. It can either be used directly, as it is a completely dynamic object, or via derived classes that implement known elements complete with type declarations; these implementations would call one of the protected methods below for direct access to host object elements. 

HostObjects support enumeration as well as dynamic lookup. It is, therefore, possible to use HostObjects as such, without having to create ActionScript wrappers for each host object class.

  

* * *