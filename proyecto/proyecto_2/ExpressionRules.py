from Nodes import *

class ExpressionRules:
    def p_string_expression(self, p):
        'expression : STRING'
        p[0] = StringNode(p[1])

    def p_float_expression(self, p):
        'num_expression : FLOAT'
        p[0] = FloatNode(p[1])
    
    def p_int_expression(self, p):
        'num_expression : INT'
        p[0] = IntNode(p[1])

    def p_num_expression(self, p):
        'expression : num_expression'
        p[0] = p[1]
    
    def p_identifier_expression(self, p):
        'expression : ID'
        p[0] = IdentifierNode(p[1])
    
    def p_plus_expression(self, p):
        'expression : expression PLUS expression'
        p[0] = PlusNode(p[1], p[3])

    def p_mult_expression(self, p):
        'expression : expression MULT expression'
        p[0] = MultNode(p[1], p[3])