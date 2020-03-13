from random import randint
print("よこそ")
secret= randint(1, 50)
guess= secret+1

while guess!=secret:
  guess=int(input("Make a guess? "))
  if guess==secret:
    print("Yo! You won this shit")
  elif guess>secret:
    print("Way too high!!")
  else:
    print("Too low!")
print("ゲームオーバー!")