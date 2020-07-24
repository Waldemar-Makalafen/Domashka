 
def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)
 

 
def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
    0    os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')
 
 
 
def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')