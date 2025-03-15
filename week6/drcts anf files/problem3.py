import os

if os.path.exists("C:/Users/123/Desktop/KBTU python/pp2'25"):
    print("The file exists")
    directory, filename = os.path.split("C:/Users/123/Desktop/KBTU python/pp2'25")

    print(directory)
    print(filename)
else:
    print("File doesnt exists")