from Nodes import *

class ExpressionRules:
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