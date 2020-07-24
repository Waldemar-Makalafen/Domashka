def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()