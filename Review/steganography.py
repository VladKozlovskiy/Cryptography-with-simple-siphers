import cv2


def code_into_bytes(data):
    # функция для перевода строк и целых чисел в двоичный вид
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, int):
        return format(data, "08b")


def code(name, extension, text):
    # функция для кодирования текста в изображение любого расширения
    # name - имя картинки
    # extension - расширение
    # text - текст
    # output_name - имя изображения куда записать результат
    input_name = name + '.' + extension
    # считываем изображерие
    image = cv2.imread(input_name)
    # рассчитываем максимальный объем кодируемых данных
    max_text_binary_size = image.shape[0] * image.shape[1] * 3 // 8
    if len(text) > max_text_binary_size:
        raise ValueError(
            "К сожалению, ваш текст оказался больше допустимого для шифрования в это изображения объема данных")
    # добавляем фразу которая будет означать что это конец кодируемого текста
    text += "stop_coding"
    count = 0
    # кодируем текст в бинарный вид
    binary_text = code_into_bytes(text)
    # кодируем текст в изображение
    for row in image:
        for pixel in row:
            for i in range(3):
                if count < len(binary_text):
                    pixel[i] = int(code_into_bytes(int(pixel[i]))[:-1] + binary_text[count], 2)
                    count += 1
                else:
                    break
    # записываем результат в нужное изображение
    cv2.imwrite(input_name, image)


def decode(name, rashirenie):
    # Функция которая достает из указанного изобрадения закодированный текст
    # name-название изображения
    # extension-расширение
    input_name = name + '.' + rashirenie
    # считываем изображение
    image = cv2.imread(input_name)
    decode_binary_text = ""
    # достаем текст в бинарном виде
    for row in image:
        for pixel in row:
            for i in range(3):
                decode_binary_text += code_into_bytes(int(pixel[i]))[-1]
    # делим текст по символам в двоичном виде(каждый символ- 8 бит)
    all_bytes = [decode_binary_text[i: i + 8] for i in range(0, len(decode_binary_text), 8)]
    decoded_text = ""
    # получаем ответ
    for byte in all_bytes:
        decoded_text += chr(int(byte, 2))
        if decoded_text[-11:] == "stop_coding":
            break
    return decoded_text[:-11]
