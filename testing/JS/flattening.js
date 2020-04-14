function flattening(listOfList){
  return listOfList.reduce((elem_A, elem_B)=>{return elem_A.concat(elem_B);});
  // return listOfList.reduce((elem_A, elem_B)=> elem_A.concat(elem_B)); // also valid
}