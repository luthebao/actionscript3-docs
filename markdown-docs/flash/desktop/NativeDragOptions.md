# Nativedragoptions

Package| [flash.desktop](package-detail.html)  
---|---  
Class| public class NativeDragOptions  
Inheritance| NativeDragOptions ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 1.0   
---|---  
  
The NativeDragOptions class defines constants for the names of drag-and-drop actions allowed in a drag-and-drop operation. 

Drag actions are part of a feedback mechanism to allow the initiating and target objects to cooperate in the drag-and-drop exchange. The actions are only a _hint_ to the operating system. It is up to the drag initiator and target objects involved in the transaction to implement the proper behavior.

An initiating object should only allow the actions that it supports. For example, an initiating object should allow the _move_ action only if that object's internal logic removes the source data when a target accepts a drop with a move action.

A new NativeDragOptions object has all properties initialized to `true` (all actions allowed).

See also

[flash.desktop.NativeDragManager](../desktop/NativeDragManager.html)   
[flash.events.NativeDragEvent](../events/NativeDragEvent.html)

  

* * *