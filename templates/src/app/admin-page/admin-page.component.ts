import { BreakpointObserver, Breakpoints } from "@angular/cdk/layout";
import { HttpClient } from "@angular/common/http";
import { Component, Injectable } from "@angular/core";
import { FormControl, Validators } from "@angular/forms";
const submit=require("./../icons/submit.png").default as string;
const logo = require("./../icons/logo.png").default as string;
const visibility_off = require("./../icons/visibility_off.png").default as string;
const visibility_on = require("./../icons/visibility_on.png").default as string;

@Component({
  selector: 'admin-page-component',
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.css']
})
@Injectable()
export class AdminPageComponent {
  visibility_off = visibility_off
  visibility_on = visibility_on
  logo = logo;
  submit = submit;
  url= 'localhost:5000/login/';
  hide : boolean = true;
  email: string;
  password: string;
  cols: number;
  rows: number = 8;
  gridByBreakpoint = {
    xl: 3,
    lg: 3,
    md: 1,
    sm: 1,
    xs: 1
  }
  EmailFormControl = new FormControl('', [Validators.required, Validators.email]);
  PassFormControl = new FormControl('', [Validators.required,Validators.pattern("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")]);

  constructor(private breakpointObserver: BreakpointObserver,
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
          this.rows = 2;
        }
        else if (result.breakpoints[Breakpoints.Small]) {
          this.cols = this.gridByBreakpoint.sm;
          this.rows = 2;
        }
        else if (result.breakpoints[Breakpoints.Medium]) {
          this.cols = this.gridByBreakpoint.md;
          this.rows = 2;
        }
        else if (result.breakpoints[Breakpoints.Large]) {
          this.cols = this.gridByBreakpoint.lg;
          this.rows = 8;
        }
        else if (result.breakpoints[Breakpoints.XLarge]) {
          this.cols = this.gridByBreakpoint.xl;
          this.rows = 8;
        }
      }
    });
  }

  login(event: Event): void {
    event.preventDefault();
    this.http.get(this.url+this.email+'/'+this.password+'').toPromise().then(
      (response) => {
        console.log(response);
      },
      (response) => {
        console.error(response);
      }
    );
  }
}
