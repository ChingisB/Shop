import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { Cart } from './interfaces/cart';
import { CreateCart } from './interfaces/create_cart';

@Injectable({
  providedIn: 'root'
})
export class CartService implements OnInit {

  private apiUrl: string = "";

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { }

  ngOnInit(): void {
    this.apiUrl = this.apiService.getApiUrl() + "cart/"
  }

  getCart(): Observable<Cart>{
    return this.httpClient.get<Cart>(this.apiUrl)
  }

  createCart(cart: CreateCart): Observable<Cart>{
    return this.httpClient.post<Cart>(this.apiUrl, cart)
  }
}
