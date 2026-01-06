# File

Package| [flash.filesystem](package-detail.html)  
---|---  
Class| public class File  
Inheritance| File ![Inheritance](../../images/inherit-arrow.gif) [FileReference](../net/FileReference.html) ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
A File object represents a path to a file or directory. This can be an existing file or directory, or it can be one that does not yet exist; for instance, it can represent the path to a file or directory that you plan to create. 

The File class has a number of properties and methods for getting information about the file system and for performing operations, such as copying files and directories.

You can use File objects along with the FileStream class to read and write files. 

The File class extends the FileReference class. The FileReference class, which is available in Flash® Player as well as Adobe® AIR®, represents a pointer to a file, but the File class adds properties and methods that are not exposed in Flash Player (in a SWF running in a browser), due to security considerations.

The File class includes static properties that let you reference commonly used directory locations. These static properties include:

  * `File.applicationStorageDirectory`—a storage directory unique to each installed AIR application
  * `File.applicationRemovableStorageDirectory`—(Android-only): a storage directory on an exterrnal/removal device unique to each installed AIR application
  * `File.applicationDirectory`—the read-only directory where the application is installed (along with any installed assets)
  * `File.desktopDirectory`—the user's desktop directory
  * `File.documentsDirectory`—the user's documents directory
  * `File.userDirectory`—the user directory

These properties have meaningful values on different operating systems. For example, Mac OS, Linux, and Windows each have different native paths to the user's desktop directory. However, the `File.desktopDirectory` property points to the correct desktop directory path on each of these platforms. To write applications that work well across platforms, use these properties as the basis for referencing other files used by the application. Then use the `resolvePath()` method to refine the path. For example, this code points to the preferences.xml file in the application storage directory:
    
    
     var prefsFile:File = File.applicationStorageDirectory;
    
      prefsFile = prefsFile.resolvePath("preferences.xml");
    
    
     var prefsFile = air.File.applicationStorageDirectory;
    
      prefsFile = prefsFile.resolvePath("preferences.xml");

If you use a literal native path in referencing a file, it will only work on one platform. For example, the following File object would only work on Windows:
    
    
    new File("C:\Documents and Settings\joe\My Documents\test.txt")
    
    
    new air.File("C:\Documents and Settings\joe\My Documents\test.txt")

The application storage directory is particularly useful. It gives an application-specific storage directory for the AIR application. It is defined by the `File.applicationStorageDirectory` property. Note that on Mac OS, this location changed between AIR 3.2 and AIR 3.3.

Do not add or remove content from the application directory (where the AIR application is installed). Doing so can break an AIR application and invalidate the application signature. AIR does not let you write to the application directory by default, because the directory is not writable to all user accounts on all operating systems. Use the application storage directory to write internal application files. Use the documents directory to write files that a user expects to use outside your application, such as edited pictures or text files.

See also

[FileStream](FileStream.html)

  

* * *