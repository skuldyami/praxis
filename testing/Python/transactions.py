def save_transaction(price, credit_card, description):
  file= open("transactions.txt", "a")   #The "a" means you are always going to APPEND records to the end of the file
  file.write("%07d%s%13s\n" % (price*100, credit_card, description))
  file.close()