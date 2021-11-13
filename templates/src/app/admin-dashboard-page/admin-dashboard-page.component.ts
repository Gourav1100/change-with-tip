import { HttpClient } from "@angular/common/http";
import { Component } from "@angular/core";
import { Router } from "@angular/router";
import { AuthService } from "../admin-page/auth.service";

interface Tip {
  id: string;
  timeline: string;
  tip: string;
}

@Component({
  selector: 'admin-dashboard-page',
  templateUrl: './admin-dashboard-page.component.html'
})
export class AdminDashboardPageComponent {
  tips: Tip[];

  constructor(
    private authService: AuthService,
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit(): void {
    if (!this.authService.accessToken) {
      this.router.navigate(['/admin']);
    } else {
      this.http.get<{data : Tip[]}>('http://localhost:5000/get_tips', {
        headers: {
          Authorization: 'JWT ' + this.authService.accessToken
        }
      })
        .toPromise().then((resp) => {
          this.tips = resp.data;
        }, (err) => {
          console.log(err);
        });
    }

  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/']);
  }
}
