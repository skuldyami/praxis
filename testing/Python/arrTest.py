def arrTest(arr):
  arr= [4,5,6] #reference reassigned, NOT POSSIBLE WITHOUT POINTERS(C, C++)
  print("inside reference: " + str(arr))
arrei= [1,2,3]
print("before: "+ str(arrei))
arrTest(arrei)
print("after:" + str(arrei))