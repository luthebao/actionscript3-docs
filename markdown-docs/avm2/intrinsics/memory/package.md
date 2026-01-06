# Package

Function details for the avm2.intrinsics.memory package.

Public Functions

| Function| Defined by  
---|---|---  
|  |  [casi32](#casi32\(\))(addr:[int](../../../int.html), expectedVal:[int](../../../int.html), newVal:[int](../../../int.html)):[int](../../../int.html) A compare-and-swap operation for domainMemory. | avm2.intrinsics.memory  
|  |  [lf32](#lf32\(\))(addr:[int](../../../int.html)):[Number](../../../Number.html) Loads a 32-bit floating point value from the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [lf64](#lf64\(\))(addr:[int](../../../int.html)):[Number](../../../Number.html) Loads a 64-bit floating point value from the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [li16](#li16\(\))(addr:[int](../../../int.html)):[int](../../../int.html) Loads a 16-bit integer value from the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [li32](#li32\(\))(addr:[int](../../../int.html)):[int](../../../int.html) Loads a 32-bit integer value from the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [li8](#li8\(\))(addr:[int](../../../int.html)):[int](../../../int.html) Loads an 8-bit integer value from the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [mfence](#mfence\(\))():[void](../../../specialTypes.html#void) A complete memory barrier for domainMemory (for both load and store instructions). | avm2.intrinsics.memory  
|  |  [sf32](#sf32\(\))(value:[Number](../../../Number.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void) Stores a 32-bit floating point value into the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [sf64](#sf64\(\))(value:[Number](../../../Number.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void) Stores a 64-bit floating point value into the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [si16](#si16\(\))(value:[int](../../../int.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void) Stores a 16-bit integer value into the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [si32](#si32\(\))(value:[int](../../../int.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void) Stores a 32-bit integer value into the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [si8](#si8\(\))(value:[int](../../../int.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void) Stores an 8-bit integer value into the given `addr` in domain memory. | avm2.intrinsics.memory  
|  |  [sxi1](#sxi1\(\))(value:[int](../../../int.html)):[int](../../../int.html) Sign-extends a 1-bit integer value to a 32-bit integer value. | avm2.intrinsics.memory  
|  |  [sxi16](#sxi16\(\))(value:[int](../../../int.html)):[int](../../../int.html) Sign-extends a 16-bit integer value to a 32-bit integer value. | avm2.intrinsics.memory  
|  |  [sxi8](#sxi8\(\))(value:[int](../../../int.html)):[int](../../../int.html) Sign-extends an 8-bit integer value to a 32-bit integer value. | avm2.intrinsics.memory  
  
Function detail

casi32| ()| function  
---|---|---  
  
`public function casi32(addr:[int](../../../int.html), expectedVal:[int](../../../int.html), newVal:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
A compare-and-swap operation for domainMemory. This behaves like the `ByteArray.atomicCompareAndSwapIntAt` method, but operates on the current domain memory. The 32-bit value found at the `addr` offset into domain memory is checked, and if this is equal to the `expectedValue` value, then the `newValue` value is written into this offset, and the old (expected) value is returned. Otherwise, the domain memory is not updated, and the actual value found at this address is returned. 

Parameters | `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array at which to perform the compare/swap operation.   
---|---  
| `expectedVal:[int](../../../int.html)` — Contains the expected value of the integer to be replaced by the newValue parameter.   
| `newVal:[int](../../../int.html)` — The new value to put into the location at the addr offset, if the existing value equals the exptectedValue parameter.   
  
Returns | `[int](../../../int.html)` — Returns the previous value at the specified offset into the domain memory.   
---|---  
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)   
[ByteArray.atomicCompareAndSwapIntAt() method.](../../../flash/utils/ByteArray.html#atomicCompareAndSwapIntAt\(\))

lf32| ()| function|   
---|---|---|---  
  
`public function lf32(addr:[int](../../../int.html)):[Number](../../../Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Loads a 32-bit floating point value from the given `addr` in domain memory. 

Parameters | `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array from which to load the value.   
---|---  
  
Returns | `[Number](../../../Number.html)` — Returns the 32-bit single-precision floating point value found at this memory location.   
---|---  
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

lf64| ()| function|   
---|---|---|---  
  
`public function lf64(addr:[int](../../../int.html)):[Number](../../../Number.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Loads a 64-bit floating point value from the given `addr` in domain memory. 

Parameters | `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array from which to load the value.   
---|---  
  
Returns | `[Number](../../../Number.html)` — Returns the 64-bit double-precsision floating point value found at this memory location.   
---|---  
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

li16| ()| function|   
---|---|---|---  
  
`public function li16(addr:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Loads a 16-bit integer value from the given `addr` in domain memory. 

Parameters | `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array from which to load the value.   
---|---  
  
Returns | `[int](../../../int.html)` — Returns the 16-bit integer value found at this memory location.   
---|---  
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

li32| ()| function|   
---|---|---|---  
  
`public function li32(addr:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Loads a 32-bit integer value from the given `addr` in domain memory. 

Parameters | `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array from which to load the value.   
---|---  
  
Returns | `[int](../../../int.html)` — Returns the 32-bit integer value found at this memory location.   
---|---  
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

li8| ()| function|   
---|---|---|---  
  
`public function li8(addr:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Loads an 8-bit integer value from the given `addr` in domain memory. 

Parameters | `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array from which to load the value.   
---|---  
  
Returns | `[int](../../../int.html)` — Returns the 8-bit integer value found at this memory location.   
---|---  
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

mfence| ()| function|   
---|---|---|---  
  
`public function mfence():[void](../../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
A complete memory barrier for domainMemory (for both load and store instructions). 

See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

sf32| ()| function|   
---|---|---|---  
  
`public function sf32(value:[Number](../../../Number.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Stores a 32-bit floating point value into the given `addr` in domain memory. 

Parameters | `value:[Number](../../../Number.html)` — The 32-bit single-precision floating point value to be stored into the domain memory.   
---|---  
| `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array into which to store the value.   
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

sf64| ()| function|   
---|---|---|---  
  
`public function sf64(value:[Number](../../../Number.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Stores a 64-bit floating point value into the given `addr` in domain memory. 

Parameters | `value:[Number](../../../Number.html)` — The 64-bit double-precision floating point value to be stored into the domain memory.   
---|---  
| `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array into which to store the value.   
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

si16| ()| function|   
---|---|---|---  
  
`public function si16(value:[int](../../../int.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Stores a 16-bit integer value into the given `addr` in domain memory. 

Parameters | `value:[int](../../../int.html)` — The integer value treated as a 16-bit value to be stored into the domain memory.   
---|---  
| `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array into which to store the value.   
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

si32| ()| function|   
---|---|---|---  
  
`public function si32(value:[int](../../../int.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Stores a 32-bit integer value into the given `addr` in domain memory. 

Parameters | `value:[int](../../../int.html)` — The integer value to be stored into the domain memory.   
---|---  
| `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array into which to store the value.   
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

si8| ()| function|   
---|---|---|---  
  
`public function si8(value:[int](../../../int.html), addr:[int](../../../int.html)):[void](../../../specialTypes.html#void)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Stores an 8-bit integer value into the given `addr` in domain memory. 

Parameters | `value:[int](../../../int.html)` — The integer value treated as an 8-bit value to be stored into the domain memory.   
---|---  
| `addr:[int](../../../int.html)` — The address/offset into the domain memory byte array into which to store the value.   
  
See also

[ApplicationDomain domainMemory property](../../../flash/system/ApplicationDomain.html#domainMemory)

sxi1| ()| function|   
---|---|---|---  
  
`public function sxi1(value:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Sign-extends a 1-bit integer value to a 32-bit integer value. 

Parameters | `value:[int](../../../int.html)` — The integer value that is treated as a 1-bit value.   
---|---  
  
Returns | `[int](../../../int.html)` — Returns the 32-bit integer value created by sign-extending the 1-bit argument.   
---|---  
  
sxi16| ()| function|   
---|---|---|---  
  
`public function sxi16(value:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Sign-extends a 16-bit integer value to a 32-bit integer value. 

Parameters | `value:[int](../../../int.html)` — The integer value that is treated as a 16-bit value.   
---|---  
  
Returns | `[int](../../../int.html)` — Returns the 32-bit integer value created by sign-extending the 16-bit argument.   
---|---  
  
sxi8| ()| function|   
---|---|---|---  
  
`public function sxi8(value:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Sign-extends an 8-bit integer value to a 32-bit integer value. 

Parameters | `value:[int](../../../int.html)` — The integer value that is treated as an 8-bit value.   
---|---  
  
Returns | `[int](../../../int.html)` — Returns the 32-bit integer value created by sign-extending the 8-bit argument.   
---|---  
  
[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Mon Jun 30 2025, 11:00 AM GMT+01:00\) : Package avm2.intrinsics.memory)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Mon Jun 30 2025, 11:00 AM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)