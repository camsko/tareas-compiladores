import sys
import json
from pathlib import Path
from Lexer import Lexer
from Parser import Parser
from aux_classes.FileManager import *


lex = Lexer()
parser = Parser()

fileManager = FileManager()

compiled_dir = Path(__file__).parent / "compiled"


def compile_to_json(file_name):
    files = fileManager.loadTestFiles(file_name)
    compiled_dir.mkdir(exist_ok=True)

    for file in files:
        lex.tokenize(file.lines)
        lex.current_token_index = 0
        ast = parser.parse(lex)

        if ast:
            tree = ast.to_json()
        else:
            tree = {"type": "Error", "value": "Parse failed", "children": []}

        with open(compiled_dir / f"{file.name}.json", "w", encoding="utf-8") as json_file:
            json.dump(tree, json_file, indent=2)


def run_default():
    files = fileManager.loadTestFiles("operator_tests")

    for file in files:

        lex.tokenize(file.lines)

        clean_tokens = [f"({t.type}, {t.value}, {t.lineno})" for t in lex.generated_tokens]

        for t in clean_tokens:
            print(t)

        lex.current_token_index = 0
        ast = parser.parse(lex)

        for node in ast:
            print(node)


if len(sys.argv) > 1:
    compile_to_json(sys.argv[1])
else:
    run_default()
