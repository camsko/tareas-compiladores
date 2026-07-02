from Lexer import Lexer
from Parser import Parser
from SemanticAnalyzer import SemanticAnalyzer
from CodeGenerator import CodeGenerator
from aux_classes.FileManager import *


lex = Lexer()
parser = Parser()
semantic_analyzer = SemanticAnalyzer()
code_gen = CodeGenerator()

fileManager = FileManager()
files = fileManager.loadTestFiles("test1")

# For each file loaded by the FileManager, tokenize all of its lines and return the tokenized input 
for file in files:
    
    lex.tokenize(file.lines)
    
    clean_tokens = [f"({t.type}, {t.value}, {t.lineno})" for t in lex.generated_tokens]
    
    for t in clean_tokens:
        print(t)
    
    lex.current_token_index = 0
    ast = parser.parse(lex)

    semantic_analyzer.visit(ast)
    code_gen.visit(ast)

    cpp_code = """#include <iostream>
    #include "cpp_code/PyObject.hpp"

    using namespace std;

    int main() {
    """ + code_gen.code + """
    return 0;
    }
    """

    with open("output.cpp", "w", encoding="utf-8") as f:
        f.write(cpp_code)
        
        

