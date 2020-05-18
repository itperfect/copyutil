from typing import Any, Union

from .abstract import MyAbstract
import os.path


class FileData(MyAbstract):
    def __init__(self):
        self.src_path = None            # Путь источник
        self.list_of_src_files  = None  # список файлов с абсолютным путём
        self.curr_src_file = None       # Абсолютный путь к текущему файлу, с которым работаем
        self.curr_file_name = None      # Только имя файла, с которым сейчас работаем

        self.dst_path = None            # Путь назначения общий
        self.curr_file_dst_dir = None   # Путь назначения для текущего файла

    def set_src_dir(self, path=None):
        import glob
        self.src_path = path
        self.list_of_src_files = glob.glob(self.src_path + '/*')

    def set_dst_dir(self, path=None):
        if os.path.isdir(path):
            self.dst_path = path
        else:
            raise Exception(f"{path} is not a filesystem path")

    def get_name(self):
        for filename in self.list_of_src_files:
            yield filename

    def check_work_path(self, path):
        if not os.path.isdir(path):
            return False
        return True

    # ----------------------------------------------------------------------------------------------------------------------

    def get_parsed_name(self):
        source_file = self.curr_src_file
        self.curr_file_name = os.path.basename(source_file)

    def check_path(self):
        self.curr_file_dst_dir = self.dst_path + '/' + self.curr_file_name[0]
        if not os.path.isdir(self.curr_file_dst_dir):
            self.create_dir()

    def create_dir(self):
        import os
        try:
            os.mkdir(self.curr_file_dst_dir)
        except Exception as e:
            print(e)
            return False
        return True

    def copy_file(self):
        import shutil
        shutil.copyfile(self.curr_src_file, f'{self.curr_file_dst_dir}/{self.curr_file_name}')

    def delete_file(self):
        os.remove(self.curr_src_file)

    def flush_file(self):
        self.curr_file_dst_dir = None
        self.curr_file_name = None
        self.curr_src_file = None
