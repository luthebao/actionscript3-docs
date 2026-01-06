# Systemupdater

Package| [flash.system](package-detail.html)  
---|---  
Class| public class SystemUpdater  
Inheritance| SystemUpdater ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The SystemUpdater class allows you to update modules of the Flash Player, such as the DRM module for Adobe Access, as well as the Flash Player itself. Available modules are listed in the SystemUpdaterType class. 

Flash Player identifies the need for a Adobe-Access-module update by dispatching a NetStatusEvent event. The event has a `code` property with a value of `"DRM.UpdateNeeded"`. For updates to the Adobe Access module, user consent is not required. Listen for the event and initiate the update by calling `update("DRM")`.

Flash Player identifies the need for a player update by dispatching a StatusEvent event, with several possible `code` property values (see the `status` event). For updates to the player, user consent is required. Listen for the event and present the user with the option to update. The user must agree to the actual update and initiate the update by, for example, clicking a button in the user interface. You can then initiate the player update directly in ActionScript by calling `update("SYSTEM")`.

**Note** : The SystemUpdater API is supported on all desktop platforms.

See also

[flash.system.SystemUpdaterType](../system/SystemUpdaterType.html)

  

* * *