import sys

def multiples_3_5(num):
  sum=0
  for i in range(1, num):
    if i%3==0 or i%5==0:
      sum+=i
  return sum

if __name__ == '__main__':
  print(multiples_3_5(int(sys.argv[1])))