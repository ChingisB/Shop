import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-welcome-page',
  templateUrl: './welcome-page.component.html',
  styleUrls: ['./welcome-page.component.css']
})
export class WelcomePageComponent implements OnInit{
  toLogin(): void{
    let login = document.querySelector('app-login')
    let newAcc = document.querySelector('app-new-acc')
    // @ts-ignore
    newAcc.setAttribute('style', 'display: none')
    // @ts-ignore
    login.setAttribute('style', 'display: block')
  }
  toNewAcc(): void{
    let login = document.querySelector('app-login')
    let newAcc = document.querySelector('app-new-acc')
    // @ts-ignore
    newAcc.setAttribute('style', 'display: block')
    // @ts-ignore
    login.setAttribute('style', 'display: none')
  }
  ngOnInit(): void{
    this.toLogin()
  }
}
