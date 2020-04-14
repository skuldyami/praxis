<<<<<<< HEAD
let strChar='#';
let res='';
let size=8;
let count=0;
for(let i=0; i<size; i++){
  for(let j=0; j<size; j++){
    res=(i%2==0)?((j%2==0)?res+=' ':res+=strChar):(j%2==0)?res+=strChar:res+=' ';
    count++;
  }
  console.log(res);
  res='';
}
=======
let strChar='#';
let res='';
let size=8;
for(let i=0; i<size; i++){
  for(let j=0; j<size; j++){
    res=(i%2==0)?((j%2==0)?res+=' ':res+=strChar):(j%2==0)?res+=strChar:res+=' ';
  }
  console.log(res);
  res='';
}
>>>>>>> 768833c8ac7cd71c8e15cd5e4eb2177fe1f139b5
