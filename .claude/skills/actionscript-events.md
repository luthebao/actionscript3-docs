# ActionScript 3.0 Events and Asynchronous Programming

## Overview
This skill covers the event-driven architecture in ActionScript 3.0, including event dispatching, handling, and asynchronous patterns.

## Event System Basics

### Event Flow
ActionScript uses a three-phase event flow:
1. **Capture Phase** - Event travels from Stage down to target
2. **Target Phase** - Event reaches the target object
3. **Bubble Phase** - Event bubbles up from target to Stage

```actionscript
import flash.events.Event;
import flash.events.EventDispatcher;

// Listen in different phases
sprite.addEventListener(MouseEvent.CLICK, handler, false);  // Bubble phase
sprite.addEventListener(MouseEvent.CLICK, handler, true);   // Capture phase
```

### Adding Event Listeners
```actionscript
import flash.events.MouseEvent;

// Add listener
button.addEventListener(MouseEvent.CLICK, onClick);

function onClick(event:MouseEvent):void {
    trace("Button clicked!");
}

// With priority (higher = earlier)
button.addEventListener(MouseEvent.CLICK, onClick, false, 100);

// Weak reference (for garbage collection)
button.addEventListener(MouseEvent.CLICK, onClick, false, 0, true);
```

### Removing Event Listeners
```actionscript
// Remove specific listener
button.removeEventListener(MouseEvent.CLICK, onClick);

// Always remove listeners to prevent memory leaks
override public function dispose():void {
    button.removeEventListener(MouseEvent.CLICK, onClick);
    super.dispose();
}
```

## Built-in Event Types

### Mouse Events
```actionscript
import flash.events.MouseEvent;

// Click events
MouseEvent.CLICK          // Single click
MouseEvent.DOUBLE_CLICK   // Double click (must enable doubleClickEnabled)
MouseEvent.MOUSE_DOWN     // Mouse button pressed
MouseEvent.MOUSE_UP       // Mouse button released

// Movement events
MouseEvent.MOUSE_MOVE     // Mouse moves over object
MouseEvent.MOUSE_OVER     // Mouse enters object (bubbles)
MouseEvent.MOUSE_OUT      // Mouse leaves object (bubbles)
MouseEvent.ROLL_OVER      // Mouse enters object (doesn't bubble)
MouseEvent.ROLL_OUT       // Mouse leaves object (doesn't bubble)

// Wheel event
MouseEvent.MOUSE_WHEEL    // Mouse wheel scrolled

// Example
function onMouseEvent(event:MouseEvent):void {
    trace("Local:", event.localX, event.localY);
    trace("Stage:", event.stageX, event.stageY);
    trace("Alt:", event.altKey, "Ctrl:", event.ctrlKey);
    trace("Shift:", event.shiftKey);
}
```

### Keyboard Events
```actionscript
import flash.events.KeyboardEvent;
import flash.ui.Keyboard;

stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
stage.addEventListener(KeyboardEvent.KEY_UP, onKeyUp);

function onKeyDown(event:KeyboardEvent):void {
    trace("Key code:", event.keyCode);
    trace("Char code:", event.charCode);
    trace("Key:", String.fromCharCode(event.charCode));
    
    // Check specific keys
    if (event.keyCode == Keyboard.ENTER) {
        trace("Enter pressed");
    }
    
    // Modifiers
    if (event.ctrlKey && event.keyCode == Keyboard.S) {
        trace("Ctrl+S pressed");
    }
}
```

### Timer Events
```actionscript
import flash.utils.Timer;
import flash.events.TimerEvent;

// Create timer (1000ms delay, 10 repeats)
var timer:Timer = new Timer(1000, 10);

timer.addEventListener(TimerEvent.TIMER, onTimer);
timer.addEventListener(TimerEvent.TIMER_COMPLETE, onTimerComplete);

timer.start();

function onTimer(event:TimerEvent):void {
    trace("Tick:", timer.currentCount);
}

function onTimerComplete(event:TimerEvent):void {
    trace("Timer completed");
    timer.removeEventListener(TimerEvent.TIMER, onTimer);
    timer.removeEventListener(TimerEvent.TIMER_COMPLETE, onTimerComplete);
}

// Stop timer
timer.stop();

// Reset timer
timer.reset();
```

