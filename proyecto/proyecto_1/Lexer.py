import ply.lex as lex
import re
class Lexer:
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
        print(t.value)
        if re.search(r'\\(?![nt\\\"\'])', t.value):
            print(f"Illegal Token: {t.value}")
            return None
        if t.value[0] in ('"', "'"):
            quote = t.value[0]
            if not t.value.endswith(quote):
                print(f"Illegal Token: {t.value}")
                return None
            elif t.value.find(quote, 1) != len(t.value) - 1:
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
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def tokenize(self, data):
        self.lexer.input(data)
        return list(self.lexer)