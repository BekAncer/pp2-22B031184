import os

path=r"C:\Users\Марина\Desktop\pp2_6lab\dest.txt"
if os.access(path,os.F_OK):
    os.remove(path)
    print("file deleted")
else:
    print("file doesnt exist")