# Applicationdomain

Package| [flash.system](package-detail.html)  
---|---  
Class| public final class ApplicationDomain  
Inheritance| ApplicationDomain ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The ApplicationDomain class is a container for discrete groups of class definitions. Application domains are used to partition classes that are in the same security domain. They allow multiple definitions of the same class to exist and allow children to reuse parent definitions. 

Application domains are used when an external SWF file is loaded through the Loader class. All ActionScript 3.0 definitions in the loaded SWF file are stored in the application domain, which is specified by the `applicationDomain` property of the LoaderContext object that you pass as a `context` parameter of the Loader object's `load()` or `loadBytes()` method. The LoaderInfo object also contains an `applicationDomain` property, which is read-only.

All code in a SWF file is defined to exist in an application domain. The current application domain is where your main application runs. The system domain contains all application domains, including the current domain, which means that it contains all Flash Player classes.

Every application domain, except the system domain, has an associated parent domain. The parent domain of your main application's application domain is the system domain. Loaded classes are defined only when their parent doesn't already define them. You cannot override a loaded class definition with a newer definition.

For usage examples of application domains, see the _ActionScript 3.0 Developer's Guide_.

The `ApplicationDomain()` constructor function allows you to create an ApplicationDomain object.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.Loader.load()](../display/Loader.html#load\(\))   
[flash.display.Loader.loadBytes()](../display/Loader.html#loadBytes\(\))   
[flash.display.LoaderInfo](../display/LoaderInfo.html)   
[flash.net.URLRequest](../net/URLRequest.html)   
[flash.system.LoaderContext](../system/LoaderContext.html)

  

* * *