# Iimeclient

Package| [flash.text.ime](package-detail.html)  
---|---  
Interface| public interface IIMEClient  
  
**Language version:**|  ActionScript 3.0  
---|---  
**Runtime version:**|  AIR 2  
---|---  
  
Interface for IME (input method editor) clients. Components based on the flash.text.engine package must implement this interface to support editing text inline using an IME. This interface is not used with TextField objects. TextLayoutFramework (TLF) uses this interface to support inline IME, so clients using TLF do not need to implement this interface. 

To support inline IME, set the `imeClient` property of an `ImeEvent.IME_START_COMPOSITION` event to an object which implements this interface.

The following terms are often used in the IME related API:

  * A _conversation_ is the interchange between the IME and the application. During a conversation, a composition is updated one or more times and then confirmed by the user.
  * A _composition_ identifies the text entered by the user through the IME; including associated input state information such as the selected range and the extent of any clauses.
  * A _clause_ is a range of the composition possibly sharing semantic information, such as indicating whether the input is in a selected or converted state. A composition contains zero or more clauses.

See also

[flash.text.ime.CompositionAttributeRange](../ime/CompositionAttributeRange.html)   
[flash.events.IMEEvent.imeClient](../../events/IMEEvent.html#imeClient)

  

* * *