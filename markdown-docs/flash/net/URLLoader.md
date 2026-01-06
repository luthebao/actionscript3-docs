# Urlloader

Package| [flash.net](package-detail.html)  
---|---  
Class| public class URLLoader  
Inheritance| URLLoader ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The URLLoader class downloads data from a URL as text, binary data, or URL-encoded variables. It is useful for downloading text files, XML, or other information to be used in a dynamic, data-driven application. 

A URLLoader object downloads all of the data from a URL before making it available to code in the applications. It sends out notifications about the progress of the download, which you can monitor through the `bytesLoaded` and `bytesTotal` properties, as well as through dispatched events.

When loading very large video files, such as FLV's, out-of-memory errors may occur. 

When you use this class in Flash Player and in AIR application content in security sandboxes other than then application security sandbox, consider the following security model:

  * A SWF file in the local-with-filesystem sandbox may not load data from, or provide data to, a resource that is in the network sandbox. 
  * By default, the calling SWF file and the URL you load must be in exactly the same domain. For example, a SWF file at www.adobe.com can load data only from sources that are also at www.adobe.com. To load data from a different domain, place a URL policy file on the server hosting the data.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

[View the examples.](#includeExamplesSummary)

See also

[URLRequest](URLRequest.html)   
[URLVariables](URLVariables.html)   
[URLStream](URLStream.html)

  

* * *