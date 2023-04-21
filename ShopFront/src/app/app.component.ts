import { Component } from '@angular/core';
import {ProductService} from "./product.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ShopFront';

  constructor(private productService: ProductService) {

  }

  writeProduct(){
    try {
      this.productService.getProduct(2).subscribe(product => {
        console.log(product)
      })
    }
    catch (error){
      console.log(error)
    }
  }
}
