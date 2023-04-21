import { Component, OnInit } from '@angular/core';
import { ProductService} from "../product.service";
import { Product} from "../interfaces/product";

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  productList: Product[] = [];

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
    this.productService.getProducts().subscribe(product => {
      this.productList = product
    })
  }
  getProducts() {
    this.productService.getProducts().subscribe(products => {
      this.productList = products;
    });
  }
  getToken(){
    return localStorage.getItem("token")
  }
}
