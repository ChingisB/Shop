import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { PaymentInfo } from './interfaces/payment_info';

@Injectable({
  providedIn: 'root'
})
export class PaymentService {

  private apiUrl: string = "";

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { 
    this.apiUrl = apiService.getApiUrl() + "payment_info/"
  }

  getPaymentInfo(): Observable<PaymentInfo>{
    return this.httpClient.get<PaymentInfo>(this.apiUrl)
  }

  createPaymentInfo(payment_type: string, provider: string, account_no: string, expiry: Date): Observable<PaymentInfo>{
    return this.httpClient.post<PaymentInfo>(this.apiUrl, {payment_type, provider, account_no, expiry})
  }
}
