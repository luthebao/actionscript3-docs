# Printjob

Package| [flash.printing](package-detail.html)  
---|---  
Class| public class PrintJob  
Inheritance| PrintJob ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The PrintJob class lets you create content and print it to one or more pages. This class lets you render content that is visible, dynamic or offscreen to the user, prompt users with a single Print dialog box, and print an unscaled document with proportions that map to the proportions of the content. This capability is especially useful for rendering and printing dynamic content, such as database content and dynamic text. 

**Mobile Browser Support:** This class is not supported in mobile browsers.

_AIR profile support:_ This feature is supported on all desktop operating systems, but it is not supported on mobile devices or AIR for TV devices. You can test for support at run time using the `PrintJob.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

Use the `PrintJob()` constructor to create a print job.

Additionally, with the PrintJob class's properties, you can read your user's printer settings, such as page height, width, and image orientation, and you can configure your document to dynamically format Flash content that is appropriate for the printer settings.

**Note:** ActionScript 3.0 does not restrict a PrintJob object to a single frame (as did previous versions of ActionScript). However, since the operating system displays print status information to the user after the user has clicked the OK button in the Print dialog box, you should call `PrintJob.addPage()` and `PrintJob.send()` as soon as possible to send pages to the spooler. A delay reaching the frame containing the `PrintJob.send()` call delays the printing process.

Additionally, a 15 second script timeout limit applies to the following intervals:

  * `PrintJob.start()` and the first `PrintJob.addPage()`
  * `PrintJob.addPage()` and the next `PrintJob.addPage()`
  * The last `PrintJob.addPage()` and `PrintJob.send()`

If any of the above intervals span more than 15 seconds, the next call to `PrintJob.start()` on the PrintJob instance returns `false`, and the next `PrintJob.addPage()` on the PrintJob instance causes the Flash Player or Adobe AIR to throw a runtime exception.

[View the examples.](#includeExamplesSummary)

  

* * *