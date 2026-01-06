# Collator

Package| [flash.globalization](package-detail.html)  
---|---  
Class| public final class Collator  
Inheritance| Collator ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The Collator class provides locale-sensitive string comparison capabilities. 

This class uses the string comparison services provided by the operating system. The comparisons differ according to the locale identifier that is provided when the class instance is created. ActionScript stores strings using the Unicode character set. The Boolean string comparison operators (==, !=, <, <=, >, >=) use Unicode code points for comparison. In most cases the resulting sort order doesn't match the conventions of a particular language and region, and thus should not be used to sort strings that are presented in a user interface. In contrast the comparison methods in this class provide an order that adheres to these conventions. 

Here are some examples where the sort order differs depending on the language: 

  * In English, lowercase a is before uppercase A and uppercase A is before lowercase b.
  * ö is after z in Swedish, whereas in German ö is after o
  * ch is sorted as one character between c-d in traditional Spanish

Sort orders can even differ within the same language and region depending on the usage. For example, in German there is a different sort order used for names in a phone book versus words in a dictionary. In Chinese and Japanese there are different ways of sorting the ideographic characters: by pronunciation or by the ideographic radical and the number of strokes uses in the glyph. In Spanish and Georgian, there is a difference between modern and traditional sorting. 

The comparison methods in this class provide two main usage modes. The `initialMode` parameter of the `Collator()` constructor controls these modes. The default "sorting" mode is for sorting items that are displayed to an end user. In this mode, comparison is more strict to ensure that items that are otherwise the same are sorted in a consistent manner. For example, uppercase letters and lowercase letters do not compare as equal. In the "matching" mode the comparison is more lenient. For example in this mode uppercase and lowercase letters are treated equally. Here's an example that demonstrates both of these modes: 
    
    
     
         var sortingCollator:Collator = new Collator("en-US", CollatorMode.SORTING);
         var words:Array = new  Array("Airplane" , "airplane", "boat", "Boat");
         words.sort(sortingCollator.compare);
         trace(words);
                  
         var matchingCollator:Collator = new Collator("en-US", CollatorMode.MATCHING);
         if (matchingCollator.equals("Car", "car")) {
           trace("The words match!");
         }
         

Even when providing a locale ID parameter to the constructor as shown above, collation behavior can differ by user based on the user's operating system settings and whether a fallback locale is used when the requested locale is not supported. 

[View the examples.](#includeExamplesSummary)

  

* * *