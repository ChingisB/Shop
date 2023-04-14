import { Component } from '@angular/core';
import {WelcomePageComponent} from "../welcome-page/welcome-page.component";

@Component({
  selector: 'app-new-acc',
  templateUrl: './new-acc.component.html',
  styleUrls: ['./new-acc.component.css']
})
export class NewAccComponent {
  constructor(public welcomePageComponent: WelcomePageComponent) {
  }
  email: string | undefined;
  password: string | undefined;
  passwordCopy: string | undefined;
  onSubmit() {
    alert(`Signing in with email ${this.email} and password ${this.password} and copy of password ${this.passwordCopy}`)
  }
}
