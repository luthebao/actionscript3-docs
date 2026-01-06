# Regexp

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class RegExp  
Inheritance| RegExp ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The RegExp class lets you work with regular expressions, which are patterns that you can use to perform searches in strings and to replace text in strings. 

You can create a new RegExp object by using the `new RegExp()` constructor or by assigning a RegExp literal to a variable:
    
    
     var pattern1:RegExp = new RegExp("test-\\d", "i");
    
         var pattern2:RegExp = /test-\d/i;
    
         

For more information, see "Using Regular Expressions" in the _ActionScript 3.0 Developer's Guide_.

[View the examples.](#includeExamplesSummary)

See also

[String.match()](String.html#match\(\))   
[String.replace()](String.html#replace\(\))   
[String.search()](String.html#search\(\))

  

* * *