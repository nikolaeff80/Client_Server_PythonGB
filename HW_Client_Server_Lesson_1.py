# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

# enc_lst = ['разработка', 'сокет', 'декоратор']
# for enc_word in enc_lst:
#     if isinstance(enc_word, (str, bytes)):
#         print(type(enc_word), (enc_word))
#     else:
#         print('Это не строковое представление')
#
# enc_lst1 = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
#             '\u0441\u043e\u043a\u0435\u0442',
#             '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
# for enc_word in enc_lst1:
#     if isinstance(enc_word, (str, bytes)):
#         print(type(enc_word), (enc_word))
#     else:
#         print('Это не строковое представление')

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

# lst = [b'class', b'function', b'method']
#
# for word in lst:
#     print('Тип переменной: {}\n'.format(type(word)))
#     print('Содержание переменной - {}\n'.format(word))
#     print('Длина строки: {}\n'.format(len(word)))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

# lst = ['attribute', 'класс', 'функция', 'type']
#
# for word in lst:
#     try:
#         print(word)
#         word = word.encode('ASCII')
#         print(type(word))
#     except Exception as e:
#         print(e, '\n' 'Слова с кириллицей невозможно представить в байтовом виде')
#
# lst = ['attribute', 'класс', 'функция', 'type']

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

# lst = ['разработка', 'администрирование', 'protocol', 'standard']
# for word in lst:
#     word = word.encode('utf-8')
#     print(word, type(word))
#     word = bytes.decode(word, 'utf-8')
#     print(word, type(word))

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
# кириллице.

# import subprocess
# import platform
#
#
# def ping(host):
#     ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
#     args = "ping " + " " + ping_str + " " + host
#     con_out = subprocess.check_output(args, shell=True).decode('cp866')
#     return con_out
#
#
# hosts = ['yandex.ru', 'youtube.com']
#
# for elem in hosts:
#     elem = ping(elem)
#     string = str(elem)
#     print('s', string)

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
# его содержимое.
import locale

lst = ['сетевое программирование', 'сокет', 'декоратор']
file_coding = locale.getpreferredencoding()

with open('test_file.txt', 'w+') as f:
    for elem in lst:
        f.write(elem + '\n')
    f.close()

with open('test_file.txt', 'r', encoding=file_coding) as f:
    for elem in f:
        print(elem)
    f.close()
