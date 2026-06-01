class StatementRules:
    
##################### GLOBAL #####################
    def p_global_statement_assignment(self, p):
        'global_statement : assignment'
        p[0] = p[1]    
    
    def p_global_statement_function_call(self, p):
        'global_statement : function_call'
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
        
    def p_global_statement_for(self, p):
        'global_statement : for_statement'
        p[0] = p[1]
    def p_global_statement_class(self, p):
        'global_statement : class'
        p[0] = p[1]
    def p_global_statement_child_class(self, p):
        'global_statement : child_class'
        p[0] = p[1]
    
    def p_global_statement_function_call(self, p):
        'global_statement : function_call'
        p[0] = p[1]

    def p_global_statement_expression(self, p):
        'global_statement : expression'
        p[0] = p[1]

##################### RESTRICTED #####################
    def p_restricted_statement_assignment_single(self, p):
        'restricted_statement : assignment'
        p[0] = [p[1]]
        
    def p_restricted_statement_conditional_single(self, p):
        'restricted_statement : conditional'
        p[0] = [p[1]]
        
    def p_restricted_statement_while_single(self, p):
        'restricted_statement : while_statement'
        p[0] = [p[1]]
        
    def p_restricted_statement_for_single(self, p):
        'restricted_statement : for_statement'
        p[0] = [p[1]]

    def p_restricted_statement_return_single(self, p):
        'restricted_statement : return_statement'
        p[0] = [p[1]]
    
    def p_restricted_statement_expression_single(self, p):
        'restricted_statement : expression'
        p[0] = [p[1]]

    def p_restricted_statement_function_call_single(self, p):
        'restricted_statement : function_call'
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
        
    def p_restricted_statement_for(self, p):
        'restricted_statement : restricted_statement for_statement'
        p[0] = p[1] + [p[2]]

    def p_restricted_statement_return(self, p):
        'restricted_statement : restricted_statement return_statement'
        p[0] = p[1] + [p[2]]

    def p_restricted_statement_expression(self, p):
        'restricted_statement : restricted_statement expression'
        p[0] = p[1] + [p[2]]
    
    def p_restricted_statement_function_call(self, p):
        'restricted_statement : restricted_statement function_call'
        p[0] = p[1] + [p[2]]