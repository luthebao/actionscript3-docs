# Isimpletextselection

Package| [flash.accessibility](package-detail.html)  
---|---  
Interface| public interface ISimpleTextSelection  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The ISimpleTextSelection class can be used to add support for the MSAA ISimpleTextSelection interface to an AccessibilityImplementation. 

If an AccessibilityImplementation subclass implements the two getters in this class, a screen reader such as JAWS can determine the text selection range by calling them. The AccessibilityImplementation subclass does not have to formally declare that it implements this interface; you can simply declare getters for these two properties, as follows:
    
    
    	class TextAreaAccImpl extends AccesibilityImplementation
    	{
    	...
    		public function get selectionAnchorIndex():int
    		{
    		...
    		}
    		public function get selectionActiveIndex():int
    		{
    		...
    	}
    	}
    	

See also

[flash.accessibility.AccessibilityImplementation](../accessibility/AccessibilityImplementation.html)

  

* * *