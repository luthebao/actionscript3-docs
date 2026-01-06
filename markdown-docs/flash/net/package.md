# Package

The flash.net package contains package-level functions for opening a new browser window, sending a URL request to a server, and dealing with class aliases.

Public Functions

| Function| Defined by  
---|---|---  
|  |  [getClassByAlias](#getClassByAlias\(\))(aliasName:[String](../../String.html)):[Class](../../Class.html) Looks up a class that previously had an alias registered through a call to the `registerClassAlias()` method. | flash.net  
|  |  [navigateToURL](#navigateToURL\(\))(request:[URLRequest](URLRequest.html), window:[String](../../String.html) = null):[void](../../specialTypes.html#void) Opens or replaces a window in the application that contains the Flash Player container (usually a browser). | flash.net  
|  |  [registerClassAlias](#registerClassAlias\(\))(aliasName:[String](../../String.html), classObject:[Class](../../Class.html)):[void](../../specialTypes.html#void) Preserves the class (type) of an object when the object is encoded in Action Message Format (AMF). | flash.net  
|  |  [sendToURL](#sendToURL\(\))(request:[URLRequest](URLRequest.html)):[void](../../specialTypes.html#void) Sends a URL request to a server, but ignores any response. | flash.net  
  
Function detail

getClassByAlias| ()| function  
---|---|---  
  
`public function getClassByAlias(aliasName:[String](../../String.html)):[Class](../../Class.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Looks up a class that previously had an alias registered through a call to the `registerClassAlias()` method. 

This method does not interact with the `flash.utils.getDefinitionByName()` method.

Parameters | `aliasName:[String](../../String.html)` — The alias to find.   
---|---  
  
Returns | `[Class](../../Class.html)` — The class associated with the given alias. If not found, an exception will be thrown.   
---|---  
  
Throws | `[ReferenceError](../../ReferenceError.html) ` — The alias was not registered.   
---|---  
  
See also

[registerClassAlias()](package.html#registerClassAlias\(\))

navigateToURL| ()| function|   
---|---|---|---  
  
`public function navigateToURL(request:[URLRequest](URLRequest.html), window:[String](../../String.html) = null):[void](../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Opens or replaces a window in the application that contains the Flash Player container (usually a browser). In Adobe AIR, the function opens a URL in the default system web browser Opens a URL in the default system web browser.

**_Important Security Note_**

Developers often pass URL values to the `navigateToURL()` function that were obtained from external sources such as FlashVars. Attackers may try to manipulate these external sources to perform attacks such as cross-site scripting. Therefore, developers should validate all URLs before passing them to this function. 

Good data validation for URLs can mean different things depending on the usage of the URL within the overall application. The most common data validation techniques include validating that the URL is of the appropriate scheme. For instance, unintentionally allowing javascript: URLs may result in cross-site scripting. Validating that the URL is a within your domain can ensure that the SWF file can't be used as an open-redirector by people who conduct phishing attacks. For additional security, you may also choose to validate the path of the URL and to validate that the URL conforms to the RFC guidelines

For example, the following code shows a simple example of performing data validation by denying any URL that does not begin with http:// or https:// and validating that the URL is within your domain name. This example may not be appropriate for all web applications and you should consider whether additional checks against the URL are necessary. 
    
    
         // AS3 Regular expression pattern match for URLs that start with http:// and https:// plus your domain name.
         function checkProtocol (flashVarURL:String):Boolean {
            // Get the domain name for the SWF if it is not known at compile time.
            // If the domain is known at compile time, then the following two lines can be replaced with a hard coded string.
            var my_lc:LocalConnection = new LocalConnection();
            var domainName:String = my_lc.domain;
            // Build the RegEx to test the URL.
            // This RegEx assumes that there is at least one "/" after the
            // domain. http://www.mysite.com will not match.
            var pattern:RegExp = new RegExp("^http[s]?\:\\/\\/([^\\/]+)\\/");
            var result:Object = pattern.exec(flashVarURL);
            if (result == null || result[1] != domainName || flashVarURL.length >= 4096) {
              return (false);
            }
            return (true);
         }  
         
          

For _local_ content running in a browser, calls to the `navigateToURL()` method that specify a `"javascript:"` pseudo-protocol (via a `URLRequest` object passed as the first parameter) are only permitted if the SWF file and the containing web page (if there is one) are in the local-trusted security sandbox. Some browsers do not support using the javascript protocol with the `navigateToURL()` method. Instead, consider using the `call()` method of the `ExternalInterface` API to invoke JavaScript methods within the enclosing HTML page.

In Flash Player, and in non-application sandboxes in Adobe AIR, you cannot connect to commonly reserved ports. For a complete list of blocked ports, see "Restricting Networking APIs" in the _ActionScript 3.0 Developer's Guide_.

In Flash Player 10 and later running in a browser, using this method programmatically to open a pop-up window may not be successful. Various browsers (and browser configurations) may block pop-up windows at any time; it is not possible to guarantee any pop-up window will appear. However, for the best chance of success, use this method to open a pop-up window only in code that executes as a direct result of a user action (for example, in an event handler for a mouse click or key-press event.)

In Flash Player 10 and later, if you use a multipart Content-Type (for example "multipart/form-data") that contains an upload (indicated by a "filename" parameter in a "content-disposition" header within the POST body), the POST operation is subject to the security rules applied to uploads:

  * The POST operation must be performed in response to a user-initiated action, such as a mouse click or key press.
  * If the POST operation is cross-domain (the POST target is not on the same server as the SWF file that is sending the POST request), the target server must provide a URL policy file that permits cross-domain access.

Also, for any multipart Content-Type, the syntax must be valid (according to the RFC2046 standards). If the syntax appears to be invalid, the POST operation is subject to the security rules applied to uploads.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

In AIR, on mobile platforms, the sms: and tel: URI schemes are supported. On Android, vipaccess:, connectpro:, and market: URI schemes are supported. The URL syntax is subject to the platform conventions. For example, on Android, the URI scheme must be lower case. When you navigate to a URL using one of these schemes, the runtime opens the URL in the default application for handling the scheme. Thus, navigating to `tel:+5555555555` opens the phone dialer with the specified number already entered. A separate application or utility, such as a phone dialer must be available to process the URL.

The following code shows how you can invoke the VIP Access and Connect Pro applications on Android:
    
    
           //Invoke the VIP Access Application.
           navigateToURL(new URLRequest("vipaccess://com.verisign.mvip.main?action=securitycode"));
         
           //Invoke the Connect Pro Application.
           navigateToURL(new URLRequest("connectpro://"));
               

Parameters | `request:[URLRequest](URLRequest.html)` — A URLRequest object that specifies the URL to navigate to. For content running in Adobe AIR, when When  using the `navigateToURL()` function, the runtime treats a URLRequest that uses the POST method (one that has its `method` property set to `URLRequestMethod.POST`) as using the GET method.  
---|---  
| `window:[String](../../String.html)` (default = `null`)`` — The browser window or HTML frame in which to display the document indicated by the `request` parameter. You can enter the name of a specific window or use one of the following values: 

  * `"_self"` specifies the current frame in the current window.
  * `"_blank"` specifies a new window.
  * `"_parent"` specifies the parent of the current frame.
  * `"_top"` specifies the top-level frame in the current window.

If you do not specify a value for this parameter, a new empty window is created. In the stand-alone player, you can either specify a new (`"_blank"`) window or a named window. The other values don't apply. **Note:** When code in a SWF file that is running in the local-with-filesystem sandbox calls the `navigateToURL()` function and specifies a custom window name for the `window` parameter, the window name is transfered into a random name. The name is in the form `"_flashXXXXXXXX"`, where each X represents a random hexadecimal digit. Within the same session (until you close the containing browser window), if you call the function again and specify the same name for the `window` parameter, the same random string is used.  
  
Throws | `[Error](../../Error.html) ` — The `digest` property of the `request` object is not `null`. You should only set the `digest` property of a URLRequest object for use calling the `URLLoader.load()` method when loading a SWZ file (an Adobe platform component).   
---|---  
| `[SecurityError](../../SecurityError.html) ` — In Flash Player (and in non-application sandbox content in Adobe AIR), this error is thrown in the following situations: 

  * Local untrusted SWF files may not communicate with the Internet. You can avoid this situation by reclassifying this SWF file as local-with-networking or trusted.
  * A navigate operation attempted to evaluate a scripting pseudo-URL, but the containing document (usually an HTML document in a browser) is from a sandbox to which you do not have access. You can avoid this situation by specifying `allowScriptAccess="always"` in the containing document.
  * You cannot navigate the special windows `"_self"`, `"_top"`, or `"_parent"` if your SWF file is contained by an HTML page that has set the `allowScriptAccess` to `"none"`, or to `"sameDomain"` when the domains of the HTML file and the SWF file do not match.
  * You cannot navigate a window with a nondefault name from within a SWF file that is in the local-with-filesystem sandbox.
  * You cannot connect to commonly reserved ports. For a complete list of blocked ports, see "Restricting Networking APIs" in the _ActionScript 3.0 Developer's Guide_.

  
| `[Error](../../Error.html) ` — If the method is not called in response to a user action, such as a mouse event or keypress event. This requirement only applies to content in Flash Player and to non-application sandbox content in Adobe AIR.   
  
See also

[flash.external.ExternalInterface.call()](../external/ExternalInterface.html#call\(\))

  
Example   
The following example opens the URL http://www.adobe.com in a new browser window and passes data about a user session, captured in a URLVariables object, to the web server. 
    
    
    package {
        import flash.display.Sprite;
    	import flash.net.navigateToURL;
    	import flash.net.URLRequest;
    	import flash.net.URLVariables;
    
    	public class NavigateToURLExample extends Sprite {
    
    		public function NavigateToURLExample() {
    			var url:String = "http://www.adobe.com";
    			var variables:URLVariables = new URLVariables();
    			variables.exampleSessionId = new Date().getTime();
    			variables.exampleUserLabel = "Your Name";
    			var request:URLRequest = new URLRequest(url);
    			request.data = variables;
                try {            
    			    navigateToURL(request);
                }
                catch (e:Error) {
                    // handle error here
                }
    		}
    	}
    }

The following example shows how you can open new browser windows from Flash Player using the navigateToURL() method. Example provided by [ActionScriptExamples.com](http://actionscriptexamples.com/2008/12/08/opening-urls-in-new-browser-windows-using-actionscript-30-and-actionscript-20/). 
    
    
    // Requires
    // - Button symbol on Stage (or a display object, such as a MovieClip) with instance name "buttonSymbol"
    //
    buttonSymbol.addEventListener(MouseEvent.CLICK, buttonSymbol_click);
     
    function buttonSymbol_click(evt:MouseEvent):void {
        var req:URLRequest = new URLRequest("http://www.adobe.com/");
        navigateToURL(req, "_blank");
    }

The following example illustrates the syntax for launching the device telephone dialer with a specified number. 
    
    
    var request:URLRequest = new URLRequest( "tel:+5555555555" );
    navigateToURL( request );

The following example illustrates the syntax for launching the device text message application with a specified receipient. 
    
    
    var request:URLRequest = new URLRequest( "sms:+5555555555" );
    navigateToURL( request );

The following example illustrates the syntax for launching the Android Market app. The search parameter is set to find the Flash Player app. 
    
    
    var request:URLRequest = new URLRequest( "market://search?q=pname:com.adobe.flashplayer" );
    navigateToURL( request );

registerClassAlias| ()| function|   
---|---|---|---  
  
`public function registerClassAlias(aliasName:[String](../../String.html), classObject:[Class](../../Class.html)):[void](../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Preserves the class (type) of an object when the object is encoded in Action Message Format (AMF). When you encode an object into AMF, this function saves the alias for its class, so that you can recover the class when decoding the object. If the encoding context did not register an alias for an object's class, the object is encoded as an anonymous object. Similarly, if the decoding context does not have the same alias registered, an anonymous object is created for the decoded data. 

LocalConnection, ByteArray, SharedObject, NetConnection and NetStream are all examples of classes that encode objects in AMF.

The encoding and decoding contexts do not need to use the same class for an alias; they can intentionally change classes, provided that the destination class contains all of the members that the source class serializes.

Parameters | `aliasName:[String](../../String.html)` — The alias to use.   
---|---  
| `classObject:[Class](../../Class.html)` — The class associated with the given alias.   
  
Throws | `[TypeError](../../TypeError.html) ` — If either parameter is `null`.   
---|---  
  
See also

[ObjectEncoding class](../net/ObjectEncoding.html)

  
Example   
This example uses the `registerClassAlias()` function to register an alias (`com.example.eg`) for the class ExampleClass. Because an alias is registered for the class, the object is able to be deserialized as an instance of ExampleClass, and the code outputs `true`. If the `registerClassAlias()` call were removed, the code would output `false`. 
    
    
    package {
        import flash.display.Sprite;
    	import flash.net.registerClassAlias;
    	import flash.utils.ByteArray;
    
    	public class RegisterClassAliasExample extends Sprite {
    		public function RegisterClassAliasExample() {
    			registerClassAlias("com.example.eg", ExampleClass);
    			var eg1:ExampleClass = new ExampleClass();
    			var ba:ByteArray = new ByteArray();
    			ba.writeObject(eg1);
    			ba.position = 0;
    			var eg2:* = ba.readObject();
    			trace(eg2 is ExampleClass); // true
    		}
    	}
    }
    
    class ExampleClass {}

sendToURL| ()| function|   
---|---|---|---  
  
`public function sendToURL(request:[URLRequest](URLRequest.html)):[void](../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Sends a URL request to a server, but ignores any response. 

To examine the server response, use the `URLLoader.load()` method instead.

You cannot connect to commonly reserved ports. For a complete list of blocked ports, see "Restricting Networking APIs" in the _ActionScript 3.0 Developer's Guide_.

You can prevent a SWF file from using this method by setting the `allowNetworking` parameter of the the `object` and `embed` tags in the HTML page that contains the SWF content.

In Flash Player 10 and later, if you use a multipart Content-Type (for example "multipart/form-data") that contains an upload (indicated by a "filename" parameter in a "content-disposition" header within the POST body), the POST operation is subject to the security rules applied to uploads:

  * The POST operation must be performed in response to a user-initiated action, such as a mouse click or key press.
  * If the POST operation is cross-domain (the POST target is not on the same server as the SWF file that is sending the POST request), the target server must provide a URL policy file that permits cross-domain access.

Also, for any multipart Content-Type, the syntax must be valid (according to the RFC2046 standards). If the syntax appears to be invalid, the POST operation is subject to the security rules applied to uploads.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

Parameters | `request:[URLRequest](URLRequest.html)` — A URLRequest object specifying the URL to send data to.   
---|---  
  
Throws | `[SecurityError](../../SecurityError.html) ` — Local untrusted SWF files cannot communicate with the Internet. You can avoid this situation by reclassifying this SWF file as local-with-networking or trusted.   
---|---  
| `[SecurityError](../../SecurityError.html) ` — You cannot connect to commonly reserved ports. For a complete list of blocked ports, see "Restricting Networking APIs" in the _ActionScript 3.0 Developer's Guide_.   
  
Example   
The following example passes data about a user session, captured in a URLVariables object, to the application at http://www.yourDomain.com/application.jsp. 
    
    
     package {
        import flash.display.Sprite;
    	import flash.net.URLRequest;
    	import flash.net.URLVariables;
    	import flash.net.sendToURL;
    
    	public class SendToURLExample extends Sprite {
    
    		public function SendToURLExample() {
    			var url:String = "http://www.yourDomain.com/application.jsp";
    			var variables:URLVariables = new URLVariables();
    			variables.sessionId = new Date().getTime();
    			variables.userLabel = "Your Name";
    
    			var request:URLRequest = new URLRequest(url);
    			request.data = variables;
    			trace("sendToURL: " + request.url + "?" + request.data);
    			try {
                    sendToURL(request);
                }
                catch (e:Error) {
                    // handle error here
                }
    		}
    	}
    }

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:12 PM GMT+01:00\) : Package flash.net)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)