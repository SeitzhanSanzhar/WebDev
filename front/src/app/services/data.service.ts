import { Injectable } from '@angular/core';
import {Post} from "../shared/django-models";
import {ApiService} from "./api.service";

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private apiService: ApiService) {}

  getPosts(): Promise<Post[]> {
    return this.apiService.get('http://localhost:8000/api/posts/',  {});
  }

}
