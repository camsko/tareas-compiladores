from Nodes import *

class FunctionCallRules:
    def p_function_call(self, p):
        'function_call : ID LPAREN argument_list RPAREN'
        p[0] = FunctionCallNode(p[1], p[3])

    def p_argument_list_empty(self, p):
        'argument_list : '
        p[0] = []

    def p_argument_list_single(self, p):
        'argument_list : expression'
        p[0] = [p[1]]

    def p_argument_list_multiple(self, p):
        'argument_list : argument_list COMMA expression'
        p[0] = p[1] + [p[3]]
