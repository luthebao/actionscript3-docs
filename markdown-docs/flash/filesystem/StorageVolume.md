# Storagevolume

Package| [flash.filesystem](package-detail.html)  
---|---  
Class| public class StorageVolume  
Inheritance| StorageVolume ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
A StorageVolume object includes properties defining a mass storage volume. This class is used in two ways: 

  * The `storageVolume` property of a StorageVolumeChangeEvent object is a StorageVolume object. This object represents the storage volume that has been mounted or unmounted.
  * The `StorageVolumeInfo.storageVolumeInfo.getStorageVolumes()` method returns a vector of StorageVolume objects. Each of these StorageVolume objects represents a mounted storage volume.

[View the examples.](#includeExamplesSummary)

See also

[flash.filesystem.StorageVolumeInfo.getStorageVolumes()](../filesystem/StorageVolumeInfo.html#getStorageVolumes\(\))   
[flash.events.StorageVolumeChangeEvent.storageVolume](../events/StorageVolumeChangeEvent.html#storageVolume)

  

* * *