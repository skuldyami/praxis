def countApplesAndOranges(s, t, a, b, apples, oranges):
  #code
  num_apples=0
  num_oranges=0
  for a_dist in apples:
    if a+a_dist>=s and a+a_dist<=t:
      num_apples+=1

  for b_dist in oranges:
    if b+b_dist>=s and b+b_dist<=t:
      num_oranges+=1
  print(num_apples)
  print(num_oranges)

if __name__=="__main__":
  st=input().split()
  s=int(st[0])
  t=int(st[1])
  ab=input().split()
  a=int(ab[0])
  b=int(ab[1])
  mn=input().split()
  apples=list(map(int, input().rstrip().split()))
  oranges=list(map(int, input().rstrip().split()))

  countApplesAndOranges(s, t, a, b, apples, oranges)