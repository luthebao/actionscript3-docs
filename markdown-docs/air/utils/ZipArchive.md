# Ziparchive

Package| [air.utils](package-detail.html)  
---|---  
Class| public class ZipArchive  
Inheritance| ZipArchive ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../../flash/events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 51   
---|---  
  
The ZipArchive class is used to represent a zipped-up set of files in memory. 

It can be created by loading a .zip file, or can be saved out to a .zip file. The entries can be modified and accessed via the `ZipEntry` class.

Support is only provided for normal (32-bit) zip files without encryption, and with either 'store' or 'deflate' options.

For example: 
    
    
    
     var fZip : File = File.documentsDirectory.resolvePath("myZip.zip");
    
     var zip : ZipArchive = ZipArchive.load(fZip);
    
     for (var i : uint = 0; i < zip.entries.length; i++)
    
         trace( zip.entries[i].toString() );
    
     

or 
    
    
    
     var fZip : File = File.documentsDirectory.resolvePath("myZip.zip");
    
     var zip : ZipArchive = new ZipArchive();
    
     zip.entries.push( new ZipEntry("file_one.txt", bytes) );
    
     zip.save(fZip);
    
     

See also

[ZipEntry class](../utils/ZipEntry.html)

  

* * *