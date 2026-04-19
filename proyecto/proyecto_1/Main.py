from Lexer import Lexer
from aux_classes.FileManager import *

lex = Lexer()
fileManager = FileManager()
files = fileManager.loadTestFiles()

for file in files:
    tokenized_output = lex.tokenize(file.lines)
    print(tokenized_output)
