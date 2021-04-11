from random import choice


def code(text, key):
    # функция которая кодирует текст книжным шифром
    # text - то, что надо зашифровать
    # key  - ключ, любой текст, в котором есть все буквы алфавита языка на котором фраза для шифра
    code = []
    count = 0
    for symbol in key:
        # создаем пустой лист в который будем ложить все индексы из ключа, которые соответствую шифруемой букве текста
        tmp = []
        for i in range(len(key)):
            # если в ключе есть символ символ из текста, добавляем номер символа в ключе в  лист
            if text[count] == key[i]:
                tmp.append(i)
        try:
            # добавляем любой из полученных на предудыдущей итерции в финальный код
            code.append(choice(tmp))
        except:
            pass
        finally:
            if count < len(text) - 1:
                count += 1
            else:
                break
    return code


def decode(list, key):
    # функция для декодирования текста, зашифрованного книжным кодом
    # list - список, которым зашифрован текст
    # key -  ключ
    decode = ""
    count = 0
    for symbol in key:
        for i in range(len(key)):
            try:
                if i == (list[count]):
                    if count <= len(list) - 1:
                        count += 1
                        decode += key[i]
            except:
                break
    return decode
