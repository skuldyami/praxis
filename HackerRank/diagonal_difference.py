def diagonalDifference(arr):
  main=0
  second=0
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if i==j:
        main+=arr[i][j]
        second+=arr[i][-j-1]
  return abs(main-second)

if __name__=='__main__':
  n=int(input())
  ar=[]
  for i in range(n):
    ar.append(list(map(int, input().rstrip().split())))
  print(diagonalDifference(ar))