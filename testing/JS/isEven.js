<<<<<<< HEAD
isEven= number=> {
  if(number<0){
    number= -number;
  }
  if(number==0) {
    return true;
  }
  if(number==1) {
    return false;
  }
  return isEven(number -2);
=======
isEven= number=> {
  if(number<0){
    number= -number;
  }
  if(number==0) {
    return true;
  }
  if(number==1) {
    return false;
  }
  return isEven(number -2);
>>>>>>> 768833c8ac7cd71c8e15cd5e4eb2177fe1f139b5
};