import sqlite3

# db= sqlite3.connect("surfersDB.sdb")
# db.row_factory= sqlite3.Row
# cursor= db.cursor()

# cursor.execute("select * from surfers")
# rows= cursor.fetchall()
# for row in rows:
#   if row['id'] == 104:
#     print("ID is " + str(row['id']))
#     print("Name is " + row['name'])
#     print("Board type is " + row['board'])
# cursor.close()

# better query
# cursor.execute("select * from surfers where id="+str(104))
# row= cursor.fetchone()
# if row:
#   print("ID is " + str(row['id']))
#   print("Name is " + row['name'])
#   print("Board type is " + row['board'])
# cursor.close()

def find_details(id2find):
  db= sqlite3.connect("surfersDB.sdb")
  db.row_factory= sqlite3.Row
  cursor= db.cursor()
  cursor.execute("select * from surfers where id="+str(id2find))
  row= cursor.fetchone()
  
  # if row:
  #   cursor.close()
  #   return row
  # Building hash one key-value pair at a time
  if row:
    cursor.close()
    s={}
    s['id']=row['id']
    s['name']=row['name']
    s['country']=row['country']
    s['average']=row['average']
    s['board']=row['board']
    s['age']=row['age']
    return s

  cursor.close()
  return {}

lookup_id=int(input("Enter the id of the surfer: "))
surfer=find_details(lookup_id)
if surfer:
  print("ID: " + str(surfer['id']))
  print("Name: " + surfer['name'])
  print("Country: " + surfer['country'])
  print("Average: " + str(surfer['average']))
  print("Board Type: " + surfer['board'])
  print("Age: " + str(surfer['age']))