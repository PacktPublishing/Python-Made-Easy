import json

my_file = open("jsonddata.dat", "w")

my_data = {
    'name': 'Sam',
    'age': 32,
    'city': 'Seattle'
}


json.dump(my_data, my_file)

my_file.close()
