import os

path = "C:/Users/123/Desktop/KBTU python/stepik/Folder"

if os.path.exists(path):
    os.remove(path)
else:
    print("The file does not exist")