### Frame Events
```actionscript
import flash.events.Event;

// Enter frame (every frame)
addEventListener(Event.ENTER_FRAME, onEnterFrame);

function onEnterFrame(event:Event):void {
    // Animation or game logic
    sprite.x += 5;
}

// Exit frame
addEventListener(Event.EXIT_FRAME, onExitFrame);

// Render event (after display list updates)
addEventListener(Event.RENDER, onRender);
stage.invalidate();  // Request render event
```

### Focus Events
```actionscript
import flash.events.FocusEvent;

textField.addEventListener(FocusEvent.FOCUS_IN, onFocusIn);
textField.addEventListener(FocusEvent.FOCUS_OUT, onFocusOut);

function onFocusIn(event:FocusEvent):void {
    trace("Got focus");
}

function onFocusOut(event:FocusEvent):void {
    trace("Lost focus");
}
```

## Custom Events

### Creating Custom Events
```actionscript
package com.example.events {
    import flash.events.Event;
    
    public class UserEvent extends Event {
        public static const LOGIN:String = "login";
        public static const LOGOUT:String = "logout";
        
        public var username:String;
        public var userId:int;
        
        public function UserEvent(type:String, username:String, userId:int, 
                                  bubbles:Boolean = false, 
                                  cancelable:Boolean = false) {
            super(type, bubbles, cancelable);
            this.username = username;
            this.userId = userId;
        }
        
        // Required for event cloning
        override public function clone():Event {
            return new UserEvent(type, username, userId, bubbles, cancelable);
        }
    }
}
```

### Dispatching Custom Events
```actionscript
import com.example.events.UserEvent;
import flash.events.EventDispatcher;

public class UserManager extends EventDispatcher {
    public function login(username:String, userId:int):void {
        // Login logic...
        
        // Dispatch event
        var event:UserEvent = new UserEvent(UserEvent.LOGIN, username, userId);
        dispatchEvent(event);
    }
    
    public function logout():void {
        // Logout logic...
        
        dispatchEvent(new UserEvent(UserEvent.LOGOUT, "", 0));
    }
}

// Using the event
var userManager:UserManager = new UserManager();
userManager.addEventListener(UserEvent.LOGIN, onUserLogin);

function onUserLogin(event:UserEvent):void {
    trace("User logged in:", event.username, event.userId);
}
```

## Event Patterns

### Event Delegation
```actionscript
// Single listener for multiple children
container.addEventListener(MouseEvent.CLICK, onChildClick);

function onChildClick(event:MouseEvent):void {
    var target:DisplayObject = event.target as DisplayObject;
    trace("Clicked on:", target.name);
}
```

### Once Pattern
```actionscript
// Listen for event only once
function addOnceListener(target:IEventDispatcher, type:String, 
                        handler:Function):void {
    var onceHandler:Function = function(event:Event):void {
        target.removeEventListener(type, onceHandler);
        handler(event);
    };
    target.addEventListener(type, onceHandler);
}

// Usage
addOnceListener(button, MouseEvent.CLICK, function(e:MouseEvent):void {
    trace("This will only fire once");
});
```

### Debouncing
```actionscript
import flash.utils.Timer;
import flash.events.TimerEvent;

function debounce(func:Function, delay:int):Function {
    var timer:Timer = null;
    
    return function(...args):void {
        if (timer != null) {
            timer.stop();
            timer = null;
        }
        
        timer = new Timer(delay, 1);
        timer.addEventListener(TimerEvent.TIMER_COMPLETE, function(e:TimerEvent):void {
            func.apply(null, args);
        });
        timer.start();
    };
}

// Usage
var debouncedSearch:Function = debounce(performSearch, 300);
searchField.addEventListener(Event.CHANGE, function(e:Event):void {
    debouncedSearch(searchField.text);
});
```

### Throttling
```actionscript
function throttle(func:Function, limit:int):Function {
    var inThrottle:Boolean = false;
    
    return function(...args):void {
        if (!inThrottle) {
            func.apply(null, args);
            inThrottle = true;
            
            setTimeout(function():void {
                inThrottle = false;
            }, limit);
        }
    };
}

// Usage - limit scroll handler calls
var throttledScroll:Function = throttle(onScroll, 100);
container.addEventListener(Event.SCROLL, throttledScroll);
```

## Asynchronous Loading

