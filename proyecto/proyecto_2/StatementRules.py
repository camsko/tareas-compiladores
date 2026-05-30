class StatementRules:
    def p_global_statement_assignment(self, p):
        'global_statement : assignment'
        p[0] = p[1]

    def p_global_statement_function(self, p):
        'global_statement : function_definition'
        p[0] = p[1]
    
    def p_function_statement_assignment(self, p):
        'function_statement : assignment'
        p[0] = p[1]