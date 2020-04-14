//Array to list
function arrayToList(arr) {
  let listLast = {
      value: arr[arr.length-1],
      rest: null
  };

  for(let i=arr.length-2; i>=0; i--) {
    let list = {
      value: arr[i],
      rest: listLast
    };
    listLast= list;
  }
  return listLast;
}

function arrayToList2(arr) { //recursive version
  let list = {
    value: arr[0],
    rest: null
  };
  arrayToListRec(list, arr, 1);
  return list;
}

function arrayToListRec(list, arr, index) {
  let listNew= {
    value: arr[index],
    rest:null
  }

  list.rest= listNew;
  if(index==arr.length-1) { //ending
    return;
  }
  arrayToListRec(listNew, arr, index+1);
}


//List to array
function listToArray(list) {
  let arr=[];

  listToArrayRec(list, arr);
  return arr;
}

function listToArrayRec(list, arr) {
  arr.push(list.value);
  if(list.rest==null){
    return;
  }
  listToArrayRec(list.rest, arr);
}


//prepend
function prepend(elem, list) {
  let listNew= {
    value: elem,
    rest: list
  }

  return listNew;
}

//nth
function nth(list, n) {
  return nthRec(list, n, 0);
}
function nthRec(list, n, index) {
  if(n==index) {
    return list.value;
  }
  if(list.rest==null) {
    return undefined;
  }
  return nthRec(list.rest, n, index+1);
}