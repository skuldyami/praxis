let countChar= (strText, character)=> {
  let charCount=0;
  for(let i=0; i<strText.length; i++){
    if(strText[i]==character) {
      charCount++;
    }
  }
  return charCount;
};