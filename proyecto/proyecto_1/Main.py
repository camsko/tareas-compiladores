from Lexer import Lexer
from aux_classes.FileManager import *


lex = Lexer()
fileManager = FileManager()
files = fileManager.loadTestFiles("test3")

# For each file loaded by the FileManager, tokenize all of its lines and return the tokenized input 
for file in files:
    tokenized_output = lex.tokenize(file.lines)
    clean_tokens = [f"({t.type}, {t.value}, {t.lineno})" for t in tokenized_output]
    for t in clean_tokens:
        print(t)

