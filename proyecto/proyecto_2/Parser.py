import ply.yacc as yacc
from Lexer import Lexer
from Nodes import *

class Parser:

    SYNC_TOKENS = {
        "ID",
    }

    tokens = Lexer.tokens

    def __init__(self):
        self.parser = yacc.yacc(module=self)

    def parse(self, lexer):
        return self.parser.parse(lexer=lexer)

    def p_program_multiple(self, p):
        'program : program statement'
        p[0] = p[1] + [p[2]]

    def p_program_single(self, p):
        'program : statement'
        p[0] = [p[1]]

    def p_statement_assignment(self, p):
        'statement : assignment'
        p[0] = p[1]

    def p_pow_assign_expression(self, p):
        'assignment : ID POW_ASSIGN expression'
        p[0] = PowAssignNode(IdentifierNode(p[1]), p[3])
        
    def p_int_div_assign_expression(self, p):
        'assignment : ID INT_DIV_ASSIGN expression'
        p[0] = IntDivAssignNode(IdentifierNode(p[1]), p[3])
        
    def p_plus_assign_expression(self, p):
        'assignment : ID PLUS_ASSIGN expression'
        p[0] = PlusAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_minus_assign_expression(self, p):
        'assignment : ID MINUS_ASSIGN expression'
        p[0] = MinusAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_mult_assign_expression(self, p):
        'assignment : ID MULT_ASSIGN expression'
        p[0] = MultAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_div_assign_expression(self, p):
        'assignment : ID DIV_ASSIGN expression'
        p[0] = DivAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_assignment(self, p):
        'assignment : ID ASSIGN expression'
        p[0] = AssignNode(IdentifierNode(p[1]), p[3])

    def p_expression_int(self, p):
        'expression : INT'
        p[0] = IntNode(p[1])
    
    def p_expression_identifier(self, p):
        'expression : ID'
        p[0] = IdentifierNode(p[1])
        
    def p_error(self, p):
        if p:
            print(f"Syntax error at line {p.lineno}, token {p.type}, value '{p.value}'")

            while True:
                tok = self.parser.token()
                
                if not tok:
                    break

                if tok.type in self.SYNC_TOKENS:
                    break

            self.parser.errok()

        else:
            print("Syntax error at EOF")
