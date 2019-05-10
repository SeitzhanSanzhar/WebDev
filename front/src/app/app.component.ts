import { Component, OnInit } from '@angular/core';
import { BackendApiService } from './services/backend-api.service';
import {Book, Contact, Post} from './models';
import { HttpClient, HttpParams } from '@angular/common/http';
import { INT_TYPE } from '@angular/compiler/src/output/output_ast';
import { AngularWaitBarrier } from 'blocking-proxy/built/lib/angular_wait_barrier';
import {log} from 'util';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'todo-front';
  public posts: Post[] = [];
  public logged = false;
  public newtitle: string;
  public newbody: string;
  public newname: string;
  public newphone: string;
  public currentuser: number;
  public editId: number;
  public login: any = '';
  public password: any = '';
  public loading = false;
  constructor(private apiService: BackendApiService) {
  }

  ngOnInit() {
    const token = localStorage.getItem('token');
    this.editId = -1;
    if (token) {
      this.logged = true;
    }
    if (this.logged) {
      this.apiService.getPostList().then(res => {
        this.posts = res;
        setTimeout(() => {
          this.loading = true;
        }, 2000);
      });
    }
  }

  putDetailPost(post: Post) {
    this.apiService.putDetailPost(post);
    alert('done:)');
    this.editId = -1;
  }
  deleteItem(value) {
    this.apiService.deleteTaskList(value);
    for (let i = 0 ; i <= this.posts.length; i++) {
      if (value === this.posts[i]) {
       this.posts.splice(i, 1);
      }
    }
  }
  makeEditable(id) {
    this.editId = id;
  }
  auth() {
    if (this.login !== '' && this.password !== '') {
      this.apiService.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.currentuser = 1;
        this.apiService.getPostList().then(r => {
          this.posts = r;
          setTimeout(() => {
            this.loading = true;
          }, 2000);
        });

      });
    }
  }
  newPost() {
    // if ((this.newtitle === ' ' || this.newbody === ' ')) { return; }
    // const newPost = new Post();
    // newPost.title = this.newtitle;
    // newPost.body = this.newbody;
    // const book = new Book();
    // book.name = 'a';
    // book.author = 'a';
    // book.year = 2007;
    // book.genre = 'a';
    // newPost.book_info = book;
    // newPost.created_by = 1;
    //
    // this.apiService.createPost(newPost).then( res => {
    //         this.posts.push(res);
    //         alert('done:)');
    // });
    // this.posts.push(newPost);
  }
  // newContact() {
  //   if (this.newname !== '' && this.newphone !== '') {
  //     const contact = new Contact();
  //     contact.name = this.newname;
  //     contact.phone = this.newphone;
  //     contact.createdby = this.currentuser;
  //     this.apiService.createPost(contact).then( res => {
  //       this.posts.push(res);
  //     });
  //     // this.contacts.push(contact);
  //     alert('done:)');
  //   }
  // }
  logout() {
    this.apiService.logout().then(res => {
      localStorage.clear();
      this.logged = false;
    });
  }
}
