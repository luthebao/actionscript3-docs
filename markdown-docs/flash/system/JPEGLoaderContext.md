# Jpegloadercontext

Package| [flash.system](package-detail.html)  
---|---  
Class| public class JPEGLoaderContext  
Inheritance| JPEGLoaderContext ![Inheritance](../../images/inherit-arrow.gif) [LoaderContext](LoaderContext.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.5   
---|---  
  
The JPEGLoaderContext class includes a property for enabling a deblocking filter when loading a JPEG image. The deblocking filter improves an image's quality at higher compression settings by smoothing neighboring pixels. To apply deblocking when loading a JPEG image, create a JPEGLoaderContext object, and set its `deblockingFilter` property. Then use the JPEGLoaderContext object name as the value of the `context` parameter of the `load()` method of the Loader object used to load the image. 

The JPEGLoaderContext class extends the LoaderContext class. Set the `checkPolicyFile` property to `true` if you need programmatic access to the pixels of the loaded image (for example, if you're using the `BitmapData.draw()` method). Setting the `checkPolicyFile` property is not necessary for AIR content running in the application sandbox.

See also

[flash.display.Loader.load()](../display/Loader.html#load\(\))   
[flash.display.BitmapData.draw()](../display/BitmapData.html#draw\(\))

  

* * *