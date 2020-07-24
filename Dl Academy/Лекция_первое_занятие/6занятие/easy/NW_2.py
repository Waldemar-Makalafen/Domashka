import os
import shutil
import sys
path_dir =[('dir_' + str(i + 1)) for  i in range(9)]
 
def make_dir(paths):
    dir_path = os.path.join(os.getcwd(),paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')
 