# Loaderinfo

Package| [flash.display](package-detail.html)  
---|---  
Class| public class LoaderInfo  
Inheritance| LoaderInfo ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The LoaderInfo class provides information about a loaded SWF file or a loaded image file (JPEG, GIF, or PNG). LoaderInfo objects are available for any display object. The information provided includes load progress, the URLs of the loader and loaded content, the number of bytes total for the media, and the nominal height and width of the media. 

You can access LoaderInfo objects in two ways: 

  * The `contentLoaderInfo` property of a flash.display.Loader object— The `contentLoaderInfo` property is always available for any Loader object. For a Loader object that has not called the `load()` or `loadBytes()` method, or that has not sufficiently loaded, attempting to access many of the properties of the `contentLoaderInfo` property throws an error.
  * The `loaderInfo` property of a display object. 

The `contentLoaderInfo` property of a Loader object provides information about the content that the Loader object is loading, whereas the `loaderInfo` property of a DisplayObject provides information about the root SWF file for that display object. 

When you use a Loader object to load a display object (such as a SWF file or a bitmap), the `loaderInfo` property of the display object is the same as the `contentLoaderInfo` property of the Loader object (`DisplayObject.loaderInfo = Loader.contentLoaderInfo`). Because the instance of the main class of the SWF file has no Loader object, the `loaderInfo` property is the only way to access the LoaderInfo for the instance of the main class of the SWF file.

The following diagram shows the different uses of the LoaderInfo object—for the instance of the main class of the SWF file, for the `contentLoaderInfo` property of a Loader object, and for the `loaderInfo` property of a loaded object:

![An image of different LoaderInfo situations](../../images/loaderInfo_object.jpg)

When a loading operation is not complete, some properties of the `contentLoaderInfo` property of a Loader object are not available. You can obtain some properties, such as `bytesLoaded`, `bytesTotal`, `url`, `loaderURL`, and `applicationDomain`. When the `loaderInfo` object dispatches the `init` event, you can access all properties of the `loaderInfo` object and the loaded image or SWF file.

**Note:** All properties of LoaderInfo objects are read-only.

The `EventDispatcher.dispatchEvent()` method is not applicable to LoaderInfo objects. If you call `dispatchEvent()` on a LoaderInfo object, an IllegalOperationError exception is thrown.

[View the examples.](#includeExamplesSummary)

See also

[flash.display.Loader](../display/Loader.html)   
[flash.display.Loader.content](../display/Loader.html#content)   
[flash.display.DisplayObject](../display/DisplayObject.html)   
[flash.display.DisplayObject.loaderInfo](../display/DisplayObject.html#loaderInfo)

  

* * *