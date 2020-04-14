<<<<<<< HEAD
let num=Number(prompt("Choose to fibo"));
let prev=0;
let after=1;
let counter=0;
let temp;
while(counter < num){  
  temp=after;
  after=prev+after;
  prev=temp;
  counter=counter+1;
}
=======
let num=Number(prompt("Choose to fibo"));
let prev=0;
let after=1;
let counter=0;
let temp;
while(counter < num){  
  temp=after;
  after=prev+after;
  prev=temp;
  counter=counter+1;
}
>>>>>>> 768833c8ac7cd71c8e15cd5e4eb2177fe1f139b5
console.log(`fibo is ${prev}`);