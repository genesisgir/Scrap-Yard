import { Component } from "@angular/core";

@Component({

  selector:'fuck-app',
  templateUrl: './fuck.component.html',
  styleUrls: ['./fuck.component.css']
})

export class FuckerComponent{
  
  // var properties
  Input = '';
  password = '';
  LoginMessage = '';

  // methods
  Login(){
  
    // overwrite password property
  this.password = 'Genesis123'

  // flow control
  if (this.Input == this.password){

    this.LoginMessage = 'Access Has been granted!';
    console.log("Access Granted!") // the user has logged in
  }
  else if(this.Input != this.password){ // user has been rejected access to web-api server

    this.LoginMessage = 'Access Has been denied!';
    console.log("Access Denied!")
  }

  else {
    null;
  }
  }
  }
