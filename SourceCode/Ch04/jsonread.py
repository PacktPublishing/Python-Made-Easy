import json

my_file = open("jsonddata.dat", "r")

json_data = json.load(my_file)

print (json_data)

my_file.close()
