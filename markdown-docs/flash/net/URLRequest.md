# Urlrequest

Package| [flash.net](package-detail.html)  
---|---  
Class| public final class URLRequest  
Inheritance| URLRequest ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The URLRequest class captures all of the information in a single HTTP request. URLRequest objects are passed to the `load()` methods of the Loader, URLStream, and URLLoader classes, and to other loading operations, to initiate URL downloads. They are also passed to the `upload()` and `download()` methods of the FileReference class. 

A SWF file in the local-with-filesystem sandbox may not load data from, or provide data to, a resource that is in the network sandbox. 

By default, the calling SWF file and the URL you load must be in the same domain. For example, a SWF file at www.adobe.com can load data only from sources that are also at www.adobe.com. To load data from a different domain, place a URL policy file on the server hosting the data.

However, in Adobe AIR, content in the application security sandbox (content installed with the AIR application) is not restricted by these security limitations. For content running in Adobe AIR, files in the application security sandbox can access URLs using any of the following URL schemes:

Files in the application security domain — files installed with the AIR application — can access URLs using any of the following URL schemes:

  * `http` and `https`
  * `file`
  * `app-storage`
  * `app`

Content running in Adobe AIR that is not in the application security sandbox observes the same restrictions as content running in the browser (in Flash Player), and loading is governed by the content's domain and any permissions granted in URL policy files.

Note: App Transport Security was introduced by Apple in iOS9, which doesnt allow unsecure connections between App and Web services. Due to this change all the connections which are made to Unsecure web sites via Loader, URLLoader will discontinue and not work due to App Transport Security. Please specify exceptions to the default behaviour by adding keys to the application descriptor of your app.

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
      

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

[View the examples.](#includeExamplesSummary)

See also

[FileReference](FileReference.html)   
[URLRequestHeader](URLRequestHeader.html)   
[URLRequestDefaults](URLRequestDefaults.html)   
[URLLoader](URLLoader.html)   
[URLStream](URLStream.html)   
[HTMLLoader class](../../flash/html/HTMLLoader.html)

  

* * *