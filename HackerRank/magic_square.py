def isMagicMatrix(s):
  magic_sum=s[0][0]+s[0][1]+s[0][2] #arbitrary sum
  #diagonals
  r_diagonal=s[0][0]+s[1][1]+s[2][2]
  l_diagonal=s[-1][-1]+s[-2][-2]+s[-3][-3]
  if r_diagonal!=magic_sum or l_diagonal!=magic_sum:
    return False
  #rows&columns
  for i in range(len(s)):
    r_sum=s[i][0]+s[i][1]+s[i][2]
    c_sum=s[0][i]+s[1][i]+s[2][i]
    if r_sum!=magic_sum or c_sum!=magic_sum:
      return False
  return True

def isAllOne(nums_dict):
  for i in range(1, 10):
    if i not in nums_dict:
      return False
    else:
      if nums_dict[i]!=1:
        return False
  return True

def getSmallestHighest(nums_dict):
  max=list(nums_dict.keys())[0]    #arbitrary element
  for i in range(9, 0, -1):
    if i in nums_dict:
      if nums_dict[i]>=nums_dict[max]:
        max=i
  return max

def getSmallestEmpty(nums_dict):
  for i in range(1, 10):
    if i not in nums_dict:
      return i

def formingMagicSquare(s):
  nums_dict={}
  sum=0
  for i in range(len(s)):
    for j in range(len(s[i])):
      if s[i][j] in nums_dict:
        nums_dict[s[i][j]]+=1
      else:
        nums_dict[s[i][j]]=1
  
  # while(not isAllOne(nums_dict)):
  #   smallestHighest=getSmallestHighest(nums_dict)
  #   smallestEmpty=getSmallestEmpty(nums_dict)
  #   sum+=abs(smallestHighest-smallestEmpty)
  #   nums_dict[smallestHighest]-=1
  #   nums_dict[smallestEmpty]=1
  # return sum

  return isMagicMatrix(s) #testing



if __name__=="__main__":
    magicMat=[]
    for i in range(3):
      magicMat.append(list(map(int, input().rstrip().split())))
    print(formingMagicSquare(magicMat))