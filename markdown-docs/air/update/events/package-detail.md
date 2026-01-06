# Package Detail

The air.update.events package contains classes that define events used by the AIR application update framework. This package is only available to content running in the AIR runtime.

  

* * *

Classes

| Class| Description  
---|---|---  
| [DownloadErrorEvent](DownloadErrorEvent.html)|  A DownloadErrorEvent object is dispatched by an ApplicationUpdater or ApplicationUpdaterUI object when an error happens while downloading the update file.  
| [StatusFileUpdateErrorEvent](StatusFileUpdateErrorEvent.html)|  A StatusUpdateFileErrorEvent is dispatched when a call to the `checkForUpdate()` method of a ApplicationUpdater object encounters an error while downloading or parsing the update descriptor file.  
| [StatusFileUpdateEvent](StatusFileUpdateEvent.html)|  Dispatched after the updater successfully validates the file in the call to the `installFromAIRFile()` method.  
| [StatusUpdateErrorEvent](StatusUpdateErrorEvent.html)|  A StatusUpdateErrorEvent is dispatched when a call to the `checkForUpdate()` method of an ApplicationUpdater object encounters an error while downloading or parsing the update descriptor file.  
| [StatusUpdateEvent](StatusUpdateEvent.html)|  An updater object dispatches a StatusUpdateEvent object after the updater successfully downloads and interprets the update descriptor file.  
| [UpdateEvent](UpdateEvent.html)|  A UpdateEvent is dispatched by a ApplicationUpdater object during the update process.  
  
© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Thu Feb 27 2025, 6:06 AM GMT  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)