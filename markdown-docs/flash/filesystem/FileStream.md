# Filestream

Package| [flash.filesystem](package-detail.html)  
---|---  
Class| public class FileStream  
Inheritance| FileStream ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Implements| [IDataInput](../utils/IDataInput.html), [IDataOutput](../utils/IDataOutput.html)  
  
**Runtime version:**|  AIR 1.0   
---|---  
  
A FileStream object is used to read and write files. Files can be opened synchronously by calling the `open()` method or asynchronously by calling the `openAsync()` method. 

The advantage of opening files asynchronously is that other code can execute while Adobe AIR runs read and write processes in the background. When opened asynchronously, `progress` events are dispatched as operations proceed.

A File object that is opened synchronously behaves much like a ByteArray object; a file opened asynchronously behaves much like a Socket or URLStream object. When a File object is opened synchronously, the caller pauses while the requested data is read from or written to the underlying file. When opened asynchronously, any data written to the stream is immediately buffered and later written to the file.

Whether reading from a file synchronously or asynchronously, the actual read methods are synchronous. In both cases they read from data that is currently "available." The difference is that when reading synchronously all of the data is available at all times, and when reading asynchronously data becomes available gradually as the data streams into a read buffer. Either way, the data that can be synchronously read at the current moment is represented by the `bytesAvailable` property.

An application that is processing asynchronous input typically registers for `progress` events and consumes the data as it becomes available by calling read methods. Alternatively, an application can simply wait until all of the data is available by registering for the `complete` event and processing the entire data set when the `complete` event is dispatched. 

  

* * *