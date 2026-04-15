import ply.lex as lex

class Lexer:
    tokens = (
        'IF', 'ELSE', 'ELIF',
        'WHILE', 'FOR', 
        'BREAK', 'CONTINUE', 'PASS',
        'DEF', 'RETURN', 'CLASS',
        'TRUE', 'FALSE',
        'AND', 'OR', 'NOT',
        'ID',
    )

    reserved = {
        'if': 'IF',  'else': 'ELSE', 'elif': 'ELIF',
        'while': 'WHILE', 'for': 'FOR',
        'break': 'BREAK', 'continue': 'CONTINUE', 'pass': 'PASS',
        'def': 'DEF', 'return': 'RETURN', 'class': 'CLASS',
        'True': 'TRUE', 'False': 'FALSE',
        'and': 'AND', 'or': 'OR', 'not': 'NOT',
    }

    def t_ID(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t


    t_ignore = '\t| '

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def tokenize(self, data):
        self.lexer.input(data)
        return list(self.lexer)