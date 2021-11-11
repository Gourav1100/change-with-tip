import { Component, OnInit } from "@angular/core";

const emlogo = require("./../../icons/emlogo.png").default as string
const fblogo = require("./../../icons/fblogo.png").default as string
const inlogo = require("./../../icons/inlogo.png").default as string
const twlogo = require("./../../icons/twlogo.png").default as string
@Component({
    selector: 'aboutus-details',
    templateUrl: './AboutUs_details.component.html',
    styleUrls: ['./AboutUs_details.component.css']
})
export class AboutUsDetails implements OnInit{
    emlogo=emlogo
    inlogo=inlogo
    fblogo=fblogo
    twlogo=twlogo
    constructor(){

    }
    ngOnInit(){

    }
}
