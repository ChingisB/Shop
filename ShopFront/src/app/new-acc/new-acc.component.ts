import { Component } from '@angular/core';
import {WelcomePageComponent} from "../welcome-page/welcome-page.component";
import {UserService} from "../user.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-new-acc',
  templateUrl: './new-acc.component.html',
  styleUrls: ['./new-acc.component.css']
})
export class NewAccComponent {
  constructor(public welcomePageComponent: WelcomePageComponent,
              private userService: UserService, private router: Router) {
  }
  username: string = "";
  email: string = "";
  password: string = "";
  passwordCopy: string = "";
  onSubmit() {
    if(this.password===this.passwordCopy){
      this.userService.signUp(this.username, this.password, this.passwordCopy, this.email).subscribe(
        user => {
          this.userService.login(this.email, this.password)
          this.router.navigateByUrl('/products');
        },
        error => {
          console.error(error);
          alert("such user already exists or some field is empty");
        })
    }else{
      alert("Passwords does not match")
    }
  }
}
