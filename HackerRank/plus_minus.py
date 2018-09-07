def plusMinus(arr):
  pos=0
  neg=0
  zeros=0
  for i in range(len(arr)):
    if arr[i]>0:
      pos+=1
    elif arr[i]<0:
      neg+=1
    else:
      zeros+=1
  print("{:.6f}".format(float(pos)/len(arr)))
  print("{:.6f}".format(float(neg)/len(arr)))
  print("{:.6f}".format(float(zeros)/len(arr)))

if __name__=="__main__":
  n=int(input())
  arr=list(map(int, input().rstrip().split()))

  plusMinus(arr)