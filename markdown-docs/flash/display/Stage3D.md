# Stage3D

Package| [flash.display](package-detail.html)  
---|---  
Class| public class Stage3D  
Inheritance| Stage3D ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3   
---|---  
  
The Stage3D class provides a display area and a programmable rendering context for drawing 2D and 3D graphics. 

Stage3D provides a high-performance rendering surface for content rendered using the `Context3D` class. This surface uses the graphics processing unit (GPU) when possible. The runtime stage provides a fixed number of `Stage3D` objects. The number of instances varies by the type of device. Desktop computers typically provide four Stage3D instances.

Content drawn to the `Stage3D` viewport is composited with other visible graphics objects in a predefined order. The most distant are all `StageVideo` surfaces. `Stage3D` comes next, with traditional Flash display object content being rendered last, on top of all others. StageVideo and Stage3D layers are rendered with no transparency; thus a viewport completely obscures any other Stage3D or StageVideo viewports positioned underneath it. Display list content is rendered with transparency.

**Note:** You can use the `visible` property of a Stage3D object to remove it from the display temporarily, such as when playing a video using the StageVideo class.

A `Stage3D` object is retrieved from the Player stage using its `stage3Ds` member. Use the Stage3D instance to request an associated rendering context and to position the display on the runtime stage.

See also

[Stage](Stage.html)   
[flash.display3D.Context3D](../display3D/Context3D.html)

  

* * *