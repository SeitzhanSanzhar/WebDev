export interface Token {
  token: string;
}

export interface Book {
  id: number;
  author: string;
  name: string;
  year: number;
  category: string;
  genre: string;
}

export interface Post {
  id: number;
  title: string;
  body: string;
  created_at: Date;
  user: number;
}


