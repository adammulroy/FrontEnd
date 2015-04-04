__author__ = 'adam'
import os

def rename_files():
    path_to_pictures = r'C:\Users\adam\PycharmProjects\FrontEnd\Resources\Pictures'
    file_list = os.listdir(path_to_pictures)
    saved_path = os.getcwd()

    for file_name in file_list:
        os.chdir(path_to_pictures)
        os.rename(file_name, file_name.translate(None, '0123456789'))
    os.chdir(saved_path)
rename_files()