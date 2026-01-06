# Package

Function details for the avm2.intrinsics.iteration package.

Public Functions

| Function| Defined by  
---|---|---  
|  |  [hasnext](#hasnext\(\))(obj:[Object](../../../Object.html), idx:[int](../../../int.html)):[int](../../../int.html) Determine whether the given object has any more properties. | avm2.intrinsics.iteration  
|  |  [nextname](#nextname\(\))(obj:[Object](../../../Object.html), idx:[int](../../../int.html)):[String](../../../String.html) Get the name of the next property. | avm2.intrinsics.iteration  
|  |  [nextvalue](#nextvalue\(\))(obj:[Object](../../../Object.html), idx:[int](../../../int.html)):[*](../../../specialTypes.html#*) Get the value of the next property. | avm2.intrinsics.iteration  
  
Function detail

hasnext| ()| function  
---|---|---  
  
`public function hasnext(obj:[Object](../../../Object.html), idx:[int](../../../int.html)):[int](../../../int.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Determine whether the given object has any more properties. 

Parameters | `obj:[Object](../../../Object.html)` — The object to test for properties.   
---|---  
| `idx:[int](../../../int.html)` — The previous property index (or zero to get the first property index).   
  
Returns | `[int](../../../int.html)` — Returns the next property index for this object, or zero if there are no more properties.   
---|---  
  
nextname| ()| function|   
---|---|---|---  
  
`public function nextname(obj:[Object](../../../Object.html), idx:[int](../../../int.html)):[String](../../../String.html)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Get the name of the next property. 

Parameters | `obj:[Object](../../../Object.html)` — The object for which to get a property name.   
---|---  
| `idx:[int](../../../int.html)` — The property index (as returned by `hasnext`).   
  
Returns | `[String](../../../String.html)` — Returns the property's name based on the provided index, or null if this is an invalid index.   
---|---  
  
nextvalue| ()| function|   
---|---|---|---  
  
`public function nextvalue(obj:[Object](../../../Object.html), idx:[int](../../../int.html)):[*](../../../specialTypes.html#*)`

**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 3.6   
---|---  
  
Get the value of the next property. 

Parameters | `obj:[Object](../../../Object.html)` — The object for which to get a property value.   
---|---  
| `idx:[int](../../../int.html)` — The property index (as returned by `hasnext`).   
  
Returns | `[*](../../../specialTypes.html#*)` — Returns the property's value based on the provided index, or undefined if this is an invalid index.   
---|---  
  
[Submit Feedback](mailto:adobe.support@harman.com?subject=ASLR Feedback\(Mon Jun 30 2025, 11:00 AM GMT+01:00\) : Package avm2.intrinsics.iteration)

© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Mon Jun 30 2025, 11:00 AM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)