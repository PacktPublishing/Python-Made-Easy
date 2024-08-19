import pickle

my_file = open("pickleddata.dat", "rb")

data = pickle.load(my_file)

print (data)


