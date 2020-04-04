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
