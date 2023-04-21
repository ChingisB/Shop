import {Component, OnInit} from '@angular/core';
import {Cart} from "../interfaces/cart";
import {CartService} from "../cart.service";

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.css']
})
export class ShoppingCartComponent implements OnInit{
  cart : Cart = <Cart>{};

  constructor(private cartService: CartService) {}

  ngOnInit() {
    this.cartService.getCart().subscribe(cart => {
      this.cart=cart;
      }
    );
  }
}
