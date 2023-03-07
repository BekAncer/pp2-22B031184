import os
import shutil
source=r"C:\Users\Марина\Desktop\pp2_6lab\brands.txt"
open("dest.txt","w")
dest=r"C:\Users\Марина\Desktop\pp2_6lab\dest.txt"
def copy(source,dest):
    shutil.copy(source,dest)
copy(source,dest)
