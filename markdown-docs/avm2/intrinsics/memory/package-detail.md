# Package Detail

The amv2.intrinsics.memory package includes the low-level/intrinsic memory access APIs for loading and storing values into the application's domain memory, and for concurrency operations. Most of these functions are built into the ASC2 compiler and are replaced by single ActionScript ByteCode instructions hence eliminating the overhead involved in function calls. The concurrency utilities (mfence and casi32) are native C++ method calls.

  

* * *

Functions

| Function| Description  
---|---|---  
| [casi32](package.html#casi32\(\))|  A compare-and-swap operation for domainMemory.  
| [lf32](package.html#lf32\(\))|  Loads a 32-bit floating point value from the given `addr` in domain memory.  
| [lf64](package.html#lf64\(\))|  Loads a 64-bit floating point value from the given `addr` in domain memory.  
| [li16](package.html#li16\(\))|  Loads a 16-bit integer value from the given `addr` in domain memory.  
| [li32](package.html#li32\(\))|  Loads a 32-bit integer value from the given `addr` in domain memory.  
| [li8](package.html#li8\(\))|  Loads an 8-bit integer value from the given `addr` in domain memory.  
| [mfence](package.html#mfence\(\))|  A complete memory barrier for domainMemory (for both load and store instructions).  
| [sf32](package.html#sf32\(\))|  Stores a 32-bit floating point value into the given `addr` in domain memory.  
| [sf64](package.html#sf64\(\))|  Stores a 64-bit floating point value into the given `addr` in domain memory.  
| [si16](package.html#si16\(\))|  Stores a 16-bit integer value into the given `addr` in domain memory.  
| [si32](package.html#si32\(\))|  Stores a 32-bit integer value into the given `addr` in domain memory.  
| [si8](package.html#si8\(\))|  Stores an 8-bit integer value into the given `addr` in domain memory.  
| [sxi1](package.html#sxi1\(\))|  Sign-extends a 1-bit integer value to a 32-bit integer value.  
| [sxi16](package.html#sxi16\(\))|  Sign-extends a 16-bit integer value to a 32-bit integer value.  
| [sxi8](package.html#sxi8\(\))|  Sign-extends an 8-bit integer value to a 32-bit integer value.  
  
© 2004-2022 Adobe Systems Incorporated. All rights reserved.   
Mon Jun 30 2025, 11:00 AM GMT+01:00  
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)