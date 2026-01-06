# Mutex

Package| [flash.concurrent](package-detail.html)  
---|---  
Class| public final class Mutex  
Inheritance| Mutex ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.5   
---|---  
  
The Mutex (short for "mutual exclusion") class provides a way to make sure that only one set of code operates on a particular block of memory or other shared resource at a time. The primary use for a Mutex is to manage code in different workers accessing a shareable byte array (a ByteArray object whose `shareable` property is `true`). However, a Mutex can be used to manage workers' access to any shareable resource, such as an AIR native extension or a filesystem file. No matter what the resource, the purpose of the mutex is to ensure that only one set of code accesses the resource at a time. 

A mutex manages access using the concept of resource ownership. At any time a single mutex is "owned" by at most one worker. When ownership of a mutex switches from one worker to another the transision is atomic. This guarantees that it will never be possible for more than one worker to take ownership of the mutex. As long as code in a worker only operates on a shared resource when that worker owns the mutex, you can be certain that there will never be a conflict from multiple workers.

Use the `tryLock()` method to take ownership of the mutex if it is available. Use the `lock()` method to pause the current worker's execution until the mutex is available, then take ownership of the mutex. Once the current worker has ownership of the mutex, it can safely operate on the shared resource. When those operations are complete, call the `unlock()` method to release the mutex. At that point the current worker should no longer access the shared resource.

The Mutex class is one of the special object types that are shared between workers rather than copied between them. When you pass a mutex from one worker to another worker either by calling the Worker object's `setSharedProperty()` method or by using a MessageChannel object, both workers have a reference to the same Mutex object in the runtime's memory.

See also

[Worker class](../system/Worker.html)   
[ByteArray.shareable property](../utils/ByteArray.html#shareable)   
[Condition class](../concurrent/Condition.html)

  

* * *