# Worker

Package| [flash.system](package-detail.html)  
---|---  
Class| public final class Worker  
Inheritance| Worker ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.4   
---|---  
  
A Worker object represents a _worker_ , which is a virtual instance of the Flash runtime. Each Worker instance controls and provides access to the lifecycle and shared data of a single worker. 

A worker allows you to execute code "in the background" at the same time that other operations are running in another worker (including the main swf's worker). In a non-worker context some operations, for example processing a large set of data in a loop, take so long to execute that they prevent the main application thread from updating the screen quickly enough. This can cause stuttering or freezing the screen.

Using a worker allows you to perform a long-running or slow operation in the background. Each worker runs its code in a separate thread of execution from other workers. Long-running code in one worker does not block code in another worker from executing. Instead, the two sets of code run in parallel. Consequently, a worker can be used to execute code in the background while the main application thread stays free to continue updating the screen.

This capability of simultaneously executing multiple sets of code instructions is known as _concurrency_.

**Note:** The use of workers for concurrency is supported in both Flash Player and AIR on desktop platforms. For mobile platforms, concurrency is supported in AIR on both Android and iOS. You can use the static isSupported property to check whether concurrency is supported before attempting to use it. 

You do not create Worker instances directly by calling the `Worker()` constructor. In contexts where the use of workers for concurrency is supported, at startup the runtime automatically creates the Worker associated with the main SWF, known as the _primordial worker_.

Each additional worker is created from a separate swf. To create a new instance of the Worker class, pass a ByteArray with the bytes of the background worker's swf as an argument to the WorkerDomain class's `createWorker()`method. There are three common ways to access the bytes of a swf for this purpose:

  * Use the [Embed] metatag to embed the .swf file in the application as a ByteArray:
        
        // Embed the SWF file
         [Embed(source="../swfs/BgWorker.swf", mimeType="application/octet-stream")]
         private static var BgWorker_ByteClass:Class;
         
         private function createWorker():void
         {
           // create the background worker
           var workerBytes:ByteArray = new BgWorker_ByteClass();
           var bgWorker:Worker = WorkerDomain.current.createWorker(workerBytes);
           
           // listen for worker state changes to know when the worker is running
           bgWorker.addEventListener(Event.WORKER_STATE, workerStateHandler);
           
           // set up communication between workers using 
           // setSharedProperty(), createMessageChannel(), etc.
           // ... (not shown)
           
           bgWorker.start();
         }

  * Load an external SWF file using a URLLoader:
        
        // load the SWF file
         var workerLoader:URLLoader = new URLLoader();
         workerLoader.dataFormat = URLLoaderDataFormat.BINARY;
         workerLoader.addEventListener(Event.COMPLETE, loadComplete);
         workerLoader.load(new URLRequest("BgWorker.swf"));
         
         private function loadComplete(event:Event):void
         {
           // create the background worker
           var workerBytes:ByteArray = event.target.data as ByteArray;
           var bgWorker:Worker = WorkerDomain.current.createWorker(workerBytes);
           
           // listen for worker state changes to know when the worker is running
           bgWorker.addEventListener(Event.WORKER_STATE, workerStateHandler);
           
           // set up communication between workers using 
           // setSharedProperty(), createMessageChannel(), etc.
           // ... (not shown)
           
           bgWorker.start();
         }

  * Use a single swf as both the primordial worker and the background worker:
        
        // The primordial worker's main class constructor
         public function PrimordialWorkerClass()
         {
           init();
         }
         
         private function init():void
         {
           var swfBytes:ByteArray = this.loaderInfo.bytes;
           
           // Check to see if this is the primordial worker
           if (Worker.current.isPrimordial)    
           {
             // create a background worker
             var bgWorker:Worker = WorkerDomain.current.createWorker(swfBytes);
             
             // listen for worker state changes to know when the worker is running
             bgWorker.addEventListener(Event.WORKER_STATE, workerStateHandler);
             
             // set up communication between workers using 
             // setSharedProperty(), createMessageChannel(), etc.
             // ... (not shown)
             
             bgWorker.start();
           }
           else // entry point for the background worker
           {
             // set up communication between workers using getSharedProperty()
             // ... (not shown)
             
             // start the background work
           }
         }

Workers execute in isolation from each other and do not have access to the same memory, variables, and code. However, there are three mechanisms available for passing messages and data between Worker instances:

  * Shared properties: Each worker has an internal set of named values that can be set and read both from within the worker itself as well as from other workers. You can set a value using the `setSharedProperty()` method and read a value using the `getSharedProperty()` method.
  * MessageChannel: A MessageChannel object allows you to send one-way messages and data from one worker to another. Code in the receiving worker can listen for an event to be notified when a message arrives. To create a MessageChannel object, use the `createMessageChannel()` method.
  * Shareable ByteArray: If a ByteArray object's `shareable` property is `true`, the same underlying memory is used for instances of that ByteArray in all workers. Because code in multiple workers can access the shared memory at the same time, your code should use the mechanisms described in the `ByteArray.shareable` property description to avoid problems from unexpected data changes.

Several runtime APIs are not available in code running in a background worker. These primarily consist of APIs related to user input and output mechanisms, or operating system elements like windows and dragging. As a rule, for any API that isn't supported in all contexts, use the `isSupported`, `available`, and similar properties to check whether the API is available in the background worker context before attempting to use the API.

**Note:** Native Extensions are not supported for background and secondary workers.

Workers are useful because they decrease the chances of the frame rate dropping due to the main rendering thread being blocked by other code. However, workers require additional system memory and CPU use, which can be costly to overall application performance. Because each worker uses its own instance of the runtime virtual machine, even the overhead of a trivial worker can be large. When using workers, test your code across all your target platforms to ensure that the demands on the system are not too large. Adobe recommends that you do not use more than one or two background workers in a typical scenario.

[View the examples.](#includeExamplesSummary)

See also

[WorkerDomain class](../system/WorkerDomain.html)   
[WorkerDomain.createWorker() method](../system/WorkerDomain.html#createWorker\(\))   
[MessageChannel class](../system/MessageChannel.html)   
[Using ActionScript Workers by Lee Brimelow](http://gotoandlearn.com/play.php?id=162)   
[Intro to AS3 Workers: Image Processing by Shawn Blais](http://esdot.ca/site/2012/intro-to-as3-workers-part-2-image-processing)   
[Multithreaded Physics: Using AS3 Workers for a physics engine by Shawn Blais](http://esdot.ca/site/2012/intro-to-as3-workers-part-3-nape-physics-starling)

  

* * *