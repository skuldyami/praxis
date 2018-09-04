def simpleArraySum(ar):
  sum=0
  for a in ar:
    sum+=a
  return sum

if __name__=='__main__':
  ar_test=[6, 3, 4, 3]
  print(simpleArraySum(ar_test))