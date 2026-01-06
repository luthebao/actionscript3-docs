# Localconnection

Package| [flash.net](package-detail.html)  
---|---  
Class| public class LocalConnection  
Inheritance| LocalConnection ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The LocalConnection class lets you create a LocalConnection object that can invoke a method in another LocalConnection object. The communication can be: 

  * Within a single SWF file
  * Between multiple SWF files
  * Between content (SWF-based or HTML-based) in AIR applications
  * Between content (SWF-based or HTML-based) in an AIR application and SWF content running in a browser

_AIR profile support:_ This feature is supported on all desktop operating systems and on all AIR for TV devices, but is not supported on mobile devices. You can test for support at run time using the `LocalConnection.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

Note: AIR for TV devices support communication only between SWF-based content in AIR applications.

Local connections enable this kind of communication between SWF files without the use of `fscommand()` or JavaScript. LocalConnection objects can communicate only among files that are running on the same client computer, but they can be running in different applications — for example, a file running in a browser and a SWF file running in Adobe AIR. 

LocalConnection objects created in ActionScript 3.0 can communicate with LocalConnection objects created in ActionScript 1.0 or 2.0. The reverse is also true: LocalConnection objects created in ActionScript 1.0 or 2.0 can communicate with LocalConnection objects created in ActionScript 3.0. Flash Player handles this communication between LocalConnection objects of different versions automatically.

There are three ways to add callback methods to a LocalConnection object:

  * Subclass the LocalConnection class and add methods.
  * Set the `LocalConnection.client` property to an object that implements the methods.
  * Create a dynamic class that extends LocalConnection and dynamically attach methods.

To understand how to use LocalConnection objects to implement communication between two files, it is helpful to identify the commands used in each file. One file is called the _receiving_ file; it is the file that contains the method to be invoked. The receiving file must contain a LocalConnection object and a call to the `connect()` method. The other file is called the _sending_ file; it is the file that invokes the method. The sending file must contain another LocalConnection object and a call to the `send()` method.

Your use of `send()` and `connect()` differs depending on whether the files are in the same domain, in different domains with predictable domain names, or in different domains with unpredictable or dynamic domain names. The following paragraphs explain the three different situations, with code samples for each.

**Same domain**. This is the simplest way to use a LocalConnection object, to allow communication only between LocalConnection objects that are located in the same domain, because same-domain communication is permitted by default. When two files from the same domain communicate, you do not need to implement any special security measures, and you simply pass the same value for the `connectionName` parameter to both the `connect()` and `send()` methods:

![Loading from the same domain](../../images/localconnection_samedomains.gif)
    
    
    // receivingLC is in http://www.domain.com/receiving.swf
    receivingLC.connect('myConnection');
    
    // sendingLC is in http://www.domain.com/sending.swf
    // myMethod() is defined in sending.swf
    sendingLC.send('myConnection', 'myMethod');
    

**Different domains with predictable domain names**. When two SWF files from different domains communicate, you need to allow communication between the two domains by calling the `allowDomain()` method. You also need to qualify the connection name in the `send()` method with the receiving LocalConnection object's domain name:

![Loading from separate domains](../../images/localconnection_differentdomains.gif)
    
    
    // receivingLC is in http://www.domain.com/receiving.swf
    receivingLC.allowDomain('www.anotherdomain.com');
    receivingLC.connect('myConnection');
    
    // sendingLC is in http://www.anotherdomain.com/sending.swf
    sendingLC.send('www.domain.com:myConnection', 'myMethod');
    

**Different domains with unpredictable domain names**. Sometimes, you might want to make the file with the receiving LocalConnection object more portable between domains. To avoid specifying the domain name in the `send()` method, but to indicate that the receiving and sending LocalConnection objects are not in the same domain, precede the connection name with an underscore (_), in both the `connect()` and `send()` calls. To allow communication between the two domains, call the `allowDomain()` method and pass the domains from which you want to allow LocalConnection calls. Alternatively, pass the wildcard (*) argument to allow calls from all domains:

![Loading from unknown domain names](../../images/localconnection_unknowndomains.gif)
    
    
    // receivingLC is in http://www.domain.com/receiving.swf
    receivingLC.allowDomain('*');
    receivingLC.connect('_myConnection');
    
    // sendingLC is in http://www.anotherdomain.com/sending.swf
    sendingLC.send('_myConnection', 'myMethod');
    

**From Flash Player to an AIR application**. A LocalConnection object created in the AIR application sandbox uses a special string as it's connection prefix instead of a domain name. This string has the form: `app#appID.pubID` where appID is the application ID and pubID is the publisher ID of the application. (Only include the publisher ID if the AIR application uses a publisher ID.) For example, if an AIR application has an application ID of, "com.example", and no publisher ID, you could use: `app#com.example:myConnection` as the local connection string. The AIR application also must call the `allowDomain()` method, passing in the calling SWF file's domain of origin: 

