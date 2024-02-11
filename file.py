import os
import os.path

def strings_count(file):
    with open(file, 'r', encoding= 'utf-8') as f:
        return sum(1 for line in f)

base_path = os.getcwd()
location = os.path.abspath('C:/Users/alexe/OneDrive/Рабочий стол/file system python/join')
file_writen = os.path.abspath(
    'C:/Users/alexe/OneDrive/Рабочий стол/file system python/result.txt'
    )
total_path = os.path.join(base_path, location)

def write_result(full_path, file_write):
    result_file = []
    for i in list(os.listdir(full_path)):
        result_file.append([strings_count(
            os.path.join(full_path,i)
            ), os.path.join(base_path, location, i), i])
    for file_item in sorted(result_file):
        file_open = open(file_write, 'a', encoding='utf-8')
        file_open.write(f'{file_item[2]}\n')
        file_open.write(f'{file_item[0]}\n')
        with open(file_item[1], 'r', encoding='utf-8') as file:
            counting = 1
            for line in file:
                file_open.write(f'строка № {counting} в файле {file_item[2]} : {line}')
                counting += 1
        file_open.write('\n')
        file_open.close()
write_result(total_path, file_writen)
