from Nodes import *

class FlowControlRules:
    
##################### Conditionals #####################
    def p_conditional_definition(self, p):
            'conditional : IF comparation COLON INDENT restricted_statement DENT elif_list else_' 
            p[0] = IfNode(
                p[2],
                p[5],
                p[7],
                p[8]
            )
           
### Conditions
 
    def p_comparation_single(self, p):
        'comparation : expression compare_operator expression'
        p[0] = p[2](p[1], p[3])
        
    def p_comparation_multiple(self, p):
        'comparation : comparation logic_operator comparation'
        p[0] = p[2](p[1], p[3])
        
    def p_comparation_group(self, p):
        'comparation : LPAREN comparation RPAREN'
        p[0] = p[2]
      
    def p_and_operator(self, p):
        'logic_operator : AND'
        p[0] = AndNode
        
    def p_or_operator(self, p):
        'logic_operator : OR'
        p[0] = OrNode
    
    def p_equal_expression(self, p):
        'compare_operator : EQUAL'
        p[0] = EqualNode
    
    def p_non_equal_expression(self, p):
        'compare_operator : NON_EQUAL'
        p[0] = NonEqualNode
        
### body
 
    def p_elif_list(self, p):
        'elif_list : elif_list ELIF comparation COLON INDENT restricted_statement DENT'
        p[0] = p[1] + [ElifNode(p[3], p[6])]
    
    def p_elif_empty(self, p):
        'elif_list : '
        p[0] = []
        
    def p_else(self, p):
        'else_ : ELSE COLON INDENT restricted_statement DENT'
        p[0] = ElseNode(p[4])
    
    def p_else_empty(self, p):
        'else_ : '
        p[0] = []
    