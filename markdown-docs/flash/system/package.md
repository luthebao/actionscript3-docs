# Package

The flash.system package contains one package-level function, `fscommand()`, which facilitates communication between a SWF file and its container.

Public Functions

| Function| Defined by  
---|---|---  
|  |  [fscommand](#fscommand\(\))(command:[String](../../String.html), args:[String](../../String.html) = ""):[void](../../specialTypes.html#void) Lets the SWF file communicate with either Flash Player or the program hosting Flash Player, such as a web browser. | flash.system  
  
Function detail

fscommand| ()| function  
---|---|---  
  
`public function fscommand(command:[String](../../String.html), args:[String](../../String.html) = ""):[void](../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
Lets the SWF file communicate with either Flash Player or the program hosting Flash Player, such as a web browser. You can also use the `fscommand()` function to pass messages to Director or to Visual Basic, Visual C++, and other programs that can host ActiveX controls. 

The `fscommand()` function lets a SWF file communicate with a script in a web page. However, script access is controlled by the web page's `allowScriptAccess` setting. (You set this attribute in the HTML code that embeds the SWF file—for example, in the `PARAM` tag for Internet Explorer or the `EMBED` tag for Netscape.) 

  * When `allowScriptAccess` is set to `"sameDomain"` (the default), scripting is allowed only from SWF files that are in the same domain as the web page. 
  * When `allowScriptAccess` is set to `"always"`, the SWF file can communicate with the HTML page in which it is embedded even when the SWF file is from a different domain than the HTML page. 
  * When `allowScriptAccess` is set to `"never"`, the SWF file cannot communicate with any HTML page. Note that using this value is deprecated and not recommended, and shouldn't be necessary if you don't serve untrusted SWF files from your own domain. If you do need to serve untrusted SWF files, Adobe recommends that you create a distinct subdomain and place all untrusted content there. 

You can prevent a SWF file from using this method by setting the `allowNetworking` parameter of the the `object` and `embed` tags in the HTML page that contains the SWF content. 

The `fscommand()` function is not allowed if the calling SWF file is in the local-with-file-system or local-with-network sandbox and the containing HTML page is in an untrusted sandbox.

For more information related to security, see the Flash Player Developer Center Topic: [Security](http://www.adobe.com/go/devnet_security_en).

Usage 1: To use `fscommand()` to send a message to Flash Player, you must use predefined commands and parameters. The following table shows the values that you can specify for the `fscommand()` function's `command` and `args` parameters. These values control SWF files that are playing in Flash Player, including projectors. (A _projector_ is a SWF file saved in a format that can run as a stand-alone application—that is, without Flash Player.)

Command | Parameter (args) | Purpose  
---|---|---  
`quit` | None | Closes the projector.  
`fullscreen` | `true` or `false` | Specifying `true` sets Flash Player to full-screen mode. Specifying `false` returns the player to normal menu view.  
`allowscale` | `true` or `false` | Specifying `false` sets the player so that the SWF file is always drawn at its original size and never scaled. Specifying `true` forces the SWF file to scale to 100% of the player.  
`showmenu` | `true` or `false` | Specifying `true` enables the full set of context menu items. Specifying `false` hides all of the context menu items except About Flash Player and Settings.  
`exec` | Path to application  | Executes an application from within the projector.  
`trapallkeys` | `true` or `false` | Specifying `true` sends all key events, including accelerator keys, to the `onClipEvent(keyDown/keyUp)` handler in Flash Player.   
  
Not all of the commands listed in the table are available in all applications: 

  * None of the commands are available in web players.
  * All of the commands are available in stand-alone projector applications.
  * AIR applications should use the flash.desktop.NativeApplication class for similar functions, such as `NativeApplication.nativeApplication.exit()` instead of `fscommand("quit")`.
  * Only `allowscale` and `exec` are available in test-movie players.

The `exec` command can contain only the characters A-Z, a-z, 0-9, period (.), and underscore (_). The `exec` command runs in the subdirectory fscommand only. In other words, if you use the `exec` command to call an application, the application must reside in a subdirectory named fscommand. The `exec` command works only from within a Flash projector file.

Usage 2: To use `fscommand()` to send a message to a scripting language such as JavaScript in a web browser, you can pass any two parameters in the `command` and `args` parameters. These parameters can be strings or expressions, and they are used in a JavaScript function that handles, or _catches_ , the `fscommand()` function. 

In a web browser, `fscommand()` calls the JavaScript function `moviename_DoFScommand`, which resides in the web page that contains the SWF file. For `moviename`, supply the name of the Flash object that you used for the `NAME` attribute of the `EMBED` tag or the ID property of the `OBJECT` tag. If you assign the SWF file the name "myMovie", the JavaScript function `myMovie_DoFScommand` is called. 

In the web page that contains the SWF file, set the `allowScriptAccess` attribute to allow or deny the SWF file's ability to access the web page, as described above. (You set this attribute in the HTML code that embeds the SWF file—for example, in the `PARAM` tag for Internet Explorer or the `EMBED` tag for Netscape.) 

In Flash Player 10 and later running in a browser, using this method programmatically to open a pop-up window may not be successful. Various browsers (and browser configurations) may block pop-up windows at any time; it is not possible to guarantee any pop-up window will appear. However, for the best chance of success, use this method to open a pop-up window only in code that executes as a direct result of a user action (for example, in an event handler for a mouse click or key-press event.)

Usage 3: The `fscommand()` function can send messages to Director (Macromedia Director from Adobe). These messages are interpreted by Lingo (the Director scripting language) as strings, events, or executable Lingo code. If a message is a string or an event, you must write the Lingo code to receive the message from the `fscommand()` function and carry out an action in Director. For more information, see the Director Support Center at [www.adobe.com/support/director/](http://www.adobe.com/support/director/).

Usage 4: In VisualBasic, Visual C++, and other programs that can host ActiveX controls, `fscommand()` sends a VB event with two strings that can be handled in the environment's programming language. For more information, use the keywords "Flash method" to search the Flash Support Center at [www.adobe.com/support/flash/](http://www.adobe.com/support/flash/).

**Note:** The ExternalInterface class provides better functionality for communication between JavaScript and ActionScript (Usage 2) and between ActionScript and VisualBasic, Visual C++, or other programs that can host ActiveX controls (Usage 4). You should continue to use `fscommand()` for sending messages to Flash Player (Usage 1) and Director (Usage 3).

Parameters | `command:[String](../../String.html)` — A string passed to the host application for any use, or a command passed to Flash Player.   
---|---  
| `args:[String](../../String.html)` (default = "``")`` — A string passed to the host application for any use, or a value passed to Flash Player.   
  
Throws | `[Error](../../Error.html) ` — If the function is not called in response to a user action, such as a mouse event or keypress event.   
---|---  
  
See also

[flash.desktop.NativeApplication](../desktop/NativeApplication.html)

  
Example   
The following example shows how `fscommand()` can be used to direct Flash Player to go into full screen mode and not allow scaling. An orange box is then added to the stage using `draw()`. In `draw()`, a `click` event listener is added named `clickHandler()`, which responds to `click` events by directing Flash Player to exit using another call to `fscommand().`

**Note:** this example should be executed in the standalone Flash Player and not within a web browser.
    
    
    package {
        import flash.display.Sprite;
    	import flash.text.TextField;
    	import flash.system.fscommand;
    	import flash.events.MouseEvent;
    
    	public class FSCommandExample extends Sprite {
    		private var bgColor:uint = 0xFFCC00;
    		private var size:uint = 100;
    
    		public function FSCommandExample() {
    			fscommand("fullscreen", "true");
    			fscommand("allowscale", "false");
    			draw();
    		}
    
    		private function clickHandler(event:MouseEvent):void {
    			fscommand("quit");
    			trace("clickHandler");
    		}
    
    		private function draw():void {
    			var child:Sprite = new Sprite();
    			child.graphics.beginFill(bgColor);
    			child.graphics.drawRect(0, 0, size, size);
    			child.graphics.endFill();
    			child.buttonMode = true;
    			addEventListener(MouseEvent.CLICK, clickHandler);
    
    			var label:TextField = new TextField();
    			label.text = "quit";
    			label.selectable = false;
    			label.mouseEnabled = false;
    			child.addChild(label);
    
    			addChild(child);
    		}
    	}
    }

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:12 PM GMT+01:00\) : Package flash.system)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)