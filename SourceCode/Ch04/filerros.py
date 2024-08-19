try:
    # Open the file
    file_path = "my_file.txt"
    file = open(file_path, "r")

    # Perform file operations
    content = file.read()
    print("File content:", content)

    # Close the file
    file.close()

except FileNotFoundError:
    print(f"File '{file_path}' not found!")

except PermissionError:
    print(f"Permission denied to open file '{file_path}'!")

except IOError as e:
    print(f"I/O error occurred while accessing file '{file_path}':", str(e))

except Exception as e:
    print("An error occurred:", str(e))
