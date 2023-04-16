import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiConstService } from './api-const.service';
import { Vendor } from './interfaces/vendor';

@Injectable({
  providedIn: 'root'
})
export class VendorService implements OnInit {
  private apiUrl: string = ""

  constructor(private httpClient: HttpClient, private apiService: ApiConstService) { }

  ngOnInit(): void {
    this.apiUrl = this.apiService.getApiUrl() + 'vendor/';
  }

  getVendors(): Observable<Vendor[]>{
    return this.httpClient.get<Vendor[]>(this.apiUrl)
  }

  getVendor(vendorID: number): Observable<Vendor>{
    return this.httpClient.get<Vendor>(`${this.apiUrl}${vendorID}/`)
  }

  createVendor(vendor: Vendor): Observable<Vendor>{
    return this.httpClient.post<Vendor>(this.apiUrl, vendor)
  }

  updateVendor(vendor: Vendor): Observable<Vendor>{
    return this.httpClient.put<Vendor>(`${this.apiUrl}${vendor.id}/`, vendor)
  }

  deleteVendor(vendor: Vendor): Observable<any>{
    return this.httpClient.delete(`${this.apiUrl}${vendor.id}/`)
  }
}
