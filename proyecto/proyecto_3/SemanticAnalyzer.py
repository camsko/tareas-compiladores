from NodeVisitor import *
from SymbolTableStack import *
class SemanticAnalyzer(NodeVisitor):

  def visit_ProgramNode(self, n: ProgramNode):
    if n.scope is None:
      n.scope = SymbolTable("Global Scope")
    self.scope_stack.push(n.scope)
    for node in n.statements:
      self.visit(node)
    self.scope_stack.pop()

  def visit_IfNode(self, n: IfNode):
    self.visit(n.conditions)
    if n.scope is None:
      n.scope = SymbolTable("If Scope")
    self.scope_stack.push(n.scope)
    for b_node in n.body:
      self.visit(b_node)
    self.scope_stack.pop()
    for elif_node in n.elif_list:
      self.visit(elif_node)
    self.visit(n.else_)

  def visit_AndNode(self, n: AndNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_OrNode(self, n: OrNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_EqualNode(self, n: EqualNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_LowerEqualNode(self, n: LowerEqualNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_IdentifierNode(self, n: IdentifierNode):
    s: Symbol = self.scope_stack.find_symbol(n.name)
    if s is None:
      print("Error. Variable " + n.name + " was not declared.")
    
  def visit_IntNode(self, n: IntNode):
    pass

  def visit_FunctionCallNode(self, n: FunctionCallNode):
    s: Symbol = self.scope_stack.find_symbol(n.name)
    if s is None:
      print("Error. Function " + n.name + " was not declared.")
    
  def visit_AssignNode(self, n: AssignNode):
    self.visit(n.right)
    if type(n.left) is IdentifierNode:
        s = Symbol(n.left.name, "var", "PyObject")
        self.scope_stack.current().add(s)
    else:
        self.visit(n.left)
