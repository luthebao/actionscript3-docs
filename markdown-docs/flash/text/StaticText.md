# Statictext

Package| [flash.text](package-detail.html)  
---|---  
Class| public final class StaticText  
Inheritance| StaticText ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](../display/DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
This class represents StaticText objects on the display list. You cannot create a StaticText object using ActionScript. Only the authoring tool can create a StaticText object. An attempt to create a new StaticText object generates an `ArgumentError`. 

To create a reference to an existing static text field in ActionScript 3.0, you can iterate over the items in the display list. For example, the following snippet checks to see if the display list contains a static text field and assigns the field to a variable:
    
    
     var i:uint;
     for (i = 0; i < this.numChildren; i++) {
         var displayitem:DisplayObject = this.getChildAt(i);
         if (displayitem instanceof StaticText) {
             trace("a static text field is item " + i + " on the display list");
             var myFieldLabel:StaticText = StaticText(displayitem);
             trace("and contains the text: " + myFieldLabel.text);
         }
     }
     

  

* * *