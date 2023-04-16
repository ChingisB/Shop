import { Component } from '@angular/core';
import { UserService } from '../user.service';
import {WelcomePageComponent} from "../welcome-page/welcome-page.component";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(public welcomePageComponent: WelcomePageComponent, 
    private userService: UserService) {
  }
  email: string = ''
  password: string = ''

  onSubmit() {
      this.userService.login(this.email, this.password).subscribe(
        user => {
          alert(user.token)
        }
      )
  }
}
