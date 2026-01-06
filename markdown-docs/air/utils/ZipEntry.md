# Zipentry

Package| [air.utils](package-detail.html)  
---|---  
Class| public class ZipEntry  
Inheritance| ZipEntry ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 51   
---|---  
  
The ZipEntry class is used to represent a single file within a zip archive. 

ZipEntry objects can be created from `File` or `ByteArray` objects, and contain settings that determine how they are then stored within a `ZipArchive`.

Since a `ZipEntry` object can be associated with multiple `ZipArchive` objects, care needs to be taken if the contents are changed. Generally it would be better practice to use different instances in different archives, so a `clone()` method is provided to create a new `ZipEntry` object as a copy of an existing one.

Each entry in a zip archive is identified by a name which can include a series of folders, each folder name is separated using a forward-slash (`/`) character. Entries can either be stored, or compressed using the 'deflate' mechanism. The entry data is provided as a `ByteArray` object which is always uncompressed when in memory - i.e. the compression mechanism is only applied when the zip entry is being written into a zip archive. When reading a zip file, the data is only uncompressed when it is read (i.e. when the `data` property is first accessed).

  

* * *