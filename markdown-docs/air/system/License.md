# License

Package| [air.system](package-detail.html)  
---|---  
Class| public class License  
Inheritance| License ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../../flash/events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 51   
---|---  
  
The License class is used to provide information about the AIR SDK license, for a running application. This may include details that will be used by the runtime to determine whether or not certain features will be supported. 

Note that this initially just loads in the information from a local file. If there is no local file then it is assumed this is a 'free tier' license. For some properties, such as the number of seats available to this developer ID, it is necessary to check the details online via the HARMAN servers. For this, you would need to first call `checkDetailsOnline`, and wait for the `complete` event before then checking the values. Default zero/null values will be returned until the relevant information has been successfully retrieved.

The goal is for an application running via ADL to be able to check the status of the local license, or for an installed application to be able to find out the relevant details. In order to prevent mis-use, if someone tried to take anyone else's developer ID and find out the details for this, this should not be possible due to the security checks that are implemented within this functionality.

  

* * *