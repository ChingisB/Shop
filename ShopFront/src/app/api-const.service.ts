import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiConstService {
  private apiUrl = "http://127.0.0.1:8000/"
  constructor() { }


  getApiUrl(): string{
    return this.apiUrl;
  }
}
