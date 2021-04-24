# В этом файле прописан алгоритм взлома шифра Цезаря методом частотного анализа
from collections import Counter
from Languages_and_Alphabets import Mostly_used_letters
from Code_and_Decode import caesar_generator


def delete_letters(string):
    # Функция, которая удаляет из строки все кроме букв
    string = ''.join(i for i in string if i.isalpha())
    return string


def frequency_analysis(string, alphabet):
    # Метод частотного анализа состоит в нахождении в тексте самой встречающейся буквы, а на основе сравнения этой
    # буквы с буквой эталонного текста языка находится ключ к шифру Цезаря string- Зафишрованный текст alphabet -
    # Язык алфавита зашифрованного текста
    key = 0
    most_common = dict(Counter(delete_letters(string)).most_common(1))
    for i in most_common.keys():
        key = (alphabet.find(i) - alphabet.find(Mostly_used_letters[alphabet])) % len(alphabet)
    return caesar_generator.generate_sypher(string, key, 0, alphabet)
