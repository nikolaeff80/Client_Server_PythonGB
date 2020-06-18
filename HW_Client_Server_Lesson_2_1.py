# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
# формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
# считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить
# в соответствующий список. Должно получиться четыре списка — например,
# os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных
# отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить
# в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
# через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().


def get_data():

    file_pattern = '^info.*\.txt$'
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file in os.listdir('.'):
        if os.path.isfile(file) and re.match(file_pattern, file):
            main_data.append(parse_data(file))

    return main_data


def parse_data(file):
    os_manufacturer_pattern = '^Изготовитель ОС:\s*(.*)$'
    os_name_pattern = '^Название ОС:\s*(.*)$'
    os_product_code_pattern = '^Код продукта:\s*(.*)$'
    os_type_pattern = '^Тип системы:\s*(.*)$'
    result = []

    with open(file, 'r') as find_file:
        for line in find_file:

            matched_os_manufacturer = re.match(os_manufacturer_pattern, line)
            matched_os_name = re.match(os_name_pattern, line)
            matched_os_product_code = re.match(os_product_code_pattern, line)
            matched_os_type = re.match(os_type_pattern, line)

            if matched_os_manufacturer:
                if matched_os_manufacturer:
                    result.append(matched_os_manufacturer[1])
                else:
                    result.append('None')

            if matched_os_name:
                if matched_os_name:
                    result.append(matched_os_name[1])
                else:
                    result.append('None')

            if matched_os_product_code:
                if matched_os_product_code:
                    result.append(matched_os_product_code[1])
                else:
                    result.append('None')

            if matched_os_type:
                if matched_os_type:
                    result.append(matched_os_type[1])
                else:
                    result.append('None')

        return result


def write_to_csv(csv_file):
    if not re.match('.*\.csv$', csv_file):
        csv_file += '.csv'

    with open(csv_file, 'w', newline='') as res_file:
        writer = csv.writer(res_file)
        for row in get_data():
            writer.writerow(row)

    print(f"Created file: {csv_file}")


file_name = input("Input name for CSV: ")
write_to_csv(file_name)
