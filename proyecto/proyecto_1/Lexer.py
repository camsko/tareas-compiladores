import ply.lex as lex

class Lexer:
    tokens = (
        'ID',
    )

    t_ID = r'[A-Za-z_][A-Za-z0-9_]*'

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