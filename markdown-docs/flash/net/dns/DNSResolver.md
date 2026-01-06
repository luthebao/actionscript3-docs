# Dnsresolver

Package| [flash.net.dns](package-detail.html)  
---|---  
Class| public class DNSResolver  
Inheritance| DNSResolver ![Inheritance](../../../images/inherit-arrow.gif) [EventDispatcher](../../events/EventDispatcher.html) ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The DNSResolver class lets you lookup Domain Name System (DNS) resource records. 

_AIR profile support:_ This feature is supported on all desktop operating systems, but is not supported on mobile devices. It is partially supported on AIR for TV devices. You can test for support at run time using the `DNSResolver.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

You can look up the following types of resource records:

  * ARecord: IPv4 address for a host.
  * AAAARecord: IPv6 address for a host.
  * MXRecord: mail exchange record for a host.
  * PTRRecord: host name for an IP address.
  * SRVRecord: service record for a service

The following table indicates DNS lookup support on AIR for TV devices. Unsupported requests result in the DNSResolver object dispatching an flash.events.ErrorEvent object.

Record type specified in `DNSResolver.lookup()`| Support  
---|---  
ARecord| Full support  
AAAARecord| Full support  
MXRecord| Not supported  
PTRRecord| Supported only for IPv4 addresses, not for IPv6 addresses  
SRVRecord| Not supported  
  
[View the examples.](#includeExamplesSummary)

See also

[ARecord](../dns/ARecord.html)   
[AAAARecord](../dns/AAAARecord.html)   
[MXRecord](../dns/MXRecord.html)   
[PTRRecord](../dns/PTRRecord.html)   
[SRVRecord](../dns/SRVRecord.html)

  

* * *