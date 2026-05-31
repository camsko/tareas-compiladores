class StatementRules:
    def p_global_statement_assignment(self, p):
        'global_statement : assignment'
        p[0] = p[1]

    def p_global_statement_function(self, p):
        'global_statement : function_definition'
        p[0] = p[1]
        
    def p_global_statement_conditional(self, p):
        'global_statement : conditional'
        p[0] = p[1]
        
    def p_global_statement_while(self, p):
        'global_statement : while_statement'
        p[0] = p[1]
    
    def p_restricted_statement_assignment_single(self, p):
        'restricted_statement : assignment'
        p[0] = [p[1]]
        
    def p_restricted_statement_conditional_single(self, p):
        'restricted_statement : conditional'
        p[0] = [p[1]]
        
    def p_restricted_statement_while_single(self, p):
        'restricted_statement : while_statement'
        p[0] = [p[1]]
    
    def p_restricted_statement_assignment(self, p):
        'restricted_statement : restricted_statement assignment'
        p[0] = p[1] + [p[2]]
        
    def p_restricted_statement_conditional(self, p):
        'restricted_statement : restricted_statement conditional'
        p[0] = p[1] + [p[2]]
    
    def p_restricted_statement_while(self, p):
        'restricted_statement : restricted_statement while_statement'
        p[0] = p[1] + [p[2]]