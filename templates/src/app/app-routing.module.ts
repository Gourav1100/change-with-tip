import { createUrlResolverWithoutPackagePrefix } from '@angular/compiler';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Userpagecomponent } from './userpage/userpage.component';

const routes: Routes = [
  {
    path: "user",
    component: Userpagecomponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
