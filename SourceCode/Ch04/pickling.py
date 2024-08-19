import pickle

my_file = open("pickleddata.dat", "wb")

data = [1, 2, 3, 4, 5]

pickle.dump(data, my_file)

my_file.close()
