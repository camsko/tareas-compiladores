from Nodes import * 

class OperationRules: 

    def p_operation_or(self, p):
        'operation : operation OR and_operation'
        p[0] = OrNode(p[1], p[3])

    def p_operation_or_passthrough(self, p):
        'operation : and_operation'
        p[0] = p[1]

    def p_and_operation(self, p):
        'and_operation : and_operation AND not_operation'
        p[0] = AndNode(p[1], p[3])

    def p_and_default_operation(self, p):
        'and_operation : not_operation'
        p[0] = p[1]

    def p_not_operation(self, p):
        'not_operation : NOT not_operation'
        p[0] = NotNode(p[2], None)

    def p_not_default_operation(self, p):
        'not_operation : comparison_operation'
        p[0] = p[1]


    def p_comparison_operation_single(self, p):
        '''comparison_operation : term_operation EQUAL term_operation
                                | term_operation NON_EQUAL term_operation
                                | term_operation LOWER_THAN term_operation
                                | term_operation GREATER_THAN term_operation
                                | term_operation LOWER_EQUAL term_operation
                                | term_operation GREATER_EQUAL term_operation'''
        p[0] = self.make_comparison_node(p[2], p[1], p[3])

    def p_comparisons_multiple(self, p):
        '''comparison_operation : comparison_operation EQUAL term_operation
                                | comparison_operation NON_EQUAL term_operation
                                | comparison_operation LOWER_THAN term_operation
                                | comparison_operation GREATER_THAN term_operation
                                | comparison_operation LOWER_EQUAL term_operation
                                | comparison_operation GREATER_EQUAL term_operation'''
        rightmost = self.get_rightmost(p[1])
        new_comparison = self.make_comparison_node(p[2], rightmost, p[3])
        p[0] = AndNode(p[1], new_comparison)
    def make_comparison_node(self, op, left, right):
        if op == '==':   return EqualNode(left, right)
        elif op == '!=': return NonEqualNode(left, right)
        elif op == '<':  return LowerThanNode(left, right)
        elif op == '>':  return GreaterThanNode(left, right)
        elif op == '<=': return LowerEqualNode(left, right)
        elif op == '>=': return GreaterEqualNode(left, right)

    def get_rightmost(self, node):
        # for AndNode, drill into the right child
        if isinstance(node, AndNode):
            return self.get_rightmost(node.right)
        # for comparison nodes, return the right operand
        elif isinstance(node, BinaryNode):
            return node.right
        return node
        
    def p_comparison_default_operation(self, p):
            'comparison_operation : term_operation'
            p[0] = p[1]

    def p_term_operation(self, p):
        '''term_operation : term_operation PLUS multiplicative_operation
                            | term_operation MINUS multiplicative_operation'''
        if p[2] == '+': 
            p[0] = PlusNode(p[1], p[3])
        elif p[2] == '-': 
            p[0] = MinusNode(p[1], p[3])

    def p_term_default_operation(self, p):
        'term_operation : multiplicative_operation'
        p[0] = p[1]

    def p_multiplicative_operation(self, p):
        '''multiplicative_operation : multiplicative_operation MULT power_operation
                                    | multiplicative_operation DIV power_operation
                                    | multiplicative_operation INT_DIV power_operation
                                    | multiplicative_operation MOD power_operation'''
        if p[2] == '*':   
            p[0] = MultNode(p[1], p[3])
        elif p[2] == '/': 
            p[0] = DivNode(p[1], p[3])
        elif p[2] == '//':
            p[0] = IntDivNode(p[1], p[3])
        elif p[2] == '%': 
            p[0] = ModNode(p[1], p[3])

    def p_multiplicative_default_operation(self, p):
        'multiplicative_operation : power_operation'
        p[0] = p[1]

    def p_power_operation(self, p):
        'power_operation : primary_operation POW power_operation'
        p[0] = PowNode(p[1], p[3])

    def p_power_default_operation(self, p):
        'power_operation : primary_operation'
        p[0] = p[1]

    def p_primary_int(self, p):
        'primary_operation : INT'
        p[0] = IntNode(p[1])

    def p_primary_float(self, p):
        'primary_operation : FLOAT'
        p[0] = FloatNode(p[1])

    def p_primary_string(self, p):
        'primary_operation : STRING'
        p[0] = StringNode(p[1])

    def p_primary_id(self, p):
        'primary_operation : ID'
        p[0] = IdentifierNode(p[1])

    def p_primary_function_call(self, p):
        'primary_operation : function_call'
        p[0] = p[1]

    def p_primary_operation_group(self, p):
        'primary_operation : LPAREN operation RPAREN' 
        p[0] = p[2]