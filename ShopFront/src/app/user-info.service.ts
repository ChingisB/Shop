import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { User } from './interfaces/user';
import { UserInfo } from './interfaces/user_info';

@Injectable({
  providedIn: 'root'
})
export class UserInfoService implements OnInit{

  private apiUrl: string = ""

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { }

  ngOnInit(): void {
    this.apiUrl = this.apiService.getApiUrl() + 'user_info/'
  }

  createUserInfo(userInfo: UserInfo): Observable<UserInfo>{
    return this.httpClient.post<UserInfo>(this.apiUrl, userInfo)
  }

  updateUserInfo(userInfo: UserInfo): Observable<UserInfo>{
    return this.httpClient.put<UserInfo>(this.apiUrl, userInfo)
  }

  getUserInfo(): Observable<UserInfo>{
    return this.httpClient.get<UserInfo>(this.apiUrl)
  }
}
