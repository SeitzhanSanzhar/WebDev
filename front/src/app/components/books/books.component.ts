import { Component, OnInit } from '@angular/core';
import {Book} from "../../shared/django-models";
import {UserDataService} from "../../services/user-data.service";

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.scss']
})
export class BooksComponent implements OnInit {

  public ownBooks: Book[] = []


  constructor(private userDataService: UserDataService) { }

  ngOnInit() {
    this.userDataService.getOwnBooks().then(res => {
      this.ownBooks = res;
      console.log('!')
    });
  }

}
