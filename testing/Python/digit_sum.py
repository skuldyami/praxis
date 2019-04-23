import sys

def digit_sum(x):
  result=0
  digit=0
  while(x>=1):
    digit=x%10
    result+=digit
    x=x//10
  return result

if __name__=="__main__":
  print(digit_sum(int(sys.argv[1])))