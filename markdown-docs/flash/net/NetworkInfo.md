# Networkinfo

Package| [flash.net](package-detail.html)  
---|---  
Class| public class NetworkInfo  
Inheritance| NetworkInfo ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The NetworkInfo class provides information about the network interfaces on a computer. 

_AIR profile support:_ This feature is supported on all desktop operating systems and AIR for TV devices, but is not supported on all mobile devices. You can test for support at run time using the `NetworkInfo.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

The NetworkInfo object is a singleton. To get the single NetworkInfo object, use the static `NetworkInfo.networkInfo` property. Do not call the class constructor, `new NetworkInfo()`.

Most computers have one or more interfaces, such as a wired and a wireless network interface. Additional interfaces such as VPN, loopback, or virtual interfaces can also be present.

A NetworkInfo object dispatches a change event when the available interfaces change. Call the `findInterfaces()` method to determine the most current network information.

**Note:** The NativeApplication object also dispatches network change events.

See also

[NetworkInterface class](../net/NetworkInterface.html)   
[InterfaceAddress class](../net/InterfaceAddress.html)   
[Retrieving a list of network interfaces in Adobe AIR 2](http://www.adobe.com/go/learn_network_interfaces_en/)

  

* * *