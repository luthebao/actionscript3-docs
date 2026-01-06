# Loader

Package| [flash.display](package-detail.html)  
---|---  
Class| public class Loader  
Inheritance| Loader ![Inheritance](../../images/inherit-arrow.gif) [DisplayObjectContainer](DisplayObjectContainer.html) ![Inheritance](../../images/inherit-arrow.gif) [InteractiveObject](InteractiveObject.html) ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The Loader class is used to load SWF files or image (JPG, PNG, or GIF) files. Use the `load()` method to initiate loading. The loaded display object is added as a child of the Loader object. 

Use the URLLoader class to load text or binary data.

The Loader class overrides the following methods that it inherits, because a Loader object can only have one child display object—the display object that it loads. Calling the following methods throws an exception: `addChild()`, `addChildAt()`, `removeChild()`, `removeChildAt()`, and `setChildIndex()`. To remove a loaded display object, you must remove the _Loader_ object from its parent DisplayObjectContainer child array. 

**iOS notes**

In AIR applications on iOS, you can only load a SWF file containing ActionScript from the application package. This restriction includes any ActionScript, such as assets with class names exported for ActionScript. For loading any SWF file, you must load the SWF using the same application domain as the parent SWF, as shown in the following example:
    
    
    
     var loader:Loader = new Loader();
    
     var url:URLRequest = new URLRequest("swfs/SecondarySwf.swf");
    
     var loaderContext:LoaderContext = new LoaderContext(false, ApplicationDomain.currentDomain, null);
    
     loader.load(url, loaderContext);

In addition, on iOS you can't load a SWF file that contains any ActionScript ByteCode (ABC) then unload it and reload it. If you attempt to do this, the runtime throws error 3764.

Prior to AIR 3.6, only SWF files that do not contain ActionScript bytecode can be loaded, regardless of whether they're loaded from the application package or over a network. As an alternative to using an external SWF file with ActionScript, create a SWC library and link it in to your main SWF.

AIR 3.7 and higher supports loading of externally hosted secondary SWFs. The detailed description about this feature can be found [here](http://blogs.adobe.com/airodynamics/2013/03/08/external-hosting-of-secondary-swfs-for-air-apps-on-ios/). 

These iOS restrictions restrictions do not apply when an application is running in the iOS Simulator (ipa-test-interpreter-simulator or ipa-debug-interpreter-simulator) or interpreter mode (ipa-test-interpreter or ipa-debug-interpreter.)

**Loader security**

When you use the Loader class, consider the Flash Player and Adobe AIR security model: 

  * You can load content from any accessible source. 
  * Loading is not allowed if the calling SWF file is in a network sandbox and the file to be loaded is local. 
  * If the loaded content is a SWF file written with ActionScript 3.0, it cannot be cross-scripted by a SWF file in another security sandbox unless that cross-scripting arrangement was approved through a call to the `System.allowDomain()` or the `System.allowInsecureDomain()` method in the loaded content file.
  * If the loaded content is an AVM1 SWF file (written using ActionScript 1.0 or 2.0), it cannot be cross-scripted by an AVM2 SWF file (written using ActionScript 3.0). However, you can communicate between the two SWF files by using the LocalConnection class.
  * If the loaded content is an image, its data cannot be accessed by a SWF file outside of the security sandbox, unless the domain of that SWF file was included in a URL policy file at the origin domain of the image.
  * Movie clips in the local-with-file-system sandbox cannot script movie clips in the local-with-networking sandbox, and the reverse is also prevented. 
  * You cannot connect to commonly reserved ports. For a complete list of blocked ports, see "Restricting Networking APIs" in the _ActionScript 3.0 Developer's Guide_. 

However, in AIR, content in the `application` security sandbox (content installed with the AIR application) are not restricted by these security limitations.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

When loading a SWF file from an untrusted source (such as a domain other than that of the Loader object's root SWF file), you may want to define a mask for the Loader object, to prevent the loaded content (which is a child of the Loader object) from drawing to portions of the Stage outside of that mask, as shown in the following code:
    
    
    
     import flash.display.*;
    
     import flash.net.URLRequest;
    
     var rect:Shape = new Shape();
    
     rect.graphics.beginFill(0xFFFFFF);
    
     rect.graphics.drawRect(0, 0, 100, 100);
    
     rect.graphics.endFill();
    
     addChild(rect);
    
     var ldr:Loader = new Loader();
    
     ldr.mask = rect;
    
     var url:String = "http://www.unknown.example.com/content.swf";
    
     var urlReq:URLRequest = new URLRequest(url);
    
     ldr.load(urlReq);
    
     addChild(ldr);
    
     

Note: App Transport Security is being introduced from Apple in iOS9, which doesnt allow unsecure connections between App and Web services. Due to this change all the connections which are made to Unsecure web sites via Loader, URLLoader will discontinue and not work due to App Transport Security. Please specify exceptions to the default behaviour by adding keys to Info.plist in your app.

To turn off the feature completely you can add following in your Info.plist and it will work as before.
    
    
    
         <key>NSAppTransportSecurity</key>
    
                   <dict>
    
                       <key>NSAllowsArbitraryLoads</key><true/>
    
                   </dict>
    
      

Please specify exceptions to the default behavior by adding keys to InfoAdditions tag of application descriptor of your app.
    
    
    
      <iPhone>
    
      <InfoAdditions>
    
                       <![CDATA[
    
                              <key>NSAppTransportSecurity</key>
    
                                  <dict>
    
                                            <key>NSExceptionDomains</key>
    
                                  <dict>
    
                                           <key>www.example.com</key>
    
                                  <dict>
    
                                         <!--Include to allow subdomains-->
    
                                         <key>NSIncludesSubdomains</key>
    
                                         <true/>
    
                                         <!--Include to allow HTTP requests-->
    
                                         <key>NSTemporaryExceptionAllowsInsecureHTTPLoads</key>
    
                                         <true/>
    
                                          <!--Include to specify minimum TLS version-->
    
                                          <key>NSTemporaryExceptionMinimumTLSVersion</key>
    
                                          <string>TLSv1.1</string>
    
                                  </dict>
    
                                  </dict>
    
                                  </dict>
    
                      ]]>
    
             </InfoAdditions>
    
      </iPhone>
    
      

[View the examples.](#includeExamplesSummary)

See also

[flash.display.LoaderInfo](../display/LoaderInfo.html)   
[flash.net.URLLoader](../net/URLLoader.html)   
[flash.display.DisplayObject](../display/DisplayObject.html)

  

* * *