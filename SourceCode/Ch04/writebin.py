my_file = open("data.dat", "wb")

data = "This is a string!"

bytes_data = bytes(data, "utf-8")

my_file.write(bytes_data)

my_file.close()
