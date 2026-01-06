# Migration

The following table describes the differences between ActionScript 2.0 and 3.0.

  
| ActionScript 2.0| ActionScript 3.0| Comments  
---|---|---|---  
| **Compiler directives**  
| #endinitclip | Removed| The `#endinitclip` directive identifies the end of initialization code in ActionScript 2.0, but has no use in ActionScript 3.0.  
| #include | Removed| See the `include` statement for similar functionality.  
| #initclip | Removed| The `#initclip` directive identifies the beginning of initialization code in ActionScript 2.0, but has no use in ActionScript 3.0.  
| **Constants**  
| false | [false](statements.html#false)| The value `false`, rather than `undefined`, is the default value of a Boolean object.  
| NaN | [NaN](package.html#NaN)| The value `NaN`, rather than `undefined`, is the default value of a Number object.  
| newline | Removed| Use the escape sequence composed of the backslash character followed by the character "n" (\n).  
| null | [null](statements.html#null)| The value `null`, rather than `undefined`, is the default value of the Object and String classes.  
| undefined | [undefined](package.html#undefined)| The value `undefined` can be assigned only to untyped variables; it is not the default value of any typed object.  
| **Global functions**  
| asfunction | [flash.text.TextField dispatches event: link](flash/text/TextField.html#event:link)| Replaced by the new event handling model. You now get the same functionality by using the syntax `Event:` instead of `asfunction:`. When a user clicks the link, Flash Player dispatches a TextEvent object of type TextEvent.LINK, which your code can listen for with the `addEventListener()` method. Any text that you decide to include is stored in the event object's `text` property.  
| call() | Removed| The `call()` function was deprecated. > Use the `function` statement for similar functionality.  
| chr() | Removed| Use String.fromCharCode() instead.  
| clearInterval() | [flash.utils.clearInterval()](flash/utils/package.html#clearInterval\(\))| Moved to flash.utils package.  
| clearTimeout() | [flash.utils.clearTimeout()](flash/utils/package.html#clearTimeout\(\))| Moved to flash.utils package.  
| duplicateMovieClip() | [flash.display.MovieClip.MovieClip()](flash/display/MovieClip.html#MovieClip\(\))| Replaced by new MovieClip class constructor function.  
| eval() | Removed| There is no equivalent in ActionScript 3.0.  
| fscommand() | [flash.system.fscommand()](flash/system/package.html#fscommand\(\))| Moved to flash.system package. Also, see flash.external.ExternalInterface class for JavaScript/ActionScript communication.  
| getProperty() | Removed| To directly access properties, use the dot (.) operator.  
| getTimer() | [flash.utils.getTimer()](flash/utils/package.html#getTimer\(\))| Moved to flash.utils package.  
| getURL() | [flash.net.navigateToURL()](flash/net/package.html#navigateToURL\(\))| Replaced by the `navigateToURL()` function.  
| getVersion() | [flash.system.Capabilities.version](flash/system/Capabilities.html#version)| Moved to Capabilities class and changed to accessor property.  
| gotoAndPlay() | [flash.display.MovieClip.gotoAndPlay()](flash/display/MovieClip.html#gotoAndPlay\(\))| This function is no longer a global function, but is still available as a method of the MovieClip class.  
| gotoAndStop() | [flash.display.MovieClip.gotoAndStop()](flash/display/MovieClip.html#gotoAndStop\(\))| This function is no longer a global function, but it is still available as a method of the MovieClip class.  
| ifFrameLoaded() | [flash.display.MovieClip.framesLoaded](flash/display/MovieClip.html#framesLoaded)|   
| int() | [int()](package.html#int\(\))| int() Resurrected from deprecated status as a conversion function for the new int data type.  
| length() | [String.length](String.html#length)| This property is no longer a global property, but it is still available as a property of the String class.  
| loadMovie() | [flash.display.Loader](flash/display/Loader.html)| Use the Loader class instead.  
| loadMovieNum() | [flash.display.Loader](flash/display/Loader.html)| Use the Loader class instead.  
| loadVariables() | [flash.net.URLLoader](flash/net/URLLoader.html)| Use the URLLoader class instead.  
| loadVariablesNum() | [flash.net.URLLoader](flash/net/URLLoader.html)| Use the URLLoader class instead.  
| mbchr() | [String.fromCharCode()](String.html#fromCharCode\(\))| Removed. Use the static `String.fromCharCode()` method instead.  
| mblength() | [String.length](String.html#length)| Removed. Use `String.length` instead.  
| mbord() | [String.charCodeAt()](String.html#charCodeAt\(\))| Removed. Use `String.charCodeAt()` instead.  
| mbsubstring() | [String.substr()](String.html#substr\(\))| Removed. Use `String.substr()` instead.  
| nextFrame() | [flash.display.MovieClip.nextFrame()](flash/display/MovieClip.html#nextFrame\(\))| This function is no longer a global function, but it is still available as a method of the MovieClip class.  
| nextScene() | [flash.display.MovieClip.nextScene()](flash/display/MovieClip.html#nextScene\(\))| This function is no longer a global function, but it is still available as a method of the MovieClip class.  
| on() | [flash.events.EventDispatcher](flash/events/EventDispatcher.html)| Removed. Use the new event handling system in the flash.events package instead.  
| onClipEvent() | [flash.events.EventDispatcher](flash/events/EventDispatcher.html)| Removed. Use the new event handling system in the flash.events package instead.  
| ord() | [String](String.html)| Removed. Use String class methods instead.  
| parseInt() | [parseInt()](package.html#parseInt\(\))| A string with a leading 0 is interpreted as decimal rather than octal. For octal numbers, pass the number 8 for the radix parameter.  
| play() | [flash.display.MovieClip.play()](flash/display/MovieClip.html#play\(\))| This function is no longer a global function, but it is still available as a method of the MovieClip class.  
| prevFrame() | [flash.display.MovieClip.prevFrame()](flash/display/MovieClip.html#prevFrame\(\))| This function is no longer a global function, but it is still available as a method of the MovieClip class.  
| prevScene() | [flash.display.MovieClip.prevScene()](flash/display/MovieClip.html#prevScene\(\))| This function is no longer a global function, but it is still available as a method of the MovieClip class.  
| print() | [flash.printing.PrintJob](flash/printing/PrintJob.html)| Removed. Use the PrintJob class instead.  
| printAsBitmap() | [flash.printing.PrintJob](flash/printing/PrintJob.html)| Removed. Use the PrintJob class instead.  
| printAsBitmapNum() | [flash.printing.PrintJob](flash/printing/PrintJob.html)| Removed. Use the PrintJob class instead.  
| printNum() | [flash.printing.PrintJob](flash/printing/PrintJob.html)| Removed. Use the PrintJob class instead.  
| random() | [Math.random()](Math.html#random\(\))| Removed. Use `Math.random()` instead.  
| removeMovieClip() | Removed| Set all references to a movie clip to `null` to make the movie clip eligible for garbage collection.  
| setInterval() | [flash.utils.setInterval()](flash/utils/package.html#setInterval\(\))| Moved to flash.utils package. Consider using the Timer class instead.  
| setProperty() | Removed| To set the value of a writable property, use the dot (.) operator.  
| setTimeout() | [flash.utils.setTimeout()](flash/utils/package.html#setTimeout\(\))| Moved to flash.utils package.  
| showRedrawRegions() | [flash.profiler.showRedrawRegions()](flash/profiler/package.html#showRedrawRegions\(\))| Moved to flash.profiler package.  
| startDrag() | [flash.display.Sprite.startDrag()](flash/display/Sprite.html#startDrag\(\))| This is no longer a global function, but it is still available as a method of the Sprite class.  
| stop() | [flash.display.MovieClip.stop()](flash/display/MovieClip.html#stop\(\))| This is no longer a global function, but it is still available as a method of the MovieClip class.  
| stopAllSounds() | [flash.media.SoundMixer.stopAll()](flash/media/SoundMixer.html#stopAll\(\))| This is no longer a global function, but it is still available as a method of the SoundMixer class, which provides global sound control.  
| stopDrag() | [flash.display.Sprite.stopDrag()](flash/display/Sprite.html#stopDrag\(\))| This is no longer a global function, but it is still available as a method of the Sprite class.  
| substring() | [String.substring()](String.html#substring\(\))| This is no longer a global function, but it is still available as a method of the String class.  
| targetPath() | Removed| ActionScript 3.0 identifies display objects directly; therefore, identifying a > display object by its path is no longer necessary.  
| tellTarget() | Removed| Use the dot (.) operator or the `with` statement instead.  
| toggleHighQuality() | [flash.display.Stage.quality](flash/display/Stage.html#quality)| Removed as a global property. Use the Stage class version instead.  
| trace() | [trace()](package.html#trace\(\))| The `trace()` method accepts a comma-delimited list of arguments.  
| unloadMovie() | [flash.display.Loader.unload()](flash/display/Loader.html#unload\(\))| Removed. Use `Loader.unload()` instead.  
| unloadMovieNum() | [flash.display.Loader.unload()](flash/display/Loader.html#unload\(\))| Removed. Use `Loader.unload()` instead.  
| updateAfterEvent() | [flash.events.TimerEvent.updateAfterEvent()](flash/events/TimerEvent.html#updateAfterEvent\(\))| This is no longer a global function, but it is still available as a method of the TimerEvent, MouseEvent, and KeyboardEvent classes.  
| **Global properties**  
| _accProps | [flash.accessibility.AccessibilityProperties](flash/accessibility/AccessibilityProperties.html)| Replaced by the AccessibilityProperties class.  
| _focusrect | [flash.display.InteractiveObject.focusRect](flash/display/InteractiveObject.html#focusRect)| Replaced by the `focusRect` property of the InteractiveObject class.  
| _global | Removed| Use a static member of a class instead.  
| _highquality | [flash.display.Stage.quality](flash/display/Stage.html#quality)| Replaced by the `quality` property of the Stage class.  
| _level | Removed| The concept of levels does not exist in ActionScript 3.0, which instead provides direct access to the display list. See the flash.display package for details.  
| maxscroll | [flash.text.TextField](flash/text/TextField.html)| Replaced by the `maxScrollH` and `maxScrollV` properties of the TextField class.  
| _parent | [flash.display.DisplayObject.parent](flash/display/DisplayObject.html#parent)| Replaced by the `parent` property of the DisplayObject class.  
| _quality | [flash.display.Stage.quality](flash/display/Stage.html#quality)| Replaced by the `quality` property of the Stage class.  
| _root | [flash.display.DisplayObject.stage](flash/display/DisplayObject.html#stage)| Removed. The closest equivalent is the Stage, which serves as the root of the ActionScript 3.0 display list.  
| scroll | [flash.text.TextField](flash/text/TextField.html)| Removed. Replaced by the `scrollH` and `scrollV` properties of the TextField class.  
| _soundbuftime | [flash.media.SoundMixer.bufferTime](flash/media/SoundMixer.html#bufferTime)| Replaced by the `bufferTime` property of the SoundMixer class.  
| this | [this](statements.html#this)| Instance methods are bound to the instance that implemented the method; therefore, the `this` reference inside the body of an instance method always refers to the instance that implemented the method.  
| **Operators**  
| add (concatenation (strings))| Removed| Use the concatenation (+) operator instead.  
| eq (equality (strings))| Removed| Use the equality (==) operator instead.  
| gt (greater than (strings))| Removed| Use the greater than (`>`) operator instead.  
| ge (greater than or equal to (strings))| Removed| Use the greater than or equal to (`>=`) operator instead.  
| <> (inequality)| Removed| Use the inequality (`!=`) operator instead.  
| instanceof| [is](operators.html#is)| Although the `instanceof` operator is available, it only checks the prototype chain, which is not the primary inheritance mechanism in ActionScript 3.0. Use the `is` operator to check whether an object is a member of a specific data type.  
| lt (less than (strings))| Removed| Use the less than (`<`) operator instead.  
| le (less than or equal to (strings))| Removed| Use the less than or equal to (`<=`) operator instead.  
| and (logical AND)| Removed| Use the logical AND (`&&`) operator instead.  
| not (logical NOT)| Removed| Use the logical NOT (`!`) operator instead.  
| or (logical OR)| Removed| Use the logical OR (`||`) operator instead.  
| ne (not equal (strings))| Removed| Use the inequality (`!=`) operator instead.  
| **Statements**  
| delete| [delete](operators.html#delete)| The `delete` operator works only on properties of objects, but not on variables that hold references to objects.  
| import| [import](statements.html#import)| The `import` statement is not optional. To use a class, you must import it, whether or not you use a fully qualified name.  
| intrinsic| Removed| ActionScript 3.0 has a similar, but not identical, keyword named `native`. The `native` keyword is similar to `intrinsic` in that it directs the compiler not to expect a function body, but is dissimilar in that `native` has no effect on compile-time type checking.  
| private| [private](statements.html#private)| The ActionScript 3.0 `private` keyword specifies that an identifier is visible only within a class, and does not extend to subclasses. Moreover, in ActionScript 3.0 the `private` keyword is enforced at both compile time and run time.  
| set variable| Removed| Use the assignment (`=`) operator instead.  
| super| [super](statements.html#super)| In ActionScript 3.0, the call to `super()` in a subclass constructor does not have to be the first statement in the constructor body.  
| **Accessibility class**| [flash.accessibility.Accessibility](flash/accessibility/Accessibility.html)|   
| isActive() Method | [flash.accessibility.Accessibility.active](flash/accessibility/Accessibility.html#active)| Changed from function to accessor property. Name changed from `isActive` to `active`.  
| updateProperties() Method | [flash.accessibility.Accessibility.updateProperties()](flash/accessibility/Accessibility.html#updateProperties\(\))|   
| **arguments class**| [arguments](arguments.html)|   
| caller Property | Removed| You can achieve the same functionality by passing `arguments.callee` from the caller function as an argument to the callee function. See the Examples section of `arguments.callee` for an example.  
| **Array class**|   
| CASEINSENSITIVE Constant | [Array.CASEINSENSITIVE](Array.html#CASEINSENSITIVE)| Data type changed to uint.  
| DESCENDING Constant | [Array.DESCENDING](Array.html#DESCENDING)| Data type changed to uint.  
| length Property | [Array.length](Array.html#length)| Data type changed to uint.  
| NUMERIC Constant | [Array.NUMERIC](Array.html#NUMERIC)| Data type changed to uint.  
| RETURNINDEXEDARRAY Constant | [Array.RETURNINDEXEDARRAY](Array.html#RETURNINDEXEDARRAY)| Data type changed to uint.  
| UNIQUESORT Constant | [Array.UNIQUESORT](Array.html#UNIQUESORT)| Data type changed to uint.  
| Array Constructor | [Array.Array()](Array.html#Array\(\))| Parameter changed to use the ...(rest) parameter format.  
| push() Method | [Array.push()](Array.html#push\(\))| Parameter changed to use the ...(rest) parameter format.  
| sort() Method | [Array.sort()](Array.html#sort\(\))| Data type of the `options` parameter changed to uint.  
| sortOn() Method | [Array.sortOn()](Array.html#sortOn\(\))| Data type of the `options` parameter changed to uint. The ActionScript 3.0 version also has added functionality; you can now sort on more than one field name by passing an array of objects for the `fieldName` parameter, and each sort field can have its own matching `options` parameter if you also pass in a matching array of options flags for the `options` parameter.  
| splice() Method | [Array.splice()](Array.html#splice\(\))| The parameters can have any data type, but the preferred data types are int and uint. The `value` parameter changed to the ...(rest) parameter format.  
| unshift() Method | [Array.unshift()](Array.html#unshift\(\))| The `value` parameter changed to the ...(rest) format. Data type of the return value changed to uint.  
| **AsBroadcaster class**| [flash.events.EventDispatcher](flash/events/EventDispatcher.html)|   
| _listeners Property[read-only] | [flash.events.EventDispatcher.willTrigger()](flash/events/EventDispatcher.html#willTrigger\(\))| Not a direct equivalent. The `willTrigger()` method tells you whether any listeners are registered, but not how many.  
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| Not a direct equivalent, because the ActionScript 3.0 event model lets you add event listeners to any object in the event flow, not just to the broadcasting object.  
| broadcastMessage() Method | [flash.events.EventDispatcher.dispatchEvent()](flash/events/EventDispatcher.html#dispatchEvent\(\))| Not a direct equivalent, because the ActionScript 3.0 event model works differently. The `dispatchEvent()` method dispatches an event object into the event flow, while the `broadcastMessage()` method sends messages directly to each registered listener object.  
| initialize() Method | Removed| There is no direct equivalent in ActionScript 3.0, but similar functionality is achieved by subclassing the EventDispatcher class. For example, the DisplayObject class extends EventDispatcher, so all instances of the DisplayObject and DisplayObject subclasses are capable of sending and receiving event objects.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| Not a direct equivalent, because the ActionScript 3.0 event model lets you add event listeners to and remove them from any object in the event flow, not just the broadcasting object.  
| **BitmapData class**| [flash.display.BitmapData](flash/display/BitmapData.html)| ActionScript 3.0 uses the BitmapDataChannel class as an enumeration of constants that indicate which channel to use.  
| height Property[read-only] | [flash.display.BitmapData.height](flash/display/BitmapData.html#height)| Data type changed from Number to int.  
| rectangle Property[read-only] | [flash.display.BitmapData.rect](flash/display/BitmapData.html#rect)| Property renamed for consistency with other members of the API.  
| width Property[read-only] | [flash.display.BitmapData.width](flash/display/BitmapData.html#width)| Data type changed from Number to int.  
| copyChannel() Method | [flash.display.BitmapData.copyChannel()](flash/display/BitmapData.html#copyChannel\(\))| The `sourceChannel` and `destChannel` parameters are now uint data types.  
| draw() Method | [flash.display.BitmapData.draw()](flash/display/BitmapData.html#draw\(\))| The `source` parameter is now IBitmapDrawable; DisplayObject and BitmapData both implement the IBitmapDrawable interface, so you can pass either a DisplayObject or a BitmapData object to the `source` parameter.  
| fillRect() Method | [flash.display.BitmapData.fillRect()](flash/display/BitmapData.html#fillRect\(\))| The `color` parameter is now a uint value.  
| floodFill() Method | [flash.display.BitmapData.floodFill()](flash/display/BitmapData.html#floodFill\(\))| Now accepts int values for the `x` and `y` parameters and a uint value for `color`.  
| getColorBoundsRect() Method | [flash.display.BitmapData.getColorBoundsRect()](flash/display/BitmapData.html#getColorBoundsRect\(\))| Now accepts uint values for the `mask` and `color` parameters.  
| getPixel() Method | [flash.display.BitmapData.getPixel()](flash/display/BitmapData.html#getPixel\(\))| Now accepts `int` parameter values and returns a uint value.  
| getPixel32() Method | [flash.display.BitmapData.getPixel32()](flash/display/BitmapData.html#getPixel32\(\))| Now accepts `int` parameter values and returns a uint value.  
| hitTest() Method | [flash.display.BitmapData.hitTest()](flash/display/BitmapData.html#hitTest\(\))| Now accepts uint values for the `firstAlphaThreshold` and `secondAlphaThreshold` parameters.  
| loadBitmap() Method | Removed| This function is no longer needed because of the new bitmap support in ActionScript 3.0.  
| merge() Method | [flash.display.BitmapData.merge()](flash/display/BitmapData.html#merge\(\))| Now accepts uint values for the multiplier parameters.  
| noise() Method | [flash.display.BitmapData.noise()](flash/display/BitmapData.html#noise\(\))| Now accepts an int value for the `randomSeed` parameter and uint values for the `low`, `high`, and `channelOptions` parameters.  
| perlinNoise() Method | [flash.display.BitmapData.perlinNoise()](flash/display/BitmapData.html#perlinNoise\(\))| Now accepts an int value for the `randomSeed` parameter and uint values for the `numOctaves` and `channelOptions` parameters.  
| pixelDissolve() Method | [flash.display.BitmapData.pixelDissolve()](flash/display/BitmapData.html#pixelDissolve\(\))| Now accepts an int value for the `randomSeed` and `numPixels` parameters and a uint value for the `fillColor` parameter. (The `numPixels` parameter is named `numberOfPixels` in ActionScript 2.0.)  
| scroll() Method | [flash.display.BitmapData.scroll()](flash/display/BitmapData.html#scroll\(\))| Now accepts int values for the `x` and `y` parameters.  
| setPixel() Method | [flash.display.BitmapData.setPixel()](flash/display/BitmapData.html#setPixel\(\))| Now accepts int values for the `x` and `y` parameters and a uint value for `color`.  
| setPixel32() Method | [flash.display.BitmapData.setPixel32()](flash/display/BitmapData.html#setPixel32\(\))| Now accepts int values for the `x` and `y` parameters and a unit value for `color`.  
| threshold() Method | [flash.display.BitmapData.threshold()](flash/display/BitmapData.html#threshold\(\))| Now accepts uint values for the `threshold`, `color`, and `mask` parameters, and returns a uint value.  
| **BlurFilter class**|   
| quality Property | [flash.filters.BlurFilter.quality](flash/filters/BlurFilter.html#quality)| The `quality` property data type changed from a Number to uint.  
| **Button class**| [flash.display.SimpleButton](flash/display/SimpleButton.html)|   
| _alpha Property | [flash.display.DisplayObject.alpha](flash/display/DisplayObject.html#alpha)|   
| blendMode Property | [flash.display.DisplayObject.blendMode](flash/display/DisplayObject.html#blendMode)|   
| cacheAsBitmap Property | [flash.display.DisplayObject.cacheAsBitmap](flash/display/DisplayObject.html#cacheAsBitmap)|   
| enabled Property | [flash.display.SimpleButton.enabled](flash/display/SimpleButton.html#enabled)|   
| filters Property | [flash.display.DisplayObject.filters](flash/display/DisplayObject.html#filters)| In ActionScript 3.0, the data type is Array.  
| _focusrect Property | [flash.display.InteractiveObject.focusRect](flash/display/InteractiveObject.html#focusRect)|   
| _height Property | [flash.display.DisplayObject.height](flash/display/DisplayObject.html#height)|   
| _highquality Property | Removed| See Stage.quality.  
| _name Property | [flash.display.DisplayObject.name](flash/display/DisplayObject.html#name)|   
| _parent Property | [flash.display.DisplayObject.parent](flash/display/DisplayObject.html#parent)|   
| _quality Property | Removed| You can set rendering quality for all display objects by using `flash.display.Stage.quality`.  
| _rotation Property | [flash.display.DisplayObject.rotation](flash/display/DisplayObject.html#rotation)|   
| scale9Grid Property | [flash.display.DisplayObject.scale9Grid](flash/display/DisplayObject.html#scale9Grid)|   
| _soundbuftime Property | [flash.media.SoundMixer.bufferTime](flash/media/SoundMixer.html#bufferTime)| Moved to the SoundMixer class, which is used for global sound control. Renamed without abbreviations. Removed the initial underscore from the name.  
| tabEnabled Property | [flash.display.InteractiveObject.tabEnabled](flash/display/InteractiveObject.html#tabEnabled)|   
| tabIndex Property | [flash.display.InteractiveObject.tabIndex](flash/display/InteractiveObject.html#tabIndex)|   
| _target Property[read-only] | Removed| ActionScript 3.0 identifies display objects directly; therefore, identifying a display object by its path is no longer necessary.  
| trackAsMenu Property | [flash.display.SimpleButton.trackAsMenu](flash/display/SimpleButton.html#trackAsMenu)|   
| _url Property[read-only] | Removed| See DisplayObject.loaderInfo.url.  
| useHandCursor Property | [flash.display.SimpleButton.useHandCursor](flash/display/SimpleButton.html#useHandCursor)|   
| _visible Property | [flash.display.DisplayObject.visible](flash/display/DisplayObject.html#visible)|   
| _width Property | [flash.display.DisplayObject.width](flash/display/DisplayObject.html#width)|   
| _x Property | [flash.display.DisplayObject.x](flash/display/DisplayObject.html#x)|   
| _xmouse Property[read-only] | [flash.display.DisplayObject.mouseX](flash/display/DisplayObject.html#mouseX)|   
| _xscale Property | [flash.display.DisplayObject.scaleX](flash/display/DisplayObject.html#scaleX)|   
| _y Property | [flash.display.DisplayObject.y](flash/display/DisplayObject.html#y)|   
| _ymouse Property[read-only] | [flash.display.DisplayObject.mouseY](flash/display/DisplayObject.html#mouseY)|   
| _yscale Property | [flash.display.DisplayObject.scaleY](flash/display/DisplayObject.html#scaleY)|   
| getDepth() Method | [flash.display.DisplayObjectContainer.getChildIndex()](flash/display/DisplayObjectContainer.html#getChildIndex\(\))| ActionScript 3.0 provides direct access to the display list, so depth is handled differently.  
| onDragOut() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOut](flash/display/InteractiveObject.html#event:mouseOut)| Replaced in the new event model by a `mouseOut` event.  
| onDragOver() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOver](flash/display/InteractiveObject.html#event:mouseOver)| Replaced in the new event model by a `mouseOver` event.  
| onKeyDown() EventHandler | [flash.display.InteractiveObject dispatches event: keyDown](flash/display/InteractiveObject.html#event:keyDown)| Replaced in the new event model by a `keyDown` event.  
| onKeyUp() EventHandler | [flash.display.InteractiveObject dispatches event: keyUp](flash/display/InteractiveObject.html#event:keyUp)| Replaced in the new event model by a `keyUp` event.  
| onKillFocus() EventHandler | [flash.display.InteractiveObject dispatches event: focusOut](flash/display/InteractiveObject.html#event:focusOut)| Replaced in the new event model by a `focusOut` event.  
| onPress() EventHandler | [flash.display.InteractiveObject dispatches event: mouseDown](flash/display/InteractiveObject.html#event:mouseDown)| Replaced in the new event model by a `mouseDown` event.  
| onRelease() EventHandler | [flash.display.InteractiveObject dispatches event: mouseUp](flash/display/InteractiveObject.html#event:mouseUp)| Replaced in the new event model by a `mouseUp` event.  
| onReleaseOutside() EventHandler | [flash.display.InteractiveObject dispatches event: mouseUp](flash/display/InteractiveObject.html#event:mouseUp)| Replaced in the new event model by a `mouseUp` event.  
| onRollOut() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOut](flash/display/InteractiveObject.html#event:mouseOut)| Replaced in the new event model by a `mouseOut` event.  
| onRollOver() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOver](flash/display/InteractiveObject.html#event:mouseOver)| Replaced in the new event model by a `mouseOver` event.  
| onSetFocus() EventHandler | [flash.display.InteractiveObject dispatches event: focusIn](flash/display/InteractiveObject.html#event:focusIn)| Replaced in the new event model by a `focusIn` event.  
| **Camera class**| [flash.media.Camera](flash/media/Camera.html)|   
| activityLevel Property[read-only] | [flash.media.Camera.activityLevel](flash/media/Camera.html#activityLevel)|   
| bandwidth Property[read-only] | [flash.media.Camera.bandwidth](flash/media/Camera.html#bandwidth)|   
| currentFps Property[read-only] | [flash.media.Camera.currentFPS](flash/media/Camera.html#currentFPS)| Change in capitalization of FPS.  
| fps Property[read-only] | [flash.media.Camera.fps](flash/media/Camera.html#fps)|   
| height Property[read-only] | [flash.media.Camera.height](flash/media/Camera.html#height)| Data type changed from Number to int.  
| index Property[read-only] | [flash.media.Camera.index](flash/media/Camera.html#index)| Data type changed from String to int.  
| motionLevel Property[read-only] | [flash.media.Camera.motionLevel](flash/media/Camera.html#motionLevel)| Data type changed from Number to int.  
| motionTimeOut Property[read-only] | [flash.media.Camera.motionTimeout](flash/media/Camera.html#motionTimeout)| Data type changed from Number to int.  
| muted Property[read-only] | [flash.media.Camera.muted](flash/media/Camera.html#muted)|   
| name Property[read-only] | [flash.media.Camera.name](flash/media/Camera.html#name)|   
| names Property[read-only] | [flash.media.Camera.names](flash/media/Camera.html#names)|   
| quality Property[read-only] | [flash.media.Camera.quality](flash/media/Camera.html#quality)| Data type changed from Number to int.  
| width Property[read-only] | [flash.media.Camera.width](flash/media/Camera.html#width)| Data type changed from Number to int.  
| get() Method | [flash.media.Camera.getCamera()](flash/media/Camera.html#getCamera\(\))|   
| onActivity() EventHandler | [flash.events.ActivityEvent.ACTIVITY](flash/events/ActivityEvent.html#ACTIVITY)|   
| onStatus() EventHandler | [flash.media.Camera dispatches event: status](flash/media/Camera.html#event:status)| Replaced in the new event model by a `status` StatusEvent object.  
| setMode() Method | [flash.media.Camera.setMode()](flash/media/Camera.html#setMode\(\))| The `width` and `height` parameters changed to data type int.  
| setMotionLevel() Method | [flash.media.Camera.setMotionLevel()](flash/media/Camera.html#setMotionLevel\(\))| Both parameters changed to data type int.  
| setQuality() Method | [flash.media.Camera.setQuality()](flash/media/Camera.html#setQuality\(\))| Both parameters changed to data type int.  
| **capabilities class**| [flash.system.Capabilities](flash/system/Capabilities.html)| The class name changed from lowercase to initial capitalization.  
| **Color class**| [flash.geom.ColorTransform](flash/geom/ColorTransform.html)| The Color class has been removed because all of its functionality can be achieved with the flash.geom.ColorTransform class. Color values can be assigned directly by using the ColorTransform class constructor or properties. ColorTransform objects can then be assigned to the `colorTransform` property of a Transform object, which in turn can be assigned to the `transform` property of a DisplayObject instance.  
| Color Constructor | [flash.geom.ColorTransform.ColorTransform()](flash/geom/ColorTransform.html#ColorTransform\(\))| Removed. You can specify color values by using the `ColorTransform()` constructor.  
| getRGB() Method | [flash.geom.ColorTransform.color](flash/geom/ColorTransform.html#color)| The RGB color value can be accessed by using the `color` accessor property of the ColorTransform class.  
| getTransform() Method | Removed| Color values can be assigned directly by using the `ColorTransform()` class constructor or properties.  
| setRGB() Method | [flash.geom.ColorTransform.color](flash/geom/ColorTransform.html#color)| The RGB color value can be set by using the `color` accessor property of the ColorTransform class.  
| setTransform() Method | Removed| Color values can be assigned directly by using the `ColorTransform()` class constructor or properties.  
| **ContextMenu class**| [flash.ui.ContextMenu](flash/ui/ContextMenu.html)| The ContextMenu class is now part of the flash.ui package.  
| builtInItems Property | [flash.ui.ContextMenu.builtInItems](flash/ui/ContextMenu.html#builtInItems)|   
| customItems Property | [flash.ui.ContextMenu.customItems](flash/ui/ContextMenu.html#customItems)|   
| ContextMenu Constructor | [flash.ui.ContextMenu.ContextMenu()](flash/ui/ContextMenu.html#ContextMenu\(\))|   
| copy() Method | [flash.ui.ContextMenu.clone()](flash/ui/ContextMenu.html#clone\(\))|   
| hideBuiltInItems() Method | [flash.ui.ContextMenu.hideBuiltInItems()](flash/ui/ContextMenu.html#hideBuiltInItems\(\))|   
| onSelect() EventHandler | [flash.ui.ContextMenu dispatches event: menuSelect](flash/ui/ContextMenu.html#event:menuSelect)| Instead of invoking the `onSelect()` event handler, the ActionScript 3.0 class dispatches a `menuSelect` event.  
| **ContextMenuItem class**| [flash.ui.ContextMenuItem](flash/ui/ContextMenuItem.html)| The ContextMenuItem class is now part of the flash.ui package.  
| caption Property | [flash.ui.ContextMenuItem.caption](flash/ui/ContextMenuItem.html#caption)|   
| enabled Property | [flash.ui.ContextMenuItem.enabled](flash/ui/ContextMenuItem.html#enabled)|   
| separatorBefore Property | [flash.ui.ContextMenuItem.separatorBefore](flash/ui/ContextMenuItem.html#separatorBefore)|   
| visible Property | [flash.ui.ContextMenuItem.visible](flash/ui/ContextMenuItem.html#visible)|   
| ContextMenuItem Constructor | [flash.ui.ContextMenuItem.ContextMenuItem()](flash/ui/ContextMenuItem.html#ContextMenuItem\(\))|   
| copy() Method | [flash.ui.ContextMenuItem.clone()](flash/ui/ContextMenuItem.html#clone\(\))|   
| onSelect() EventHandler | [flash.ui.ContextMenuItem dispatches event: menuItemSelect](flash/ui/ContextMenuItem.html#event:menuItemSelect)| Instead of invoking the `onSelect()` event handler, the ActionScript 3.0 class dispatches a `menuSelect` event.  
| **ConvolutionFilter class**|   
| clone() Method | [flash.filters.ConvolutionFilter.clone()](flash/filters/ConvolutionFilter.html#clone\(\))| Now returns a BitmapFilter object.  
| **Date class**| [Date](Date.html)| ActionScript 3.0 includes a new set of read accessors for all the methods that start with get _xxx_(). For example, in ActionScript 3.0, `Date.getDate()` and `Date.date` return the same value.  
| getUTCYear() Method | [Date.getUTCFullYear()](Date.html#getUTCFullYear\(\))| This method was removed because it is not part of ECMAScript. Use `Date.getUTCFullYear()` instead.  
| getYear() Method | [Date.getFullYear()](Date.html#getFullYear\(\))| This method was removed because it is not part of ECMAScript. Use `Date.getFullYear()` instead.  
| setYear() Method | [Date.setFullYear()](Date.html#setFullYear\(\))| This method was removed because it is not part of ECMAScript. Use `Date.setFullYear()` instead.  
| **DisplacementMapFilter class**| [flash.filters.DisplacementMapFilter](flash/filters/DisplacementMapFilter.html)| The data type of several parameters changed from Number to uint.  
| color Property | [flash.filters.DisplacementMapFilter.color](flash/filters/DisplacementMapFilter.html#color)| The data type of this parameter is now uint.  
| componentX Property | [flash.filters.DisplacementMapFilter.componentX](flash/filters/DisplacementMapFilter.html#componentX)| The data type of this parameter is now uint.  
| componentY Property | [flash.filters.DisplacementMapFilter.componentY](flash/filters/DisplacementMapFilter.html#componentY)| The data type of this parameter is now uint.  
| DisplacementMapFilter Constructor | [flash.filters.DisplacementMapFilter.DisplacementMapFilter()](flash/filters/DisplacementMapFilter.html#DisplacementMapFilter\(\))| The data type of the `componentX`, `componentY`, and `color` parameters is now uint.  
| clone() Method | [flash.filters.DisplacementMapFilter.clone()](flash/filters/DisplacementMapFilter.html#clone\(\))| Now returns a BitmapFilter object.  
| **DropShadowFilter class**| [flash.filters.DropShadowFilter](flash/filters/DropShadowFilter.html)|   
| color Property | [flash.filters.DropShadowFilter.color](flash/filters/DropShadowFilter.html#color)| The data type of this parameter changed from Number to uint.  
| quality Property | [flash.filters.DropShadowFilter.quality](flash/filters/DropShadowFilter.html#quality)| The data type of this parameter changed from Number to uint.  
| DropShadowFilter Constructor | [flash.filters.DropShadowFilter.DropShadowFilter()](flash/filters/DropShadowFilter.html#DropShadowFilter\(\))| All parameters now have a default value, and some parameter types have changed.  
| clone() Method | [flash.filters.DropShadowFilter.clone()](flash/filters/DropShadowFilter.html#clone\(\))| Now returns a BitmapFilter object instead of a DropShadowFilter object.  
| **Error class**| [Error](Error.html)| Added a new `getStackTrace()` method to assist in debugging.  
| **ExternalInterface class**| [flash.external.ExternalInterface](flash/external/ExternalInterface.html)| Parameters changed for two methods in this class.  
| addCallback() Method | [flash.external.ExternalInterface.addCallback()](flash/external/ExternalInterface.html#addCallback\(\))| The ActionScript 3.0 version of this method does not accept the `instance` parameter. The `method` parameter is replaced by a `closure` parameter, which can take a reference to a function, a class method, or a method of a particular class instance. In addition, if the calling code cannot access the `closure` reference for security reasons, a `SecurityError` exception is thrown.  
| call() Method | [flash.external.ExternalInterface.call()](flash/external/ExternalInterface.html#call\(\))| If a problem occurs, the ActionScript 3.0 version of this method throws an Error or `SecurityError` exception, in addition to returning `null`.  
| **FileReference class**| [flash.net.FileReference](flash/net/FileReference.html)| The ActionScript 3.0 version inherits the `addEventListener()` and `removeEventListener()` methods from the EventDispatcher class. Dispatched events replace the event handler functions.  
| postData Property | [flash.net.URLRequest.data](flash/net/URLRequest.html#data)| The `postData` property is added to ActionScript 2.0 in Flash Player 9 to send POST data with the file upload or download. In ActionScript 3.0, use the `data` property of the URLRequest class to send either POST or GET data. See `flash.net.URLRequest.data` in this language reference for details.  
| size Property[read-only] | [flash.net.FileReference.size](flash/net/FileReference.html#size)| Returns a uint data type instead of a Number data type.  
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new event model, there is no need to have a class-specific `addListener()` method, because the class inherits the `addEventListener()` method from the EventDispatcher class.  
| browse() Method | [flash.net.FileReference.browse()](flash/net/FileReference.html#browse\(\))| In ActionScript 2.0, returns `false` when there is an error. In ActionScript 3.0, throws an `IllegalOperationError` or `ArgumentError` exception. However, the method still returns `false` if the parameters are invalid, the file-browsing dialog box does not open, or another browser session is in progress. Also, the `typelist` parameter changed. In ActionScript 2.0, you can pass the `browse()` method an array of strings to specify a file filter. In ActionScript 3.0, you pass an array of FileFilter objects.  
| download() Method | [flash.net.FileReference.download()](flash/net/FileReference.html#download\(\))| When an error occurs, throws exceptions instead of returning `false`. The data type for the first parameter has changed. In ActionScript 2.0, the first parameter you pass to `download()` is a string. In ActionScript 3.0, you pass a URLRequest object.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new event model, there is no need to have a class-specific `removeListener()` method, because the class inherits the `removeEventListener()` method from the EventDispatcher class.  
| upload() Method | [flash.net.FileReference.upload()](flash/net/FileReference.html#upload\(\))| Various changes have occurred: 

  * The data type for the first parameter has changed. In ActionScript 2.0, the first parameter you pass to `upload()` is a string. In ActionScript 3.0, you pass a URLRequest object.
  * In ActionScript 3.0, there is a new second parameter, `uploadDataFieldName`, which is the field name that precedes the file data in the upload POST operation.
  * In ActionScript 3.0, there is a new third parameter, `testUpload`, that lets you control whether Flash Player performs a test upload before uploading the file.
  * When an error occurs, `browse()` throws exceptions instead of returning `false`.

  
| onCancel Listener | [flash.net.FileReference dispatches event: cancel](flash/net/FileReference.html#event:cancel)| In ActionScript 3.0, instead of invoking the `onCancel()` event handler, this class dispatches an event named `cancel`.  
| onComplete Listener | [flash.net.FileReference dispatches event: complete](flash/net/FileReference.html#event:complete)| In ActionScript 3.0, instead of invoking the `onComplete()` event handler, this class dispatches an event named `complete`.  
| onHTTPError Listener | [flash.net.FileReference dispatches event: httpStatus](flash/net/FileReference.html#event:httpStatus)| In ActionScript 3.0, instead of invoking the `onHTTPError()` event handler, this class dispatches an event named `httpStatus`.  
| onIOError Listener | [flash.net.FileReference dispatches event: ioError](flash/net/FileReference.html#event:ioError)| In ActionScript 3.0, instead of invoking the `onIOError()` event handler, this class dispatches an event named `ioError`.  
| onOpen Listener | [flash.net.FileReference dispatches event: open](flash/net/FileReference.html#event:open)| In ActionScript 3.0, instead of invoking the `onOpen()` event handler, this class dispatches an event named `open`.  
| onProgress Listener | [flash.net.FileReference dispatches event: progress](flash/net/FileReference.html#event:progress)| In ActionScript 3.0, instead of invoking the `onProgress()` event handler, this class dispatches an event named `progress`.  
| onSecurityError Listener | [flash.net.FileReference dispatches event: securityError](flash/net/FileReference.html#event:securityError)| In ActionScript 3.0, instead of invoking the `onSecurityError()` event handler, this class dispatches an event named `securityError`.  
| onSelect Listener | [flash.net.FileReference dispatches event: select](flash/net/FileReference.html#event:select)| In ActionScript 3.0, instead of invoking the `onSelect()` event handler, this class dispatches an event named `select`.  
| onUploadCompleteData | [flash.net.FileReference dispatches event: complete](flash/net/FileReference.html#event:complete)| In ActionScript 3.0, instead of invoking the `onUploadCompleteData()` event handler, this class dispatches an event named `uploadCompleteData`.  
| **FileReferenceList class**| [flash.net.FileReferenceList](flash/net/FileReferenceList.html)| The ActionScript 3.0 class inherits the `addEventListener()` and `removeEventListener()` methods from the EventDispatcher class. Instead of the `onCancel()` and `onSelect()` event handlers, the ActionScript 3.0 class uses events named `cancel` and `select`.  
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new event model, there is no need to have a class-specific `addListener()` method, because the class inherits the `addEventListener()` method from the EventDispatcher class.  
| browse() Method | [flash.net.FileReferenceList.browse()](flash/net/FileReferenceList.html#browse\(\))| In ActionScript 3.0, instead of returning `false` when there is an error, this method throws an `IllegalOperationError` exception. Also, the `typelist` parameter changed. In ActionScript 2.0, you can pass the `browse()` method an array of strings to specify a file filter. In ActionScript 3.0, you pass an array of FileFilter objects.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new event model, there is no need to have a class-specific `removeListener()` method, because the class inherits the `removeEventListener()` method from the EventDispatcher class.  
| onCancel Listener | [flash.net.FileReferenceList dispatches event: cancel](flash/net/FileReferenceList.html#event:cancel)| In ActionScript 3.0, instead of invoking the `onCancel()` event handler, this class dispatches an event named `cancel`.  
| onSelect Listener | [flash.net.FileReferenceList dispatches event: select](flash/net/FileReferenceList.html#event:select)| In ActionScript 3.0, instead of invoking the `onSelect()` event handler, this class dispatches an event named `select`.  
| **GlowFilter class**| [flash.filters.GlowFilter](flash/filters/GlowFilter.html)| The data type of several properties changed from Number to unit.  
| color Property | [flash.filters.GlowFilter.color](flash/filters/GlowFilter.html#color)| The data type of this property changed from Number to unit.  
| quality Property | [flash.filters.GlowFilter.quality](flash/filters/GlowFilter.html#quality)| The data type of this property changed from Number to unit.  
| GlowFilter Constructor | [flash.filters.GlowFilter.GlowFilter()](flash/filters/GlowFilter.html#GlowFilter\(\))| The `color` and `quality` parameters are now uint and int data types, respectively, instead of Number. All parameters are now assigned a default value.  
| clone() Method | [flash.filters.GlowFilter.clone()](flash/filters/GlowFilter.html#clone\(\))| Returns a BitmapFilter object instead of a GlowFilter object.  
| **GradientBevelFilter class**| [flash.filters.GradientBevelFilter](flash/filters/GradientBevelFilter.html)|   
| quality Property | [flash.filters.GradientBevelFilter.quality](flash/filters/GradientBevelFilter.html#quality)| The data type of this property changed from Number to int.  
| clone() Method | [flash.filters.GradientBevelFilter.clone()](flash/filters/GradientBevelFilter.html#clone\(\))| Returns a BitmapFilter object instead of a GradientBevelFilter object.  
| **GradientGlowFilter class**| [flash.filters.GradientGlowFilter](flash/filters/GradientGlowFilter.html)|   
| quality Property | [flash.filters.GradientGlowFilter.quality](flash/filters/GradientGlowFilter.html#quality)| The data type of this property changed from Number to int.  
| GradientGlowFilter Constructor | [flash.filters.GradientGlowFilter.GradientGlowFilter()](flash/filters/GradientGlowFilter.html#GradientGlowFilter\(\))| Default values added to all parameters and the data type of the `quality` parameter changed from Number to int.  
| clone() Method | [flash.filters.GradientGlowFilter.clone()](flash/filters/GradientGlowFilter.html#clone\(\))| Returns a BitmapFilter object instead of a GradientGlowFilter object.  
| **IME class**| [flash.system.IME](flash/system/IME.html)| This class has been moved to the flash.system package.  
| ALPHANUMERIC_FULL Constant | [flash.system.IMEConversionMode.ALPHANUMERIC_FULL](flash/system/IMEConversionMode.html#ALPHANUMERIC_FULL)|   
| ALPHANUMERIC_HALF Constant | [flash.system.IMEConversionMode.ALPHANUMERIC_HALF](flash/system/IMEConversionMode.html#ALPHANUMERIC_HALF)|   
| CHINESE Constant | [flash.system.IMEConversionMode.CHINESE](flash/system/IMEConversionMode.html#CHINESE)|   
| JAPANESE_HIRAGANA Constant | [flash.system.IMEConversionMode.JAPANESE_HIRAGANA](flash/system/IMEConversionMode.html#JAPANESE_HIRAGANA)|   
| JAPANESE_KATAKANA_FULL Constant | [flash.system.IMEConversionMode.JAPANESE_KATAKANA_FULL](flash/system/IMEConversionMode.html#JAPANESE_KATAKANA_FULL)|   
| JAPANESE_KATAKANA_HALF Constant | [flash.system.IMEConversionMode.JAPANESE_KATAKANA_HALF](flash/system/IMEConversionMode.html#JAPANESE_KATAKANA_HALF)|   
| KOREAN Constant | [flash.system.IMEConversionMode.KOREAN](flash/system/IMEConversionMode.html#KOREAN)|   
| UNKNOWN Constant | [flash.system.IMEConversionMode.UNKNOWN](flash/system/IMEConversionMode.html#UNKNOWN)|   
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new event model, there is no need to have a class-specific `addListener()` method, because the class inherits the `addEventListener()` method from the EventDispatcher class.  
| getConversionMode() Method | [flash.system.IME.conversionMode](flash/system/IME.html#conversionMode)| Changed to an accessor property.  
| getEnabled() Method | [flash.system.IME.enabled](flash/system/IME.html#enabled)| Changed to an accessor property.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new event model, there is no need to have a class-specific `removeListener()` method, because the class inherits the `removeEventListener()` method from the EventDispatcher class.  
| setConversionMode() Method | [flash.system.IME.conversionMode](flash/system/IME.html#conversionMode)| Changed to an accessor property.  
| setEnabled() Method | [flash.system.IME.enabled](flash/system/IME.html#enabled)| Changed to an accessor property.  
| onIMEComposition Listener | [flash.system.IME dispatches event: imeComposition](flash/system/IME.html#event:imeComposition)| In ActionScript 3.0, instead of invoking the `onIMEComposition()` event handler, this class dispatches an event named `imeComposition`.  
| **Key class**| [flash.ui.Keyboard](flash/ui/Keyboard.html)| This class has a new name in ActionScript 3.0 to match other classes that pertain to the Keyboard class, such as KeyboardEvent.  
| BACKSPACE Constant | [flash.ui.Keyboard.BACKSPACE](flash/ui/Keyboard.html#BACKSPACE)| Declared as a constant in ActionScript 3.0 and data type changed to unit.  
| CAPSLOCK Constant | [flash.ui.Keyboard.CAPS_LOCK](flash/ui/Keyboard.html#CAPS_LOCK)| Declared as a constant in ActionScript 3.0, underscore added, and data type changed to uint.  
| CONTROL Constant | [flash.ui.Keyboard.CONTROL](flash/ui/Keyboard.html#CONTROL)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| DELETEKEY Constant | [flash.ui.Keyboard.DELETE](flash/ui/Keyboard.html#DELETE)| Name changed to `DELETE` in ActionScript 3.0, declared as a constant, and data type changed to uint.  
| DOWN Constant | [flash.ui.Keyboard.DOWN](flash/ui/Keyboard.html#DOWN)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| END Constant | [flash.ui.Keyboard.END](flash/ui/Keyboard.html#END)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| ENTER Constant | [flash.ui.Keyboard.ENTER](flash/ui/Keyboard.html#ENTER)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| ESCAPE Constant | [flash.ui.Keyboard.ESCAPE](flash/ui/Keyboard.html#ESCAPE)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| HOME Constant | [flash.ui.Keyboard.HOME](flash/ui/Keyboard.html#HOME)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| INSERT Constant | [flash.ui.Keyboard.INSERT](flash/ui/Keyboard.html#INSERT)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| LEFT Constant | [flash.ui.Keyboard.LEFT](flash/ui/Keyboard.html#LEFT)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| _listeners Property[read-only] | [flash.events.EventDispatcher.willTrigger()](flash/events/EventDispatcher.html#willTrigger\(\))| Not a direct equivalent. The `willTrigger()` method tells you whether any listeners are registered, but not how many.  
| PGDN Constant | [flash.ui.Keyboard.PAGE_DOWN](flash/ui/Keyboard.html#PAGE_DOWN)| Name changed to `PAGE_DOWN` in ActionScript 3.0, declared as a constant, and data type changed to uint.  
| PGUP Constant | [flash.ui.Keyboard.PAGE_UP](flash/ui/Keyboard.html#PAGE_UP)| Name changed to `PAGE_UP` in ActionScript 3.0, declared as a constant, and data type changed to uint.  
| RIGHT Constant | [flash.ui.Keyboard.RIGHT](flash/ui/Keyboard.html#RIGHT)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| SHIFT Constant | [flash.ui.Keyboard.SHIFT](flash/ui/Keyboard.html#SHIFT)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| SPACE Constant | [flash.ui.Keyboard.SPACE](flash/ui/Keyboard.html#SPACE)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| TAB Constant | [flash.ui.Keyboard.TAB](flash/ui/Keyboard.html#TAB)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| UP Constant | [flash.ui.Keyboard.UP](flash/ui/Keyboard.html#UP)| Declared as a constant in ActionScript 3.0 and data type changed to uint.  
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In ActionScript 3.0, there is no need to have a class-specific `addListener()` method, because all display objects inherit the `addEventListener()` method from the EventDispatcher class.  
| getAscii() Method | [flash.events.KeyboardEvent.charCode](flash/events/KeyboardEvent.html#charCode)|   
| getCode() Method | [flash.events.KeyboardEvent.keyCode](flash/events/KeyboardEvent.html#keyCode)|   
| isAccessible() Method | [flash.ui.Keyboard.isAccessible()](flash/ui/Keyboard.html#isAccessible\(\))|   
| isDown() Method | Removed| Removed for security reasons.  
| isToggled() Method | Removed| Removed for security reasons.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In ActionScript 3.0, there is no need to have a class-specific `removeListener()` method, because all display objects inherit the `removeEventListener()` method from the EventDispatcher class.  
| onKeyDown Listener | [flash.display.InteractiveObject dispatches event: keyDown](flash/display/InteractiveObject.html#event:keyDown)| In ActionScript 3.0, instead of invoking the `onKeyDown` event handler, the InteractiveObject class dispatches a `keyDown` KeyboardEvent object.  
| onKeyUp Listener | [flash.display.InteractiveObject dispatches event: keyUp](flash/display/InteractiveObject.html#event:keyUp)| In ActionScript 3.0, instead of invoking the `onKeyUp` event handler, the InteractiveObject class dispatches a `keyUp` KeyboardEvent object.  
| **LoadVars class**| [flash.net.URLLoader](flash/net/URLLoader.html)| The LoadVars class functionality is replaced by the URLLoader, URLRequest, URLStream, and URLVariables classes.  
| contentType Property | [flash.net.URLRequest.contentType](flash/net/URLRequest.html#contentType)|   
| loaded Property | Removed| There is no corresponding Boolean property in ActionScript 3.0, but you can use `flash.events.Event.COMPLETE` to set up listeners that receive notification when data is loaded.  
| LoadVars Constructor | [flash.net.URLLoader.URLLoader()](flash/net/URLLoader.html#URLLoader\(\))|   
| addRequestHeader() Method | [flash.net.URLRequestHeader](flash/net/URLRequestHeader.html)|   
| decode() Method | [flash.net.URLVariables.decode()](flash/net/URLVariables.html#decode\(\))|   
| getBytesLoaded() Method | [flash.net.URLLoader.bytesLoaded](flash/net/URLLoader.html#bytesLoaded)| Class changed to URLLoader; changed from function to property accessor; and name changed from `getBytesLoaded` to `bytesLoaded`.  
| getBytesTotal() Method | [flash.net.URLLoader.bytesTotal](flash/net/URLLoader.html#bytesTotal)| Class changed to URLLoader; changed from function to property accessor; and name changed from `getBytesTotal` to `bytesTotal`.  
| load() Method | [flash.net.URLLoader.load()](flash/net/URLLoader.html#load\(\))|   
| onData() EventHandler | [flash.net.URLLoader dispatches event: complete](flash/net/URLLoader.html#event:complete)| See the URLLoader class. A `complete` event is dispatched when the download operation is complete but before any data is parsed.  
| onHTTPStatus() EventHandler | [flash.net.URLLoader dispatches event: httpStatus](flash/net/URLLoader.html#event:httpStatus)| In ActionScript 3.0, instead of invoking the `onHTTPStatus` event handler, the URLLoader class dispatches an HTTPStatusEvent object named `httpStatus`.  
| onLoad() EventHandler | [flash.net.URLLoader dispatches event: complete](flash/net/URLLoader.html#event:complete)| See the URLLoader class. A `complete` event is dispatched when the download operation is complete.  
| send() Method | [flash.net.sendToURL()](flash/net/package.html#sendToURL\(\))|   
| sendAndLoad() Method | [flash.net.sendToURL()](flash/net/package.html#sendToURL\(\))| The `sendToURL()` method sends a URL request to the server, but ignores the response. To receive the response, use `flash.net.sendToURL()`.  
| toString() Method | Removed| This method is no longer necessary in ActionScript 3.0.  
| **LocalConnection class**| [flash.net.LocalConnection](flash/net/LocalConnection.html)| This class has been moved to the flash.net package.  
| LocalConnection Constructor | [flash.net.LocalConnection.LocalConnection()](flash/net/LocalConnection.html#LocalConnection\(\))|   
| allowDomain() EventHandler | [flash.net.LocalConnection.allowDomain()](flash/net/LocalConnection.html#allowDomain\(\))| Changed to a regular method in ActionScript 3.0, no longer an event handler. Parameter changed to use the ...(rest) parameter format. Return value changed to `void`.  
| allowInsecureDomain() EventHandler | [flash.net.LocalConnection.allowInsecureDomain()](flash/net/LocalConnection.html#allowInsecureDomain\(\))| Changed to a regular method in ActionScript 3.0, no longer an event handler. Parameter changed to use the ...(rest) parameter format. Return value changed to `void`.  
| close() Method | [flash.net.LocalConnection.close()](flash/net/LocalConnection.html#close\(\))|   
| connect() Method | [flash.net.LocalConnection.connect()](flash/net/LocalConnection.html#connect\(\))|   
| domain() Method | [flash.net.LocalConnection.domain](flash/net/LocalConnection.html#domain)| Changed to a property accessor.  
| onStatus() EventHandler | [flash.net.LocalConnection dispatches event: status](flash/net/LocalConnection.html#event:status)| In the new event model, callback functions are replaced by event objects.  
| send() Method | [flash.net.LocalConnection.send()](flash/net/LocalConnection.html#send\(\))| Third parameter changed to use the ...(rest) parameter format. Return type changed to `void`.  
| **Microphone class**| [flash.media.Microphone](flash/media/Microphone.html)| This class has been moved to the flash.media package.  
| index Property[read-only] | [flash.media.Microphone.index](flash/media/Microphone.html#index)| Data type changed to uint.  
| rate Property[read-only] | [flash.media.Microphone.rate](flash/media/Microphone.html#rate)| Data type changed to uint.  
| silenceTimeOut Property[read-only] | [flash.media.Microphone.silenceTimeout](flash/media/Microphone.html#silenceTimeout)| Change in capitalization to "Timeout." Data type changed to int.  
| get() Method | [flash.media.Microphone.getMicrophone()](flash/media/Microphone.html#getMicrophone\(\))| Name changed from `get()` to `getMicrophone()`. Data type of parameter changed to uint.  
| onActivity() EventHandler | [flash.media.Microphone dispatches event: activity](flash/media/Microphone.html#event:activity)| In ActionScript 3.0, instead of invoking the `onActivity` event handler, this class dispatches an `activity` event.  
| onStatus() EventHandler | [flash.media.Microphone dispatches event: status](flash/media/Microphone.html#event:status)| In ActionScript 3.0, instead of invoking the `onStatus` event handler, this class dispatches a `status` event.  
| setGain() Method | [flash.media.Microphone.gain](flash/media/Microphone.html#gain)| Combined `gain` property and `setGain()` method into a get/set property accessor named `gain`. Data type changed to uint.  
| setRate() Method | [flash.media.Microphone.rate](flash/media/Microphone.html#rate)| Combined `rate` property and `setRate()` method into a get/set property accessor named `rate`. Data type changed to uint.  
| setSilenceLevel() Method | [flash.media.Microphone.setSilenceLevel()](flash/media/Microphone.html#setSilenceLevel\(\))| Data type of `timeOut` parameter changed to int. Capitalization of the `timeOut` parameter changed to `timeout`.  
| setUseEchoSuppression() Method | [flash.media.Microphone.setUseEchoSuppression()](flash/media/Microphone.html#setUseEchoSuppression\(\))|   
| **Mouse class**| [flash.ui.Mouse](flash/ui/Mouse.html)|   
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new ActionScript 3.0 event model, there is no need to have a class-specific `addListener()` method, because all display objects inherit the `addEventListener()` method from the EventDispatcher class.  
| hide() Method | [flash.ui.Mouse.hide()](flash/ui/Mouse.html#hide\(\))| Changed to return `void`.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new ActionScript 3.0 event model, there is no need to have a class-specific `removeListener()` method, because all display objects inherit the `removeEventListener()` method from the EventDispatcher class.  
| show() Method | [flash.ui.Mouse.show()](flash/ui/Mouse.html#show\(\))| Changed to return `void`.  
| onMouseDown Listener | [flash.display.InteractiveObject dispatches event: mouseDown](flash/display/InteractiveObject.html#event:mouseDown)| Replaced in the new event model by a `mouseDown` event.  
| onMouseMove Listener | [flash.display.InteractiveObject dispatches event: mouseMove](flash/display/InteractiveObject.html#event:mouseMove)| Replaced in the new event model by a `mouseMove` event.  
| onMouseUp Listener | [flash.display.InteractiveObject dispatches event: mouseUp](flash/display/InteractiveObject.html#event:mouseUp)| Replaced in the new event model by a `mouseUp` event.  
| onMouseWheel Listener | [flash.display.InteractiveObject dispatches event: mouseWheel](flash/display/InteractiveObject.html#event:mouseWheel)| Replaced in the new event model by a `mouseWheel` event.  
| **MovieClip class**| [flash.display.MovieClip](flash/display/MovieClip.html)| Many of the MovieClip methods have been moved to other classes in ActionScript 3.0. All event handlers have been replaced by event objects in the new event model.  
| _alpha Property | [flash.display.DisplayObject.alpha](flash/display/DisplayObject.html#alpha)| Moved to DisplayObject class and removed initial underscore from name.  
| blendMode Property | [flash.display.DisplayObject.blendMode](flash/display/DisplayObject.html#blendMode)|   
| cacheAsBitmap Property | [flash.display.DisplayObject.cacheAsBitmap](flash/display/DisplayObject.html#cacheAsBitmap)|   
| _currentframe Property[read-only] | [flash.display.MovieClip.currentFrame](flash/display/MovieClip.html#currentFrame)| Removed initial underscore from name.  
| _droptarget Property[read-only] | [flash.display.Sprite.dropTarget](flash/display/Sprite.html#dropTarget)| Moved to Sprite class, removed initial underscore from name, and changed to mixed case.  
| filters Property | [flash.display.DisplayObject.filters](flash/display/DisplayObject.html#filters)|   
| focusEnabled Property | Removed| In ActionScript 3.0, all interactive objects are focus enabled; therefore, this property is no longer needed.  
| _focusrect Property | [flash.display.InteractiveObject.focusRect](flash/display/InteractiveObject.html#focusRect)| Moved to InteractiveObject class, removed initial underscore from name, and changed to mixed case.  
| _framesloaded Property[read-only] | [flash.display.MovieClip.framesLoaded](flash/display/MovieClip.html#framesLoaded)| Removed initial underscore from name and changed to mixed case.  
| _height Property | [flash.display.DisplayObject.height](flash/display/DisplayObject.html#height)| Moved to DisplayObject class and removed initial underscore from name.  
| _highquality Property | Removed| See Stage.quality.  
| hitArea Property | [flash.display.Sprite.hitArea](flash/display/Sprite.html#hitArea)| Moved to Sprite class.  
| _lockroot Property | Removed| In ActionScript 3.0, the root of a display object is set automatically; therefore, the `_lockroot` property is effectively always on. See flash.display.DisplayObject.root for details.  
| menu Property | Removed| See InteractiveObject.contextMenu.  
| _name Property | [flash.display.DisplayObject.name](flash/display/DisplayObject.html#name)| Moved to DisplayObject class and removed initial underscore from name.  
| opaqueBackground Property | [flash.display.DisplayObject.opaqueBackground](flash/display/DisplayObject.html#opaqueBackground)|   
| _parent Property | [flash.display.DisplayObject.parent](flash/display/DisplayObject.html#parent)| Moved to DisplayObject class and removed initial underscore from name.  
| _quality Property | [flash.display.Stage.quality](flash/display/Stage.html#quality)|   
| _rotation Property | [flash.display.DisplayObject.rotation](flash/display/DisplayObject.html#rotation)| Moved to DisplayObject class and removed initial underscore from name.  
| scale9Grid Property | [flash.display.DisplayObject.scale9Grid](flash/display/DisplayObject.html#scale9Grid)|   
| scrollRect Property | [flash.display.DisplayObject.scrollRect](flash/display/DisplayObject.html#scrollRect)| Changed to Rectangle data type.  
| _soundbuftime Property | [flash.media.SoundMixer.bufferTime](flash/media/SoundMixer.html#bufferTime)| Moved to SoundMixer class, which is used for global sound control, renamed without abbreviations, and removed initial underscore from name.  
| tabChildren Property | [flash.display.DisplayObjectContainer.tabChildren](flash/display/DisplayObjectContainer.html#tabChildren)|   
| tabEnabled Property | [flash.display.InteractiveObject.tabEnabled](flash/display/InteractiveObject.html#tabEnabled)|   
| tabIndex Property | [flash.display.InteractiveObject.tabIndex](flash/display/InteractiveObject.html#tabIndex)|   
| _target Property[read-only] | Removed| ActionScript 3.0 identifies display objects directly; therefore, identifying a display object by its path is no longer necessary.  
| _totalframes Property[read-only] | [flash.display.MovieClip.totalFrames](flash/display/MovieClip.html#totalFrames)| Changed to mixed case and removed initial underscore from name.  
| trackAsMenu Property | [flash.display.MovieClip.trackAsMenu](flash/display/MovieClip.html#trackAsMenu)|   
| transform Property | [flash.display.DisplayObject.transform](flash/display/DisplayObject.html#transform)|   
| _url Property[read-only] | [flash.display.Loader.contentLoaderInfo](flash/display/Loader.html#contentLoaderInfo)|   
| useHandCursor Property | [flash.display.Sprite.useHandCursor](flash/display/Sprite.html#useHandCursor)|   
| _visible Property | [flash.display.DisplayObject.visible](flash/display/DisplayObject.html#visible)| Moved to DisplayObject class and removed initial underscore from name.  
| _width Property | [flash.display.DisplayObject.width](flash/display/DisplayObject.html#width)| Moved to DisplayObject class and removed initial underscore from name.  
| _x Property | [flash.display.DisplayObject.x](flash/display/DisplayObject.html#x)| Moved to DisplayObject class and removed initial underscore from name.  
| _xmouse Property[read-only] | [flash.display.DisplayObject.mouseX](flash/display/DisplayObject.html#mouseX)| Moved to DisplayObject class, changed name to `mouseX`, and removed initial underscore from name.  
| _xscale Property | [flash.display.DisplayObject.scaleX](flash/display/DisplayObject.html#scaleX)| Moved to DisplayObject class, changed name to `scaleX`, and removed initial underscore from name.  
| _y Property | [flash.display.DisplayObject.y](flash/display/DisplayObject.html#y)| Moved to DisplayObject class and removed initial underscore from name.  
| _ymouse Property[read-only] | [flash.display.DisplayObject.mouseY](flash/display/DisplayObject.html#mouseY)| Moved to DisplayObject class, changed name to `mouseY`, and removed initial underscore from name.  
| _yscale Property | [flash.display.DisplayObject.scaleY](flash/display/DisplayObject.html#scaleY)| Moved to DisplayObject class, changed name to `scaleY`, and removed initial underscore from name.  
| attachAudio() Method | Removed| If the audio source is a Microphone object, use [ `NetStream.attachAudio()`](flash/net/NetStream.html#attachAudio\(\)) or [ `Microphone.setLoopBack()`](flash/media/Microphone.html#setLoopBack\(\)). If the audio source is an FLV file, use [ `Video.attachNetStream()`](flash/media/Video.html#attachNetStream\(\)) and a [ NetStream](flash/net/NetStream.html) object.  
| attachBitmap() Method | Removed| In ActionScript 3.0, use `addChild()` to add child display objects.  
| attachMovie() Method | Removed| In ActionScript 3.0, use `addChild()` to add child display objects.  
| beginBitmapFill() Method | [flash.display.Graphics.beginBitmapFill()](flash/display/Graphics.html#beginBitmapFill\(\))|   
| beginFill() Method | [flash.display.Graphics.beginFill()](flash/display/Graphics.html#beginFill\(\))| Moved to Graphics class and changed data type of the first parameter to uint.  
| beginGradientFill() Method | [flash.display.Graphics.beginGradientFill()](flash/display/Graphics.html#beginGradientFill\(\))|   
| clear() Method | [flash.display.Graphics.clear()](flash/display/Graphics.html#clear\(\))|   
| createEmptyMovieClip() Method | Removed| In ActionScript 3.0, use the `new` operator to create movie clips.  
| createTextField() Method | Removed| In ActionScript 3.0, use the `new` operator to create text fields.  
| curveTo() Method | [flash.display.Graphics.curveTo()](flash/display/Graphics.html#curveTo\(\))|   
| duplicateMovieClip() Method | Removed| In ActionScript 3.0, use the `new` operator to create a new instance.  
| endFill() Method | [flash.display.Graphics.endFill()](flash/display/Graphics.html#endFill\(\))|   
| getBounds() Method | [flash.display.DisplayObject.getBounds()](flash/display/DisplayObject.html#getBounds\(\))|   
| getBytesLoaded() Method | [flash.net.URLLoader.bytesLoaded](flash/net/URLLoader.html#bytesLoaded)| Moved to URLLoader class and data type changed from Number to int.  
| getBytesTotal() Method | [flash.net.URLLoader.bytesTotal](flash/net/URLLoader.html#bytesTotal)| Moved to URLLoader class and data type changed from Number to int.  
| getDepth() Method | [flash.display.DisplayObjectContainer.getChildIndex()](flash/display/DisplayObjectContainer.html#getChildIndex\(\))| ActionScript 3.0 provides direct access to the display list, so depth is handled differently.  
| getInstanceAtDepth() Method | [flash.display.DisplayObjectContainer.getChildAt()](flash/display/DisplayObjectContainer.html#getChildAt\(\))| ActionScript 3.0 provides direct access to the display list, so depth is handled differently.  
| getNextHighestDepth() Method | [flash.display.DisplayObjectContainer.addChild()](flash/display/DisplayObjectContainer.html#addChild\(\))| Not a direct equivalent, but the `addChild()` method adds a child behind all other children of the DisplayObjectContainer instance, so there is no need for a method that determines the next available depth.  
| getRect() Method | [flash.display.DisplayObject.getRect()](flash/display/DisplayObject.html#getRect\(\))|   
| getSWFVersion() Method | [flash.display.LoaderInfo.swfVersion](flash/display/LoaderInfo.html#swfVersion)| Moved to LoaderInfo class and changed data type to uint.  
| getTextSnapshot() Method | [flash.display.DisplayObjectContainer.textSnapshot](flash/display/DisplayObjectContainer.html#textSnapshot)|   
| getURL() Method | [flash.net.navigateToURL()](flash/net/package.html#navigateToURL\(\))| Replaced by the `flash.net.navigateToURL()` and `flash.net.sentToURL()` methods. Also see URLLoader class.  
| globalToLocal() Method | [flash.display.DisplayObject.globalToLocal()](flash/display/DisplayObject.html#globalToLocal\(\))|   
| gotoAndStop() Method | [flash.display.MovieClip.gotoAndStop()](flash/display/MovieClip.html#gotoAndStop\(\))|   
| hitTest() Method | [flash.display.DisplayObject.hitTestObject()](flash/display/DisplayObject.html#hitTestObject\(\))|   
| lineGradientStyle() Method | [flash.display.Graphics.lineGradientStyle()](flash/display/Graphics.html#lineGradientStyle\(\))|   
| lineStyle() Method | [flash.display.Graphics.lineStyle()](flash/display/Graphics.html#lineStyle\(\))|   
| lineTo() Method | [flash.display.Graphics.lineTo()](flash/display/Graphics.html#lineTo\(\))|   
| loadMovie() Method | [flash.display.Loader.load()](flash/display/Loader.html#load\(\))| See Loader class.  
| loadVariables() Method | [flash.net.URLLoader](flash/net/URLLoader.html)| Removed. See URLLoader class.  
| localToGlobal() Method | [flash.display.DisplayObject.localToGlobal()](flash/display/DisplayObject.html#localToGlobal\(\))|   
| moveTo() Method | [flash.display.Graphics.moveTo()](flash/display/Graphics.html#moveTo\(\))|   
| nextFrame() Method | [flash.display.MovieClip.nextFrame()](flash/display/MovieClip.html#nextFrame\(\))|   
| onData() EventHandler | [flash.display.LoaderInfo dispatches event: complete](flash/display/LoaderInfo.html#event:complete)| Replaced in the new event model by a `complete` event, which is dispatched when the download operation is complete but before any data is parsed.  
| onDragOut() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOut](flash/display/InteractiveObject.html#event:mouseOut)| Replaced in the new event model by a `mouseOut` event.  
| onDragOver() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOver](flash/display/InteractiveObject.html#event:mouseOver)| Replaced in the new event model by a `mouseOver` event.  
| onEnterFrame() EventHandler | [flash.display.DisplayObject dispatches event: enterFrame](flash/display/DisplayObject.html#event:enterFrame)| Replaced in the new event model by an `enterFrame` event.  
| onKeyDown() EventHandler | [flash.display.InteractiveObject dispatches event: keyDown](flash/display/InteractiveObject.html#event:keyDown)| Replaced in the new event model by a `keyDown` event.  
| onKeyUp() EventHandler | [flash.display.InteractiveObject dispatches event: keyUp](flash/display/InteractiveObject.html#event:keyUp)| Replaced in the new event model by a `keyUp` event.  
| onKillFocus() EventHandler | [flash.display.InteractiveObject dispatches event: focusOut](flash/display/InteractiveObject.html#event:focusOut)| Replaced in the new event model by a `focusOut` event.  
| onLoad() EventHandler | [flash.display.LoaderInfo dispatches event: complete](flash/display/LoaderInfo.html#event:complete)| Also see URLLoader class. A `complete` event is dispatched when the download operation is complete.  
| onMouseDown() EventHandler | [flash.display.InteractiveObject dispatches event: mouseDown](flash/display/InteractiveObject.html#event:mouseDown)| Replaced in the new event model by a `mouseDown` event.  
| onMouseMove() EventHandler | [flash.display.InteractiveObject dispatches event: mouseMove](flash/display/InteractiveObject.html#event:mouseMove)| Replaced in the new event model by a `mouseMove` event.  
| onMouseUp() EventHandler | [flash.display.InteractiveObject dispatches event: mouseUp](flash/display/InteractiveObject.html#event:mouseUp)| Replaced in the new event model by a `mouseUp` event.  
| onPress() EventHandler | [flash.display.InteractiveObject dispatches event: mouseDown](flash/display/InteractiveObject.html#event:mouseDown)| Replaced in the new event model by a `mouseDown` event.  
| onRelease() EventHandler | [flash.display.InteractiveObject dispatches event: mouseUp](flash/display/InteractiveObject.html#event:mouseUp)| Replaced in the new event model by a `mouseUp` event.  
| onReleaseOutside() EventHandler | [flash.display.InteractiveObject dispatches event: mouseUp](flash/display/InteractiveObject.html#event:mouseUp)| Replaced in the new event model by a `mouseUp` event.  
| onRollOut() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOut](flash/display/InteractiveObject.html#event:mouseOut)| Replaced in the new event model by a `mouseOut` event.  
| onRollOver() EventHandler | [flash.display.InteractiveObject dispatches event: mouseOver](flash/display/InteractiveObject.html#event:mouseOver)| Replaced in the new event model by a `mouseOver` event.  
| onSetFocus() EventHandler | [flash.display.InteractiveObject dispatches event: focusIn](flash/display/InteractiveObject.html#event:focusIn)| Replaced in the new event model by a `focusIn` event.  
| onUnload() EventHandler | [flash.display.LoaderInfo dispatches event: unload](flash/display/LoaderInfo.html#event:unload)| Replaced in the new event model by an `unload` event.  
| play() Method | [flash.display.MovieClip.play()](flash/display/MovieClip.html#play\(\))|   
| prevFrame() Method | [flash.display.MovieClip.prevFrame()](flash/display/MovieClip.html#prevFrame\(\))|   
| removeMovieClip() Method | [flash.display.DisplayObjectContainer.removeChild()](flash/display/DisplayObjectContainer.html#removeChild\(\))| Removed. Call the `removeChild()` method of the parent display object container that contains the movie clip.  
| setMask() Method | [flash.display.DisplayObject.mask](flash/display/DisplayObject.html#mask)|   
| startDrag() Method | [flash.display.Sprite.startDrag()](flash/display/Sprite.html#startDrag\(\))|   
| stop() Method | [flash.display.MovieClip.stop()](flash/display/MovieClip.html#stop\(\))|   
| stopDrag() Method | [flash.display.Sprite.stopDrag()](flash/display/Sprite.html#stopDrag\(\))|   
| swapDepths() Method | Removed| In ActionScript 3.0, you can achieve similar functionality by using the methods of the DisplayObjectContainer class, such as the `addChildAt()`, `setChildIndex()`, `swapChildren()`, and `swapChildrenAt()` methods.  
| unloadMovie() Method | [flash.display.Loader.unload()](flash/display/Loader.html#unload\(\))|   
| **MovieClipLoader class**| [flash.display.Loader](flash/display/Loader.html)| Replaced by the flash.display.Loader class.  
| MovieClipLoader Constructor | [flash.display.Loader.Loader()](flash/display/Loader.html#Loader\(\))|   
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new event model, there is no need to have a class-specific `addListener()` method, because the class inherits the `addEventListener()` method from the EventDispatcher class.  
| getProgress() Method | [flash.display.LoaderInfo dispatches event: progress](flash/display/LoaderInfo.html#event:progress)| Replaced in the new event model by a `progress` event. Event objects of `progress` type contain properties named `bytesLoaded` and `bytesTotal`.  
| loadClip() Method | [flash.display.Loader.load()](flash/display/Loader.html#load\(\))| Replaced by the `load()` method of flash.display.Loader class.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new event model, there is no need to have a class-specific `removeListener()` method, because the class inherits the `removeEventListener()` method from the EventDispatcher class.  
| unloadClip() Method | [flash.display.Loader.unload()](flash/display/Loader.html#unload\(\))| Replaced by `unload()` method of flash.display.Loader class.  
| onLoadComplete Listener | [flash.display.LoaderInfo dispatches event: complete](flash/display/LoaderInfo.html#event:complete)| Replaced in the new event model by a `complete` event.  
| onLoadError Listener | [flash.display.LoaderInfo dispatches event: ioError](flash/display/LoaderInfo.html#event:ioError)| Replaced in the new event model by an `ioError` event.  
| onLoadInit Listener | [flash.display.LoaderInfo dispatches event: init](flash/display/LoaderInfo.html#event:init)| Replaced in the new event model by an `init` event.  
| onLoadProgress Listener | [flash.display.LoaderInfo dispatches event: progress](flash/display/LoaderInfo.html#event:progress)| Replaced in the new event model by a `progress` event.  
| onLoadStart Listener | [flash.display.LoaderInfo dispatches event: open](flash/display/LoaderInfo.html#event:open)| Replaced in the new event model by an `open` event.  
| **NetConnection class**| [flash.net.NetConnection](flash/net/NetConnection.html)| This class has been moved to the flash.net package.  
| NetConnection Constructor | [flash.net.NetConnection.NetConnection()](flash/net/NetConnection.html#NetConnection\(\))|   
| connect() Constructor | [flash.net.NetConnection.connect()](flash/net/NetConnection.html#connect\(\))| ActionScript 3.0 version adds a ...(rest) parameter.  
| **NetStream class**| [flash.net.NetStream](flash/net/NetStream.html)| This class has been moved to the flash.net package.  
| bytesLoaded Property[read-only] | [flash.net.NetStream.bytesLoaded](flash/net/NetStream.html#bytesLoaded)| Data type changed to uint.  
| bytesTotal Property[read-only] | [flash.net.NetStream.bytesTotal](flash/net/NetStream.html#bytesTotal)| Data type changed to uint.  
| currentFps Property[read-only] | [flash.net.NetStream.currentFPS](flash/net/NetStream.html#currentFPS)| In ActionScript 3.0, FPS is all uppercase.  
| onStatus() EventHandler | [flash.net.NetStream dispatches event: netStatus](flash/net/NetStream.html#event:netStatus)| Replaced in the new event model by a `netStatus` event.  
| pause() Method | [flash.net.NetStream.pause()](flash/net/NetStream.html#pause\(\))| In ActionScript 3.0, the `pause` method does not take a parameter. Two new methods are available to achieve the same functionality: [ `resume()`](flash/net/NetStream.html#resume\(\)) and [ `togglePause()`](flash/net/NetStream.html#togglePause\(\)).  
| play() Method | [flash.net.NetStream.play()](flash/net/NetStream.html#play\(\))| The `name`, `start`, `len`, and `reset` parameters are no longer valid; ...`arguments` is used instead.  
| setBufferTime() Method | [flash.net.NetStream.bufferTime](flash/net/NetStream.html#bufferTime)| In ActionScript 3.0, changed to read-write accessor property.  
| **Number class**| [Number](Number.html)|   
| Number Constructor | [Number.Number()](Number.html#Number\(\))| In ActionScript 3.0, the `Number()` constructor and the `Number()` global function have the same effect. Also, there is no difference between a Number object and a literal Number value.  
| **Object class**| [Object](Object.html)|   
| __proto__ Property | Removed| In ActionScript 3.0, direct manipulation of the prototype chain is not allowed. To create a subclass, use the `extends` statement in the subclass declaration. For information about an object's inheritance tree and data type, use the new reflection API `flash.utils.describeType()`.  
| __resolve Property | [flash.utils.Proxy](flash/utils/Proxy.html)| Use the new Proxy class for similar functionality.  
| addProperty() Method | Removed| In ActionScript 3.0, accessor properties can be created directly using the keywords `get` and `set`.  
| registerClass() Method | Removed| In ActionScript 3.0, all classes are registered by default. If you are encoding an object using AMF, the class of the object is not preserved during the encoding process unless you use the `flash.utils.registerClassAlias()` function.  
| unwatch() Method | Removed| ActionScript 3.0 does not have watchpoints; therefore, the `unwatch()` method is obsolete.  
| watch() Method | Removed| Use accessor properties (get/set functions) or the flash.utils.Proxy class for similar functionality.  
| **PrintJob class**| [flash.printing.PrintJob](flash/printing/PrintJob.html)|   
| orientation Property[read-only] | [flash.printing.PrintJob.orientation](flash/printing/PrintJob.html#orientation)| This property now has a value from the PrintJobOrientation class.  
| pageHeight Property[read-only] | [flash.printing.PrintJob.pageHeight](flash/printing/PrintJob.html#pageHeight)| Data type changed to int.  
| pageWidth Property[read-only] | [flash.printing.PrintJob.pageWidth](flash/printing/PrintJob.html#pageWidth)| Data type changed to int.  
| paperHeight Property[read-only] | [flash.printing.PrintJob.paperHeight](flash/printing/PrintJob.html#paperHeight)| Data type changed to int.  
| paperWidth Property[read-only] | [flash.printing.PrintJob.paperWidth](flash/printing/PrintJob.html#paperWidth)| Data type changed to int.  
| PrintJob Constructor | [flash.printing.PrintJob.PrintJob()](flash/printing/PrintJob.html#PrintJob\(\))|   
| addPage() Method | [flash.printing.PrintJob.addPage()](flash/printing/PrintJob.html#addPage\(\))| In ActionScript 3.0, changed data types of parameters: First parameter `target` is a Sprite data type; second parameter `printArea` is a Rectangle data type; third parameter `options` is the new PrintJobOptions data type; and fourth parameter `frameNum` is an int data type.  
| send() Method | [flash.printing.PrintJob.send()](flash/printing/PrintJob.html#send\(\))|   
| start() Method | [flash.printing.PrintJob.start()](flash/printing/PrintJob.html#start\(\))|   
| **Rectangle class**|   
| containsRectangle() Method | [flash.geom.Rectangle.containsRect()](flash/geom/Rectangle.html#containsRect\(\))| Renamed for consistency.  
| **security class**| [flash.system.Security](flash/system/Security.html)| This class has been moved to the flash.system package.  
| **Selection class**|  Removed| Methods of this class have been moved to other classes.  
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new event model, there is no need to have a class-specific `addListener()` method, because any display object inherits the `addEventListener()` method from the EventDispatcher class.  
| getBeginIndex() Method | [flash.text.TextField.selectionBeginIndex](flash/text/TextField.html#selectionBeginIndex)| Changed from method to accessor property and name changed to `selectionBeginIndex`.  
| getCaretIndex() Method | [flash.text.TextField.caretIndex](flash/text/TextField.html#caretIndex)| Changed from method to accessor property and name changed to `caretIndex`.  
| getEndIndex() Method | [flash.text.TextField.selectionEndIndex](flash/text/TextField.html#selectionEndIndex)| Changed from method to accessor property and name changed to `selectionEndIndex`.  
| getFocus() Method | [flash.display.Stage.focus](flash/display/Stage.html#focus)| Changed from method to property accessor and name changed to `focus`. In ActionScript 2.0 the data type of the return value is String, but in ActionScript 3.0 the property has the InteractiveObject data type.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new event model, there is no need to have a class-specific `removeListener()` method, because display objects inherit the `removeEventListener()` method from the EventDispatcher class.  
| setFocus() Method | [flash.display.Stage.focus](flash/display/Stage.html#focus)| Changed from method to accessor property and name changed to `focus`. In ActionScript 2.0 the data type of the return value is String, but in ActionScript 3.0 the property has the InteractiveObject data type.  
| setSelection() Method | [flash.text.TextField.setSelection()](flash/text/TextField.html#setSelection\(\))| Both parameters changed from Number to uint data type.  
| onSetFocus Listener | [flash.display.InteractiveObject dispatches event: focusIn](flash/display/InteractiveObject.html#event:focusIn)| Replaced in the new event model by a `focusIn` event.  
| **SharedObject class**| [flash.net.SharedObject](flash/net/SharedObject.html)| This class has been moved to the flash.net package.  
| flush() Method | [flash.net.SharedObject.flush()](flash/net/SharedObject.html#flush\(\))| This method no longer returns a Boolean value. If the flush fails, Flash Player throws an exception; if the flush succeeds or is pending user interaction, Flash Player returns a string `"flushed"` or `"pending"`. Also, the data type of the `minDiskSpace` parameter changed to int.  
| getSize() Method | [flash.net.SharedObject.size](flash/net/SharedObject.html#size)| Changed to accessor property. Data type changed to uint.  
| onStatus() EventHandler | [flash.net.SharedObject dispatches event: netStatus](flash/net/SharedObject.html#event:netStatus)| Replaced in the new event model by a `netStatus` event.  
| **Sound class**| [flash.media.Sound](flash/media/Sound.html)| This class has been moved to the flash.media package.  
| checkPolicyFile | [flash.media.SoundChannel.stop()](flash/media/SoundChannel.html#stop\(\))| Replaced by the `flash.media.SoundChannel.stop()` method.  
| duration Property[read-only] | [flash.media.Sound.length](flash/media/Sound.html#length)|   
| id3 Property[read-only] | [flash.media.Sound.id3](flash/media/Sound.html#id3)| Data type changed from Object to ID3Info. ID3Info is a new class that contains the ID3 properties. Also, the spelling of the `songname` property changed to `songName`.  
| position Property[read-only] | [flash.media.SoundChannel.position](flash/media/SoundChannel.html#position)| Moved to the SoundChannel class.  
| attachSound() Method | Removed| Create an instance of a Sound subclass that is associated with sound data; for example, by using `new Sound()` instead.  
| getBytesLoaded() Method | [flash.media.Sound.bytesLoaded](flash/media/Sound.html#bytesLoaded)| Changed to accessor property and data type changed to uint.  
| getBytesTotal() Method | [flash.media.Sound.bytesTotal](flash/media/Sound.html#bytesTotal)| Changed to property accessor and data type changed to uint.  
| getPan() Method | [flash.media.SoundTransform.pan](flash/media/SoundTransform.html#pan)| Changed to accessor property and moved to the SoundTransform class.  
| getTransform() Method | [flash.media.SoundMixer.soundTransform](flash/media/SoundMixer.html#soundTransform)| Changed to accessor property and data type changed to SoundTransform.  
| getVolume() Method | [flash.media.SoundTransform.volume](flash/media/SoundTransform.html#volume)| Set the `flash.media.SoundTransform.volume` property to control sound volume.  
| loadSound() Method | [flash.media.Sound.load()](flash/media/Sound.html#load\(\))| The first parameter changed from a simple URL string to a URLRequest object. The second parameter changed from a Boolean value representing whether sound begins playing as soon as possible to a SoundLoaderContext object.  
| onID3() EventHandler | [flash.media.Sound dispatches event: id3](flash/media/Sound.html#event:id3)| Replaced in the new event model by an `id3` event.  
| onLoad() EventHandler | [flash.media.Sound dispatches event: complete](flash/media/Sound.html#event:complete)| Replaced in the new event model by a `complete` event.  
| onSoundComplete() EventHandler | [flash.media.SoundChannel dispatches event: soundComplete](flash/media/SoundChannel.html#event:soundComplete)| Replaced in the new event model by a `soundComplete` event.  
| setPan() Method | [flash.media.SoundTransform.pan](flash/media/SoundTransform.html#pan)| Changed to accessor property and moved to SoundTransform class.  
| setTransform() Method | [flash.media.SoundMixer.soundTransform](flash/media/SoundMixer.html#soundTransform)| Changed to accessor property and data type changed to SoundTransform.  
| setVolume() Method | [flash.media.SoundChannel](flash/media/SoundChannel.html)| Removed. Use `flash.media.SoundChannel.leftPeak` and `flash.media.SoundChannel.rightPeak` to monitor the amplitude of a sound channel.  
| start() Method | [flash.media.Sound.play()](flash/media/Sound.html#play\(\))| The `loops` parameter data type changed from Number to int. Added a third parameter, `sndTransform`, to specify the initial sound transform to be used by the sound channel.  
| stop() Method | [flash.media.SoundChannel.stop()](flash/media/SoundChannel.html#stop\(\))|   
| **Stage class**| [flash.display.Stage](flash/display/Stage.html)| This class has been moved to the flash.display package. In ActionScript 3.0, the Stage is no longer a global object. You access the Stage by using the new `DisplayObject.stage` property.  
| align Property | [flash.display.Stage.align](flash/display/Stage.html#align)|   
| height Property | [flash.display.Stage.stageHeight](flash/display/Stage.html#stageHeight)| Name changed from `height` to `stageHeight` so that it does not conflict with the `flash.display.DisplayObject.height` property.  
| scaleMode Property | [flash.display.Stage.scaleMode](flash/display/Stage.html#scaleMode)|   
| showMenu Property | [flash.display.Stage.showDefaultContextMenu](flash/display/Stage.html#showDefaultContextMenu)| Name changed to better reflect which menu is shown.  
| width Property | [flash.display.Stage.stageWidth](flash/display/Stage.html#stageWidth)| Name changed from `width` to `stageWidth` so that it does not conflict with the `flash.display.DisplayObject.width` property.  
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new event model, there is no need to have a class-specific `addListener()` method, because the class inherits the `addEventListener()` method from the EventDispatcher class.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new event model, there is no need to have a class-specific `removeListener()` method, because the class inherits the `removeEventListener()` method from the EventDispatcher class.  
| onResize Listener | [flash.display.Stage dispatches event: resize](flash/display/Stage.html#event:resize)| Replaced in the new event model by a `resize` event.  
| **String class**| [String](String.html)| Adds support for regular expressions with three new methods: `match()`, `replace()`, and `search()`.  
| concat() Method | [String.concat()](String.html#concat\(\))| Parameter changed to ...(rest) parameter format.  
| **StyleSheet class**| [flash.text.StyleSheet](flash/text/StyleSheet.html)| This class has been moved to the flash.text package. The `load()` and `onLoad()` members have been removed, and some private functions and variables have been added.  
| StyleSheet Constructor | [flash.text.StyleSheet.StyleSheet()](flash/text/StyleSheet.html#StyleSheet\(\))|   
| clear() Method | [flash.text.StyleSheet.clear()](flash/text/StyleSheet.html#clear\(\))|   
| getStyle() Method | [flash.text.StyleSheet.getStyle()](flash/text/StyleSheet.html#getStyle\(\))| Parameter name changed to `n`.  
| getStyleNames() Method | [flash.text.StyleSheet.styleNames](flash/text/StyleSheet.html#styleNames)| Changed to accessor property.  
| load() Method | [flash.net.URLLoader.load()](flash/net/URLLoader.html#load\(\))| Use the new URLLoader and URLRequest classes for loading URLs.  
| onLoad() EventHandler | [flash.net.URLLoader dispatches event: complete](flash/net/URLLoader.html#event:complete)| Replaced in the new event model by a `complete` event.  
| parseCSS() Method | [flash.text.StyleSheet.parseCSS()](flash/text/StyleSheet.html#parseCSS\(\))| In ActionScript 3.0, returns `void` instead of a Boolean value.  
| setStyle() Method | [flash.text.StyleSheet.setStyle()](flash/text/StyleSheet.html#setStyle\(\))| Parameter name changed to `n` and style to `s`.  
| transform() Method | [flash.text.StyleSheet.transform()](flash/text/StyleSheet.html#transform\(\))|   
| **System class**| [flash.system.System](flash/system/System.html)|   
| exactSettings Property | [flash.system.Security.exactSettings](flash/system/Security.html#exactSettings)| Moved to the flash.System.Security class.  
| useCodepage Property | [flash.system.System.useCodePage](flash/system/System.html#useCodePage)| In ActionScript 3.0, the letter 'P' in `useCodePage` is uppercase.  
| onStatus() EventHandler | Removed| This event hander is obsolete in the ActionScript 3.0 event model.  
| setClipboard() Method | [flash.system.System.setClipboard()](flash/system/System.html#setClipboard\(\))|   
| showSettings() Method | [flash.system.Security.showSettings()](flash/system/Security.html#showSettings\(\))|   
| **TextField class**| [flash.text.TextField](flash/text/TextField.html)| This class has been moved to the flash.text package.  
| _alpha Property | [flash.display.DisplayObject.alpha](flash/display/DisplayObject.html#alpha)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| antiAliasType Property | [flash.text.TextField.antiAliasType](flash/text/TextField.html#antiAliasType)|   
| autoSize Property | [flash.text.TextField.autoSize](flash/text/TextField.html#autoSize)|   
| background Property | [flash.text.TextField.background](flash/text/TextField.html#background)|   
| backgroundColor Property | [flash.text.TextField.backgroundColor](flash/text/TextField.html#backgroundColor)|   
| border Property | [flash.text.TextField.border](flash/text/TextField.html#border)|   
| borderColor Property | [flash.text.TextField.borderColor](flash/text/TextField.html#borderColor)| In ActionScript 3.0, returns a uint instead of a Number.  
| bottomScroll Property[read-only] | [flash.text.TextField.bottomScrollV](flash/text/TextField.html#bottomScrollV)| In ActionScript 3.0, returns a uint instead of a Number.  
| condenseWhite Property | [flash.text.TextField.condenseWhite](flash/text/TextField.html#condenseWhite)|   
| embedFonts Property | [flash.text.TextField.embedFonts](flash/text/TextField.html#embedFonts)|   
| filters Property | [flash.display.DisplayObject.filters](flash/display/DisplayObject.html#filters)|   
| gridFitType Property | [flash.text.TextField.gridFitType](flash/text/TextField.html#gridFitType)|   
| _height Property | [flash.display.DisplayObject.height](flash/display/DisplayObject.html#height)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _highquality Property | [flash.display.Stage.quality](flash/display/Stage.html#quality)| Removed. Replaced by the `quality` property of the Stage class.  
| hscroll Property | [flash.text.TextField.scrollH](flash/text/TextField.html#scrollH)| Data type changed from Number to uint. Name changed from `hscroll` to `scrollH`.  
| html Property | [flash.text.TextField.htmlText](flash/text/TextField.html#htmlText)| Removed. In ActionScript 3.0, all text fields are treated as HTML text fields. Use the `TextField.htmlText` property to set HTML text.  
| htmlText Property | [flash.text.TextField.htmlText](flash/text/TextField.html#htmlText)|   
| length Property[read-only] | [flash.text.TextField.length](flash/text/TextField.html#length)| Data type changed from Number to uint.  
| maxChars Property | [flash.text.TextField.maxChars](flash/text/TextField.html#maxChars)| Data type changed from Number to uint.  
| maxhscroll Property[read-only] | [flash.text.TextField.maxScrollH](flash/text/TextField.html#maxScrollH)| Data type changed from Number to uint.  
| maxscroll Property[read-only] | [flash.text.TextField.maxScrollV](flash/text/TextField.html#maxScrollV)| Data type changed from Number to uint. Name changed to use uppercase S and to add the letter V to represent vertical scrolling.  
| menu Property | [flash.display.InteractiveObject.contextMenu](flash/display/InteractiveObject.html#contextMenu)| This property is now inherited from the InteractiveObject class.  
| mouseWheelEnabled Property | [flash.text.TextField.mouseWheelEnabled](flash/text/TextField.html#mouseWheelEnabled)|   
| multiline Property | [flash.text.TextField.multiline](flash/text/TextField.html#multiline)|   
| _name Property | [flash.display.DisplayObject.name](flash/display/DisplayObject.html#name)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _parent Property | [flash.display.DisplayObject.parent](flash/display/DisplayObject.html#parent)| This property is now inherited from the DisplayObject class. Removed the initial underscore. Data type changed from MovieClip to DisplayObjectContainer.  
| password Property | [flash.text.TextField.displayAsPassword](flash/text/TextField.html#displayAsPassword)| Renamed property for consistency.  
| _quality Property | [flash.display.Stage.quality](flash/display/Stage.html#quality)| Moved to Stage class.  
| restrict Property | [flash.text.TextField.restrict](flash/text/TextField.html#restrict)|   
| _rotation Property | [flash.display.DisplayObject.rotation](flash/display/DisplayObject.html#rotation)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| scroll Property | [flash.text.TextField.scrollV](flash/text/TextField.html#scrollV)| Data type changed from Number to uint and name changed from `scroll` to `scrollV`.  
| selectable Property | [flash.text.TextField.selectable](flash/text/TextField.html#selectable)|   
| sharpness Property | [flash.text.TextField.sharpness](flash/text/TextField.html#sharpness)|   
| _soundbuftime Property | [flash.media.SoundMixer.bufferTime](flash/media/SoundMixer.html#bufferTime)| Properties and methods for global sound control in a SWF file are now in the flash.media.SoundMixer class.  
| styleSheet Property | [flash.text.TextField.styleSheet](flash/text/TextField.html#styleSheet)|   
| tabEnabled Property | [flash.display.InteractiveObject.tabEnabled](flash/display/InteractiveObject.html#tabEnabled)| This property is now inherited from the InteractiveObject class.  
| tabIndex Property | [flash.display.InteractiveObject.tabIndex](flash/display/InteractiveObject.html#tabIndex)| This property is now inherited from the InteractiveObject class.  
| _target Property[read-only] | Removed| ActionScript 3.0 identifies display objects directly; therefore, identifying the path is no longer necessary.  
| text Property | [flash.text.TextField.text](flash/text/TextField.html#text)|   
| textColor Property | [flash.text.TextField.textColor](flash/text/TextField.html#textColor)| Data type changed from Number to uint.  
| textHeight Property | [flash.text.TextField.textHeight](flash/text/TextField.html#textHeight)|   
| textWidth Property | [flash.text.TextField.textWidth](flash/text/TextField.html#textWidth)|   
| thickness Property | [flash.text.TextField.thickness](flash/text/TextField.html#thickness)|   
| type Property | [flash.text.TextField.type](flash/text/TextField.html#type)|   
| _url Property[read-only] | [flash.display.LoaderInfo.url](flash/display/LoaderInfo.html#url)|   
| variable Property | Removed| This variable is no longer necessary in ActionScript 3.0.  
| _visible Property | [flash.display.DisplayObject.visible](flash/display/DisplayObject.html#visible)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _width Property | [flash.display.DisplayObject.width](flash/display/DisplayObject.html#width)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| wordWrap Property | [flash.text.TextField.wordWrap](flash/text/TextField.html#wordWrap)|   
| _x Property | [flash.display.DisplayObject.x](flash/display/DisplayObject.html#x)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _xmouse Property[read-only] | [flash.display.DisplayObject.mouseX](flash/display/DisplayObject.html#mouseX)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _xscale Property | [flash.display.DisplayObject.scaleX](flash/display/DisplayObject.html#scaleX)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _y Property | [flash.display.DisplayObject.y](flash/display/DisplayObject.html#y)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _ymouse Property[read-only] | [flash.display.DisplayObject.mouseY](flash/display/DisplayObject.html#mouseY)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| _yscale Property | [flash.display.DisplayObject.scaleY](flash/display/DisplayObject.html#scaleY)| This property is now inherited from the DisplayObject class. Removed the initial underscore.  
| addListener() Method | [flash.events.EventDispatcher.addEventListener()](flash/events/EventDispatcher.html#addEventListener\(\))| In the new event model, there is no need to have a class-specific `addListener()` method, because the class inherits the `addEventListener()` method from the EventDispatcher class.  
| getDepth() Method | [flash.display.DisplayObjectContainer](flash/display/DisplayObjectContainer.html)| Removed. Use the methods of the DisplayObjectContainer class to ascertain text field depth.  
| getFontList() Method | [flash.text.Font.enumerateFonts()](flash/text/Font.html#enumerateFonts\(\))| Removed. Use `Font.enumerateFonts()` with the `enumerateDeviceFonts` parameter set to `true`.  
| getNewTextFormat() Method | [flash.text.TextField.defaultTextFormat](flash/text/TextField.html#defaultTextFormat)| Name changed from `getNewTextFormat` to `defaultTextFormat`. Changed from method to accessor property.  
| getTextFormat() Method | [flash.text.TextField.getTextFormat()](flash/text/TextField.html#getTextFormat\(\))| Data type of both parameters changed from Number to uint.  
| onChanged() EventHandler | [flash.text.TextField dispatches event: change](flash/text/TextField.html#event:change)| Replaced in the new event model by a `change` event.  
| onKillFocus() EventHandler | [flash.display.InteractiveObject dispatches event: focusOut](flash/display/InteractiveObject.html#event:focusOut)| Replaced in the new event model by a `focusOut` event.  
| onScroller() EventHandler | [flash.text.TextField dispatches event: scroll](flash/text/TextField.html#event:scroll)| Replaced in the new event model by a `scroll` event.  
| onSetFocus() EventHandler | [flash.display.InteractiveObject dispatches event: focusIn](flash/display/InteractiveObject.html#event:focusIn)| Replaced in the new event model by a `focusIn` event.  
| removeListener() Method | [flash.events.EventDispatcher.removeEventListener()](flash/events/EventDispatcher.html#removeEventListener\(\))| In the new event model, there is no need to have a class-specific `removeListener()` method, because the class inherits the `removeEventListener()` method from the EventDispatcher class.  
| removeTextField() Method | [flash.display.DisplayObjectContainer.removeChild()](flash/display/DisplayObjectContainer.html#removeChild\(\))| Removed. Call the `removeChild()` method of the parent display object container that contains the text field.  
| replaceSel() Method | [flash.text.TextField.replaceSelectedText()](flash/text/TextField.html#replaceSelectedText\(\))| Name changed from `replacesel()` to `replaceSelectedText()`. Replaced the `newText` parameter with a string value.  
| replaceText() Method | [flash.text.TextField.replaceText()](flash/text/TextField.html#replaceText\(\))| Data types of first two parameters changed from Number to uint.  
| setNewTextFormat() Method | [flash.text.TextField.defaultTextFormat](flash/text/TextField.html#defaultTextFormat)| Name changed from `setNewTextFormat` to `defaultTextFormat`. Changed from method to accessor property.  
| setTextFormat() Method | [flash.text.TextField.setTextFormat()](flash/text/TextField.html#setTextFormat\(\))| Order of parameters changed. Index parameters data type changed from Number to int.  
| **TextFormat class**| [flash.text.TextFormat](flash/text/TextFormat.html)| This class has been moved to the flash.text package.  
| align Property | [flash.text.TextFormat.align](flash/text/TextFormat.html#align)|   
| blockIndent Property | [flash.text.TextFormat.blockIndent](flash/text/TextFormat.html#blockIndent)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| bold Property | [flash.text.TextFormat.bold](flash/text/TextFormat.html#bold)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Boolean data type in ActionScript 3.0.  
| bullet Property | [flash.text.TextFormat.bullet](flash/text/TextFormat.html#bullet)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Boolean data type in ActionScript 3.0.  
| color Property | [flash.text.TextFormat.color](flash/text/TextFormat.html#color)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| font Property | [flash.text.TextFormat.font](flash/text/TextFormat.html#font)|   
| indent Property | [flash.text.TextFormat.indent](flash/text/TextFormat.html#indent)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| italic Property | [flash.text.TextFormat.bullet](flash/text/TextFormat.html#bullet)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Boolean data type in ActionScript 3.0.  
| kerning Property | [flash.text.TextFormat.kerning](flash/text/TextFormat.html#kerning)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Boolean data type in ActionScript 3.0.  
| leading Property | [flash.text.TextFormat.leading](flash/text/TextFormat.html#leading)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| leftMargin Property | [flash.text.TextFormat.leftMargin](flash/text/TextFormat.html#leftMargin)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| letterSpacing Property | [flash.text.TextFormat.letterSpacing](flash/text/TextFormat.html#letterSpacing)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| rightMargin Property | [flash.text.TextFormat.rightMargin](flash/text/TextFormat.html#rightMargin)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| size Property | [flash.text.TextFormat.size](flash/text/TextFormat.html#size)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Number data type in ActionScript 3.0.  
| underline Property | [flash.text.TextFormat.underline](flash/text/TextFormat.html#underline)| In ActionScript 3.0, data type changed to Object because one of the possible values is `null`, which is not a member of the Boolean data type in ActionScript 3.0.  
| url Property | [flash.text.TextFormat.url](flash/text/TextFormat.html#url)|   
| TextFormat Constructor | [flash.text.TextFormat.TextFormat()](flash/text/TextFormat.html#TextFormat\(\))| The `size`, `color`, `bold`, `italic`, `underline`, `url`, `leftMargin`, `rightMargin`, `indent`, and `leading` parameters have all been converted to objects.  
| getTextExtent() Method | Removed| Use the properties of flash.text.TextField for the measurements of a field containing a line of text, and use flash.text.TextLineMetrics for the measurements of the content within the text field.  
| **TextRenderer class**| [flash.text.TextRenderer](flash/text/TextRenderer.html)| Location changed. Moved to flash.text package.  
| maxLevel Property | [flash.text.TextRenderer.maxLevel](flash/text/TextRenderer.html#maxLevel)| Defined as a `uint` in ActionScript 3.0.  
| setAdvancedAntialiasingTable() Method | [flash.text.TextRenderer.setAdvancedAntiAliasingTable()](flash/text/TextRenderer.html#setAdvancedAntiAliasingTable\(\))| The `fontStyle` and `colorType` parameter values can now be set using the FontStyle and TextColorType constants, respectively. The `advancedAntiAliasingTable` parameter now takes an array of one or more CSMSettings objects.  
| **TextSnapshot class**| [flash.text.TextSnapshot](flash/text/TextSnapshot.html)| This class has been moved to the flash.text package. Several parameters have changed, as well as some method names and some return types.  
| findText() Method | [flash.text.TextSnapshot.findText()](flash/text/TextSnapshot.html#findText\(\))| Name of the `startIndex` parameter changed to `beginIndex`. Data type of the `startIndex` parameter changed from Number to int.  
| getCount() Method | [flash.text.TextSnapshot.charCount](flash/text/TextSnapshot.html#charCount)| Changed from method to accessor property. Data return type changed from Number to uint.  
| getSelected() Method | [flash.text.TextSnapshot.getSelected()](flash/text/TextSnapshot.html#getSelected\(\))| Data type of parameters changed from Number to uint and names changed from `start` and `end` to `beginIndex` and `EndIndex`.  
| getSelectedText() Method | [flash.text.TextSnapshot.getSelectedText()](flash/text/TextSnapshot.html#getSelectedText\(\))| In ActionScript 3.0, the parameter has a default value of `false`.  
| getText() Method | [flash.text.TextSnapshot.getText()](flash/text/TextSnapshot.html#getText\(\))| Data type of `start` and `end` parameters changed from Number to uint and names changed from `start` and `end` to `beginIndex` and `endIndex`.  
| getTextRunInfo() Method | [flash.text.TextSnapshot.getTextRunInfo()](flash/text/TextSnapshot.html#getTextRunInfo\(\))| Data type of parameters changed from Number to uint.  
| hitTestTextNearPos() Method | [flash.text.TextSnapshot.hitTestTextNearPos()](flash/text/TextSnapshot.html#hitTestTextNearPos\(\))| Name of the `closeDist` parameter changed to `maxDistance`; now has a default value = 0.  
| setSelectColor() Method | [flash.text.TextSnapshot.setSelectColor()](flash/text/TextSnapshot.html#setSelectColor\(\))| Data type of parameter changed from Number to uint and has a default value = 0xFFFF00.  
| setSelected() Method | [flash.text.TextSnapshot.setSelected()](flash/text/TextSnapshot.html#setSelected\(\))| Data type of `start` and `end` parameters changed from Number to uint and names changed from `start` and `end` to `beginIndex` and `endIndex`.  
| **Video class**| [flash.media.Video](flash/media/Video.html)| This class has been moved to the flash.media package. Video objects can now be created dynamically in ActionScript with the `Video()` constructor. Attach a video stream to the Video object by using `attachCamera()` or `attachNetStream()`.  
| _alpha Property | [flash.display.DisplayObject.alpha](flash/display/DisplayObject.html#alpha)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| deblocking Property | [flash.media.Video.deblocking](flash/media/Video.html#deblocking)| Data type changed from Number to int.  
| _height Property | [flash.display.DisplayObject.height](flash/display/DisplayObject.html#height)| This property is inherited from the DisplayObject class Removed the initial underscore.  
| height Property[read-only] | [flash.media.Video.videoHeight](flash/media/Video.html#videoHeight)| Data type changed from Number to int.  
| _name Property | [flash.display.DisplayObject.name](flash/display/DisplayObject.html#name)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _parent Property | [flash.display.DisplayObject.parent](flash/display/DisplayObject.html#parent)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _rotation Property | [flash.display.DisplayObject.rotation](flash/display/DisplayObject.html#rotation)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| smoothing Property | [flash.media.Video.smoothing](flash/media/Video.html#smoothing)|   
| _visible Property | [flash.display.DisplayObject.visible](flash/display/DisplayObject.html#visible)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _width Property | [flash.display.DisplayObject.width](flash/display/DisplayObject.html#width)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| width Property[read-only] | [flash.media.Video.videoWidth](flash/media/Video.html#videoWidth)| Data type changed from Number to int.  
| _x Property | [flash.display.DisplayObject.x](flash/display/DisplayObject.html#x)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _xmouse Property[read-only] | [flash.display.DisplayObject.mouseX](flash/display/DisplayObject.html#mouseX)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _xscale Property | [flash.display.DisplayObject.scaleX](flash/display/DisplayObject.html#scaleX)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _y Property | [flash.display.DisplayObject.y](flash/display/DisplayObject.html#y)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _ymouse Property[read-only] | [flash.display.DisplayObject.mouseY](flash/display/DisplayObject.html#mouseY)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| _yscale Property | [flash.display.DisplayObject.scaleY](flash/display/DisplayObject.html#scaleY)| This property is inherited from the DisplayObject class. Removed the initial underscore.  
| attachVideo() Method | [flash.media.Video.attachNetStream()](flash/media/Video.html#attachNetStream\(\))| To specify a video stream from a camera object, use `flash.media.Video.attachCamera()`.  
| clear() Method | [flash.media.Video.clear()](flash/media/Video.html#clear\(\))|   
| **XML class**| [flash.xml.XMLDocument](flash/xml/XMLDocument.html)| This class has been moved to the flash.xml package and its name has been changed to XMLDocument to avoid conflict with the new top-level XML class that implements ECMAScript for XML (E4X).  
| contentType Property | [flash.net.URLRequest.contentType](flash/net/URLRequest.html#contentType)|   
| docTypeDecl Property | [flash.xml.XMLDocument.docTypeDecl](flash/xml/XMLDocument.html#docTypeDecl)|   
| idMap Property | [flash.xml.XMLDocument.idMap](flash/xml/XMLDocument.html#idMap)|   
| ignoreWhite Property | [flash.xml.XMLDocument.ignoreWhite](flash/xml/XMLDocument.html#ignoreWhite)|   
| loaded Property | Removed| File loading functionality was removed from the XMLDocument class. Use URLLoader instead.  
| status Property | Removed| Parse failures are now reported by exceptions.  
| xmlDecl Property | [flash.xml.XMLDocument.xmlDecl](flash/xml/XMLDocument.html#xmlDecl)|   
| XML Constructor | [flash.xml.XMLDocument.XMLDocument()](flash/xml/XMLDocument.html#XMLDocument\(\))|   
| addRequestHeader() Method | [flash.net.URLRequest.requestHeaders](flash/net/URLRequest.html#requestHeaders)|   
| createElement() Method | [flash.xml.XMLDocument.createElement()](flash/xml/XMLDocument.html#createElement\(\))|   
| createTextNode() Method | [flash.xml.XMLDocument.createTextNode()](flash/xml/XMLDocument.html#createTextNode\(\))|   
| getBytesLoaded() Method | [flash.net.URLLoader.bytesLoaded](flash/net/URLLoader.html#bytesLoaded)| File loading functionality was removed from the XMLDocument class. Use URLLoader instead.  
| getBytesTotal() Method | [flash.net.URLLoader.bytesTotal](flash/net/URLLoader.html#bytesTotal)| File loading functionality was removed from the XMLDocument class. Use URLLoader instead.  
| load() Method | Removed| File loading functionality was removed from the XMLDocument class (formerly the XML class in ActionScript 2.0). Use URLLoader instead.  
| onData() EventHandler | [flash.net.URLLoader dispatches event: complete](flash/net/URLLoader.html#event:complete)| File loading functionality was removed from the XMLDocument class. Use URLLoader instead. Replaced in the new event model by a `complete` event.  
| onHTTPStatus() EventHandler | [flash.net.URLLoader dispatches event: httpStatus](flash/net/URLLoader.html#event:httpStatus)| File loading functionality was removed from the XMLDocument class. Use URLLoader instead. Replaced in the new event model by an `httpStatus` event.  
| onLoad() EventHandler | [flash.net.URLLoader dispatches event: complete](flash/net/URLLoader.html#event:complete)| File loading functionality was removed from the XMLDocument class. Use URLLoader instead. Replaced in the new event model by a `complete` event.  
| parseXML() Method | [flash.xml.XMLDocument.parseXML()](flash/xml/XMLDocument.html#parseXML\(\))|   
| send() Method | Removed| Send functionality was removed from the XMLDocument class (formerly the XML class in ActionScript 2.0). Use the functions and classes of the flash.net package instead.  
| sendAndLoad() Method | Removed| Send and load functionality were removed from the XMLDocument class (formerly the XML class in ActionScript 2.0). Use URLRequest and URLLoader instead.  
| **XMLNode class**| [flash.xml.XMLNode](flash/xml/XMLNode.html)| Location changed. This class has been moved to the flash.xml package.  
| nodeType Property[read-only] | [flash.xml.XMLNode.nodeType](flash/xml/XMLNode.html#nodeType)| Data type changed from Number to uint.  
| XMLNode Constructor | [flash.xml.XMLNode.XMLNode()](flash/xml/XMLNode.html#XMLNode\(\))| Data type of the `type` parameter changed from Number to uint.  
| **XMLSocket class**| [flash.net.XMLSocket](flash/net/XMLSocket.html)| This class has been moved to the flash.net package.  
| XMLSocket Constructor | [flash.net.XMLSocket.XMLSocket()](flash/net/XMLSocket.html#XMLSocket\(\))| Added two optional parameters to specify host and port.  
| connect() Method | [flash.net.XMLSocket.connect()](flash/net/XMLSocket.html#connect\(\))| Data type of the `port` parameter changed to int.  
| onClose() EventHandler | [flash.net.XMLSocket dispatches event: close](flash/net/XMLSocket.html#event:close)| Replaced in the new event model by a `close` event.  
| onConnect() EventHandler | [flash.net.XMLSocket dispatches event: connect](flash/net/XMLSocket.html#event:connect)| Replaced in the new event model by a `connect` event.  
| onData() EventHandler | [flash.net.XMLSocket dispatches event: data](flash/net/XMLSocket.html#event:data)| Replaced in the new event model by a `data` event.  
| onXML() EventHandler | Removed| In ActionScript 3.0, only the `data` event is dispatched, so that you can choose whether to use E4X or the legacy XML (XMLDocument class) parser. The old `onXML` event handler was called after XML was parsed, so it doesn't make sense in ActionScript 3.0 because you can now choose between the XML (E4X) class and the XMLDocument (legacy) class to parse the XML.  
  
[All Packages](package-summary.html) | [All Classes](class-summary.html) | [Language Elements](language-elements.html) | [Index](all-index-Symbols.html) | [Appendices](appendices.html) | [Conventions](conventions.html) | [Frames](index.html?migration.html&all-classes.html)[No Frames]()

[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Wed Sep 28 2022, 6:13 PM GMT+01:00\) : Migration)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Wed Sep 28 2022, 6:13 PM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)