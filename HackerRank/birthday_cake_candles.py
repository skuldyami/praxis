import sys

def birthdayCakeCandles(ar):
  mp={}
  mx=ar[0]
  for item in ar:
    if item in mp:
      mp[item]+=1
    else:
      mp[item]=1
    if item>mx:
      mx=item
  return mp[mx]


if __name__=="__main__":
  n=int(input())
  arr=list(map(int, input().rstrip().split()))
  print(birthdayCakeCandles(arr))