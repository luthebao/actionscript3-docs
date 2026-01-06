# Filereference

Package| [flash.net](package-detail.html)  
---|---  
Class| public class FileReference  
Inheritance| FileReference ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
Subclasses| [File](../filesystem/File.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The FileReference class provides a means to upload and download files between a user's computer and a server. An operating-system dialog box prompts the user to select a file to upload or a location for download. Each FileReference object refers to a single file on the user's disk and has properties that contain information about the file's size, type, name, creation date, modification date, and creator type (Macintosh only). 

**Note:** In Adobe AIR, the File class, which extends the FileReference class, provides more capabilities and has less security restrictions than the FileReference class.

FileReference instances are created in the following ways:

  * When you use the `new` operator with the FileReference constructor: `var myFileReference = new FileReference();`
  * When you call the `FileReferenceList.browse()` method, which creates an array of FileReference objects.

During an upload operation, all the properties of a FileReference object are populated by calls to the `FileReference.browse()` or `FileReferenceList.browse()` methods. During a download operation, the `name` property is populated when the `select` event is dispatched; all other properties are populated when the `complete` event is dispatched.

The `browse()` method opens an operating-system dialog box that prompts the user to select a file for upload. The `FileReference.browse()` method lets the user select a single file; the `FileReferenceList.browse()` method lets the user select multiple files. After a successful call to the `browse()` method, call the `FileReference.upload()` method to upload one file at a time. The `FileReference.download()` method prompts the user for a location to save the file and initiates downloading from a remote URL.

The FileReference and FileReferenceList classes do not let you set the default file location for the dialog box that the `browse()` or `download()` methods generate. The default location shown in the dialog box is the most recently browsed folder, if that location can be determined, or the desktop. The classes do not allow you to read from or write to the transferred file. They do not allow the SWF file that initiated the upload or download to access the uploaded or downloaded file or the file's location on the user's disk.

The FileReference and FileReferenceList classes also do not provide methods for authentication. With servers that require authentication, you can download files with the Flash® Player browser plug-in, but uploading (on all players) and downloading (on the stand-alone or external player) fails. Listen for FileReference events to determine whether operations complete successfully and to handle errors.

For content running in Flash Player or for content running in Adobe AIR outside of the application security sandbox, uploading and downloading operations can access files only within its own domain and within any domains that a URL policy file specifies. Put a policy file on the file server if the content initiating the upload or download doesn't come from the same domain as the file server.

Note that because of new functionality added to the Flash Player, when publishing to Flash Player 10, you can have only one of the following operations active at one time: `FileReference.browse()`, `FileReference.upload()`, `FileReference.download()`, `FileReference.load()`, `FileReference.save()`. Otherwise, Flash Player throws a runtime error (code 2174). Use `FileReference.cancel()` to stop an operation in progress. This restriction applies only to Flash Player 10. Previous versions of Flash Player are unaffected by this restriction on simultaneous multiple operations.

While calls to the `FileReference.browse()`, `FileReferenceList.browse()`, or `FileReference.download()` methods are executing, SWF file playback pauses in stand-alone and external versions of Flash Player and in AIR for Linux and Mac OS X 10.1 and earlier

The following sample HTTP `POST` request is sent from Flash Player to a server-side script if no parameters are specified: 
    
    
      POST /handler.cfm HTTP/1.1 
      Accept: text/*
      Content-Type: multipart/form-data; 
      boundary=----------Ij5ae0ae0KM7GI3KM7 
      User-Agent: Shockwave Flash 
      Host: www.example.com 
      Content-Length: 421 
      Connection: Keep-Alive 
      Cache-Control: no-cache
      
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="Filename"
      
      MyFile.jpg
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="Filedata"; filename="MyFile.jpg"
      Content-Type: application/octet-stream
      
      FileDataHere
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="Upload"
      
      Submit Query
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7--
      

Flash Player sends the following HTTP `POST` request if the user specifies the parameters `"api_sig"`, `"api_key"`, and `"auth_token"`: 
    
    
      POST /handler.cfm HTTP/1.1 
      Accept: text/*
      Content-Type: multipart/form-data; 
      boundary=----------Ij5ae0ae0KM7GI3KM7 
      User-Agent: Shockwave Flash 
      Host: www.example.com 
      Content-Length: 421 
      Connection: Keep-Alive 
      Cache-Control: no-cache
      
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="Filename"
      
      MyFile.jpg
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="api_sig"
      
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="api_key"
      
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="auth_token"
      
      XXXXXXXXXXXXXXXXXXXXXX
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="Filedata"; filename="MyFile.jpg"
      Content-Type: application/octet-stream
      
      FileDataHere
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7
      Content-Disposition: form-data; name="Upload"
      
      Submit Query
      ------------Ij5GI3GI3ei4GI3ei4KM7GI3KM7KM7--
      

[View the examples.](#includeExamplesSummary)

See also

[flash.net.FileReferenceList](../net/FileReferenceList.html)   
[flash.filesystem.File](../filesystem/File.html)

  

* * *