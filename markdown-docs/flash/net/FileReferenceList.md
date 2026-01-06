# Filereferencelist

Package| [flash.net](package-detail.html)  
---|---  
Class| public class FileReferenceList  
Inheritance| FileReferenceList ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The FileReferenceList class provides a means to let users select one or more files for uploading. A FileReferenceList object represents a group of one or more local files on the user's disk as an array of FileReference objects. For detailed information and important considerations about FileReference objects and the FileReference class, which you use with FileReferenceList, see the FileReference class. 

To work with the FileReferenceList class:

  * Instantiate the class: `var myFileRef = new FileReferenceList();`
  * Call the `FileReferenceList.browse()` method, which opens a dialog box that lets the user select one or more files for upload: `myFileRef.browse();`
  * After the `browse()` method is called successfully, the `fileList` property of the FileReferenceList object is populated with an array of FileReference objects.
  * Call `FileReference.upload()` on each element in the `fileList` array.

The FileReferenceList class includes a `browse()` method and a `fileList` property for working with multiple files. While a call to `FileReferenceList.browse()` is executing, SWF file playback pauses in stand-alone and external versions of Flash Player and in AIR for Linux and Mac OS X 10.1 and earlier.

[View the examples.](#includeExamplesSummary)

See also

[FileReference](FileReference.html)

  

* * *