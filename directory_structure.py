# print contents of current working directory along with their full path

from os import listdir
from os.path import abspath, join

folder = abspath(".")   # current folder with in its absolute path
flist = listdir(folder) # contents of cwd, but not with their full path

for file in flist:
    print(join(folder, file))   # join dir name with the file to get the full path