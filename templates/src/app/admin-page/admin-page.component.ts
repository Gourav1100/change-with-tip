import { HttpClient } from "@angular/common/http";
import { Component } from "@angular/core";

@Component({
  selector: 'admin-page-component',
  templateUrl: './admin-page.component.html'
})
export class AdminPageComponent {
  email: string;
  password: string;

  constructor(
    private http: HttpClient
  ) {}

  login(event: Event): void {
    event.preventDefault();
  }
}
