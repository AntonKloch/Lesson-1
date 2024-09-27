from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, "w", encoding = 'utf-8')
    string_positions = {}
    num_str = 0
    byte_start_str = file.seek(0)
    for string_ in strings:
        file.write(string_ +'\n')
        num_str += 1
        key = (num_str, byte_start_str)
        string_positions[key] = string_
        byte_start_str = file.tell()
    file.close()
    return string_positions

file = 'test.txt'
strings = [
        'Text for tell.' ,
         'Используйте кодировку utf-8.' ,
         'Because there are 2 languages!' ,
         'Спасибо!',  'Всего хорошего!'
    ]

result = custom_write('test.txt', strings)

pprint(result)
