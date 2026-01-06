# Storagevolumechangeevent

Package| [flash.events](package-detail.html)  
---|---  
Class| public class StorageVolumeChangeEvent  
Inheritance| StorageVolumeChangeEvent ![Inheritance](../../images/inherit-arrow.gif) [Event](Event.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The `StorageVolumeInfo.storageVolumeInfo` object dispatches a StorageVolumeChangeEvent event object when a storage volume is mounted or unmounted. There are two types of StorageVolumeChangeEvent: `storageVolumeMount` and `storageVolumeUnmount`. 

On Linux, the StorageVolumeInfo object only dispatches `storageVolumeMount` and `storageVolumeUnmount` events for physical devices. It does not dispatch events when the user mounts or unmounts volumes over a network.

Some devices, such as some digital cameras and phones, appear in the `StorageVolumeInfo.getStorageVolumes()` array, but they do not dispatch StorageVolumeChangeEvent objects when mounted or unmounted.

See also

[flash.filesystem.StorageVolumeInfo](../filesystem/StorageVolumeInfo.html)

  

* * *