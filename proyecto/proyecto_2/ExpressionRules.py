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
    
    def p_bool_true_expression(self, p):
        'expression : TRUE'
        p[0] = BoolNode(True)

    def p_bool_false_expression(self, p):
        'expression : FALSE'
        p[0] = BoolNode(False)

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
        
    ##################### Lists #####################
    def p_list_expression(self, p):
        'expression : LBRACKET list_items RBRACKET'
        p[0] = ListNode(p[2])

    def p_list_items_multiple(self, p):
        'list_items : list_items COMMA expression'
        p[0] = p[1] + [p[3]]

    def p_list_items_single(self, p):
        'list_items : expression'
        p[0] = [p[1]]

    def p_list_items_empty(self, p):
        'list_items : '
        p[0] = []
        
    ##################### Tuples #####################
    def p_tuple_expression(self, p):
        'expression : LPAREN tuple_items RPAREN'
        p[0] = TupleNode(p[2])

    def p_tuple_items_multiple(self, p):
        'tuple_items : tuple_items COMMA expression'
        p[0] = p[1] + [p[3]]

    def p_tuple_items_single(self, p):
        'tuple_items : expression'
        p[0] = [p[1]]

    def p_tuple_items_empty(self, p):
        'tuple_items : '
        p[0] = []
        
    ##################### Dictionaries #####################
    def p_dict_expression(self, p):
        'expression : LBRACE dict_items RBRACE'
        p[0] = DictNode(p[2])

    def p_dict_items_multiple(self, p):
        'dict_items : dict_items COMMA dict_pair'
        p[0] = p[1] + [p[3]]

    def p_dict_items_single(self, p):
        'dict_items : dict_pair'
        p[0] = [p[1]]

    def p_dict_items_empty(self, p):
        'dict_items : '
        p[0] = []

    def p_dict_pair(self, p):
        'dict_pair : expression COLON expression'
        p[0] = (p[1], p[3])
