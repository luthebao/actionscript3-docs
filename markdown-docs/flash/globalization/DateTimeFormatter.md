# Datetimeformatter

Package| [flash.globalization](package-detail.html)  
---|---  
Class| public final class DateTimeFormatter  
Inheritance| DateTimeFormatter ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The DateTimeFormatter class provides locale-sensitive formatting for Date objects and access to localized date field names. The methods of this class use functions and settings provided by the operating system. 

There are two ways to select a date time format: using a predefined pattern or a custom pattern. For most applications the predefined styles specified by the DateTimeStyle constants (`LONG`, `MEDIUM`, `NONE`, or `SHORT` should be used. These constants specify the default patterns for the requested locale or the default patterns based on the user's operating system settings. 

For example the following code creates a date string using the default short date format: 
    
    
     
    	 var df:DateTimeFormatter = new DateTimeFormatter(LocaleID.DEFAULT, DateTimeStyle.SHORT, DateTimeStyle.NONE);
    	 var currentDate:Date = new Date();
    	 var shortDate:String = df.format(currentDate);
    	 

When an instance of this class is created, if the requested locale is supported by the operating system then the properties of the instance are set according to the conventions and defaults of the requested locale and the constructor's `dateStyle` and `timeStyle` parameters. If the requested locale is not available, then the properties are set according to a fallback or default system locale, which can be retrieved using the `actualLocaleIDName` property. 

This class contains additional methods to get localized strings for month names and weekday names, and to retrieve the first day of the week that can be used in a calendar picker or other similar application. 

Due to the use of the user's settings, the use of formatting patterns provided by the operating system, and the use of a fallback locale when a requested locale is not supported, different users can see different formatting results even when using the same locale ID. 

[View the examples.](#includeExamplesSummary)

See also

[actualLocaleIDName](../globalization/DateTimeFormatter.html#actualLocaleIDName)   
[DateTimeStyle](DateTimeStyle.html)

  

* * *