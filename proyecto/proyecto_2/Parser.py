import ply.yacc as yacc
from Lexer import Lexer

from ProgramRules import ProgramRules
from StatementRules import StatementRules
from AssignmentRules import AssignmentRules
from ExpressionRules import ExpressionRules
from FunctionRules import FunctionRules
from FlowControlRules import  FlowControlRules
from StringOperationRules import StringOperationRules
class Parser(
    ProgramRules,
    StatementRules,
    AssignmentRules,
    ExpressionRules,
    FunctionRules,
    FlowControlRules,
    StringOperationRules
):

    SYNC_TOKENS = {
        "ID",
    }

    tokens = Lexer.tokens
    start = 'program'
    def __init__(self):
        self.parser = yacc.yacc(module=self)

    def parse(self, lexer):
        return self.parser.parse(lexer=lexer)

    def p_error(self, p):
        if p:
            print(f"Syntax error at line {p.lineno}, token {p.type}, value '{p.value}'")

            while True:
                tok = self.parser.token()
                
                if not tok:
                    break

                if tok.type in self.SYNC_TOKENS:
                    break

            self.parser.errok()

        else:
            print("Syntax error at EOF")
