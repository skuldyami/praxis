import sys
import math

def is_prime(x):
  if x<=1:
    return False

  for num in range(2, int(math.sqrt(abs(x)))+1):
    if x%num==0:
      return False
  return True

if __name__=="__main__":
  print(is_prime(int(sys.argv[1])))