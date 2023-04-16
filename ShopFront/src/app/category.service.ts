import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { Category } from './interfaces/category';

@Injectable({
  providedIn: 'root'
})
export class CategoryService implements OnInit{

  private apiUrl: string = ""

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { }

  ngOnInit(): void {
    this.apiUrl = this.apiService.getApiUrl() + "category/"
  }

  getCategories(): Observable<Category[]>{
    return this.httpClient.get<Category[]>(this.apiUrl)
  }

  getVendor(categoryID: number): Observable<Category>{
    return this.httpClient.get<Category>(`${this.apiUrl}${categoryID}/`)
  }

  createVendor(category: Category): Observable<Category>{
    return this.httpClient.post<Category>(this.apiUrl, category)
  }

  updateVendor(category: Category): Observable<Category>{
    return this.httpClient.put<Category>(`${this.apiUrl}${category.id}/`, category)
  }

  deleteVendor(category: Category): Observable<any>{
    return this.httpClient.delete(`${this.apiUrl}${category.id}/`)
  }
}
