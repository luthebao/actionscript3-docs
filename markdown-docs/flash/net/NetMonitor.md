# Netmonitor

Package| [flash.net](package-detail.html)  
---|---  
Class| public class NetMonitor  
Inheritance| NetMonitor ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2.7   
---|---  
  
The NetMonitor class maintains a list of NetStream objects. 

Use the NetMonitor class to keep track of NetStream objects in use in an application. An instance of this class dispatches a `netStreamCreate` event whenever a new NetStream object is created.

You can use the NetMonitor class to help track video playback and related events without regard to the specific video player being used. This facility can be helpful when implementing media measurement, analytics, and usage tracking libraries.

**Note:** NetStream monitoring is not supported by Flash Player in the browser on Android and Blackberry Tablet OS, or by AIR on iOS.

See also

[NetStream](../net/NetStream.html)

  

* * *