scores={}
results_f=open("results.txt")

for line in results_f:
  (name, score)=line.split()      #multiple assignment
  scores[score]=name
results_f.close()

print("The top scores were:")
# for each_score in scores.keys():
for each_score in sorted(scores.keys(), reverse=True):
  print("Surfer " + scores[each_score] + " scored " + each_score)