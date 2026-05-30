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
        
    def p_statement_function(self, p):
        'statement : function_definition'
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
        
    def p_mod_assign_expression(self, p):
        'assignment : ID MOD_ASSIGN expression'
        p[0] = ModAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_assignment(self, p):
        'assignment : ID ASSIGN expression'
        p[0] = AssignNode(IdentifierNode(p[1]), p[3])

    def p_string_expression(self, p):
        'expression : STRING'
        p[0] = StringNode(p[1])

    def p_float_expression(self, p):
        'expression : FLOAT'
        p[0] = FloatNode(p[1])

    def p_int_expression(self, p):
        'expression : INT'
        p[0] = IntNode(p[1])
    
    def p_identifier_expression(self, p):
        'expression : ID'
        p[0] = IdentifierNode(p[1])
    
    def p_function_definition(self, p):
        'function_definition : DEF ID LPAREN parameter_list RPAREN COLON INDENT program DENT'
        p[0] = FunctionNode(
            IdentifierNode(p[2]),
            p[4],
            p[8]
        )

    def p_parameter_list_empty(self, p):
        'parameter_list : '
        p[0] = []
    
    def p_parameter_list_single(self, p):
        'parameter_list : ID'
        p[0] = [IdentifierNode(p[1])]

    def p_parameter_list_multiple(self, p):
        'parameter_list : parameter_list COMMA ID'
        p[0] = p[1] + [IdentifierNode(p[3])]
        
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
