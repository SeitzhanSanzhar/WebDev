import { Component, OnInit } from '@angular/core';
import {LoginService} from "../../services/login.service";

import {Router} from '@angular/router';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private router: Router, private service: LoginService) { }

  username: string;
  password: string;
  loginState: boolean = false;

  ngOnInit() {
  }

  login() {
    if (this.username !== '' && this.password !== '') {
      this.service.login(this.username, this.password).then(res => {localStorage.setItem('token', res.token);
        this.loginState = true;
        this.router.navigate(['home']);
      });
    }
  }

  logout() {
    this.service.logout().then(res => {
      localStorage.clear();
      this.loginState = false;
    });
  }

}

