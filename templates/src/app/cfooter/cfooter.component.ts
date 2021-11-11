import {Component,OnInit} from '@angular/core';
const logo = require("./../icons/logo.png").default as string
const emlogo = require("./../icons/emlogo.png").default as string
const fblogo = require("./../icons/fblogo.png").default as string
const inlogo = require("./../icons/inlogo.png").default as string
const twlogo = require("./../icons/twlogo.png").default as string
@Component({
  selector: 'cfooter',
  templateUrl: './cfooter.component.html',
  styleUrls: ['./cfooter.component.css']
})
export class Cfooter implements OnInit{
  logo=logo
  emlogo=emlogo;
  fblogo=fblogo;
  inlogo=inlogo;
  twlogo=twlogo;
  constructor(){

  }
  ngOnInit(){

  }
}
