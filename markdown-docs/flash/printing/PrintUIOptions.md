# Printuioptions

Package| [flash.printing](package-detail.html)  
---|---  
Class| public final class PrintUIOptions  
Inheritance| PrintUIOptions ![Inheritance](../../images/inherit-arrow.gif) [Object](../../Object.html)  
  
**Language version:**|  ActionScript 3.0   
---|---  
**Runtime version:**|  AIR 2   
---|---  
  
The PrintUIOptions class is used to specify options for print dialogs that are displayed to the user. Create a PrintUIOptions instance, set its properties, and pass it as the `uiOptions` parameter of the `PrintJob.showPageSetupDialog()` or `PrintJob.start2()` method. 

For example, the following code uses a PrintUIOptions instance to specify the min and max page numbers when the Page Setup dialog is displayed:
    
    
    import flash.printing.PrintJob;
     
     var myPrintJob:PrintJob = new PrintJob();
     if (myPrintJob.supportsPageSetupDialog)
     {
         var uiOpt:PrintUIOptions = new PrintUIOptions();
         uiOpt.minPage = 1;
         uiOpt.maxPage = 3;
         myPrintJob.showPageSetupDialog(uiOpt);
     }

See also

[PrintJob](PrintJob.html)   
[PrintJob.showPageSetupDialog()](PrintJob.html#showPageSetupDialog\(\))   
[PrintJob.start2()](PrintJob.html#start2\(\))

  

* * *