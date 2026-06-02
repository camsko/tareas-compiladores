from Nodes import *

class StringOperationRules:
    def p_index_expression(self, p):
        'expression : expression LBRACKET expression RBRACKET'
        p[0] = IndexNode(p[1], p[3])
        
    def p_method_call_expression(self, p):
        'expression : expression DOT ID LPAREN argument_list RPAREN'
        p[0] = MethodCallNode(
            p[1],
            p[3],
            p[5]
        )
    
    def p_argument_list_multiple(self, p):
        'argument_list : argument_list COMMA expression'
        p[0] = p[1] + [p[3]]

    def p_argument_list_single(self, p):
        'argument_list : expression'
        p[0] = [p[1]]

    def p_argument_list_empty(self, p):
        'argument_list : '
        p[0] = []
    