# Numberformatter

Package| [flash.globalization](package-detail.html)  
---|---  
Class| public final class NumberFormatter  
Inheritance| NumberFormatter ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The NumberFormatter class provides locale-sensitive formatting and parsing of numeric values. It can format `int`, `uint`, and `Number` objects. 

The NumberFormatter class uses the data and functionality provided by the operating system and is designed to format numbers according to the conventions of a specific locale, based on the user's preferences and features supported by the user's operating system. The position of the negative symbol, the decimal separator, the grouping separator, the grouping pattern, and other elements within the number format can vary depending on the locale.

If the operating system supports the requested locale, the number formatting properties are set according to the conventions and defaults of the requested locale. If the requested locale is not available, then the properties are set according to a fallback or default system locale, which can be retrieved using the `actualLocaleIDName` property. 

Due to the use of the user's settings, the use of formatting patterns provided by the operating system, and the use of a fallback locale when a requested locale is not supported, different users can see different formatting results, even when using the same locale ID. 

[View the examples.](#includeExamplesSummary)

  

* * *