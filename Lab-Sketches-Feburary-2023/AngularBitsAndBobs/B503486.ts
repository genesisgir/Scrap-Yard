//function number(numx, numy, numz) {
//    // return mathematical expression
//    return numx + numy + numz;
//}
//console.log(number(5, 87, 5));


//function combinestr(word01, word02){
//
//  return console.log(`${word01} ${word02}`);
//}
//
//combinestr(`Hello`, `GenesisGir`);

function CreateAccount(user_parm: string, password_parm: string){

  // username account create
  let username = user_parm

  // password account create
  let password = password_parm
  
  // account credential prompts
  let respusername = prompt(`Enter your Account username >`)
  let resppassword = prompt(`Enter your Account password >`)

  // save responses within a array
  const AccountData = [respusername, resppassword];

  // account creation conditions
  if(AccountData[0] === username && AccountData[1] === password){

    console.log(`Access granted ${username}!`) // correct account values
  }
  else{ // user entered incorrect credentials 
    console.log(`Access Denied!`);
  }
}

// function call with postional arguments being sent to the params
CreateAccount(`Genesis`, `Apple`)