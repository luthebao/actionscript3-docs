# Compositionattributerange

Package| [flash.text.ime](package-detail.html)  
---|---  
Class| public final class CompositionAttributeRange  
Inheritance| CompositionAttributeRange ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 2  
---|---  
  
The CompositionAttributeRange class represents a range of composition attributes for use with IME (input method editor) events. For example, when editing text in the IME, the text is divided by the IME into composition ranges. These composition ranges are flagged as selected (such as currently being lengthened, shortened, or edited), and/or converted (meaning the range went through the IME dictionary lookup, already). 

By convention, the client should adorn these composition ranges with underlining or highlighting according to the flags.

For example:
    
    
         !converted              = thick gray underline (raw text)
         !selected && converted  = thin black underline
          selected && converted  = thick black underline
    

See also

[flash.text.ime.IIMEClient](../ime/IIMEClient.html)

  

* * *