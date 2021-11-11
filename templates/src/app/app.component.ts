import { Component, OnInit } from '@angular/core';

const submit=require("./icons/submit.png").default as string
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'app';
  submit=submit
  constructor(){

  }
  ngOnInit(){

  }
}