### Loading External Files
```actionscript
import flash.net.URLLoader;
import flash.net.URLRequest;
import flash.events.Event;
import flash.events.IOErrorEvent;

var loader:URLLoader = new URLLoader();
loader.addEventListener(Event.COMPLETE, onLoadComplete);
loader.addEventListener(IOErrorEvent.IO_ERROR, onLoadError);
loader.addEventListener(ProgressEvent.PROGRESS, onLoadProgress);

loader.load(new URLRequest("data.json"));

function onLoadComplete(event:Event):void {
    var data:String = loader.data;
    trace("Loaded:", data);
    cleanup();
}

function onLoadError(event:IOErrorEvent):void {
    trace("Error loading:", event.text);
    cleanup();
}

function onLoadProgress(event:ProgressEvent):void {
    var percent:Number = event.bytesLoaded / event.bytesTotal * 100;
    trace("Progress:", percent.toFixed(2) + "%");
}

function cleanup():void {
    loader.removeEventListener(Event.COMPLETE, onLoadComplete);
    loader.removeEventListener(IOErrorEvent.IO_ERROR, onLoadError);
    loader.removeEventListener(ProgressEvent.PROGRESS, onLoadProgress);
}
```

### Loading Images
```actionscript
import flash.display.Loader;
import flash.net.URLRequest;

var loader:Loader = new Loader();
loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onImageLoaded);
loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, onImageError);

loader.load(new URLRequest("image.jpg"));

function onImageLoaded(event:Event):void {
    var bitmap:Bitmap = loader.content as Bitmap;
    addChild(bitmap);
}

function onImageError(event:IOErrorEvent):void {
    trace("Failed to load image");
}
```

## Best Practices

### 1. Always Remove Event Listeners
```actionscript
// Bad - memory leak
button.addEventListener(MouseEvent.CLICK, onClick);

// Good - cleanup
override public function dispose():void {
    button.removeEventListener(MouseEvent.CLICK, onClick);
    super.dispose();
}
```

### 2. Use Weak References for Temporary Objects
```actionscript
// Weak reference (last parameter = true)
tempObject.addEventListener(Event.COMPLETE, onComplete, false, 0, true);
```

### 3. Stop Event Propagation When Needed
```actionscript
function onClick(event:MouseEvent):void {
    event.stopPropagation();        // Stop bubbling
    event.stopImmediatePropagation();  // Stop all listeners
}
```

### 4. Use Event Constants
```actionscript
// Good
dispatchEvent(new Event(Event.COMPLETE));

// Bad - typos not caught
dispatchEvent(new Event("complet"));
```

### 5. Handle Errors
```actionscript
loader.addEventListener(IOErrorEvent.IO_ERROR, onError);
loader.addEventListener(SecurityErrorEvent.SECURITY_ERROR, onError);

function onError(event:ErrorEvent):void {
    trace("Error:", event.text);
    // Show user-friendly message
}
```

### 6. Centralized Event Management
```actionscript
public class EventBus extends EventDispatcher {
    private static var _instance:EventBus;
    
    public static function get instance():EventBus {
        if (!_instance) {
            _instance = new EventBus();
        }
        return _instance;
    }
}

// Usage - decouple components
EventBus.instance.dispatchEvent(new GameEvent(GameEvent.SCORE_CHANGED));
EventBus.instance.addEventListener(GameEvent.SCORE_CHANGED, onScoreChanged);
```

## Common Gotchas

1. **Anonymous functions can't be removed**
   ```actionscript
   // Bad - can't remove
   button.addEventListener(MouseEvent.CLICK, function(e:Event):void {
       trace("clicked");
   });
   
   // Good - can be removed
   button.addEventListener(MouseEvent.CLICK, onClick);
   ```

2. **Event listeners persist after removeChild**
   ```actionscript
   // Still has listeners after removal
   container.removeChild(sprite);
   
   // Must explicitly remove listeners
   sprite.removeEventListener(MouseEvent.CLICK, onClick);
   ```

3. **MOUSE_OVER vs ROLL_OVER**
   - MOUSE_OVER bubbles, ROLL_OVER doesn't
   - Use ROLL_OVER for simpler hit detection

4. **Timer continues after stop() until listener removed**
   ```actionscript
   timer.stop();
   timer.removeEventListener(TimerEvent.TIMER, onTimer);
   ```
