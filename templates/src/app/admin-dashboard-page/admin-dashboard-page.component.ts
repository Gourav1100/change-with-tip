import { HttpClient } from "@angular/common/http";
import { Component } from "@angular/core";
import { Router } from "@angular/router";
import { AuthService } from "../admin-page/auth.service";

const logout_button = require("./../icons/logout.png").default as string

interface Tip {
  id: string;
  timeline: string;
  tip: string;
}

@Component({
  selector: 'admin-dashboard-page',
  templateUrl: './admin-dashboard-page.component.html',
  styleUrls: ["./admin-dashboard-page.component.css"]
})
export class AdminDashboardPageComponent {
  tips: Tip[];
  logout_button = logout_button
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
