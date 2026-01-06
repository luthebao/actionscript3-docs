# Filemode

Package| [flash.filesystem](package-detail.html)  
---|---  
Class| public class FileMode  
Inheritance| FileMode ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The FileMode class defines string constants used in the `fileMode` parameter of the `open()` and `openAsync()` methods of the FileStream class. The `fileMode` parameter of these methods determines the capabilities available to the FileStream object once the file is opened. 

The following capabilities are available, in various combinations, based on the `fileMode` parameter value specified in the open method:

  * Reading—The FileStream object can read data from the file.
  * Writing—The FileStream object can write data to the file.
  * Creating—The FileStream object creates a nonexistent file upon opening.
  * Truncate upon opening—Data in the file is deleted upon opening (before any data is written).
  * Append written data—Data is always written to the end of the file (when any write method is called).

The following table shows the capabilities that each constant in the FileMode class provides when applied as the `fileMode` parameter of an open method of a FileStream object:

FileMode constant | Reading | Writing | Creating | Truncate upon opening | Append written data  
---|---|---|---|---|---  
`READ` |  •  |  |  |  |   
`WRITE` |  |  •  |  •  |  •  |   
`APPEND` |  |  •  |  •  |  |  •   
`UPDATE` |  •  |  •  |  •  |  |   
  
See also

[FileStream.open()](FileStream.html#open\(\))   
[FileStream.openAsync()](FileStream.html#openAsync\(\))

  

* * *