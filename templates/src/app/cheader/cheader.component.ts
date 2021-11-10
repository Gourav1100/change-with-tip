import {Component, OnInit} from '@angular/core';

const logo = require("./../icons/logo.png").default as string

@Component({
  selector: 'cheader',
  templateUrl: './cheader.component.html',
  styleUrls: ['./cheader.component.css']
})
export class Cheader implements OnInit{
  logo=logo;
  constructor(){

  }
  ngOnInit(){

  }
}
