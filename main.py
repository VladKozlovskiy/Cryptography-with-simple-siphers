import argparse
import steganography
import Code_and_Decode
import frequency_analysis_method
import Book_sypher
from Languages_and_Alphabets import Alphabets

d = {'Code': 1, 'Decode': 0}
# Словарь который переводит текстовые команды пользователя на язык переменных
parser = argparse.ArgumentParser(description="Run the encryptor program")
parser.add_argument('Cypher_type', required=True, help='Function of encryptor you want to use')
parser.add_argument('path', required=False, help='Path to file with text')
parser.add_argument('Code_or_decode', required=False, help='Do you want to code or to decode smth')
parser.add_argument('language', required=False, help='Language your data is in')
parser.add_argument('key', required=False, help='Key for your coding')
parser.add_argument('filename', required=False, help='Name of file with image')
parser.add_argument('extension', required=False, help='extension of image')
parser.add_argument('list', type=list, required=False, help='if you want to encrypt smth coded with book sypher')
args = parser.parse_args()
file = open(args.path, 'r')
text = file.read()
output = {
    'Vizhner': Code_and_Decode.vizhner_generator.generate_sypher(text, args.key, d[args.Code_or_decode],
                                                                 Alphabets[args.language]),
    'Vernam': Code_and_Decode.vernam_generator.generate_sypher(text, args.key, d[args.Code_or_decode],
                                                               Alphabets[args.language]),
    'Caesar': Code_and_Decode.caesar_generator.generate_sypher(text, int(args.key), d[args.Code_or_decode],
                                                               Alphabets[args.language]),
    'Book sypher': Book_sypher.create_book_sypher(d[args.Code_or_decode], text, args.list, args.key),
    'Steganography': steganography.create_steganography(d[args.Code_or_decode], args.filename, args.extension, text),
    'Frequency analysis method': frequency_analysis_method.frequency_analysis(text, Alphabets[args.language])
}
print(output[args.Cypher_type])
file.close()
