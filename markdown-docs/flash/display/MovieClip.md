# Movieclip

Package| [flash.display](package-detail.html)  
---|---  
Class| public dynamic class MovieClip  
Inheritance| MovieClip ![Inheritance](../../images/inherit-arrow.gif) [Sprite](Sprite.html) ![Inheritance](../../images/inherit-arrow.gif) [DisplayObjectContainer](DisplayObjectContainer.html) ![Inheritance](../../images/inherit-arrow.gif) [InteractiveObject](InteractiveObject.html) ![Inheritance](../../images/inherit-arrow.gif) [DisplayObject](DisplayObject.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The MovieClip class inherits from the following classes: Sprite, DisplayObjectContainer, InteractiveObject, DisplayObject, and EventDispatcher. 

Unlike the Sprite object, a MovieClip object has a timeline.

>In Flash Professional, the methods for the MovieClip class provide the same functionality as actions that target movie clips. Some additional methods do not have equivalent actions in the Actions toolbox in the Actions panel in the Flash authoring tool. 

Children instances placed on the Stage in Flash Professional cannot be accessed by code from within the constructor of a parent instance since they have not been created at that point in code execution. Before accessing the child, the parent must instead either create the child instance by code or delay access to a callback function that listens for the child to dispatch its `Event.ADDED_TO_STAGE` event.

If you modify any of the following properties of a MovieClip object that contains a motion tween, the playhead is stopped in that MovieClip object: `alpha`, `blendMode`, `filters`, `height`, `opaqueBackground`, `rotation`, `scaleX`, `scaleY`, `scale9Grid`, `scrollRect`, `transform`, `visible`, `width`, `x`, or `y`. However, it does not stop the playhead in any child MovieClip objects of that MovieClip object.

**Note:** Flash Lite 4 supports the MovieClip.opaqueBackground property only if FEATURE_BITMAPCACHE is defined. The default configuration of Flash Lite 4 does not define FEATURE_BITMAPCACHE. To enable the MovieClip.opaqueBackground property for a suitable device, define FEATURE_BITMAPCACHE in your project.

[View the examples.](#includeExamplesSummary)

  

* * *