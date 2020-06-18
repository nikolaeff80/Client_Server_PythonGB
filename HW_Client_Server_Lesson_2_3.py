# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml

YAML_FILE = 'file.yaml'


def write_to_yaml(dict, file):
    with open(file, 'w') as yaml_file:
        yaml.dump(dict, yaml_file, Dumper=yaml.Dumper, default_flow_style=False, allow_unicode=True)


def read_yaml(file):
    with open(file, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.Loader)
        print(data)


dict = {'list': ['one', 'two', 3, 4], 'int': 999, 'dict': {'dict1': '€', 'dict2': 999}}
write_to_yaml(dict, YAML_FILE)
print(dict)
read_yaml(YAML_FILE)
