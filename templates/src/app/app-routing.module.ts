import { createUrlResolverWithoutPackagePrefix } from '@angular/compiler';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminDashboardPageComponent } from './admin-dashboard-page/admin-dashboard-page.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { Userpagecomponent } from './userpage/userpage.component';

const routes: Routes = [
  {
    path: 'admin-dashboard',
    component: AdminDashboardPageComponent
  },
  {
    path: 'admin',
    component: AdminPageComponent
  },
  {
    path: '',
    component: Userpagecomponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
