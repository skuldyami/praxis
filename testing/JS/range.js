function range(start, end, step=1) {
  const arr=[];
  if(step > 0) {    
    for(let i=start; i<=end; i+=step){
      arr.push(i);
    }
  } else {
    for(let i=start; i>=end; i+=step){
      arr.push(i);
    }
  }

  return arr;
}

function sum(arr) {
  let s=0;
  for(let ar of arr) {
    s+=ar
  }
  return s;
}