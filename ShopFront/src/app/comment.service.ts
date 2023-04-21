import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { Comment } from './interfaces/comment';

@Injectable({
  providedIn: 'root'
})
export class CommentService{

  private apiUrl: string = "";

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) {
    this.apiUrl = this.apiService.getApiUrl() + "products/"
  }

  getComments(productID: number): Observable<Comment[]>{
    return this.httpClient.get<Comment[]>(`${this.apiUrl}${productID}/comments`)
  }

  getComment(productID: number, commentID: number): Observable<Comment>{
    return this.httpClient.get<Comment>(`${this.apiUrl}${productID}/comments/${commentID}/`)
  }

  createComment(productID: number, text: string): Observable<Comment>{
    return this.httpClient.post<Comment>(`${this.apiUrl}${productID}/comments`, {text})
  }

  deleteComment(productID: number, commentID: number){
    return this.httpClient.delete<Comment>(`${this.apiUrl}${productID}/comments/${commentID}/`)
  }
}
