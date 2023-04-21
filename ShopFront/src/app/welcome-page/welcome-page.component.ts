import {Component, OnInit} from '@angular/core';
import {UserService} from "../user.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-welcome-page',
  templateUrl: './welcome-page.component.html',
  styleUrls: ['./welcome-page.component.css']
})
export class WelcomePageComponent implements OnInit{
  private WelcomeMode: string | undefined;

  constructor(private userService: UserService, private router: Router) {}
  ngOnInit(): void{
    if(localStorage.getItem("token")){
      this.router.navigateByUrl("/products")
    }
    this.toLogin()
    this.WelcomeMode = "Login"
  }
  toLogin(): void{
    this.WelcomeMode="Login"
  }
  toNewAcc(): void{
    this.WelcomeMode="NewAcc"
  }

  getMode(){
    return this.WelcomeMode
  }
}
