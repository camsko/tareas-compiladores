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
    parenthesis_depth = 0
    bracket_depth = 0
    brace_depth = 0

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

        #Arrow
        "ARROW",
        
        #Indentation
        'INDENT', 'DENT',

        #Imports
        'IMPORT', 'FROM'

    )

    reserved = {
        'if': 'IF',  'else': 'ELSE', 'elif': 'ELIF',
        'while': 'WHILE', 'for': 'FOR',
        'break': 'BREAK', 'continue': 'CONTINUE', 'pass': 'PASS',
        'def': 'DEF', 'return': 'RETURN', 'class': 'CLASS',
        'True': 'TRUE', 'False': 'FALSE',
        'and': 'AND', 'or': 'OR', 'not': 'NOT',
        'import': 'IMPORT', 'from': 'FROM'
    }

    # Matches strings starting with " or ', allowing escaped characters (\.) 
    # and preventing incorrect closure by looking ahead for quotes (?!" or ?!\').
    def t_STRING(self, t):
        # The closing quote is optional ("? or \'?) to capture unterminated strings for validation.
        r'"((?!"|\\).|\\.)*"?|\'((?!\'|\\).|\\.)*\'?'
        quote = t.value[0]
        valid_escapes = r'\\([nt\\\'"])'
            
        # Remove valid escape sequences from a copy of the string (excluding the final character)
        # to check for any remaining illegal backslashes.
        reduced_value = re.sub(valid_escapes, '', t.value[:-1])
            
        # Check if the string is correctly closed and not just a single quote
        if not t.value.endswith(quote) or len(t.value) < 2:
            print(f"Illegal Token: {t.value}")
            return None
            
        # If any backslash remains after removing valid escapes, the token is illegal
        elif '\\' in reduced_value:
            print(f"Illegal Token: {t.value}")
            return None
        return t

    # Matches identifiers and maps reserved words to their token type.
    def t_ID(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t
        
    # Matches and converts decimal numbers into Python float objects.
    def t_FLOAT(self, t):
        r'[0-9]+\.[0-9]+'
        t.value = float(t.value)
        return t

    # Matches and converts int numbers into Python integer objects.       
    def t_INT(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    t_ARROW = r"\-\>"
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
    
    t_LPAREN   = r'\('
    t_RPAREN   = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBRACE   = r'\{'
    t_RBRACE   = r'\}'
    t_DOT    = r'\.'
    t_COLON    = r':'
    t_COMMA    = r','
    
    # Handles indentation changes and adds INDENT/DENT tokens when needed.
    def t_indent(self, t):
        r'^(\ |(\t))+'

        # Mark that this line started with indentation characters.
        self.found_spaces = True

        # Convert indentation to "spaces" where a tab counts as 4.
        space_count = t.value.count(" ") + t.value.count("\t") * 4
        is_indentation_valid = space_count % 4 == 0
        indent_count = space_count // 4

        # Indentation must be in blocks of 4 spaces.
        if not is_indentation_valid:
            print(f"Invalid indentation at line {t.lexer.lineno}. Amount of spaces must be a multiple of 4.")
            return

        # After a line ending with ':' we require exactly one extra indent level.
        if self.previous_indent_state == Indent.MUST_INDENT:
            if indent_count == self.previous_indent_level + 1:
                # Correct expected indentation: emit INDENT.
                t.type = "INDENT"
                self.previous_indent_level = indent_count
                return t
            elif indent_count > self.previous_indent_level + 1:
                # Indented too much compared to expected level.
                print(f"Invalid indentation at line {t.lexer.lineno}. Expected {self.previous_indent_level * 4 + 4} spaces, got {space_count}.")
                return None
            else:
                # Needed indentation but it was missing.
                print(f"Expected indentation at line {t.lexer.lineno}, but none found.")
                self.previous_indent_level = indent_count
                return None

        elif self.previous_indent_state == Indent.NO_INDENT:
            # When indentation is not expected, deeper indentation is invalid.
            if indent_count > self.previous_indent_level:
                print(f"Unexpected indentation at line {t.lexer.lineno}")
            if indent_count < self.previous_indent_level:
                # Dented one or more levels: emit one DENT now and queue the rest.
                t.type = "DENT"
                self.extra_dent_tokens = self.previous_indent_level - indent_count - 1
                self.previous_indent_level = indent_count
                return t
        else:
            # In MAY_INDENT mode only dentation is tokenized.
            if indent_count < self.previous_indent_level:
                t.type = "DENT"
                self.previous_indent_level = indent_count
                return t
            
        

    
    # Ignores standalone spaces and tabs.
    def t_ignore_whitespace(self, t):
        r'\t|\ '

    

    # Consumes newline characters.
    def t_newline(self, t):
        r'\n+'

    # Reports invalid characters and skips them.
    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}' in line {t.lexer.lineno}")
        t.lexer.skip(1)

    # Builds the PLY lexer instance for this class.
    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Resets counters and indentation state before tokenizing input.
    def reset_tokenization_state(self):
        self.lexer.lineno = 0
        self.previous_indent_state = Indent.NO_INDENT
        self.previous_indent_level = 0
        self.parenthesis_depth = 0
        self.bracket_depth = 0
        self.brace_depth = 0

    # Takes in a single line of input, sends it to preprocessing, 
    # tokenizes it, and then adds the extra dent tokens.
    def process_token_line(self, line: str) -> list[lex.LexToken]:
        line_tokens = []

        # Reset per-line temporary state used by indentation logic.
        self.extra_dent_tokens = 0
        self.found_spaces = False

        # Remove comments and compute the indentation expectation for next line.
        current_indent_state, new_line = self.preprocess_line(line)
        self.lexer.lineno += 1

        # Ignore empty lines after preprocessing.
        if new_line.strip() == "":
            return line_tokens

        # Tokenize current line with PLY.
        self.lexer.input(new_line)
        new_tokens = list(self.lexer)

        # If line starts without indentation, close any open blocks.
        line_tokens += self.add_dents_if_no_indents_in_line()
        # Add any additional DENT tokens computed inside t_indent.
        line_tokens += self.add_extra_dents(self.extra_dent_tokens)
        # Append tokens found in the actual line text.
        line_tokens += new_tokens

        # Save state used by the next line.
        self.previous_indent_state = current_indent_state
        return line_tokens

    # Adds all pending DENT tokens when a line starts with no indentation.
    def add_dents_if_no_indents_in_line(self) -> list[lex.LexToken]:
        dent_tokens = []
        # If no indents were found in the line...
        if not self.found_spaces and self.previous_indent_level > 0:
            dent_tokens = self.add_extra_dents(self.previous_indent_level)
            self.previous_indent_level = 0
        return dent_tokens

    # Adds extra DENT tokens accumulated during indentation processing.
    def add_extra_dents(self, extra_dents : int) -> list[lex.LexToken]:
        dent_tokens = []
        for _ in range(extra_dents):
            dent_tokens.append(self.create_token("DENT", "", self.lexer.lineno, 0))
        return dent_tokens
    
    # Closes any remaining indentation levels at the end of file.
    def add_eof_dents(self) -> list[lex.LexToken]:
        return self.add_extra_dents(self.previous_indent_level)

    # Tokenizes all input lines and returns the final token list.
    def tokenize(self, data: list[str]) -> list[lex.LexToken]:
        tokens = []
        self.reset_tokenization_state()

        for line in data:
            tokens += self.process_token_line(line)

        # Adds dents when a file ends in an indentation
        tokens += self.add_eof_dents() 
        return tokens

    # Removes comments and determines indentation state (may, must, or not indent) for a line.
    def preprocess_line(self, line: str):
        line_without_comment = self.remove_comments_and_track_depth(line)
        current_state = self.get_indent_state_for_line(line_without_comment)
        return current_state, line_without_comment

    # Strips inline comments and updates bracket/parenthesis/brace depth.
    def remove_comments_and_track_depth(self, line: str) -> str:
        # Track whether we are currently inside single or double quoted strings.
        single_quote_open = False
        double_quote_open = False
        line_without_comment = line

        for i in range(len(line)):
            c = line[i]

            # Toggle quote state only when quote is not escaped.
            if c == '"' and (i == 0 or line[i - 1] != "\\"):
                double_quote_open = not double_quote_open
            if c == "'" and (i == 0 or line[i - 1] != "\\"):
                single_quote_open = not single_quote_open

            # A '#' starts a comment only when outside strings.
            if c == "#" and not single_quote_open and not double_quote_open:
                line_without_comment = line[:i].rstrip() + "\n"
                break

            # Keep grouping depth updated for (), [] and {}.
            self.update_grouping_depth(c)

        return line_without_comment

    # Updates grouping depth counters for (), [] and {}.
    def update_grouping_depth(self, character: str):
        if character == "(":
            self.parenthesis_depth += 1
        if character == ")":
            self.parenthesis_depth -= 1
        if character == "[":
            self.bracket_depth += 1
        if character == "]":
            self.bracket_depth -= 1
        if character == "{":
            self.brace_depth += 1
        if character == "}":
            self.brace_depth -= 1

    # Determines whether the next line must, may, or must not be indented.
    def get_indent_state_for_line(self, line: str) -> Indent:
        current_state = Indent.NO_INDENT

        if line and line[-1] == "\n":
            if len(line) > 1 and line[-2] == ":":
                current_state = Indent.MUST_INDENT
            elif self.parenthesis_depth > 0 or self.bracket_depth > 0 or self.brace_depth > 0:
                current_state = Indent.MAY_INDENT
            else:
                current_state = Indent.NO_INDENT

        return current_state

    # Creates a token object manually with the given values. Used for extra DENTs.
    def create_token(self, type, value, lineno, lexpos) -> lex.LexToken:
        t = lex.LexToken()
        t.type = type
        t.value = value
        t.lineno = lineno
        t.lexpos = lexpos
        return t