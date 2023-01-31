class Person{    
    
    name: string;

    
    constructor(name: string){
        this.name = name;
    
    }    
    // define methods it can be anything
    shitPoopFucker(){
        return console.log(this.name)
    }
}  

// now you can create multiple persons with different names from this class 
let createPerson = new Person("Gen");
let cp = new Person("what ever")
let zaion = new Person("Zaion")
createPerson.shitPoopFucker()

zaion.shitPoopFucker();