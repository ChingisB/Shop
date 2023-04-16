import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UserWithToken } from './interfaces/userwithtoken';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService implements OnInit{

  private user: UserWithToken = <UserWithToken>{};
  private static apiUrl = "http://127.0.0.1:8000";
  logged: boolean = false;

  ngOnInit(){
    const token = localStorage.getItem("token")
    if(token){
      this.logged = true
    }

  }

  constructor(private httpClient: HttpClient) { }

  login(username: String, password: String): Observable<UserWithToken> {
    return this.httpClient.post<UserWithToken>(`${UserService.apiUrl}/login/`, {"username": username, "password": password})
      .pipe(
        tap(user => {
          localStorage.setItem("token", user.token)
          this.user = user;
        })
      );
  }

  getUserInfo(): UserWithToken {
    return this.user;
  }


}
