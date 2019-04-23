line="101;Johny 'wave-boy' Jones;USA;8.32;Fish;21"
# (ID, name, country, average, board_type, age)=line.split(";")
s={}
(s['id'], s['name'], s['country'], s['average'], s['board_type'], s['age'])=line.split(";")

print("ID: " + s['id'])
print("Name: " + s['name'])
print("Country: " + s['country'])
print("Average: " + s['average'])
print("Board Type: " + s['board_type'])
print("Age: " + s['age'])