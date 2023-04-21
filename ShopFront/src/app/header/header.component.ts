import { Component } from '@angular/core';
import {WelcomePageComponent} from "../welcome-page/welcome-page.component";
import {UserService} from "../user.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  constructor(private router: Router) {}
  toHome(){
    this.router.navigateByUrl('/products');
  }
  toCart(){
    this.router.navigateByUrl('/cart');
  }
  toProfile(){
    this.router.navigateByUrl('/profile');
  }
  toOrders(){
    this.router.navigateByUrl('/orders');
  }
}