![Flash Player to AIR connection](../../images/localconnection_flash2AIR.gif)
    
    
    // receivingLC is an AIR application with app ID = com.example (and no publisher ID)
    receivingLC.allowDomain('www.domain.com');
    receivingLC.connect('myConnection');
    
    // sendingLC is in http://www.domain.com/sending.swf
    sendingLC.send('app#com.example:myConnection', 'myMethod');
    

**Note:** If an AIR application loads a SWF outside the AIR application sandbox, then the rules for establishing a local connection with that SWF are the same as the rules for establishing a connection with a SWF running in Flash Player.

**From an AIR application to Flash Player**. When an AIR application communicates with a SWF running in the Flash Player runtime, you need to allow communication between the two by calling the `allowDomain()` method and passing in the AIR application's connection prefix. For example, if an AIR application has an application ID of, "com.example", and no publisher ID, you could pass the string: `app#com.example` to the `allowDomain()` method. You also need to qualify the connection name in the `send()` method with the receiving LocalConnection object's domain name (use "localhost" as the domain for SWF files loaded from the local file system):

![AIR to Flash Player communication](../../images/localconnection_AIR2flash.gif)
    
    
    // receivingLC is in http://www.domain.com/receiving.swf
    receivingLC.allowDomain('app#com.example');
    receivingLC.connect('myConnection');
    
    // sendingLC is an AIR application with app ID = com.example (and no publisher ID)
    sendingLC.send('www.domain.com:myConnection', 'myMethod');
    

**From an AIR application to another AIR application**. To communicate between two AIR applications, you need to allow communication between the two by calling the `allowDomain()` method and passing in the sending AIR application's connection prefix. For example, if the sending application has an application ID of, "com.example", and no publisher ID, you could pass the string: `app#com.example` to the `allowDomain()` method in the receiving application. You also need to qualify the connection name in the `send()` method with the receiving LocalConnection object's connection prefix:

![AIR to AIR communication](../../images/localconnection_AIR2AIR.gif)
    
    
    // receivingLC is an AIR application with app ID = com.sample (and no publisher ID)
    receivingLC.allowDomain('app#com.example');
    receivingLC.connect('myConnection');
    
    // sendingLC is an AIR application with app ID = com.example (and no publisher ID)
    sendingLC.send('app#com.sample:myConnection', 'myMethod');
    

You can use LocalConnection objects to send and receive data within a single file, but this is not a typical implementation.

For more information about the `send()` and `connect()` methods, see the discussion of the `connectionName` parameter in the `LocalConnection.send()` and `LocalConnection.connect()`entries. Also, see the `allowDomain()` and `domain` entries.

[View the examples.](#includeExamplesSummary)

See also

[flash.net.LocalConnection.send()](../net/LocalConnection.html#send\(\))   
[flash.net.LocalConnection.allowDomain()](../net/LocalConnection.html#allowDomain\(\))   
[flash.net.LocalConnection.domain](../net/LocalConnection.html#domain)

  

* * *