import * as moment from 'moment';
import _date = moment.unitOfTime._date;

export interface IAuthResponse {
    token: string;
}

export class Contact {
  id: number;
  name: string;
  phone: string;
  createdby: number;
}

export class User {
  id: number;
  username: string;
  email: string;
}

export class Book {
  name: string;
  year: number;
  author: string;
  genre: string;
}

export class Post {
  id: number;
  title: string;
  body: string;
  created_by: User;
  book_info: Book;
  created_at: string;
}
