import { Component } from "@angular/core";

@Component({
  selector: 'blob-app',
  templateUrl: './blob.component.html',
  styleUrls: ['./blob.component.css']
})

export class BlobComponent{
  
  // variables
  UserInput = '';
  Array: string[] = [];
  Items:any;
  
  // button methods
  SubmitToArray(){

    if(this.Array.includes(this.UserInput)){
     alert("This items allready exist in the array")
      
    }else if(this.UserInput == ''){
      
      alert("input field is empty")
      
    }else{

      this.Array.push(this.UserInput)
    }
  }

  ShowArray(){
    if(this.Array == null || this.Array.length <= 0){
      alert("Array is empty")
    }else{

      this.Items = this.Array
    }
  }
}