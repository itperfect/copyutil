from abc import ABC


class MyAbstract(ABC):


    def process_file(self):
        self.get_parsed_name()
        self.check_path()
        self.copy_file()
        self.delete_file()

    def get_name(self):
        pass

    def get_parsed_name(self):
        pass

    def check_path(self):
        pass

    def create_dir(self):
        pass

    def copy_file(self):
        pass

    def delete_file(self):
        pass
