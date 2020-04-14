<<<<<<< HEAD
function reverseArray(arr) {
  const newArr= [];
  for(let ar of arr) {
    newArr.unshift(ar);
  }
  return newArr;
}

function reverseArrayInPlace(arr) {
  let temp;
  for(let i=0; i<arr.length/2; i++){
    temp= arr[arr.length-1-i];
    arr[arr.length-1-i]= arr[i];
    arr[i]=temp;
  }
=======
function reverseArray(arr) {
  const newArr= [];
  for(let ar of arr) {
    newArr.unshift(ar);
  }
  return newArr;
}

function reverseArrayInPlace(arr) {
  let temp;
  for(let i=0; i<arr.length/2; i++){
    temp= arr[arr.length-1-i];
    arr[arr.length-1-i]= arr[i];
    arr[i]=temp;
  }
>>>>>>> 768833c8ac7cd71c8e15cd5e4eb2177fe1f139b5
}