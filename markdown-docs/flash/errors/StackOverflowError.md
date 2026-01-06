# Stackoverflowerror

Package| [flash.errors](package-detail.html)  
---|---  
Class| public dynamic class StackOverflowError  
Inheritance| StackOverflowError ![Inheritance](../../images/inherit-arrow.gif) [Error](../../Error.html) ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
ActionScript throws a StackOverflowError exception when the stack available to the script is exhausted. ActionScript uses a stack to store information about each method call made in a script, such as the local variables that the method uses. The amount of stack space available varies from system to system. 

A StackOverflowError exception might indicate that infinite recursion has occurred, in which case a termination case needs to be added to the function. It also might indicate that the recursive algorithm has a proper terminating condition but has exhausted the stack anyway. In this case, try to express the algorithm iteratively instead.

[View the examples.](#includeExamplesSummary)

  

* * *