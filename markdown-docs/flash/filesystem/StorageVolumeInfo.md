# Storagevolumeinfo

Package| [flash.filesystem](package-detail.html)  
---|---  
Class| public final class StorageVolumeInfo  
Inheritance| StorageVolumeInfo ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The StorageVolumeInfo object dispatches a StorageVolumeChangeEvent object when a storage volume is mounted or unmounted. The `StorageVolume.storageVolume` static property references the singleton StorageVolumeInfo object, which dispatches the events. The StorageVolumeInfo class also defines a `getStorageVolumes` method for listing currently mounted storage volumes. 

_AIR profile support:_ This feature is supported on all desktop operating systems, but it is not supported on all AIR for TV devices. It is also not supported on mobile devices. You can test for support at run time using the `StorageVolumeInfo.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

On modern Linux distributions, the StorageVolumeInfo object only dispatches `storageVolumeMount` and `storageVolumeUnmount` events for physical devices and network drives mounted at particular locations.

  

* * *