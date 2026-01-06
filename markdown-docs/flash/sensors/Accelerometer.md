# Accelerometer

Package| [flash.sensors](package-detail.html)  
---|---  
Class| public class Accelerometer  
Inheritance| Accelerometer ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The Accelerometer class dispatches events based on activity detected by the device's motion sensor. This data represents the device's location or movement along a 3-dimensional axis. When the device moves, the sensor detects this movement and returns acceleration data. The Accelerometer class provides methods to query whether or not accelerometer is supported, and also to set the rate at which acceleration events are dispatched. 

**Note:** Use the `Accelerometer.isSupported` property to test the runtime environment for the ability to use this feature. While the Accelerometer class and its members are accessible to the Runtime Versions listed for each API entry, the current environment for the runtime determines the availability of this feature. For example, you can compile code using the Accelerometer class properties for Flash Player 10.1, but you need to use the `Accelerometer.isSupported` property to test for the availability of the Accelerometer feature in the current deployment environment for the Flash Player runtime. If `Accelerometer.isSupported` is `true` at runtime, then Accelerometer support currently exists.

_AIR profile support:_ This feature is supported only on mobile devices. It is not supported on desktop or AIR for TV devices. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles. 

[View the examples.](#includeExamplesSummary)

See also

[isSupported](../sensors/Accelerometer.html#isSupported)   
[flash.events.AccelerometerEvent](../events/AccelerometerEvent.html)   
[Michael Chaize: AIR and the Accelerometer](http://www.riagora.com/2010/04/air-and-the-accelerometer/)   
[Michael Chaize: Become an AIR Pilot](http://www.riagora.com/2010/05/become-an-air-pilot/)

  

* * *