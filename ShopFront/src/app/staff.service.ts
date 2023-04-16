import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { User } from './interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class StaffService implements OnInit {
  private apiUrl: string = ""

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { }

  ngOnInit(): void {
    this.apiUrl = this.apiService.getApiUrl() + "staff/"
  }

  getAllStaff(): Observable<User[]>{
    return this.httpClient.get<User[]>(this.apiUrl);
  }

  getStaff(staffID: number): Observable<User>{
    return this.httpClient.get<User>(`${this.apiUrl}${staffID}/`);
  }

  createStaff(username: string, password: string, confirm_password: string, email: string): Observable<any>{
    return this.httpClient.post(this.apiUrl, {username, password, email, confirm_password})
  }

  deleteStaff(user: User): Observable<any>{
    return this.httpClient.delete(`${this.apiUrl}${user.id}/`)
  }
}