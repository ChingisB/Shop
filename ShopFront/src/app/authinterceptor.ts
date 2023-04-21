import { Injectable } from '@angular/core';
import {
  HttpInterceptor,
  HttpEvent,
  HttpHandler,
  HttpRequest,
  HttpClient,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { ApiConstService } from './api-const.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  private isValid = true;

  constructor(private http: HttpClient, private apiService: ApiConstService) {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    const token = this.getToken()
    if(token){
        req = req.clone({setHeaders: {
        Authorization: `Token ${token}`
      }})
    }
    return next.handle(req)
  }

  public getToken(){
    return localStorage.getItem('token');
  }
}
