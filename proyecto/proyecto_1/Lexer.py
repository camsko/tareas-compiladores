import ply.lex as lex
import re

class Lexer:

    current_indent = 0

    tokens = (
        'IF', 'ELSE', 'ELIF',
        'WHILE', 'FOR', 
        'BREAK', 'CONTINUE', 'PASS',
        'DEF', 'RETURN', 'CLASS',
        'TRUE', 'FALSE',
        'AND', 'OR', 'NOT',
        'ID', 
        
        #Numeric literals
        'INT', 'FLOAT', 
        
        #String
        'STRING',
        
        #Arithmetic
        'PLUS', 'MINUS', 'MULT',
        'DIV', 'INT_DIV', 'MOD',
        'POW',
        
        #Relational
        'EQUAL', 'NON_EQUAL', 'LOWER_THAN',
        'GREATER_THAN', 'LOWER_EQUAL', 'GREATER_EQUAL',
        
        #Assingment
        'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN',
        'MULT_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN',
        'INT_DIV_ASSIGN', 'POW_ASSIGN',
        
        #Delimiters
        'LPAREN', 'RPAREN', 'LBRACKET',
        'RBRACKET', 'LBRACE', 'RBRACE',
        'COLON', 'COMMA', 'DOT',
    )

    reserved = {
        'if': 'IF',  'else': 'ELSE', 'elif': 'ELIF',
        'while': 'WHILE', 'for': 'FOR',
        'break': 'BREAK', 'continue': 'CONTINUE', 'pass': 'PASS',
        'def': 'DEF', 'return': 'RETURN', 'class': 'CLASS',
        'True': 'TRUE', 'False': 'FALSE',
        'and': 'AND', 'or': 'OR', 'not': 'NOT',
    }

    def t_STRING(self, t):
        r'"((?!"|\\).|\\.)*"?|\'((?!\'|\\).|\\.)*\'?'
        quote = t.value[0]
        valid_escapes = r'\\([nt\\\'"])'
        reduced_value = re.sub(valid_escapes, '', t.value[:-1])
        if not t.value.endswith(quote) or len(t.value) < 2:
            print(f"Illegal Token: {t.value}")
            return None
        elif '\\' in reduced_value:
            print(f"Illegal Token: {t.value}")
            return None
        return t

    def t_ID(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_FLOAT(self, t):
        r'[0-9]+\.[0-9]+'
        t.value = float(t.value)
        return t
    
    def t_INT(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    t_POW_ASSIGN     = r'\*\*='
    t_INT_DIV_ASSIGN = r'//='
    t_PLUS_ASSIGN    = r'\+='
    t_MINUS_ASSIGN   = r'-='
    t_MULT_ASSIGN    = r'\*='
    t_DIV_ASSIGN     = r'/='
    t_MOD_ASSIGN     = r'%='
    t_ASSIGN         = r'='

    t_EQUAL          = r'=='
    t_NON_EQUAL      = r'!='
    t_LOWER_EQUAL    = r'<='
    t_GREATER_EQUAL  = r'>='
    t_LOWER_THAN     = r'<'
    t_GREATER_THAN   = r'>'

    t_POW            = r'\*\*'
    t_INT_DIV        = r'//'
    t_PLUS           = r'\+'
    t_MINUS          = r'-'
    t_MULT           = r'\*'
    t_DIV            = r'/'
    t_MOD            = r'%'
    
    t_LPAREN         = r'\('
    t_RPAREN         = r'\)'
    t_LBRACKET       = r'\['
    t_RBRACKET       = r'\]'
    t_LBRACE         = r'\{'
    t_RBRACE         = r'\}'
    t_DOT            = r'\.'
    t_COLON          = r':'
    t_COMMA          = r','

    t_ignore = '\t| '

    def t_newline(self, t):
        r'\n+'

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}' in line {t.lexer.lineno}")
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def tokenize(self, data: list[str]):
        tokens = []
        self.lexer.lineno = 0
        for line in data:
            new_line = self.preprocess_line(line)
            self.lexer.lineno += 1
            self.lexer.input(new_line)
            tokens += list(self.lexer)
        return tokens

    def preprocess_line(self, line: str):
        single_comma_open = False
        double_comma_open = False
        line_without_comment = line
        for i in range(len(line)):
            c = line[i]
            if c == '"' and (i == 0 or line[i - 1] != "\\"):
                double_comma_open = not double_comma_open
            if c == "'" and (i == 0 or line[i - 1] != "\\"):
                single_comma_open = not single_comma_open
            if c == "#" and not single_comma_open and not double_comma_open:
                line_without_comment = line[:i] + "\n"
                break

        print(repr(line))
        print(repr(line_without_comment))
        return line_without_comment
