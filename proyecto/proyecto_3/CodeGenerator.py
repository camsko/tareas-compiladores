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

  def visit_Scope(self, t: SymbolTable, skip=None):
    if skip is None:
        skip = set()
    for key, value in t.symbols.items():
        print(type(value), value)
        if key in skip:
            continue
        self.visit_Symbol(value)
        print("Emitting symbol: " + str(value))
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
    functions = [s for s in n.statements if type(s) is FunctionNode]
    others = [s for s in n.statements if type(s) is not FunctionNode]
 
    for func in functions:
      self.visit(func)
 
    self.emit("int main() {\n")
    self.visit_Scope(n.scope, skip={f.name.name for f in functions})
    self.emit_statements(others)
    self.emit("return 0;\n")
    self.emit("}\n")
    print(self.code)

  def visit_FunctionNode(self, n: FunctionNode):
    self.emit("PyObject ")
    self.visit(n.name)
    self.emit("(")
    for i, param in enumerate(n.parameters):
      if i > 0:
        self.emit(", ")
      self.visit(param)
    self.emit(") {\n")
    self.visit_Scope(n.scope, skip={p.name.name for p in n.parameters})
    body = n.body[0] if len(n.body) == 1 and isinstance(n.body[0], list) else n.body
    self.emit_statements(body)
    self.emit("}\n")
 
  def visit_ParameterNode(self, n: ParameterNode):
    self.emit("PyObject ")
    self.visit(n.name)
 
  def visit_ReturnNode(self, n: ReturnNode):
    self.emit("return ")
    self.visit(n.value)


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

  def visit_WhileNode(self, n: WhileNode):
    self.emit("while (")
    self.visit(n.conditions)
    self.emit(") {\n")
    self.visit_Scope(n.scope)
    self.emit_statements(n.body)
    self.emit("}\n")
    
  def visit_ForNode(self, n: ForNode):
    if isinstance(n.gen_func, RangeNode):

        self.emit("for (PyObject ")
        self.emit(n.i_var)
        self.emit(" = ")

        # range(stop)
        if n.gen_func.stop is None:

            self.emit("0; ")
            self.emit(n.i_var)
            self.emit(" < ")
            self.visit(n.gen_func.start)
            self.emit("; ++")
            self.emit(n.i_var)

        # range(start, stop)
        elif n.gen_func.step is None:

            self.visit(n.gen_func.start)

            self.emit("; ")
            self.emit(n.i_var)
            self.emit(" < ")
            self.visit(n.gen_func.stop)

            self.emit("; ")
            self.emit(n.i_var)
            self.emit("++")

        # range(start, stop, step)
        else:

            self.visit(n.gen_func.start)

            self.emit("; ")
            self.emit(n.i_var)
            self.emit(" < ")
            self.visit(n.gen_func.stop)

            self.emit("; ")
            self.emit(n.i_var)
            self.emit(" += ")
            self.visit(n.gen_func.step)

        self.emit(") {\n")

    else:

        self.emit("for (PyObject ")
        self.emit(n.i_var)
        self.emit(" : ")
        self.visit(n.gen_func)
        self.emit(") {\n")

    #self.visit_Scope(n.scope, skip={n.i_var})
    self.emit_statements(n.body)

    self.emit("}\n")
    
  def visit_RangeNode(self, n: RangeNode):
    self.emit("range(")
    self.visit(n.start)
    if n.stop is not None:
        self.emit(", ")
        self.visit(n.stop)
    if n.step is not None:
        self.emit(", ")
        self.visit(n.step)
    self.emit(")")
    
  def visit_AssignNode(self, n: AssignNode):
    self.visit(n.left)
    self.emit(" = ")
    self.visit(n.right)
  
  def visit_IdentifierNode(self, n: IdentifierNode):
    self.emit(n.name)
  
  def visit_AndNode(self, n: AndNode):
    self.visit_operand(n.left)
    self.emit(" && ")
    self.visit_operand(n.right)

  def visit_EqualNode(self, n: EqualNode):
    self.visit_operand(n.left)
    self.emit(" == ")
    self.visit_operand(n.right)
  
  def visit_NonEqualNode(self, n: NonEqualNode):
    self.visit_operand(n.left)
    self.emit(" != ")
    self.visit_operand(n.right)

  def visit_OrNode(self, n: OrNode):
    self.visit_operand(n.left)
    self.emit(" || ")
    self.visit_operand(n.right)

  def visit_LowerEqualNode(self, n: LowerEqualNode):
    self.visit_operand(n.left)
    self.emit(" <= ")
    self.visit_operand(n.right)
  
  def visit_GreaterEqualNode(self, n: GreaterEqualNode):
    self.visit_operand(n.left)
    self.emit(" >= ")
    self.visit_operand(n.right)
    
  def visit_GreaterThanNode(self, n: GreaterThanNode):
    self.visit_operand(n.left)
    self.emit(" > ")
    self.visit_operand(n.right)

  def visit_LowerThanNode(self, n: LowerThanNode):
      self.visit_operand(n.left)
      self.emit(" < ")
      self.visit_operand(n.right)
  
  def visit_PlusNode(self, n: PlusNode):
      self.visit_operand(n.left)
      self.emit(" + ")
      self.visit_operand(n.right)
      
  def visit_MinusNode(self, n: MinusNode):
      self.visit_operand(n.left)
      self.emit(" - ")
      self.visit_operand(n.right)
  
  def visit_MultNode(self, n: MultNode):
      self.visit_operand(n.left)
      self.emit(" * ")
      self.visit_operand(n.right)
    
  def visit_DivNode(self, n: DivNode):
      self.visit_operand(n.left)
      self.emit(" / ")
      self.visit_operand(n.right)
  
  def visit_ModNode(self, n: ModNode):
      self.visit_operand(n.left)
      self.emit(" % ")
      self.visit_operand(n.right)
      
  def visit_NotNode(self, n: NotNode):
    self.emit("!")
    self.visit_operand(n.operand)
  
  def visit_FunctionCallNode(self, n: FunctionCallNode):
    if n.name == "print":
        self.emit("std::cout << ")
        if len(n.parameters) > 0:
            self.visit(n.parameters[0])
        self.emit(" << std::endl")
        return
    self.emit(n.name)
    self.emit("(")
    for i, arg in enumerate(n.parameters):
        if i > 0:
            self.emit(", ")
        self.visit(arg)
    self.emit(")")
  
  def visit_IntNode(self, n: IntNode):
    self.emit("PyObject(")
    self.emit(str(n.value))
    self.emit(")")
  
  def visit_FloatNode(self, n: FloatNode):
    self.emit("PyObject(")
    self.emit(str(n.value))
    self.emit(")")
    
  def visit_StringNode(self, n: StringNode):
    self.emit('PyObject(')
    self.emit(n.value)
    self.emit(')')
  
  def visit_BoolNode(self, n: BoolNode):
    self.emit("PyObject(")
    self.emit(str(n.value).lower())
    self.emit(")")