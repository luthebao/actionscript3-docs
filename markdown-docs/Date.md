# Date

Package| [Top Level](package-detail.html)  
---|---  
Class| public final dynamic class Date  
Inheritance| Date ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0  
---|---  
  
The Date class represents date and time information. An instance of the Date class represents a particular point in time for which the properties such as month, day, hours, and seconds can be queried or modified. The Date class lets you retrieve date and time values relative to universal time (Greenwich mean time, now called universal time or UTC) or relative to local time, which is determined by the local time zone setting on the operating system that is running Flash Player. The methods of the Date class are not static but apply only to the individual Date object specified when the method is called. The `Date.UTC()` and `Date.parse()` methods are exceptions; they are static methods. 

The Date class handles daylight saving time differently, depending on the operating system and runtime version. Flash Player 6 and later versions handle daylight saving time on the following operating systems in these ways:

  * Windows - the Date object automatically adjusts its output for daylight saving time. The Date object detects whether daylight saving time is employed in the current locale, and if so, it detects the standard-to-daylight saving time transition date and times. However, the transition dates currently in effect are applied to dates in the past and the future, so the daylight saving time bias might calculate incorrectly for dates in the past when the locale had different transition dates.
  * Mac OS X - the Date object automatically adjusts its output for daylight saving time. The time zone information database in Mac OS X is used to determine whether any date or time in the present or past should have a daylight saving time bias applied.
  * Mac OS 9 - the operating system provides only enough information to determine whether the current date and time should have a daylight saving time bias applied. Accordingly, the date object assumes that the current daylight saving time bias applies to all dates and times in the past or future.

Flash Player 5 handles daylight saving time on the following operating systems as follows:

  * Windows - the U.S. rules for daylight saving time are always applied, which leads to incorrect transitions in Europe and other areas that employ daylight saving time but have different transition times than the U.S. Flash correctly detects whether daylight saving time is used in the current locale.

To use the Date class, construct a Date instance using the `new` operator.

ActionScript 3.0 adds several new accessor properties that can be used in place of many Date class methods that access or modify Date instances. ActionScript 3.0 also includes several new variations of the `toString()` method that are included for ECMA-262 3rd Edition compliance, including: `Date.toLocaleString()`, `Date.toTimeString()`, `Date.toLocaleTimeString()`, `Date.toDateString()`, and `Date.toLocaleDateString()`.

To compute relative time or time elapsed, see the `getTimer()` method in the flash.utils package.

[View the examples.](#includeExamplesSummary)

See also

[flash.utils.getTimer()](flash/utils/package.html#getTimer\(\))

  

* * *