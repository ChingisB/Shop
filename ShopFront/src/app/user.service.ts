import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UserWithToken } from './interfaces/userwithtoken';
import { tap } from 'rxjs/operators';
import { ApiConstService } from './api-const.service';

@Injectable({
  providedIn: 'root'
})
export class UserService implements OnInit{

  private user: UserWithToken = <UserWithToken>{};

  logged: boolean = false;

  ngOnInit(){
    const token = localStorage.getItem("token")
    if(token){
      this.logged = true
    }
  }

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { }

  login(username: String, password: String): Observable<UserWithToken> {
    return this.httpClient.post<UserWithToken>(`${this.apiService.getApiUrl()}login/`, {"username": username, "password": password})
      .pipe(
        tap(user => {
          localStorage.setItem("token", user.token)
          this.user = user;
        })
      );
  }

  getUser(): UserWithToken {
    return this.user;
  }

  logout(): Observable<any>{
    localStorage.removeItem('token');
    this.logged = false;
    return this.httpClient.post(`${this.apiService.getApiUrl()}logout/`, {})
  }

  signUp(username: string, password: string, confirm_password: string, email: string){
    return this.httpClient.post(`${this.apiService.getApiUrl()}signup/`, {username, password, confirm_password, email})
  }


}
