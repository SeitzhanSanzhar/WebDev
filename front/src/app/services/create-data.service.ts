import { Injectable } from '@angular/core';
import {ApiService} from "./api.service";
import {HttpClient} from "@angular/common/http";
import {Book} from "../shared/django-models";

@Injectable({
  providedIn: 'root'
})
export class CreateDataService extends ApiService {

  constructor(http: HttpClient) {super(http); }


  createBook(name: any, author: any, year: any, category: any, genre: any): Promise<Book> {
    return this.post('http://localhost:8000/api/books/', {name, author, year, category, genre})
  }

}
