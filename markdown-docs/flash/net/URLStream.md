# Urlstream

Package| [flash.net](package-detail.html)  
---|---  
Class| public class URLStream  
Inheritance| URLStream ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IDataInput](../utils/IDataInput.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The URLStream class provides low-level access to downloading URLs. Data is made available to application code immediately as it is downloaded, instead of waiting until the entire file is complete as with URLLoader. The URLStream class also lets you close a stream before it finishes downloading. The contents of the downloaded file are made available as raw binary data. 

The read operations in URLStream are nonblocking. This means that you must use the `bytesAvailable` property to determine whether sufficient data is available before reading it. An `EOFError` exception is thrown if insufficient data is available.

All binary data is encoded by default in big-endian format, with the most significant byte first.

The security rules that apply to URL downloading with the URLStream class are identical to the rules applied to URLLoader objects. Policy files may be downloaded as needed. Local file security rules are enforced, and security warnings are raised as needed.

[View the examples.](#includeExamplesSummary)

See also

[URLLoader](URLLoader.html)   
[URLRequest](URLRequest.html)

  

* * *