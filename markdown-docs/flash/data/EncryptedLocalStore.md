# Encryptedlocalstore

Package| [flash.data](package-detail.html)  
---|---  
Class| public class EncryptedLocalStore  
Inheritance| EncryptedLocalStore ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The EncryptedLocalStore class (ELS) provides an encrypted local storage mechanism that can be used as a small cache for an application's private data. 

ELS data cannot be shared between applications. The intent of ELS is to allow an application to store easily recreated items such as login credentials and other private information. ELS data should not be considered as permanent; see "Limitations of the encrypted local store" and "Best practices for using ELS." below. 

_AIR profile support:_ This feature is not supported on AIR for TV devices. You can test for support at run time using the `EncryptedLocalStore.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

AIR provides an encrypted local store (ELS) for each AIR application installed on a user's computer or device. This lets you save and retrieve data that is stored on the user's local hard drive in an encrypted format that cannot easily be deciphered by other users. A separate encrypted local store is used for each AIR application, and each AIR application uses a separate encrypted local store for each user account on the computer. 

Use the encrypted local store to cache information that must be secured, such as login credentials for web services. The ELS is appropriate for storing information that must be kept private from other users. It does not, however, protect the data from other processes run under the same user account. It is thus not appropriate for protecting secret application data, such as DRM or encryption keys.

AIR uses platform-specific storage mechanisms in order to secure the key to the ELS file. Internally it then uses AES-CBC 256- bit encryption to secure the data. This same approach is now used across all platforms/operating systems.

With AIR 51.0, a new mechanism is being used, but if a `getItem` call fails to find the item in the new store, the older mechanism will be queried instead. When `setItem` is called, the item will be set in the new store, and removed from the old. In a future update of AIR, this fallback mechanism will be removed, so it would be necessary for applications to update through a 51.x version if they want to migrate the data.

Information in the encrypted local store is only available to AIR application content in the application security sandbox. 

If you update an AIR application, the updated version retains access to any existing data in the encrypted local store unless:

  * The items were added with the `stronglyBound` parameter set to `true`
  * You have upgraded from the AIR 3.2 namespace to AIR 3.3 (the physical location of the encrypted local store changed between AIR 3.2 and AIR 3.3 for both Mac OS and Windows)
  * The existing and update versions are both published prior to AIR 1.5.3 and the update is signed with a migration signature

**Limitations of the encrypted local store**

The data in the encrypted local store is protected by the user's operating system account credentials. Other entities cannot access the data in the store unless they can login as that user. However, the data is not secure against access by other applications run by an authenticated user. Thus, data that your application may want to keep secret from users, such as keys used for licensing or digital rights management, is not secure. The ELS is not an appropriate location for storing such information. It is only an appropriate place for storing a user's private data, such as passwords. Note that the relevant user will normally have the access rights to be able to view the key that AIR uses to secure their ELS files.

Data in the ELS can be lost for a variety of reasons. For example, the user could uninstall the application and delete the encrypted file. Or, the publisher ID could be changed as a result of an update. Thus the ELS should be treated as a private cache, not permanent data storage. 

The `stronglyBound` parameter is deprecated and should not be set to `true`. Setting the parameter to `true` does not provide any additional protection for data. At the same time, access to the data is lost whenever the application is updated - even if the publisher ID stays the same.

The encrypted local store may perform more slowly if the stored data exceeds 10MB.

When you uninstall an AIR application, the uninstaller does not delete data stored in the encrypted local store. 

**Best practices for using ELS**

The best practices for using the ELS include:

  * Use the ELS to store sensitive user data such as passwords (setting `stronglyBound` to `false`)
  * Do not use the ELS to store applications secrets such as DRM keys or licensing tokens
  * Provide a way for your application to recreate the data stored in the ELS if the ELS data is lost. For example, by prompting the user to re-enter their account credentials when necessary.
  * Do not use the `stronglyBound` parameter.
  * If you do set `stronglyBound` to `true`, do not migrate stored items during an update. Recreate the data after the update instead.
  * Only store relatively small amounts of data. For large amounts of data, use an AIR SQL database with encryption.

Items in the encrypted local store are identified with a string. All items are stored as byte array data.

**Note** that any internal failure within the ELS code may result in an error being thrown, by any of the functions, via an internal method called `processErrorCode()`. There are different types of errors, with different descriptions, based on the underlying failure. These details are not fully documented but indicate an unrecoverable error within the ELS handlers. The most appropriate behaviour would be to enclose any ELS function calls within a `try`/`catch` block and then call `EncryptedLocalStore.reset()` within the error handler. This would remove the ELS file and should allow information to then be successfully stored and retrieved again.

[View the examples.](#includeExamplesSummary)

  

* * *