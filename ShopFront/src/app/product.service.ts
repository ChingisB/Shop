import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { Product } from './interfaces/product';
import { ProductDetails } from './interfaces/product-details';

@Injectable({
  providedIn: 'root'
})
export class ProductService implements OnInit{

  private apiUrl: string = "";

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { }

  ngOnInit(): void {
    this.apiUrl = this.apiService.getApiUrl() + "products/"
  }

  like(productID: number){
    return this.httpClient.post(`${this.apiUrl}${productID}/likes/`, {})
  }

  dislike(productID: number){
    return this.httpClient.delete(`${this.apiUrl}${productID}/likes/`, {})
  }

  getLikedProducts(): Observable<Product[]>{
    return this.httpClient.get<Product[]>(`${this.apiUrl}/liked/`)
  }

  getProducts(page="", name="", sorting="", 
              order="", min_price="", max_price="", 
              category="", vendor=""): Observable<Product[]>{

    return this.httpClient.get<Product[]>(`${this.apiUrl}?page=${page}&name=${name}&sorting=${sorting}&order=${order}&min_price=${min_price}&max_price=${max_price}&category=${category}&vendor=${vendor}`)
  }

  getProduct(productID: number): Observable<Product>{
    return this.httpClient.get<Product>(`${this.apiUrl}${productID}/`)
  }

  createProduct(name: string, 
                description: string, category_id: number, 
                vendor_id: number, quantity: number, price: number, images: File[]): Observable<ProductDetails>{
    const data = new FormData();
    data.append('product_info', JSON.stringify({name, description, vendor_id, category_id, quantity, price}));
    for (let file of images){
      data.append(`image${file.name}`, file, file.name)
    }
    return this.httpClient.post<ProductDetails>(this.apiUrl, data)
  }

  updateProduct(product_id: number, name: string, 
    description: string, category_id: number, 
    vendor_id: number, quantity: number, price: number): Observable<ProductDetails>{
    return this.httpClient.post<ProductDetails>(`${this.apiUrl}${product_id}`, {name, description, vendor_id, category_id, quantity, price})
  }

  deleteProduct(product_id: number){
    return this.httpClient.delete(`${this.apiUrl}${product_id}`)
  }

  giveRating(product_id: number, rating: number){
    try{
      return this.httpClient.put(`${this.apiUrl}${product_id}`, {rating})
      
    }
    catch{
      return this.httpClient.post(`${this.apiUrl}${product_id}`, {rating})
    }
  }
}
