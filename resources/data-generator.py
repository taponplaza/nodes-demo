import random

names = ["Jon", "Monica", "Carl", "Ron", "Anna", "Lucy", "Eddy", "Eva", "Tom", "Harry", "Donna", "Jessica", "Peter", "Ritta", "Sarah", "Rodney", "Phyllis", "Meredith", "Angela",
         "Kelly", "Armando", "Kindra", "Monty", "Jona", "Val", "Lenny", "Bruce", "Simon", "Hector", "Laura", "Oleta", "Drucilla", "Rick", "Morty", "Jerry", "Beth", "Summer", "Eric", "Kenny"]

number_of_nodes = 30

f = open("data_30.json", "w+")
f.write('{"nodes": [')
for i in range(number_of_nodes):
    row = '{"id": '+ str(i) +', "name": "'+str(random.choice(names))+'"},\n'
    f.write(row)

f.write('],"links": [')
for i in range(number_of_nodes):
    row = '{"source": '+ str(i) +', "target": '+str(random.randrange(number_of_nodes))+'},\n'
    f.write(row)

f.write(']}')
f.close()