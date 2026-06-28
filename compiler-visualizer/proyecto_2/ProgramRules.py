from Nodes import ProgramNode


class ProgramRules:
    def p_program_multiple(self, p):
        'program : program global_statement'
        p[0] = ProgramNode(p[1].statements + [p[2]])
    def p_program_single(self, p):
        'program : global_statement'
        p[0] = ProgramNode([p[1]])  