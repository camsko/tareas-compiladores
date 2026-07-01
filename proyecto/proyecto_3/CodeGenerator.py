from NodeVisitor import *

class CodeGenerator(NodeVisitor):

  def __init__(self):
    super().__init__()
    self.code: str = ""

  def emit(self, s: str):
    self.code += s

  def visit_Symbol(self, s: Symbol):
    if s.kind == "var":
      self.emit(s.symbol_type)
      self.emit(" ")
      self.emit(s.name)

  def visit_Scope(self, t: SymbolTable):
    for key, value in t.symbols.items():
      self.visit_Symbol(value)
      self.emit(";\n")

  def visit_operand(self, child):
    if isinstance(child, BinaryNode):
        self.emit("(")
        self.visit(child)
        self.emit(")")
    else:
        self.visit(child)

  def emit_statements(self, statements):
    for statement in statements:
      self.visit(statement)
      if (type(statement) is not IfNode
          and type(statement) is not WhileNode
          and type(statement) is not ForNode
          and type(statement) is not TryNode
          and type(statement) is not FunctionNode):
        self.emit(";\n")

  def visit_ProgramNode(self, n: ProgramNode):

    self.visit_Scope(n.scope)

    self.emit_statements(n.statements)
    print(self.code)

  def visit_IfNode(self, n: IfNode):
    self.emit("if (")
    self.visit(n.conditions)
    self.emit(") {\n")
    self.visit_Scope(n.scope)
    self.emit_statements(n.body)
    self.emit("}\n")
    for elif_node in n.elif_list:
      self.visit(elif_node)
    self.visit(n.else_)
    
  def visit_ElifNode(self, n: ElifNode):
    self.emit("else if (")
    self.visit(n.conditions)
    self.emit(") {\n")
    self.visit_Scope(n.scope)
    self.emit_statements(n.body)
    self.emit("}\n")
      
  def visit_ElseNode(self, n: ElseNode):
    self.emit("else {\n")
    self.visit_Scope(n.scope)
    self.emit_statements(n.body)
    self.emit("}\n")

  def visit_AssignNode(self, n: AssignNode):
    self.visit(n.left)
    self.emit(" = ")
    self.visit(n.right)
  
  def visit_IdentifierNode(self, n: IdentifierNode):
    self.emit(n.name)
  
  def visit_IntNode(self, n: IntNode):
    self.emit("PyObject(")
    self.emit(str(n.value))
    self.emit(")")

  def visit_AndNode(self, n: AndNode):
    self.visit_operand(n.left)
    self.emit(" && ")
    self.visit_operand(n.right)

  def visit_EqualNode(self, n: EqualNode):
    self.visit_operand(n.left)
    self.emit(" == ")
    self.visit_operand(n.right)

  def visit_OrNode(self, n: OrNode):
    self.visit_operand(n.left)
    self.emit(" || ")
    self.visit_operand(n.right)

  def visit_LowerEqualNode(self, n: LowerEqualNode):
    self.visit_operand(n.left)
    self.emit(" <= ")
    self.visit_operand(n.right)
  
  def visit_FunctionCallNode(self, n: FunctionCallNode):
    self.emit(n.name)
    self.emit("(")
    for i, arg in enumerate(n.parameters):
        if i > 0:
            self.emit(", ")
        self.visit(arg)
    self.emit(")")
  
  def visit_BoolNode(self, n: BoolNode):
    self.emit("PyObject(")
    self.emit(str(n.value).lower())
    self.emit(")")