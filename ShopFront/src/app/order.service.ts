import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { CreateOrder, Order } from './interfaces/create_order';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  
  private apiUrl: string = "";

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { 
    this.apiUrl = this.apiService.getApiUrl() + "orders/"
  }

  getOrders(): Observable<Order[]>{
    return this.httpClient.get<Order[]>(this.apiUrl)
  }

  getOrder(orderID: number): Observable<Order>{
    return this.httpClient.get<Order>(`${this.apiUrl}${orderID}/`)
  }

  createOrder(createOrder: CreateOrder): Observable<Order>{
    return this.httpClient.post<Order>(this.apiUrl, createOrder)
  }
}
