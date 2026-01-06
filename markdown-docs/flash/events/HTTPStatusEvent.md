# Httpstatusevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class HTTPStatusEvent  
Inheritance| HTTPStatusEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The application dispatches HTTPStatusEvent objects when a network request returns an HTTP status code. 

HTTPStatusEvent objects are always sent before error or completion events. An HTTPStatusEvent object does not necessarily indicate an error condition; it simply reflects the HTTP status code (if any) that is provided by the networking stack. Some Flash Player environments may be unable to detect HTTP status codes; a status code of 0 is always reported in these cases.

In Flash Player, there is only one type of HTTPStatus event: `httpStatus`. In the AIR runtime, a FileReference, URLLoader, or URLStream can register to listen for an `httpResponseStatus`, which includes `responseURL` and `responseHeaders` properties. These properties are undefined in a `httpStatus` event.

[View the examples.](#includeExamplesSummary)

  

* * *