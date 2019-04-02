import time as Time
import subprocess
import os

def update(file_name, old_file, sleep_time, counter):
        Time.sleep(sleep_time)
        file = open(file_name, "r", encoding="utf-8")
        file = file.read()
        if(counter % 6 == 0):
            return True, file
        if (file != old_file):
            return True, file
        else:
            return False, file


def get_path():
    path = input("Path to .tex: ")
    return path

def change_path(path):
    os.chdir(path)

def get_file_name():
    file_name = input("File name of .tex: ")
    return file_name


if __name__ == '__main__':
    while True:
        try:
            path = get_path()
            change_path(path)
            break
        except:
            print("Something wrong with your path")

    file_name = get_file_name()

    file_temp = open(file_name, "r", encoding="utf-8")
    file_temp = file_temp.read()

    counter = 0

    while True:
        counter += 1
        boolen, file_temp = update(file_name, file_temp, 10, counter)
        if(boolen):
            print("Compile")
            subprocess.call("pdflatex.exe -synctex=1 -interaction=nonstopmode " + file_name)

