def miniMaxSum(arr):
  arr.sort()
  num_1=arr[0]+arr[1]+arr[2]+arr[3]
  num_2=arr[1]+arr[2]+arr[3]+arr[4]
  print("{} {}".format(num_1, num_2))

if __name__=="__main__":
  arr=list(map(int, input().rstrip().split()))
  miniMaxSum(arr)