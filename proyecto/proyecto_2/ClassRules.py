from Nodes import *

class ClassRules:
    def p_class_definition(self, p):
      'class : CLASS ID COLON INDENT class_body DENT'
      p[0] = ClassNode(
          IdentifierNode(p[2]),
          ClassBodyNode(p[5])
      )    
      
    def p_child_class_definition(self, p):
      'child_class : CLASS ID LPAREN ID RPAREN COLON INDENT class_body DENT'
      p[0] = ChildClassNode(
          IdentifierNode(p[2]),
          IdentifierNode(p[4]),
          ClassBodyNode(p[8])
      )

    def p_class_body_multiple(self, p):
        'class_body : class_body function_definition'
        p[0] = p[1] + [p[2]]


    def p_class_body(self, p):
        'class_body : function_definition'
        p[0] = [p[1]]

