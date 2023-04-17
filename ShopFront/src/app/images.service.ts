import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { Image } from './interfaces/image';

@Injectable({
  providedIn: 'root'
})
export class ImagesService {

  private apiUrl: string = "";

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { 
    this.apiUrl = this.apiService.getApiUrl() + "images/"
  }

  getImages(): Observable<Image[]>{
    return this.httpClient.get<Image[]>(this.apiUrl)
  }

  getImage(image_id: number): Observable<Image>{
    return this.httpClient.get<Image>(`${this.apiUrl}${image_id}/`)
  }

  createImages(product_id: number, images: File[]){
    const data = new FormData();
    for (let file of images){
      data.append(`image${file.name}`, file, file.name)
    }
    return this.httpClient.post(`${this.apiUrl}${product_id}/`, data)
  }

  changeImage(image_id: number, file: File){
    const data = new FormData();
    data.append(`image${file.name}`, file, file.name)
    return this.httpClient.put(`${this.apiUrl}${image_id}/`, data)
  }
}
