# Currencyformatter

Package| [flash.globalization](package-detail.html)  
---|---  
Class| public final class CurrencyFormatter  
Inheritance| CurrencyFormatter ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The CurrencyFormatter class provides locale-sensitive formatting and parsing of currency values. 

The CurrencyFormatter class uses the data and functionality provided by the operating system and is designed to format currency values according to the conventions of a specific locale and type of currency. The position of the currency symbol, the negative symbol, the decimal separator, the grouping separator, the grouping pattern decimal separator, and other elements can vary depending on the locale.

If the operating system supports the requested locale, the properties and currency type are set according to the conventions and defaults of the requested locale. If the requested locale is not available, then the properties are set according to a fallback or default system locale, which can be retrieved using the `actualLocaleIDName` property. 

Due to the use of the user's settings, the use of formatting patterns provided by the operating system, and the use of a fallback locale when a requested locale is not supported, different users can see different formatting results, even when using the same locale ID. 

[View the examples.](#includeExamplesSummary)

  

* * *