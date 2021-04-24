# В этом файле находятся алгоритмы шифровки/дешифровки текстов.
import operator
from abc import abstractmethod


def decode(x, y):
    # Т.к. шифрование и дешиврование отличается знаком, то функции слодения и вычитания были вынесены отдельно,
    # чтобы не дублировать код
    return x - y


def code(x, y):
    return x + y


a = {0: decode, 1: code}


# Словарь, которые в зависимости от того кодируем мы или декодируем будет выдавать нам функцию функцию сложения/
# умножения


class sypher_generator:
    # Класс, который содержит общие детали алгоритмов шифрования, от него наследуются остальные алгоритмы.
    def __init__(self):
        pass

    @abstractmethod
    def create_next_symbol(self, symbol, key, code_or_encode, count, alphabet):
        # Функция, которая переобпределяется для каждого класса, получая на вход символ строки и шифрует его по
        # заданному алгоритму. symbol - символ key - ключ шифрования code_or_encode - раскодировать/закодировать
        # count - какой по счету символ alphabet - символ какого языка
        return symbol

    @classmethod
    def generate_sypher(self, string, key, code_or_encode, alphabet):
        # Функция общая для всех методов шифрования. На вход получает текстовую строку, ключ, сигнал к
        # кодированию/раскодированию, и алфавит языка данной строки string - текстовая строка key - ключ
        # code_or_encode - сигнал к кодированию/раскодированию alphabet - алфавит языка Функция проверяет является ли
        # символ буквенным. Если нет, то пропускает его, иначе шифрует по алгоритму. На выходе получается
        # зашифрованный текст
        answer = ''
        count = -1
        for symbol in string.lower():
            if symbol not in alphabet:
                next_symbol = symbol
            else:
                count += 1
                next_symbol = self.create_next_symbol(self, symbol, key, code_or_encode, count, alphabet)
            answer += next_symbol
        return answer


class caesar_generator(sypher_generator):
    # Класс, в котором переодпределяется функция, шифрующая символы по алгоритму для шифра Цезаря
    def create_next_symbol(self, symbol, key, code_or_encode, count, alphabet):
        # Функция сдвигает символ по алфавиту на заданный ключ
        # symbol - исходный символ
        # key - ключ шифрования
        # code_or_encode - определяет шифровать или дештфровать текст
        # count - данный параметр не используется в функции, но перенаследовался от абстрактного класса
        # alphabet - алфавит языка
        return alphabet[(a[code_or_encode](alphabet.find(symbol), int(key))) % len(alphabet)]


class vizhner_generator(sypher_generator):
    # Класс, в котором переодпределяется функция, шифрующая символы по алгоритму для шифра Вижнера Алгоритм Вижнера
    # заключается в сложении номер в алфавите символов исходной строки и символа ключа. В данном алгоритме длина
    # ключа не играет роли, т.к. он будет циклически повторяться пока не достигнет длины строки
    def create_next_symbol(self, symbol, key, code_or_decode, count, alphabet):
        # Функция складывает номер в алфавите исходного ключа и символ соответсвующий ему символ ключа, тем самым
        # получается номер символа в закодированной строке symbol - исходный символ key - ключ шифрования
        # code_or_encode - определяет шифровать или дештфровать текст count - alphabet - алфавит языка
        answer = alphabet[(a[code_or_decode](alphabet.find(symbol), alphabet.find(key[count % len(key)]))) %
                          len(alphabet)]
        return answer


class vernam_generator(sypher_generator):
    # Класс, в котором переодпределяется функция, шифрующая символы по алгоритму для шифра Вернама В алгоритме
    # вернама важно чтоб ключевая строка была длины со строкой которую шифруем. В алгоритме делается оперция  XOR над
    # порядковыми номерами букв ключа и исходника в алфавите
    def create_next_symbol(self, symbol, key, code_or_decode, count, alphabet):
        # Функция делает  XOR над  номерами в алфавите символа исходной строки  символ соответсвующий ему символ
        # ключа, тем самым получается номер символа в закодированной строке symbol - исходный символ key - ключ
        # шифрования code_or_encode - определяет шифровать или дешифровать текст count - номер символа в строке
        # alphabet - алфавит языка
        index_of_next_cypher_letter = 0
        for i in range(code_or_decode + 1):
            index_of_next_cypher_letter = operator.xor(alphabet.find(symbol), alphabet.find(key[count]))
        return alphabet[index_of_next_cypher_letter % len(alphabet)]
