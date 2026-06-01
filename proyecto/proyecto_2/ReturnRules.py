
from Nodes import *

class ReturnRules:
    def p_return_expression(self, p):
        'return_statement : RETURN expression'
        p[0] = ReturnNode(p[2])
