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

  # ControlFlow 

  def visit_IfNode(self, n: IfNode):
    self.visit(n.conditions)
    if n.scope is None:
        n.scope = SymbolTable("If Scope")
    self.scope_stack.push(n.scope)
    for b_node in n.body:
        self.visit(b_node)
    self.scope_stack.pop()
    if n.elif_list is not None:
        for elif_node in n.elif_list:
            self.visit(elif_node)
    if n.else_ is not None:
        self.visit(n.else_)
    
  def visit_ElifNode(self, n: ElifNode):
    self.visit(n.conditions)
    if n.scope is None:
        n.scope = SymbolTable("Elif Scope")
    self.scope_stack.push(n.scope)
    for b_node in n.body:
        self.visit(b_node)
    self.scope_stack.pop()

  def visit_ElseNode(self, n: ElseNode):
    if n.scope is None:
        n.scope = SymbolTable("Else Scope")
    self.scope_stack.push(n.scope)
    for b_node in n.body:
        self.visit(b_node)
    self.scope_stack.pop()


  def visit_WhileNode(self, n: WhileNode):
    self.visit(n.conditions)
    if n.scope is None:
        n.scope = SymbolTable("While Scope")
    self.scope_stack.push(n.scope)
    for b_node in n.body:
        self.visit(b_node)
    self.scope_stack.pop()
  
  def visit_ForNode(self, n: ForNode):
    self.visit(n.gen_func)
#    if n.scope is None:
#        n.scope = SymbolTable("For Scope")
#   self.scope_stack.push(n.scope)
    s = Symbol(n.i_var, "var", "PyObject")
    self.scope_stack.current().add(s)
    for statement in n.body:
        self.visit(statement)
#    self.scope_stack.pop()
    
  def visit_RangeNode(self, n: RangeNode):
    self.visit(n.start)

    if n.stop is not None:
        self.visit(n.stop)

    if n.step is not None:
        self.visit(n.step)
    
  # Expressions
    
  def visit_AndNode(self, n: AndNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_OrNode(self, n: OrNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_EqualNode(self, n: EqualNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_NonEqualNode(self, n: NonEqualNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_LowerEqualNode(self, n: LowerEqualNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_GreaterEqualNode(self, n: GreaterEqualNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_LowerThanNode(self, n: LowerThanNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_GreaterThanNode(self, n: GreaterThanNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_PlusNode(self, n: PlusNode):
    self.visit(n.left)
    self.visit(n.right)
    
  def visit_MinusNode(self, n: MinusNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_MultNode(self, n: MultNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_DivNode(self, n: DivNode):
    self.visit(n.left)
    self.visit(n.right)
  
  def visit_ModNode(self, n: ModNode):
    self.visit(n.left)
    self.visit(n.right)
    
  def visit_NotNode(self, n: NotNode):
    self.visit(n.operand)

  def visit_IdentifierNode(self, n: IdentifierNode):
    s: Symbol = self.scope_stack.find_symbol(n.name)
    if s is None:
      print("Error. Variable " + n.name + " was not declared.")
    
  def visit_AssignNode(self, n: AssignNode):
    self.visit(n.right)
    if type(n.left) is IdentifierNode:
        s = Symbol(n.left.name, "var", "PyObject")
        self.scope_stack.current().add(s)
    else:
        self.visit(n.left)
  
  def visit_FunctionCallNode(self, n: FunctionCallNode):
    s: Symbol = self.scope_stack.find_symbol(n.name)
    if s is None:
      print("Error. Function " + n.name + " was not declared.")
    for arg in n.parameters:
      self.visit(arg)

  def visit_FunctionNode(self, n: FunctionNode):
    self.scope_stack.current().add(
        Symbol(n.name.name, "function", "PyObject")
    )
    if n.scope is None:
      n.scope = SymbolTable("Function Scope")
    self.scope_stack.push(n.scope)
    for param in n.parameters:
      self.scope_stack.current().add(
        Symbol(param.name.name, "var", "PyObject")
      )
    body = n.body[0] if len(n.body) == 1 and isinstance(n.body[0], list) else n.body
    for node in body:
        self.visit(node)
    self.scope_stack.pop()

  def visit_ListNode(self, n: ListNode):
    for element in n.elements:
      self.visit(element)

  def visit_TupleNode(self, n: TupleNode):
    for element in n.elements:
      self.visit(element)

  def visit_DictNode(self, n: DictNode):
    for pair in n.elements:
      self.visit(pair[0])
      self.visit(pair[1])

  def visit_IndexNode(self, n: IndexNode):
    self.visit(n.value)
    self.visit(n.index)

  def visit_ReturnNode(self, n: ReturnNode):
    self.visit(n.value)

  def visit_PowNode(self, n: PowNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_IntDivNode(self, n: IntDivNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_PlusAssignNode(self, n: PlusAssignNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_MinusAssignNode(self, n: MinusAssignNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_MultAssignNode(self, n: MultAssignNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_DivAssignNode(self, n: DivAssignNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_ModAssignNode(self, n: ModAssignNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_IntDivAssignNode(self, n: IntDivAssignNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_PowAssignNode(self, n: PowAssignNode):
    self.visit(n.left)
    self.visit(n.right)

  def visit_FloatNode(self, n: FloatNode):
    pass

  def visit_StringNode(self, n: StringNode):
    pass

  def visit_BoolNode(self, n: BoolNode):
    pass

  def visit_BreakNode(self, n: BreakNode):
    pass

  def visit_ContinueNode(self, n: ContinueNode):
    pass

  def visit_PassNode(self, n: PassNode):
    pass

  
