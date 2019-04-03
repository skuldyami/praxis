highest_score=0
results_f=open("results.txt")

for line in results_f:
	if float(line)>highest_score:
		highest_score=float(line)
print("The higher score was: "+str(highest_score))