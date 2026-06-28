from Nodes import *

class AssignmentRules:
    def p_pow_assign_expression(self, p):
        'assignment : ID POW_ASSIGN expression'
        p[0] = PowAssignNode(IdentifierNode(p[1]), p[3])
        
    def p_int_div_assign_expression(self, p):
        'assignment : ID INT_DIV_ASSIGN expression'
        p[0] = IntDivAssignNode(IdentifierNode(p[1]), p[3])
        
    def p_plus_assign_expression(self, p):
        'assignment : ID PLUS_ASSIGN expression'
        p[0] = PlusAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_minus_assign_expression(self, p):
        'assignment : ID MINUS_ASSIGN expression'
        p[0] = MinusAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_mult_assign_expression(self, p):
        'assignment : ID MULT_ASSIGN expression'
        p[0] = MultAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_div_assign_expression(self, p):
        'assignment : ID DIV_ASSIGN expression'
        p[0] = DivAssignNode(IdentifierNode(p[1]), p[3])
        
    def p_mod_assign_expression(self, p):
        'assignment : ID MOD_ASSIGN expression'
        p[0] = ModAssignNode(IdentifierNode(p[1]), p[3])
    
    def p_assignment_member_access(self, p):
        'assignment : ID member_access ASSIGN expression'
        p[0] = AssignNode(MemberAccessNode(IdentifierNode(p[1]), p[2]), p[4])

    def p_assignment(self, p):
        'assignment : ID ASSIGN expression'
        p[0] = AssignNode(IdentifierNode(p[1]), p[3])    
        
 