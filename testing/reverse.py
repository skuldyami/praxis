def reverse(text):
  st=list(text)
  for i in range(len(text)//2):
    st[i]=text[-i-1]
    st[-i-1]=text[i]
  return "".join(st)

if __name__=="__main__":
  print(reverse("string"))