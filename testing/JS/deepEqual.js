function deepEqual(val1, val2){
  if(typeof val1=='object' && typeof val2=='object'){ //objects
    if(val1!==null && val2!==null){ //not null objects
      let val1Keys=Object.keys(val1);
      let val2Keys=Object.keys(val2);
      if(val1Keys.length==val2Keys.length){ //same length properties
        let booley= true;
        let i=0;
        while(booley && i<val1Keys.length){
          booley= deepEqual(val1Keys[i],val2Keys[i]) //equal keys
                 && deepEqual(val1[val1Keys[i]],val2[val2Keys[i]]); //equal values
          i++;
        }
        return booley;

        // for(let i=0; i<val1Keys.length; i++){
        //   booley= deepEqual(val1Keys[i],val2Keys[i]) //equal keys
        //          && deepEqual(val1[val1Keys[i]],val2[val2Keys[i]]); //equal values
        //   if(!booley){
        //     return false;
        //   }
        // }
        // return true;
      }
      return false;
    }else if(val1===null && val2===null){
      return true;
    }else{
      return false;
    }
    return true; //testing
  }else if(typeof val1!='object' && typeof val2!='object'){ //not objects - values
    if(val1!==null && val2!==null){ //not null values
      if(val1===val2){
        return true;
      }
      return false;
    }else if(val1===null && val2===null){
      return true;
    }else{
      return false;
    }
  } else {
    return false;
  }
}