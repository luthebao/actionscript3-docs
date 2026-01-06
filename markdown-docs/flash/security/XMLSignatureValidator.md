# Xmlsignaturevalidator

Package| [flash.security](package-detail.html)  
---|---  
Class| public class XMLSignatureValidator  
Inheritance| XMLSignatureValidator ![Inheritance](../../images/inherit-arrow.gif) [EventDispatcher](../events/EventDispatcher.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The XMLSignatureValidator class validates whether an XML signature file is well formed, unmodified, and, optionally, whether it is signed using a key linked to a trusted digital certificate. 

_AIR profile support:_ This feature is supported on all desktop operating systems and AIR for TV devices, but it is not supported on mobile devices. You can test for support at run time using the `XMLSignatureValidator.isSupported` property. See [ AIR Profile Support](http://help.adobe.com/en_US/air/build/WS144092a96ffef7cc16ddeea2126bb46b82f-8000.html) for more information regarding API support across multiple profiles.

XMLSignatureValidator implements a subset of the W3C Recommendation for XML-Signature Syntax and Processing and should not be considered a conforming implementation. The supported subset of the recommendation includes:

  * All of the core signature syntax except KeyInfo element.
  * The KeyInfo element only supports the X509Data element.
  * The X509Data element only supports the X509Certificate element.
  * The SHA256 digest method algorithm.
  * The PKCS1 signing algorithm.
  * The "Canonical XML without comments" Canonicalization Method and Transform algorithm.
  * The Manifest element in additional signature syntax.

You must provide an IURIDereferencer implementation in order to verify an XML signature. This implementation class is responsible for resolving the URIs specified in the SignedInfo elements of the signature file and returning the referenced data in an object, such as a ByteArray, that implements the IDataInput interface.

In order to verify that the signing certificate chains to a trusted certificate, either the XML signature must contain the certificates required to build the chain in X509Certificate elements, or you must supply the certificates required to build the chain using the `addCertificate()` method.

**To verify an XMLSignature:**

  1. Create an instance of the XMLSignatureValidator class.
  2. Set the `uriDereferencer` property of the instance to an instance of your IURIDereferencer implementation class.
  3. Supply DER-encoded certificates for building the certificate trust chain, if desired, using the `addCertificate()` method.
  4. Call the XMLSignatureValidator `verify` method, passing in the signature to be verified.
  5. Check the `validityStatus` property after the XMLSignatureValidator object dispatches a complete event.

**About signature status:**

The validity of an XML signature can be valid, invalid, or unknown. The overall status depends on the verification status of the individual components of the signature file:

  * `digestStatus` — The validity of the cryptographic of the signature computed over the SignedInfo element. Can be `valid`, `invalid`, or `unknown`.
  * `identityStatus` — The validity of the signing certificate. If the certificate has expired, has been revoked, or altered, the status is `invalid`. If the certificate cannot be chained to a trusted root certificate, the status is `unknown`. The certificate is not checked if the digest is invalid. If not checked, the status will be reported as `unknown`.
  * `referencesStatus` — The validity of the data addressed by the references in the SignedInfo element of the signature file. Can be `valid`, `invalid`, or `unknown`. The references are not checked if the digest or certificate is invalid. Reference checking can also be skipped based on the setting of the `referencesValidationSetting` property. If not checked, the status will be reported as `unknown`.

The signature validity reported by the `validityStatus` property can be:

  * `valid` — If `referencesStatus`, `digestStatus`, and `identityStatus` are all `valid`.
  * `invalid` — If any individual status is `invalid`.
  * `unknown` — If `referencesStatus`, `digestStatus`, or `identityStatus` is `unknown`.

**Canonicalization limitations:**

The XML engine in AIR does not always produce the expected XML string when canonicalizing an XML document. For this reason, it is recommended that you avoid putting inter-element whitespace in enveloped or detached signature documents and do not redefine namespaces inside a signature document. In both cases, AIR may not recreate the document with the same character sequence as the original and, therefore, validation will fail.

[View the examples.](#includeExamplesSummary)

See also

[IURIDereferencer](IURIDereferencer.html)   
[XML-Signature Syntax and Processing](http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/)   
[Canonical XML](http://www.w3.org/TR/2001/REC-xml-c14n-20010315)   
[PKCS #1](http://www.ietf.org/rfc/rfc2437.txt)

  

* * *