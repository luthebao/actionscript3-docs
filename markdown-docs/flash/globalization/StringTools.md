# Stringtools

Package| [flash.globalization](package-detail.html)  
---|---  
Class| public final class StringTools  
Inheritance| StringTools ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The StringTools class provides locale-sensitive case conversion methods. 

In some situations the conversion between uppercase and lowercase letters is not a simple mapping from one character to another and instead requires language- or context-specific processing. For example:

  * In Turkish and Azeri, the uppercase of the dotted lowercase **i** is an uppercase dotted **İ** (U+0130). Similarly the lowercase of a dotless uppercase **I** , is a lowercase dotless **ı** (U+0131). 
  * The lowercase sharp S, **ß** (U+00DF), used in German is converted to uppercase double SS.
  * In Greek there are two representations of the lowercase sigma, **σ** (U+03C3) and **ς** (U+03C2), which both convert to the single uppercase sigma **Σ** (U+03A3). 

The `toLowerCase()` and `toUpperCase()` methods of this class provide this special case conversion logic. 

Due to the use of the user's settings, the use of case conversion rules provided by the operating system, and the use of a fallback locale when a requested locale is not supported, different users can see different case conversion results even when using the same locale ID. 

[View the examples.](#includeExamplesSummary)

  

* * *