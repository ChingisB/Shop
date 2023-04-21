import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../user.service';
import {WelcomePageComponent} from "../welcome-page/welcome-page.component";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(public welcomePageComponent: WelcomePageComponent,
    private userService: UserService, private router: Router) {
  }
  username: string = ''
  password: string = ''

  onSubmit() {
    this.userService.login(this.username, this.password).subscribe(
    user => {
        this.router.navigateByUrl('/products');
      },
      error => {
        console.error(error);
        alert("wrong login or password");
      })
  }
}
