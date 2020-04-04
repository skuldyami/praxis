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
console.log(`fibo is ${prev}`);