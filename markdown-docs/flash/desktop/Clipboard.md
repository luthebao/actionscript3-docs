# Clipboard

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public class Clipboard  
Inheritance| Clipboard ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The Clipboard class provides a container for transferring data and objects through the clipboard. The operating system clipboard can be accessed through the static `generalClipboard` property. 

A Clipboard object can contain the same information in more than one format. By supplying information in multiple formats, you increase the chances that another application will be able to use that information. Add data to a Clipboard object with the `setData()` or `setDataHandler()` method.

The standard formats are:

  * BITMAP_FORMAT: a BitmapData object (AIR only)
  * FILE_LIST_FORMAT: an array of File objects (AIR only)
  * HTML_FORMAT: HTML-formatted string data
  * TEXT_FORMAT: string data
  * RICH_TEXT_FORMAT: a ByteArray containing Rich Text Format data
  * URL_FORMAT: a URL string (AIR only)

These constants for the names of the standard formats are defined in the ClipboardFormats class.

When a transfer to or from the operating system occurs, the standard formats are automatically translated between JavaScript ActionScript data types and the native operating system clipboard types.

You can use application-defined formats to add JavaScript ActionScript objects to a Clipboard object. If an object is serializable, both a reference and a clone of the object can be made available. Object references are valid only within the originating application.

When it is computationally expensive to convert the information to be transferred into a particular format, you can supply the name of a function that performs the conversion. The function is called if and only if that format is read by the receiving component or application. Add a deferred rendering function to a Clipboard object with the `setDataHandler()` method. Note that in some cases, the operating system calls the function before a drop occurs. For example, when you use a handler function to provide the data for a file dragged from an AIR application to the file system, the operating system calls the data handler function as soon as the drag gesture leaves the AIR application—typically resulting in an undesireable pause as the file data is downloaded or created.

**Note for AIR applications:** The clipboard object referenced by the event objects dispatched for HTML drag-and-drop and copy-and-paste events are not the same type as the AIR Clipboard object. The JavaScript clipboard object is described in the AIR developer's guide.

**Note for Flash Player applications:** In Flash Player 10, a paste operation from the clipboard first requires a user event (such as a keyboard shortcut for the Paste command or a mouse click on the Paste command in a context menu). `Clipboard.getData()` will return the contents of the clipboard only if the InteractiveObject has received and is acting on a paste event. Calling `Clipboard.getData()` under any other circumstances will be unsuccessful. The same restriction applies in AIR for content outside the application sandbox.

On Linux, clipboard data does not persist when an AIR application closes.

[View the examples.](#includeExamplesSummary)

See also

[flash.desktop.NativeDragManager](../desktop/NativeDragManager.html)   
[flash.desktop.ClipboardFormats](../desktop/ClipboardFormats.html)   
[flash.desktop.ClipboardTransferMode](../desktop/ClipboardTransferMode.html)

  

* * *