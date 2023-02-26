// interface
interface Person {
  
  // properties
  name: string;
  sex?: string;
  age?: number;
  job?: string;
}

interface job {
  
  // properties
  position: string
  salary?: string;
}

// job array
const jobs = [
  
  // job positions
  'back-end programer',
  'front-end programmer'
];

// salaries
const salary = ['$100,000', '$112,000', '$150,000', '$170,000'];

// employee class
class Emp{
  
  // employee properties
  public name: Person;
  public age?: number;
  public job: job;
  public salary?: string;

  // emp constructor
  constructor(name: Person, job: job, age?: number, salary?: string) {
    
    //  constructor variables
    this.name = name;
    this.age = age;
    this.job = job;
    this.salary = salary;
  }
  
  // class methods
  public static EmpName(employee_name: string){ // return employee name
    
    // return employee name
    console.log(`${employee_name}`);
  }

  public static Job(position: job) {
    
    // return employee job
    console.log(`${this.name}'s job within the company is ${this.Job}`);
  }
}

// object instances
let genesisgir = new Emp({'name': 'GenesisGir'}, {'position': jobs[1]}, undefined, salary[0])

// log message
console.log(`The salary of ${genesisgir.name.name} is ${genesisgir.salary} and his job position is a ${genesisgir.job.position} `)

// function calls
Emp.EmpName(genesisgir.name.name)