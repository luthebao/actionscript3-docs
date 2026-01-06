# Filefilter

Package| [flash.net](package-detail.html)  
---|---  
Class| public final class FileFilter  
Inheritance| FileFilter ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The FileFilter class is used to indicate what files on the user's system are shown in the file-browsing dialog box that is displayed when the `FileReference.browse()` method, the `FileReferenceList.browse()` method is called or a browse method of a File, FileReference, or FileReferenceList object is called. FileFilter instances are passed as a value for the optional `typeFilter` parameter to the method. If you use a FileFilter instance, extensions and file types that aren't specified in the FileFilter instance are filtered out; that is, they are not available to the user for selection. If no FileFilter object is passed to the method, all files are shown in the dialog box. 

You can use FileFilter instances in one of two ways:

  * A description with file extensions only
  * A description with file extensions and Macintosh file types

The two formats are not interchangeable within a single call to the browse method. You must use one or the other.

You can pass one or more FileFilter instances to the browse method, as shown in the following:
    
    
     var imagesFilter:FileFilter = new FileFilter("Images", "*.jpg;*.gif;*.png");
     var docFilter:FileFilter = new FileFilter("Documents", "*.pdf;*.doc;*.txt");
     var myFileReference:FileReference = new FileReference();
     myFileReference.browse([imagesFilter, docFilter]);
     

Or in an AIR application:
    
    
     var imagesFilter:FileFilter = new FileFilter("Images", "*.jpg;*.gif;*.png");
     var docFilter:FileFilter = new FileFilter("Documents", "*.pdf;*.doc;*.txt");
     var myFile:File = new File();
     myFile.browseForOpen("Open", [imagesFilter, docFilter]);
     
    
    
     var imagesFilter = new air.FileFilter("Images", "*.jpg;*.gif;*.png");
     var docFilter = new air.FileFilter("Documents", "*.pdf;*.doc;*.txt");
     var myFile = new air.File();
     myFile.browseForOpen("Open", [imagesFilter, docFilter]);
     

The list of extensions in the `FileFilter.extension` property is used to filter the files shown in the file browsing dialog. The list is not actually displayed in the dialog box; to display the file types for users, you must list the file types in the description string as well as in the extension list. The description string is displayed in the dialog box in Windows and Linux. (It is not used on the Macintosh®.) On the Macintosh, if you supply a list of Macintosh file types, that list is used to filter the files. If not, the list of file extensions is used. 

  

* * *