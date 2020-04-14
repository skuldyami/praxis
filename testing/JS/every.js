function every(array, test){
  for(let elem of array){
    if(!test(elem)){
      return false;
    }
  }
  return true;
}


function every2(array, test){
  let negateTest= n=> !test(n); //hard as shit to come up with that, tried to negate it in the wrong places
  if(array.some(negateTest)){
    return false;
  }
  return true;
}