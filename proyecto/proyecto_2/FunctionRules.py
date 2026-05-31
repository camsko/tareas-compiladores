from Nodes import *

class FunctionRules:
    def p_function_definition(self, p):
            'function_definition : DEF ID LPAREN parameter_list RPAREN COLON INDENT function_body DENT'
            p[0] = FunctionNode(
                IdentifierNode(p[2]),
                p[4],
                p[8]
            )
    def p_function_body_multiple(self, p):
        'function_body : function_body restricted_statement'
        p[0] = p[1] + [p[2]]

    def p_function_body_single(self, p):
        'function_body : restricted_statement'
        p[0] = [p[1]]
        
    def p_parameter_list_empty(self, p):
        'parameter_list : '
        p[0] = []
    
    def p_parameter_list_single(self, p):
        'parameter_list : parameter'
        p[0] = [p[1]]

    def p_parameter_list_multiple(self, p):
        'parameter_list : parameter_list COMMA parameter'
        p[0] = p[1] + [p[3]]
        
    def p_parameter(self, p):
        'parameter : ID'
        p[0] = ParameterNode(
            IdentifierNode(p[1]),
            None
        )

    def p_parameter_default(self, p):
        'parameter : ID ASSIGN expression'
        p[0] = ParameterNode(
            IdentifierNode(p[1]),
            p[3]
        )