import { Component } from '@angular/core';
import {WelcomePageComponent} from "../welcome-page/welcome-page.component";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(public welcomePageComponent: WelcomePageComponent) {
  }
  email: string | undefined;
  password: string | undefined;
  onSubmit() {
    alert(`Signing in with email ${this.email} and password ${this.password}`)
  }
}
