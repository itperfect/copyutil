# Реализовать паттерн проектирования "Шаблонный метод"
# Тематику выбирайте какую хотите (кафе, заводы, машины и прочее).
# В реализации пожеланий нет(функции, классы ...), главное чтобы решалась проблема описанная в паттерне который Вам попался.


import mycopy

source_path = "/tmp/qwerty"
destination_path = "/tmp/qwerty2"

template = mycopy.FileData()
template.set_src_dir(source_path)
template.set_dst_dir(destination_path)

if not template.check_work_path(source_path):
    print("Not valid source path")
    exit(0)

if not template.check_work_path(destination_path):
    print("Not valid destination path")
    if template.create_dir(destination_path) is True:
        print("Directory created successfully")
    else:
        print("Can not create destination path")
        exit(0)

filelist_gen = template.get_name()

try:
    source_file = next(filelist_gen)
except StopIteration:
    print("No files to copy")
    exit(0)

while source_file:

    template.curr_src_file = source_file

    template.process_file()

    try:
        source_file = next(filelist_gen)
    except StopIteration:
        source_file = False
