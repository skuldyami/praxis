from random import randint

print("Welcome!")
secret=randint(1,10)
guess=secret+1
while guess != secret:
	g= input("Guess a number: ")
	guess= int(g)	
	if guess==secret:
		print("You win!")
	elif guess<secret:
		print("Too low!")
	else:
		print("Too high!")
print("Game over!")