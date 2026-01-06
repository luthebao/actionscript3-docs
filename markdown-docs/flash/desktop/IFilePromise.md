# Ifilepromise

Package| [flash.desktop](package-detail.html)  
---|---  
Interface| public interface IFilePromise  
Implementors| [MediaPromise](../media/MediaPromise.html)  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The IFilePromise interface defines the interface used by the AIR runtime to read data for a file promise. 

A file promise is a drag-and-drop clipboard format that allows a user to drag a file that does not yet exist out of an AIR application. AIR uses the methods and properties defined by the IFilePromise interface to access the data to be written when the file promise is dropped.

When a file promise is dropped on a suitable target, AIR calls the IFilePromise `open()` method. The implementation of this method must return the data provider as an object that implements the IDataInput interface. The provider object can be one of the built-in classes, such as ByteArray, FileStream, Socket, and URLStream, or it can be a custom class.

If the data from the data provider is accessed synchronously, such as with a ByteArray, AIR reads the amount of data indicated by the IDataInput `bytesAvailable` property and writes it to the destination file.

If the data from the data provider is accessed asynchronously, such as with a Socket, AIR uses events dispatched by the provider to regulate the process of reading the data and writing it to the file. Data is read at each progress event until a complete or a close event is received. The runtime listens for the following events (but a data provider does not need to dispatch every event):

  * Event.OPEN
  * ProgressEvent.PROGRESS
  * ProgressEvent.SOCKET_DATA
  * Event.COMPLETE
  * Event.CLOSE
  * IOErrorEvent.IOERROR
  * SecurityErrorEvent.SECURITY_ERROR
  * HTTPStatusEvent.HTTP_STATUS
  * HTTPStatusEvent.HTTP_RESPONSE_STATUS

Custom data provider classes should dispatch either a `progress` event or a `socketData` event when data is available. Likewise, either a `complete` or a `close` event should be dispatched when all the requested data has been read. The error events inform the runtime that the data transfer has failed and should be aborted. The other events should be dispatched as appropriate to aid in error handling and in debugging application logic.

The methods defined by IFilePromise are only intended to be called by the AIR runtime after a drag and drop operation has completed. Developers should not typically call these methods from their own code. 

**Note:** The URLFilePromise class, available in the air.desktop library implements the IFilePromise interface and uses the URLStream as a data provider. The air.desktop library is included as separate SWF and SWC files in the AIR SDK.

See also

[flash.desktop.Clipboard](../desktop/Clipboard.html)   
[flash.desktop.ClipboardFormats](../desktop/ClipboardFormats.html)   
[flash.desktop.NativeDragManager](../desktop/NativeDragManager.html)

  

* * *