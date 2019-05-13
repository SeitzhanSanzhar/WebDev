import { Component, OnInit } from '@angular/core';
import {Post} from "../../shared/django-models";
import {UserDataService} from "../../services/user-data.service";
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-home-posts',
  templateUrl: './home-posts.component.html',
  styleUrls: ['./home-posts.component.scss']
})
export class HomePostsComponent implements OnInit {

  public ownPosts: Post[] = [];
  public editId: number;

  firstFormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
  });
  secondFormGroup = new FormGroup({
    author: new FormControl('', Validators.required),
  });
  thirdFormGroup = new FormGroup({
    year: new FormControl('', Validators.required),
  });
  fourthFormGroup = new FormGroup({
    category: new FormControl('', Validators.required),
  });
  fifthFormGroup = new FormGroup({
    genre: new FormControl('', Validators.required)});

  constructor(private userDataService: UserDataService) { }

  ngOnInit() {
    this.editId = -1;
    this.userDataService.getOwnPosts().then(res => {
      this.ownPosts = res;
    });
  }

  makeEditable(id: number) {
    this.editId = id;
  }

}
