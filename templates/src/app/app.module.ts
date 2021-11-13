import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {AboutUs} from "./userpage/AboutUs/AboutUs.component";
import { Cheader } from './cheader/cheader.component';
import { AboutUsDetails } from './userpage/aboutus_details/AboutUs_details.component';
import { Cfooter } from './cfooter/cfooter.component';
import { Userpagecomponent } from './userpage/userpage.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { AdminDashboardPageComponent } from './admin-dashboard-page/admin-dashboard-page.component';
import { CookieModule } from 'ngx-cookie';
import {MatCardModule} from '@angular/material/card';

@NgModule({
  declarations: [
    AdminPageComponent,
    AdminDashboardPageComponent,
    AppComponent,
    AboutUs,
    Cheader,
    AboutUsDetails,
    Userpagecomponent,
    Cfooter
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    CookieModule.forRoot(),
    MatGridListModule,
    MatInputModule,
    MatButtonModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    MatCardModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
