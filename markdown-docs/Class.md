# Class

Package| [Top Level](package-detail.html)  
---|---  
Class| public dynamic class Class  
Inheritance| Class ![Inheritance](images/inherit-arrow.gif) [Object](Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
A Class object is created for each class definition in a program. Every Class object is an instance of the Class class. The Class object contains the static properties and methods of the class. The class object creates instances of the class when invoked using the `new` operator. 

Some methods, such as `flash.net.getClassByAlias()`, return an object of type Class. Other methods may have a parameter of type Class, such as `flash.net.registerClassAlias()`. 

The class name is the reference to the Class object, as this example shows:
    
    
     
    
     class Foo {
    
     }
    
     

The `class Foo{}` statement is the class definition that creates the Class object Foo. Additionally, the statement `new Foo()` will create a new instance of class Foo, and the result will be of type Foo.

Use the `class` statement to declare your classes. Class objects are useful for advanced techniques, such as assigning classes to an existing instance object at runtime, as shown in the "Examples" section below.

Any static properties and methods of a class live on the class's Class object. Class, itself, declares `prototype`.

Generally, you do not need to declare or create variables of type Class manually. However, in the following code, a class is assigned as a public Class property `circleClass`, and you can refer to this Class property as a property of the main Library class:
    
    
    
     package {
    
      import flash.display.Sprite;
    
      public class Library extends Sprite {
    
          
    
          public var circleClass:Class = Circle;
    
          public function Library() {
    
          }
    
      }
    
     }
    
      
    
     import flash.display.Shape;
    
     class Circle extends Shape {
    
      public function Circle(color:uint = 0xFFCC00, radius:Number = 10) {
    
          graphics.beginFill(color);
    
          graphics.drawCircle(radius, radius, radius);
    
      }
    
     }
    
     

Another SWF file can load the resulting Library.swf file and then instantiate objects of type Circle. The following example shows one way to get access to a child SWF file's assets. (Other techniques include using `flash.utils.getDefnitionByName()` or importing stub definitions of the child SWF file.)
    
    
    
     package {
    
      import flash.display.Sprite;
    
      import flash.display.Shape;
    
      import flash.display.Loader;
    
      import flash.net.URLRequest;
    
      import flash.events.Event;
    
      public class LibaryLoader extends Sprite {
    
          public function LibaryLoader() {
    
              var ldr:Loader = new Loader();
    
              var urlReq:URLRequest = new URLRequest("Library.swf");
    
              ldr.load(urlReq);
    
              ldr.contentLoaderInfo.addEventListener(Event.COMPLETE, loaded);
    
          }
    
          private function loaded(event:Event):void {
    
              var library:Object = event.target.content;
    
              var circle:Shape = new library.circleClass();
    
              addChild(circle);
    
          }
    
      }
    
     }
    
     

In ActionScript 3.0, you can create embedded classes for external assets (such as images, sounds, or fonts) that are compiled into SWF files. In earlier versions of ActionScript, you associated those assets using a linkage ID with the `MovieClip.attachMovie()` method. In ActionScript 3.0, each embedded asset is represented by a unique embedded asset class. Therefore, you can use the `new` operator to instantiate the asset's associated class and call methods and properties on that asset.

For example, if you are using an MXML compiler to generate SWF files, you would create an embedded class as follows:
    
    
    
         [Embed(source="bratwurst.jpg")]
    
         public var imgClass:Class;
    
     

And, to instantiate it, you write the following:
    
    
    
         var myImg:Bitmap = new imgClass();
    
     

[View the examples.](#includeExamplesSummary)

See also

[Object.prototype](Object.html#prototype)   
[new operator](operators.html#new)

  

* * *