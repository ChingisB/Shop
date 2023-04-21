import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductListComponent } from './product-list/product-list.component';
import { ProfileComponent } from "./profile/profile.component";
import {WelcomePageComponent} from "./welcome-page/welcome-page.component";
import {ShoppingCartComponent} from "./shopping-cart/shopping-cart.component";
import {ProductDetailsComponent} from "./product-details/product-details.component";
import {ProfileSettingsComponent} from "./profile-settings/profile-settings.component";
import {OrdersComponent} from "./orders/orders.component";

const routes: Routes = [
  {path: "", component: WelcomePageComponent},
  {path: "products", component: ProductListComponent},
  {path: "products/:productID", component: ProductDetailsComponent},
  {path: "profile", component: ProfileComponent},
  {path: "profile/settings", component: ProfileSettingsComponent},
  {path: "cart", component: ShoppingCartComponent},
  {path: "orders", component: OrdersComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
