// 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 
// interface for company accounts
interface account{

  // account interface properties
  username: string;
  password: string;
  password_hints: string;
}

// employee class
class employee{
  
  // emp properties
  name: string;
  employee_id: string;
  age?: number;
  job_postition: string;
  salary: number;
  
  // constructor
  constructor(name: string, employee_id: string, job_postition: string, salary: number, age?: number,){
    
    // constructor variables
    this.name = name;
    this.employee_id = employee_id
    this.salary = salary;
    this.job_postition = job_postition;
    this.age = age;
  }

  // class methods
  Taxes(taxdue: number, deposited: number){
    // employee tax method
    console.log(`${this.name} owes ${taxdue} and has depsoited ${deposited} into the tax bill for the company.`)
  }

  CreateAccount(){
    

    // employee creates account for Genesis corp.
    let username = prompt(`Enter your username for Genesis Corp.`)
    console.log(`The username ${username} has been created!`)
    let password = prompt(`Enter your password for Genesis Corp.`)
    console.log(`The password ${password} has been created!`)
  }

  Signin(){

    // employee signs into the company account with credentials
    console.log(`Welcome to the Genesis`)
    
    // username credentials prompt
    console.log(`Enter your username`)
    let username_r = prompt(`Enter your company username >`)
    
    // password credentials prompt
    console.log(`Enter your username`)
    let password_r = prompt(`Enter your company password >`)
  }
}
// object instances/intializers
const genesis = new employee('GenesisGir', '001', 'Programmer', 15000, 19)

// 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 

