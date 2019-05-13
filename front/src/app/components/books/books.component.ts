import { Component, OnInit } from '@angular/core';
import {Book} from "../../shared/django-models";
import {UserDataService} from "../../services/user-data.service";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {CreateDataService} from "../../services/create-data.service";

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.scss']
})
export class BooksComponent implements OnInit {

  public ownBooks: Book[] = [];

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


  constructor(private _formBuilder: FormBuilder, private userDataService: UserDataService, private createDataService: CreateDataService) { }

  ngOnInit() {
    this.userDataService.getOwnBooks().then(res => {
      this.ownBooks = res;
      console.log('!')
    });
  }

  createBook() {
    this.createDataService.createBook(this.firstFormGroup.value['name'],
      this.secondFormGroup.value['author'],
      this.thirdFormGroup.value['year'],
      this.fourthFormGroup.value['category'],
      this.fifthFormGroup.value['genre']).then(res => {this.ownBooks.push(res)});
  }

}
