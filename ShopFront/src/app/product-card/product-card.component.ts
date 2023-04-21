import {Component, Input, OnInit} from '@angular/core';
import {Product} from "../interfaces/product";
import {Router} from "@angular/router";

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css']
})
export class ProductCardComponent{
  @Input() product : Product = <Product>{};

  constructor(private router: Router) {}

  reformatImage(imageURL: string): string{
    return imageURL.replace("92.47.4.210:59001","127.0.0.1")
  }

  toDetails(){
    this.router.navigateByUrl('/products/'+this.product.id);
  }
  addToCart(event: Event){
    event.stopPropagation();
    alert("go to cart")
  }
}
