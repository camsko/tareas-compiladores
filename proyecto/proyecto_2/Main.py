from Lexer import Lexer
from Parser import Parser
from aux_classes.FileManager import *


lex = Lexer()
parser = Parser()

fileManager = FileManager()
files = fileManager.loadTestFiles("operator_tests")

# For each file loaded by the FileManager, tokenize all of its lines and return the tokenized input 
for file in files:
    
    lex.tokenize(file.lines)
    
    clean_tokens = [f"({t.type}, {t.value}, {t.lineno})" for t in lex.generated_tokens]
    
    for t in clean_tokens:
        print(t)
    
    lex.current_token_index = 0
    ast = parser.parse(lex)

    for node in ast:
        print(node)
        

