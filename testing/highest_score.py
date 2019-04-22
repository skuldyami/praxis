name=""
score="0"
highest_score=0
scores=[]
results_f=open("results.txt")

for line in results_f:
  (name, score)=line.split()      #multiple assignment
  scores.append(float(score))
  # if float(score)>highest_score:
  #   highest_score=float(score)
# print("The higher score was: "+str(highest_score))
# scores.sort()
# scores.reverse()
scores.sort(reverse=True)
print(scores[0])
print(scores[1])
print(scores[2])
results_f.close()