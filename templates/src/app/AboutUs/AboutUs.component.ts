import { NumberSymbol } from '@angular/common';
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'aboutus',
  templateUrl: './AboutUs.component.html',
  styleUrls: ['./AboutUs.component.css']
})
export class AboutUs implements AfterViewInit{
  @ViewChild('content') div:ElementRef
  content:string="Nobody should be whipped. \n Remember that, once and for all. \n Neither man nor animal can be influenced\n by anything but suggestion.\n - \b Mikhail Bulgakov \b"
  itterator
  stoptyping():void{
    clearInterval(this.itterator);
  }
  ngAfterViewInit(){
    let i:number=0;
    let flag: number=0
    this.itterator = setInterval(()=>{
      if(i<this.content.length){
        if(this.content[i]=="\n"){
          this.div.nativeElement.innerHTML+="<br>"
          i++
        }
        else if(this.content[i]=="\b"){
          let text:string=""
          i++
          while(this.content[i]!="\b"){
            text+=this.content[i]
            i++
          }
          this.div.nativeElement.innerHTML+="<b>"+text+"</b>"
        }
        else{
          this.div.nativeElement.innerHTML+=this.content[i++];
        }
      }
      else{
        this.stoptyping();
      }
     }, 50);
  }
}
