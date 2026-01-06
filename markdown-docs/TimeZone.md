# Timezone

Package| [Top Level](package-detail.html)  
---|---  
Class| public class TimeZone  
Inheritance| TimeZone ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 50   
---|---  
  
The TimeZone class provides information about timezones that can be used in date calculations and to find out about different locations and their time zone offsets. The information available will vary according to the operating system being used as the time zone objects are created based on APIs that are made available by the device OS. 

To list available time zones, use the `TimeZone.availableTimeZoneNames` property which will be initialized on first use by the operating system. Strings that are available here can then be used to create a TimeZone object using the `TimeZone.getTimeZone` method.

  

* * *