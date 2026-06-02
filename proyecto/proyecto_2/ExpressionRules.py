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

    def p_identifier_member_access_expression(self, p):
        'expression : ID member_access'
        p[0] = MemberAccessNode(
            IdentifierNode(p[1]),
            p[2]
        )    
    def p_function_call_member_access_expression(self, p):
        'expression : function_call member_access'
        p[0] = MemberAccessNode(
            p[1],
            p[2]
        )
    
    def p_member_access_multiple(self, p):
        'member_access : member_access DOT ID'
        p[0] = p[1] + [IdentifierNode(p[3])]

    def p_member_access_single(self, p):
        'member_access : DOT ID'
        p[0] = [IdentifierNode(p[2])]

    def p_member_access_function_multiple(self, p):
        'member_access : member_access DOT function_call'
        p[0] = p[1] + [p[3]]

    def p_member_access_function_single(self, p):
        'member_access : DOT function_call'
        p[0] = [p[2]]

    def p_identifier_expression(self, p):
        'expression : ID'
        p[0] = IdentifierNode(p[1])

    #TODO CHECK IF THIS IS NEEDED, lo agregue para que se puedan usar funciones luego de asignaciones. 
    #Sin embargo, también permite que se usen funciones como argumentos
    def p_function_call_expression(self, p):
        'expression : function_call'
        p[0] = p[1]
    
    def p_plus_expression(self, p):
        'expression : expression PLUS expression'
        p[0] = PlusNode(p[1], p[3])

    def p_mult_expression(self, p):
        'expression : expression MULT expression'
        p[0] = MultNode(p[1], p[3])
