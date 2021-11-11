import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {AboutUs} from "./AboutUs/AboutUs.component";
import { Cheader } from './cheader/cheader.component';
import { AboutUsDetails } from './aboutus_details/AboutUs_details.component';
import { Cfooter } from './cfooter/cfooter.component';

@NgModule({
  declarations: [
    AppComponent,
    AboutUs,
    Cheader,
    AboutUsDetails,
    Cfooter
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatGridListModule,
    MatInputModule,
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
