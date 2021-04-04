import sys
import Code_and_Decode
import frequency_analysis_method
from Languages_and_Alphabets import Alphabets

d = {'Code': 1, 'Decode': 0}
# Словарь который переводит текстовые команды пользователя на язык переменных
if len(sys.argv) == 6:
    # Вводим аргументы и запускаем программу из командой строки
    Path_to_file = sys.argv[1]
    file = open(Path_to_file, "r")
    text = file.read()
    Language = sys.argv[2]
    Key = sys.argv[3]
    Code_or_Decode = int(d[sys.argv[4]])
    Cypher_type = sys.argv[5]
    output = {
        'Vizhner': Code_and_Decode.vizhner_generator.generate_sypher(text, Key, Code_or_Decode,
                                                                     Alphabets[Language]),
        'Vernam': Code_and_Decode.vernam_generator.generate_sypher(text, Key, Code_or_Decode,
                                                                   Alphabets[Language])
    }
    print(output[Cypher_type])
    file.close()
elif len(sys.argv) == 5:
    Path_to_file = sys.argv[1]
    file = open(Path_to_file, "r")
    text = file.read()
    Language = sys.argv[2]
    Key = int(sys.argv[3])
    Code_or_Decode = int(d[sys.argv[4]])
    print(Code_and_Decode.caesar_generator.generate_sypher(text, Key, Code_or_Decode, Alphabets[Language]))
    file.close()
elif len(sys.argv) == 3:
    Path_to_file = sys.argv[1]
    file = open(Path_to_file, "r")
    text = file.read()
    Language = sys.argv[2]
    print(frequency_analysis_method.frequency_analysis(text, Alphabets[Language]))
    file.close()
