def timeConversion(st):
  if st[-2:]=="AM":
    if st[:2]!="12":
      print(st[:-2])
    else:
      print("00"+st[2:-2])
  else:
    if st[:2]!="12":
      print(str(int(st[:2])+12)+st[2:-2])
    else:
      print(st[:-2])

if __name__=="__main__":
  st=input()

  timeConversion(st)