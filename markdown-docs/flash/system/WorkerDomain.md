# Workerdomain

Package| [flash.system](package-detail.html)  
---|---  
Class| public final class WorkerDomain  
Inheritance| WorkerDomain ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.4   
---|---  
  
The WorkerDomain class provides a way to create Worker objects and access them. A WorkerDomain represents the runtime's mechanism for managing the set of workers within a security domain. 

**Note:** The use of workers for concurrency is supported in both Flash Player and AIR on desktop platforms. For mobile platforms, concurrency is supported in AIR on Android but not in AIR on iOS. You can use the static isSupported property to check whether concurrency is supported before attempting to use it.

You do not create WorkerDomain instances directly by calling the `WorkerDomain()` constructor. There is one single WorkerDomain instance for an application. In contexts where the use of workers for concurrency is supported, the runtime automatically creates the WorkerDomain at startup. You access that instance using the static `current` property.

To create a new instance of the Worker class, use the `createWorker()` method. To access the set of Worker objects that are currently running, use the `listWorkers()` method.

See also

[flash.system.Worker](../system/Worker.html)

  

* * *