# Iexternalizable

Package| [flash.utils](package-detail.html)  
---|---  
Interface| public interface IExternalizable  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|   
---|---  
  
The IExternalizable interface provides control over serialization of a class as it is encoded into a data stream. The `writeExternal()` and `readExternal()` methods of the IExternalizable interface are implemented by a class to allow customization of the contents and format of the data stream (but not the classname or type) for an object and its supertypes. Each individual class must serialize and reconstruct the state of its instances. These methods must be symmetrical with the supertype to save its state. These methods supercede the native Action Message Format (AMF) serialization behavior. 

If a class does not implement, nor inherits from a class which implements, the IExternalizable interface, then an instance of the class will be serialized using the default mechanism of public members only. As a result, private, internal, and protected members of a class will not be available.

To serialize private members, a class must use the IExternalizable interface. For example, the following class will not serialize any of its members because they are private:
    
    
    
     class Example {
    
     
           private var one:int;
    
           private var two:int;
    
     }
    
     

However, if you implement the IExternalizable interface, you can write to, and read from, the data stream the private members of the class as follows:
    
    
    
     class Example implement IExternalizable {
    
     
           private var one:int;
    
           private var two:int;
    
     
           public function writeExternal(output:IDataOutput) {
    
                output.writeInt(one);
    
                output.writeInt(two);
    
           }
    
     
           public function readExternal(input:IDataInput) {
    
                one = input.readInt();
    
                two = input.readInt();
    
           }
    
     }
    
     

**Note:** If a class implements IExternalizable the default serialization no longer applies to instances of that class. If that class inherits public members from a super class, you must carefully manage those members as well.

When a subclass of a class implementing IExternalizable has private members of its own, the subclass must override the methods of IExternalizable, as follows:
    
    
    
     public class Base implements IExternalizable {
    
     
          private var one:Boolean;
    
     
          public function writeExternal(output:IDataOutput):void {
    
              output.writeBoolean(one);
    
          }
    
     
          public function readExternal(input:IDataInput):void {
    
              one = input.readBoolean();
    
          }
    
     }
    
     
     public class Example extends Base {
    
     
          private var one:String;
    
     
     
          public override function writeExternal(output:IDataOutput):void {
    
              super.writeExternal(output);
    
              output.writeUTF(one);
    
          }
    
     
          public override function readExternal(input:IDataInput):void {
    
              super.readExternal(input);
    
              one = input.readUTF();
    
          }
    
     }
    
     

The IExternalizable interface can also be used to compress data before writing it to a data stream. For example:
    
    
    
     class Example implements IExternalizable {
    
     
          public var one:Boolean;
    
          public var two:Boolean;
    
          public var three:Boolean;
    
          public var four:Boolean;
    
          public var five:Boolean;
    
          public var six:Boolean;
    
          public var seven:Boolean;
    
          public var eight:Boolean;
    
     
          public function writeExternal(output:IDataOutput) {
    
              var flag:int = 0;
    
     
              if (one) flag |= 1;
    
              if (two) flag |= 2;
    
              if (three) flag |= 4;
    
              if (four) flag |= 8;
    
              if (five) flag |= 16;
    
              if (six) flag |= 32;
    
              if (seven) flag |= 64;
    
              if (eight) flag |= 128;
    
     
              output.writeByte(flag);
    
          }
    
     
          public function readExternal(input:IDataInput) {
    
              var flag:int = input.readByte();
    
     
              one = (flag & 1) != 0;
    
              two = (flag & 2) != 0;
    
              three = (flag & 4) != 0;
    
              four = (flag & 8) != 0;
    
              five = (flag & 16) != 0;
    
              six = (flag & 32) != 0;
    
              seven = (flag & 64) != 0;
    
              eight = (flag & 128) != 0;
    
          }
    
     }
    
     

See also

[flash.net.ObjectEncoding](../net/ObjectEncoding.html)

  

* * *