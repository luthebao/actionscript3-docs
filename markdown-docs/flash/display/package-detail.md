# Package Detail

The flash.display package contains the core classes that the Flash Player uses to build visual displays.

  

* * *

Interfaces

| Interface| Description  
---|---|---  
|  _[IBitmapDrawable](IBitmapDrawable.html)_|  The IBitmapDrawable interface is implemented by objects that can be passed as the `source` parameter of the `draw()` method of the BitmapData class.  
|  _[IGraphicsData](IGraphicsData.html)_|  This interface is used to define objects that can be used as parameters in the flash.display.Graphics methods, including fills, strokes, and paths.  
|  _[IGraphicsFill](IGraphicsFill.html)_|  This interface is used to define objects that can be used as fill parameters in the flash.display.Graphics methods and drawing classes.  
|  _[IGraphicsPath](IGraphicsPath.html)_|  This interface is used to define objects that can be used as path parameters in the flash.display.Graphics methods and drawing classes.  
|  _[IGraphicsStroke](IGraphicsStroke.html)_|  This interface is used to define objects that can be used as stroke parameters in the flash.display.Graphics methods and drawing classes.  
  
Classes

| Class| Description  
---|---|---  
| [ActionScriptVersion](ActionScriptVersion.html)|  The ActionScriptVersion class is an enumeration of constant values that indicate the language version of a loaded SWF file.  
| [AVM1Movie](AVM1Movie.html)|  AVM1Movie is a simple class that represents AVM1 movie clips, which use ActionScript 1.0 or 2.0.  
| [Bitmap](Bitmap.html)|  The Bitmap class represents display objects that represent bitmap images.  
| [BitmapData](BitmapData.html)|  The BitmapData class lets you work with the data (pixels) of a Bitmap object bitmap image.  
| [BitmapDataChannel](BitmapDataChannel.html)|  The BitmapDataChannel class is an enumeration of constant values that indicate which channel to use: red, blue, green, or alpha transparency.  
| [BitmapEncodingColorSpace](BitmapEncodingColorSpace.html)|  The BitmapEncodingColorSpace class defines the constants that specify how color channels are sampled by the `flash.display.BitmapData.encode()` method when specifying the compressor as flash.display.JPEGXREncoderOptions.  
| [BlendMode](BlendMode.html)|  A class that provides constant values for visual blend mode effects.  
| [CapsStyle](CapsStyle.html)|  The CapsStyle class is an enumeration of constant values that specify the caps style to use in drawing lines.  
| [ColorCorrection](ColorCorrection.html)|  The ColorCorrection class provides values for the `flash.display.Stage.colorCorrection` property.  
| [ColorCorrectionSupport](ColorCorrectionSupport.html)|  The ColorCorrectionSupport class provides values for the `flash.display.Stage.colorCorrectionSupport` property.  
| [DisplayObject](DisplayObject.html)|  The DisplayObject class is the base class for all objects that can be placed on the display list.  
| [DisplayObjectContainer](DisplayObjectContainer.html)|  The DisplayObjectContainer class is the base class for all objects that can serve as display object containers on the display list.  
| [FocusDirection](FocusDirection.html)|  The FocusDirection class enumerates values to be used for the `direction` parameter of the `assignFocus()` method of a Stage object and for the `direction` property of a FocusEvent object.  
| [FrameLabel](FrameLabel.html)|  The FrameLabel object contains properties that specify a frame number and the corresponding label name.  
| [GradientType](GradientType.html)|  The GradientType class provides values for the `type` parameter in the `beginGradientFill()` and `lineGradientStyle()` methods of the flash.display.Graphics class.  
| [Graphics](Graphics.html)|  The Graphics class contains a set of methods that you can use to create a vector shape.  
| [GraphicsBitmapFill](GraphicsBitmapFill.html)|  Defines a bitmap fill.  
| [GraphicsEndFill](GraphicsEndFill.html)|  Indicates the end of a graphics fill.  
| [GraphicsGradientFill](GraphicsGradientFill.html)|  Defines a gradient fill.  
| [GraphicsPath](GraphicsPath.html)|  A collection of drawing commands and the coordinate parameters for those commands.  
| [GraphicsPathCommand](GraphicsPathCommand.html)|  Defines the values to use for specifying path-drawing commands.  
| [GraphicsPathWinding](GraphicsPathWinding.html)|  The GraphicsPathWinding class provides values for the `flash.display.GraphicsPath.winding` property and the `flash.display.Graphics.drawPath()` method to determine the direction to draw a path.  
| [GraphicsShaderFill](GraphicsShaderFill.html)|  Defines a shader fill.  
| [GraphicsSolidFill](GraphicsSolidFill.html)|  Defines a solid fill.  
| [GraphicsStroke](GraphicsStroke.html)|  Defines a line style or stroke.  
| [GraphicsTrianglePath](GraphicsTrianglePath.html)|  Defines an ordered set of triangles that can be rendered using either (u,v) fill coordinates or a normal fill.  
| [InteractiveObject](InteractiveObject.html)|  The InteractiveObject class is the abstract base class for all display objects with which the user can interact, using the mouse, keyboard, or other user input device.  
| [InterpolationMethod](InterpolationMethod.html)|  The InterpolationMethod class provides values for the `interpolationMethod` parameter in the `Graphics.beginGradientFill()` and `Graphics.lineGradientStyle()` methods.  
| [JointStyle](JointStyle.html)|  The JointStyle class is an enumeration of constant values that specify the joint style to use in drawing lines.  
| [JPEGEncoderOptions](JPEGEncoderOptions.html)|  The JPEGEncoderOptions class defines a compression algorithm for the `flash.display.BitmapData.encode()` method.  
| [JPEGXREncoderOptions](JPEGXREncoderOptions.html)|  The JPEGXREncoderOptions class defines a compression algorithm for the `flash.display.BitmapData.encode()` method.  
| [LineScaleMode](LineScaleMode.html)|  The LineScaleMode class provides values for the `scaleMode` parameter in the `Graphics.lineStyle()` method.  
| [Loader](Loader.html)|  The Loader class is used to load SWF files or image (JPG, PNG, or GIF) files.  
| [LoaderInfo](LoaderInfo.html)|  The LoaderInfo class provides information about a loaded SWF file or a loaded image file (JPEG, GIF, or PNG).  
| [MorphShape](MorphShape.html)|  The MorphShape class represents MorphShape objects on the display list.  
| [MovieClip](MovieClip.html)|  The MovieClip class inherits from the following classes: Sprite, DisplayObjectContainer, InteractiveObject, DisplayObject, and EventDispatcher.  
| [NativeMenu](NativeMenu.html)|  The NativeMenu class contains methods and properties for defining native menus.  
| [NativeMenuItem](NativeMenuItem.html)|  The NativeMenuItem class represents a single item in a menu.  
| [NativeWindow](NativeWindow.html)|  The NativeWindow class provides an interface for creating and controlling native desktop windows.  
| [NativeWindowDisplayState](NativeWindowDisplayState.html)|  The NativeWindowDisplayState class defines constants for the names of the window display states.  
| [NativeWindowInitOptions](NativeWindowInitOptions.html)|  The NativeWindowInitOptions class defines the initialization options used to construct a new NativeWindow instance.  
| [NativeWindowRenderMode](NativeWindowRenderMode.html)|  The NativeWindowRenderMode class defines constants for the `renderMode` property of the NativeWindowInitOptions object used to create a native window.  
| [NativeWindowResize](NativeWindowResize.html)|  The NativeWindowResize class defines constants for the possible values of the `edgeOrCorner` parameter of the NativeWindow `startResize()` method.  
| [NativeWindowSystemChrome](NativeWindowSystemChrome.html)|  The NativeWindowSystemChrome class defines constants for the `systemChrome` property of the NativeWindowInitOptions object used to create a native window.  
| [NativeWindowType](NativeWindowType.html)|  The NativeWindowType class defines constants for the `type` property of the NativeWindowInitOptions object used to create a native window.  
| [PixelSnapping](PixelSnapping.html)|  The PixelSnapping class is an enumeration of constant values for setting the pixel snapping options by using the `pixelSnapping` property of a Bitmap object.  
| [PNGEncoderOptions](PNGEncoderOptions.html)|  The PNGEncoderOptions class defines a compression algorithm for the `flash.display.BitmapData.encode()` method.  
| [Scene](Scene.html)|  The Scene class includes properties for identifying the name, labels, and number of frames in a scene.  
| [Screen](Screen.html)|  The Screen class provides information about the display screens available to this application.  
| [ScreenMode](ScreenMode.html)|  The ScreenMode object provides information about the width, height and refresh rate of a Screen.  
| [Shader](Shader.html)|  A Shader instance represents a Pixel Bender shader kernel in ActionScript.  
| [ShaderData](ShaderData.html)|  A ShaderData object contains properties representing any parameters and inputs for a shader kernel, as well as properties containing any metadata specified for the shader.  
| [ShaderInput](ShaderInput.html)|  A ShaderInput instance represents a single input image for a shader kernel.  
| [ShaderJob](ShaderJob.html)|  A ShaderJob instance is used to execute a shader operation in stand-alone mode.  
| [ShaderParameter](ShaderParameter.html)|  A ShaderParameter instance represents a single input parameter of a shader kernel.  
| [ShaderParameterType](ShaderParameterType.html)|  This class defines the constants that represent the possible values for the ShaderParameter class's `type` property.  
| [ShaderPrecision](ShaderPrecision.html)|  This class defines the constants that represent the possible values for the Shader class's `precisionHint` property.  
| [Shape](Shape.html)|  This class is used to create lightweight shapes using the ActionScript drawing application program interface (API).  
| [SimpleButton](SimpleButton.html)|  The SimpleButton class lets you control all instances of button symbols in a SWF file.  
| [SpreadMethod](SpreadMethod.html)|  The SpreadMethod class provides values for the `spreadMethod` parameter in the `beginGradientFill()` and `lineGradientStyle()` methods of the Graphics class.  
| [Sprite](Sprite.html)|  The Sprite class is a basic display list building block: a display list node that can display graphics and can also contain children.  
| [Stage](Stage.html)|  The Stage class represents the main drawing area.  
| [Stage3D](Stage3D.html)|  The Stage3D class provides a display area and a programmable rendering context for drawing 2D and 3D graphics.  
| [StageAlign](StageAlign.html)|  The StageAlign class provides constant values to use for the `Stage.align` property.  
| [StageAspectRatio](StageAspectRatio.html)|  The StageAspectRatio class provides values for the `Stage.setAspectRatio()` method.  
| [StageDisplayState](StageDisplayState.html)|  The StageDisplayState class provides values for the `Stage.displayState` property.  
| [StageOrientation](StageOrientation.html)|  The StageOrientation class defines constants enumerating the possible orientations of the stage and the device.  
| [StageQuality](StageQuality.html)|  The StageQuality class provides values for the `Stage.quality` property and for the value of the `quality` parameter to the `BitmapData.drawWithQuality()` method.  
| [StageScaleMode](StageScaleMode.html)|  The StageScaleMode class provides values for the `Stage.scaleMode` property.  
| [SWFVersion](SWFVersion.html)|  The SWFVersion class is an enumeration of constant values that indicate the file format version of a loaded SWF file.  
| [TriangleCulling](TriangleCulling.html)|  Defines codes for culling algorithms that determine which triangles not to render when drawing triangle paths.  
  
© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:12 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)