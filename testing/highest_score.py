name=""
score="0"
highest_score=0
results_f=open("results.txt")

for line in results_f:
  (name, score)=line.split()      #multiple assignment
  if float(score)>highest_score:
    highest_score=float(score)
print("The higher score was: "+str(highest_score))