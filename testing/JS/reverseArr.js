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
}