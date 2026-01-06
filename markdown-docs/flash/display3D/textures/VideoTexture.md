# Videotexture

Package| [flash.display3D.textures](package-detail.html)  
---|---  
Class| public final class VideoTexture  
Inheritance| VideoTexture ![Inheritance](../../../images/inherit-arrow.gif) [TextureBase](TextureBase.html) ![Inheritance](../../../images/inherit-arrow.gif) [EventDispatcher](../../events/EventDispatcher.html) ![Inheritance](../../../images/inherit-arrow.gif) [Object](../../../Object.html)  
  
Prior to Flash Player 21, the use of video in Stage3D required the use of the Video object (which is not hardware accelerated), copying of video frame to a BitmapData object, and loading of the data onto the GPU which is CPU intensive. Thus, Video texture object was introduced. It allows hardware decoded video to be used in Stage 3D content. 

For Flash Player 22, video texture objects were added to support NetStream and Cameras in a manner consistent/ similar to StageVideo. Such textures can be used as source textures in the stage3D rendering pipeline. The textures can be used as rectangular, RGB, no mipmap textures in the rendering of a scene. They are treated as ARGB texture by the shaders (that is, the AGAL shaders do not have to bother about YUV->RGB conversion) and so the standard shaders with static images can be used without change. The image used by the rendering pipeline is the latest up-to-date frame at the time the rendering occurs using this texture. There is no tearing in a video frame, however if the same texture is used several times, some of the instances may be from different timestamps.

  

* * *