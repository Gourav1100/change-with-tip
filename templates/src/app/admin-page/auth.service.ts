import { Injectable } from "@angular/core";
import { CookieService } from "ngx-cookie";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _accessToken: string;

  constructor(
    private cookieService: CookieService
  ) {
    let cachedAccessToken = cookieService.get('access_token') || '';
    if (cachedAccessToken) {
      this._accessToken = cachedAccessToken;
    }
  }

  set accessToken(accessToken: string) {
    this._accessToken = accessToken;
    this.cookieService.put('access_token', this._accessToken);
  }

  get accessToken(): string {
    return this._accessToken;
  }

  logout(): void {
    this._accessToken = '';
    this.cookieService.put('access_token', '');
  }
}
