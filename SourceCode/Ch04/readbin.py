my_file = open("data.dat", "rb")

fourbytes = my_file.read(4)

print(fourbytes)


my_file.close()
