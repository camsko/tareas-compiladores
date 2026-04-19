import ply.lex as lex
import re
from enum import Enum

class Indent(Enum):
        MUST_INDENT = 1
        MAY_INDENT = 2
        NO_INDENT = 3

class Lexer:

    previous_indent_state = Indent.NO_INDENT
    previous_indent_level = 0
    found_spaces = False
    extra_dent_tokens = 0

    tokens = (
        'IF', 'ELSE', 'ELIF',
        'WHILE', 'FOR', 
        'BREAK', 'CONTINUE', 'PASS',
        'DEF', 'RETURN', 'CLASS',
        'TRUE', 'FALSE',
        'AND', 'OR', 'NOT',
        'ID', 
        
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

        #Indentation
        'INDENT', 'DENT'
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

    t_POW_ASSIGN     = r'\*\*='
    t_INT_DIV_ASSIGN = r'//='
    t_PLUS_ASSIGN    = r'\+='
    t_MINUS_ASSIGN   = r'-='
    t_MULT_ASSIGN    = r'\*='
    t_DIV_ASSIGN     = r'/='
    t_MOD_ASSIGN     = r'%='
    t_ASSIGN         = r'='

    t_EQUAL  = r'=='
    t_NON_EQUAL = r'!='
    t_LOWER_EQUAL  = r'<='
    t_GREATER_EQUAL  = r'>='
    t_LOWER_THAN  = r'<'
    t_GREATER_THAN  = r'>'

    t_POW     = r'\*\*'
    t_INT_DIV = r'//'
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_MULT    = r'\*'
    t_DIV     = r'/'
    t_MOD     = r'%'
    
    t_LPAREN   = r'\('
    t_RPAREN   = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBRACE   = r'\{'
    t_RBRACE   = r'\}'
    t_DOT    = r'\.'
    t_COLON    = r':'
    t_COMMA    = r','
    
    def t_indent(self, t):
        r'^(\ |(\t))+'
        self.found_spaces = True
        space_count = t.value.count(" ") + t.value.count("\t") * 4
        is_indentation_valid = space_count % 4 == 0
        indent_count = space_count // 4
        if not is_indentation_valid:
            print(f"Invalid indentation at line {t.lexer.lineno}. Amount of spaces must be a multiple of 4.")
            return
        if self.previous_indent_state == Indent.MUST_INDENT:
            if indent_count == self.previous_indent_level + 1:
                t.type = "INDENT"
                self.previous_indent_level = indent_count
                return t
            elif indent_count > self.previous_indent_level + 1:
                print(f"Invalid indentation at line {t.lexer.lineno}. Expected {self.previous_indent_level * 4 + 4} spaces, got {space_count}.")
                return None
            else:
                print(f"Expected indentation at line {t.lexer.lineno}, but none found.")
                self.previous_indent_level = indent_count
                return None

        elif self.previous_indent_state == Indent.NO_INDENT:
            if indent_count > self.previous_indent_level:
                print(f"Unexpected indentation at line {t.lexer.lineno}")
            if indent_count < self.previous_indent_level:
                t.type = "DENT"
                self.extra_dent_tokens = self.previous_indent_level - indent_count - 1
                self.previous_indent_level = indent_count
                return t
        else:
            if indent_count < self.previous_indent_level:
                t.type = "DENT"
                self.previous_indent_level = indent_count
                return t
            
        

    
    def t_testignore(self, t):
        r'\t|\ '

    

    def t_newline(self, t):
        r'\n+'

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}' in line {t.lexer.lineno}")
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def tokenize(self, data: list[str]) -> list[lex.LexToken]:
        tokens = []
        self.lexer.lineno = 0
        self.previous_indent_state = Indent.NO_INDENT
        self.previous_indent_level = 0
        for line in data:
            self.extra_dent_tokens = 0
            self.found_spaces = False
            current_indent_state, new_line = self.preprocess_line(line)
            self.lexer.lineno += 1

            self.lexer.input(new_line)

            new_tokens = list(self.lexer)
            
            if (not self.found_spaces and self.previous_indent_level > 0):
                self.previous_indent_level = 0
                tokens.append(self.create_token("DENT", "", self.lexer.lineno, 0))
            
            for i in range(self.extra_dent_tokens):
                tokens.append(self.create_token("DENT", "", self.lexer.lineno, 0))

            tokens += new_tokens

            self.previous_indent_state = current_indent_state
        
        for i in range(self.previous_indent_level):
            tokens.append(self.create_token("DENT", "", self.lexer.lineno, 0))
        return tokens

    def preprocess_line(self, line: str):
        single_comma_open = False
        double_comma_open = False
        line_without_comment = line

        current_state = Indent.NO_INDENT

        for i in range(len(line)):
            c = line[i]
            if c == '"' and (i == 0 or line[i - 1] != "\\"):
                double_comma_open = not double_comma_open
            if c == "'" and (i == 0 or line[i - 1] != "\\"):
                single_comma_open = not single_comma_open
            if c == "#" and not single_comma_open and not double_comma_open:
                line_without_comment = line[:i].rstrip() + "\n"
                break
        line = line_without_comment
        if line[-1] == "\n":
            if (len(line) > 1 and (line[-2] == ":")):
                current_state = Indent.MUST_INDENT #tokenize indentation
            elif (len(line) > 1 and ((line[-2] == "(") or (line[-2] == "[") or (line[-2] == "{"))):
                current_state = Indent.MAY_INDENT
            else:
                current_state = Indent.NO_INDENT

            
        return current_state, line_without_comment

    def create_token(self, type, value, lineno, lexpos) -> lex.LexToken:
        t = lex.LexToken()
        t.type = type
        t.value = value
        t.lineno = lineno
        t.lexpos = lexpos
        return t