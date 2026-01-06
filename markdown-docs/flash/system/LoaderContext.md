# Loadercontext

Package| [flash.system](package-detail.html)  
---|---  
Class| public class LoaderContext  
Inheritance| LoaderContext ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [JPEGLoaderContext](../system/JPEGLoaderContext.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The LoaderContext class provides options for loading SWF files and other media by using the Loader class. The LoaderContext class is used as the `context` parameter in the `load()` and `loadBytes()` methods of the Loader class. 

When loading SWF files with the `Loader.load()` method, you have two decisions to make: into which security domain the loaded SWF file should be placed, and into which application domain within that security domain? For more details on these choices, see the `applicationDomain` and `securityDomain` properties.

When loading a SWF file with the `Loader.loadBytes()` method, you have the same application domain choice to make as for `Loader.load()`, but it's not necessary to specify a security domain, because `Loader.loadBytes()` always places its loaded SWF file into the security domain of the loading SWF file.

When loading images (JPEG, GIF, or PNG) instead of SWF files, there is no need to specify a SecurityDomain or an application domain, because those concepts are meaningful only for SWF files. Instead, you have only one decision to make: do you need programmatic access to the pixels of the loaded image? If so, see the `checkPolicyFile` property. If you want to apply deblocking when loading an image, use the JPEGLoaderContext class instead of the LoaderContext class.

See also

[flash.display.Loader.load()](../display/Loader.html#load\(\))   
[flash.display.Loader.loadBytes()](../display/Loader.html#loadBytes\(\))   
[flash.system.ApplicationDomain](../system/ApplicationDomain.html)   
[flash.system.JPEGLoaderContext](../system/JPEGLoaderContext.html)   
[flash.system.LoaderContext.applicationDomain](../system/LoaderContext.html#applicationDomain)   
[flash.system.LoaderContext.checkPolicyFile](../system/LoaderContext.html#checkPolicyFile)   
[flash.system.LoaderContext.securityDomain](../system/LoaderContext.html#securityDomain)   
[flash.system.SecurityDomain](../system/SecurityDomain.html)   
[flash.system.ImageDecodingPolicy](../system/ImageDecodingPolicy.html)

  

* * *