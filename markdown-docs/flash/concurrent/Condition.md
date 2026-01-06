# Condition

Package| [flash.concurrent](package-detail.html)  
---|---  
Class| public final class Condition  
Inheritance| Condition ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.5   
---|---  
  
A Condition object is a tool for sharing a resource between workers with the additional capability of pausing execution until a particular condition is satisfied. A Condition object is used in conjunction with a Mutex object, and adds additional functionality to the mutex's behavior. By working in combination with a mutex, the runtime ensures that each transition of ownership between workers is atomic. 

The following is one possible workflow for using a Condition object:

  1. Before using a Condition object, the first worker must take ownership of the condition's associated mutex by calling the Mutex object's `lock()` or `tryLock()` methods.
  2. The worker's code operates on the shared resource until some condition becomes false, preventing the worker from doing more work with the shared resource. For example, if the shared resource is a set of data to process, when there is no more data to process the worker can't do any more work.
  3. At that point, call the Condition object's `wait()` method to pause the worker's execution and release ownership of the mutex.
  4. At some point, a second worker takes ownership of the mutex. Because the mutex is available, it is safe for the second worker's code to operate on the shared resource. The second worker does whatever is necessary to satisfy the condition so that the first worker can do its work again. For example, if the first worker has no data to process, the second worker could pass more data to process into the shared resource.
  5. At that point, the condition related to the first worker's work is now true, so the first worker needs to be notified that the condition is fulfilled. To notify the first worker, the second worker's code calls the Condition object's `notify()` method or its `notifyAll()` method.
  6. In addition to calling `notify()`, the second worker needs to release ownership of the mutex. It does this either by calling the Mutex object's `unlock()` method or the Condition object's `wait()` method. Since the first worker called the `wait()` method, ownership of the mutex returns to the first worker. Code execution in the first worker then continues again with the next line of code following the `wait()` call.

The Condition class is one of the special object types that are shared between workers rather than copied between them. When you pass a condition from one worker to another worker either by calling the Worker object's `setSharedProperty()` method or by using a MessageChannel object, both workers have a reference to the same Condition object in the runtime's memory.

See also

[Mutex class](../concurrent/Mutex.html)   
[Worker class](../system/Worker.html)

  

* * *