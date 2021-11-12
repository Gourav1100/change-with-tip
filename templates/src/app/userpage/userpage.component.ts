import { Component, ElementRef, ViewChild } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const submit=require("./../icons/submit.png").default as string
@Component({
  selector: 'userpage',
  templateUrl: './userpage.component.html',
  styleUrls: ['./userpage.component.css']
})
@Injectable()
export class Userpagecomponent {
  submit=submit
  cols : number;
  public tip: string = '';
  Url = "https://127.0.0.1:5000/submit_tip/"

  gridByBreakpoint = {
    xl: 2,
    lg: 2,
    md: 2,
    sm: 1,
    xs: 1
  }

  constructor(
    private breakpointObserver: BreakpointObserver,
    private http: HttpClient
    ) {
    this.breakpointObserver.observe([
      Breakpoints.XSmall,
      Breakpoints.Small,
      Breakpoints.Medium,
      Breakpoints.Large,
      Breakpoints.XLarge
    ]).subscribe(result => {
      if (result.matches) {
        if (result.breakpoints[Breakpoints.XSmall]) {
          this.cols = this.gridByBreakpoint.xs;
        }
        else if (result.breakpoints[Breakpoints.Small]) {
          this.cols = this.gridByBreakpoint.sm;
        }
        else if (result.breakpoints[Breakpoints.Medium]) {
          this.cols = this.gridByBreakpoint.md;
        }
        else if (result.breakpoints[Breakpoints.Large]) {
          this.cols = this.gridByBreakpoint.lg;
        }
        else if (result.breakpoints[Breakpoints.XLarge]) {
          this.cols = this.gridByBreakpoint.xl;
        }
      }
    });
  }

  submitTip(event: Event): void {
    event.preventDefault
    this.http.post(this.Url+this.tip,{}).toPromise().then(
      (response)=>{
        // if(=="Tip Submission Successful!")
        console.log(response)
      },
      (response)=>{
        console.error(response)

      }
    );
  }
}
