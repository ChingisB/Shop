import { Component } from '@angular/core';
import {UserService} from "../user.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  constructor(private router: Router, private userService: UserService) {
  }
  logOut(){
    this.userService.logout().subscribe(user=>{
    })
    this.router.navigateByUrl("")
  }
  toSettings(){
    this.router.navigateByUrl("profile/settings")
  }
}
