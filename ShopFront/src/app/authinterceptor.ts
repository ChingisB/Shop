import { Injectable } from "@angular/core"
import { HttpInterceptor, HttpEvent, HttpHandler} from "@angular/common/http"
import { HttpRequest, HttpResponse, HttpErrorResponse} from "@angular/common/http"
import { Observable, tap} from "rxjs"

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor() {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    const token = localStorage.getItem("token")
    if(token){
        const authReq = req.clone({
            headers: req.headers.set('Authorization', `Token ${token}`),})
        return next.handle(authReq)
    }

    return next.handle(req)
  }
}