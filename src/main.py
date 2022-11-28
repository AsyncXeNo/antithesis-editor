#!venv/bin/python3

from level_editor import Editor

from utils import clean_temp_files

if __name__ == '__main__':
    Editor()
    clean_temp_files()