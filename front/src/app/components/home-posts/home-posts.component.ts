import { Component, OnInit } from '@angular/core';
import {Post} from "../../shared/django-models";
import {UserDataService} from "../../services/user-data.service";

@Component({
  selector: 'app-home-posts',
  templateUrl: './home-posts.component.html',
  styleUrls: ['./home-posts.component.scss']
})
export class HomePostsComponent implements OnInit {

  public ownPosts: Post[] = [];

  constructor(private userDataService: UserDataService) { }

  ngOnInit() {
    this.userDataService.getOwnPosts().then(res => {
      this.ownPosts = res;
      console.log('!')
    });
  }

}
