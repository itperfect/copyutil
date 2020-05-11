# Реализовать паттерн проектирования "Шаблонный метод"
# Тематику выбирайте какую хотите (кафе, заводы, машины и прочее).
# В реализации пожеланий нет(функции, классы ...), главное чтобы решалась проблема описанная в паттерне который Вам попался.


from abc import ABC, abstractmethod


class MyAbstract(ABC):

    def parse_file(self):
        self.get_name()
        self.get_ext()
        self.get_date()
        self.get_size()
        self.get_owner()
        self.get_path_len()

    def set_dir(self, abs_path):
        self.abs_path = abs_path

    def get_name(self):
        pass

    def get_ext(self):
        pass

    def get_size(self):
        pass

    def get_date(self):
        pass

    def get_owner(self):
        pass

    def get_path_len(self):
        pass


class FileData(MyAbstract):

    def get_name(self):
        print(self.abs_path)

    def get_ext(self):
        pass

    def get_size(self):
        pass

    def get_date(self):
        pass

    def get_owner(self):
        pass

    def get_path_len(self):
        pass


template = FileData()
template.set_dir("/home/albert")
template.parse_file()

