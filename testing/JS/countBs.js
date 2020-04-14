let countBs= strText=> {
  let bCount=0;
  for(let i=0; i<strText.length; i++){
    if(strText[i]=="B") {
      bCount++;
    }
  }
  return bCount;
};