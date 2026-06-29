from Nodes import *
from SymbolTableStack import *


class NodeVisitor:
  def __init__(self):
    self.scope_stack = SymbolTableStack()
    builtin_scope = SymbolTable("Builtin Scope")
    builtin_scope.add(Symbol("print", "builtin"))
    self.scope_stack.push(builtin_scope)

  def visit(self, n: Node):
    if type(n) is ProgramNode:
      return self.visit_ProgramNode(n)
    elif type(n) is BinaryNode:
      return self.visit_BinaryNode(n)
    elif type(n) is AssignNode:
      return self.visit_AssignNode(n)
    elif type(n) is IdentifierNode:
      return self.visit_IdentifierNode(n)
    elif type(n) is MemberAccessNode:
      return self.visit_MemberAccessNode(n)
    elif type(n) is StringNode:
      return self.visit_StringNode(n)
    elif type(n) is FloatNode:
      return self.visit_FloatNode(n)
    elif type(n) is IntNode:
      return self.visit_IntNode(n)
    elif type(n) is BoolNode:
      return self.visit_BoolNode(n)
    elif type(n) is FunctionNode:
      return self.visit_FunctionNode(n)
    elif type(n) is ParameterNode:
      return self.visit_ParameterNode(n)
    elif type(n) is FunctionCallNode:
      return self.visit_FunctionCallNode(n)
    elif type(n) is IfNode:
      return self.visit_IfNode(n)
    elif type(n) is ElifNode:
      return self.visit_ElifNode(n)
    elif type(n) is ElseNode:
      return self.visit_ElseNode(n)
    elif type(n) is TryNode:
      return self.visit_TryNode(n)
    elif type(n) is ExceptNode:
      return self.visit_ExceptNode(n)
    elif type(n) is WhileNode:
      return self.visit_WhileNode(n)
    elif type(n) is ForNode:
      return self.visit_ForNode(n)
    elif type(n) is RangeNode:
      return self.visit_RangeNode(n)
    elif type(n) is IndexNode:
      return self.visit_IndexNode(n)
    elif type(n) is MethodCallNode:
      return self.visit_MethodCallNode(n)
    elif type(n) is ClassNode:
      return self.visit_ClassNode(n)
    elif type(n) is ChildClassNode:
      return self.visit_ChildClassNode(n)
    elif type(n) is ClassBodyNode:
      return self.visit_ClassBodyNode(n)
    elif type(n) is ReturnNode:
      return self.visit_ReturnNode(n)
    elif type(n) is ParameterHintNode:
      return self.visit_ParameterHintNode(n)
    elif type(n) is ListNode:
      return self.visit_ListNode(n)
    elif type(n) is TupleNode:
      return self.visit_TupleNode(n)
    elif type(n) is DictNode:
      return self.visit_DictNode(n)
    elif type(n) is BreakNode:
      return self.visit_BreakNode(n)
    elif type(n) is ContinueNode:
      return self.visit_ContinueNode(n)
    elif type(n) is PassNode:
      return self.visit_PassNode(n)
    elif type(n) is PowAssignNode:
      return self.visit_PowAssignNode(n)
    elif type(n) is IntDivAssignNode:
      return self.visit_IntDivAssignNode(n)
    elif type(n) is PlusAssignNode:
      return self.visit_PlusAssignNode(n)
    elif type(n) is MinusAssignNode:
      return self.visit_MinusAssignNode(n)
    elif type(n) is MultAssignNode:
      return self.visit_MultAssignNode(n)
    elif type(n) is DivAssignNode:
      return self.visit_DivAssignNode(n)
    elif type(n) is ModAssignNode:
      return self.visit_ModAssignNode(n)
    elif type(n) is EqualNode:
      return self.visit_EqualNode(n)
    elif type(n) is NonEqualNode:
      return self.visit_NonEqualNode(n)
    elif type(n) is LowerThanNode:
      return self.visit_LowerThanNode(n)
    elif type(n) is GreaterThanNode:
      return self.visit_GreaterThanNode(n)
    elif type(n) is LowerEqualNode:
      return self.visit_LowerEqualNode(n)
    elif type(n) is GreaterEqualNode:
      return self.visit_GreaterEqualNode(n)
    elif type(n) is AndNode:
      return self.visit_AndNode(n)
    elif type(n) is OrNode:
      return self.visit_OrNode(n)
    elif type(n) is RangeBinaryNode:
      return self.visit_RangeBinaryNode(n)
    elif type(n) is PlusNode:
      return self.visit_PlusNode(n)
    elif type(n) is MultNode:
      return self.visit_MultNode(n)
    elif type(n) is NotNode:
      return self.visit_NotNode(n)
    elif type(n) is PowNode:
      return self.visit_PowNode(n)
    elif type(n) is IntDivNode:
      return self.visit_IntDivNode(n)
    elif type(n) is MinusNode:
      return self.visit_MinusNode(n)
    elif type(n) is DivNode:
      return self.visit_DivNode(n)
    elif type(n) is ModNode:
      return self.visit_ModNode(n)

  def visit_ProgramNode(self, n: ProgramNode):
    print("visit_ProgramNode method not implemented.")

  def visit_BinaryNode(self, n: BinaryNode):
    print("visit_BinaryNode method not implemented.")

  def visit_AssignNode(self, n: AssignNode):
    print("visit_AssignNode method not implemented.")

  def visit_IdentifierNode(self, n: IdentifierNode):
    print("visit_IdentifierNode method not implemented.")

  def visit_MemberAccessNode(self, n: MemberAccessNode):
    print("visit_MemberAccessNode method not implemented.")

  def visit_StringNode(self, n: StringNode):
    print("visit_StringNode method not implemented.")

  def visit_FloatNode(self, n: FloatNode):
    print("visit_FloatNode method not implemented.")

  def visit_IntNode(self, n: IntNode):
    print("visit_IntNode method not implemented.")

  def visit_BoolNode(self, n: BoolNode):
    print("visit_BoolNode method not implemented.")

  def visit_FunctionNode(self, n: FunctionNode):
    print("visit_FunctionNode method not implemented.")

  def visit_ParameterNode(self, n: ParameterNode):
    print("visit_ParameterNode method not implemented.")

  def visit_FunctionCallNode(self, n: FunctionCallNode):
    print("visit_FunctionCallNode method not implemented.")

  def visit_IfNode(self, n: IfNode):
    print("visit_IfNode method not implemented.")

  def visit_ElifNode(self, n: ElifNode):
    print("visit_ElifNode method not implemented.")

  def visit_ElseNode(self, n: ElseNode):
    print("visit_ElseNode method not implemented.")

  def visit_TryNode(self, n: TryNode):
    print("visit_TryNode method not implemented.")

  def visit_ExceptNode(self, n: ExceptNode):
    print("visit_ExceptNode method not implemented.")

  def visit_WhileNode(self, n: WhileNode):
    print("visit_WhileNode method not implemented.")

  def visit_ForNode(self, n: ForNode):
    print("visit_ForNode method not implemented.")

  def visit_RangeNode(self, n: RangeNode):
    print("visit_RangeNode method not implemented.")

  def visit_IndexNode(self, n: IndexNode):
    print("visit_IndexNode method not implemented.")

  def visit_MethodCallNode(self, n: MethodCallNode):
    print("visit_MethodCallNode method not implemented.")

  def visit_ClassNode(self, n: ClassNode):
    print("visit_ClassNode method not implemented.")

  def visit_ChildClassNode(self, n: ChildClassNode):
    print("visit_ChildClassNode method not implemented.")

  def visit_ClassBodyNode(self, n: ClassBodyNode):
    print("visit_ClassBodyNode method not implemented.")

  def visit_ReturnNode(self, n: ReturnNode):
    print("visit_ReturnNode method not implemented.")

  def visit_ParameterHintNode(self, n: ParameterHintNode):
    print("visit_ParameterHintNode method not implemented.")

  def visit_ListNode(self, n: ListNode):
    print("visit_ListNode method not implemented.")

  def visit_TupleNode(self, n: TupleNode):
    print("visit_TupleNode method not implemented.")

  def visit_DictNode(self, n: DictNode):
    print("visit_DictNode method not implemented.")

  def visit_BreakNode(self, n: BreakNode):
    print("visit_BreakNode method not implemented.")

  def visit_ContinueNode(self, n: ContinueNode):
    print("visit_ContinueNode method not implemented.")

  def visit_PassNode(self, n: PassNode):
    print("visit_PassNode method not implemented.")

  def visit_PowAssignNode(self, n: PowAssignNode):
    print("visit_PowAssignNode method not implemented.")

  def visit_IntDivAssignNode(self, n: IntDivAssignNode):
    print("visit_IntDivAssignNode method not implemented.")

  def visit_PlusAssignNode(self, n: PlusAssignNode):
    print("visit_PlusAssignNode method not implemented.")

  def visit_MinusAssignNode(self, n: MinusAssignNode):
    print("visit_MinusAssignNode method not implemented.")

  def visit_MultAssignNode(self, n: MultAssignNode):
    print("visit_MultAssignNode method not implemented.")

  def visit_DivAssignNode(self, n: DivAssignNode):
    print("visit_DivAssignNode method not implemented.")

  def visit_ModAssignNode(self, n: ModAssignNode):
    print("visit_ModAssignNode method not implemented.")

  def visit_EqualNode(self, n: EqualNode):
    print("visit_EqualNode method not implemented.")

  def visit_NonEqualNode(self, n: NonEqualNode):
    print("visit_NonEqualNode method not implemented.")

  def visit_LowerThanNode(self, n: LowerThanNode):
    print("visit_LowerThanNode method not implemented.")

  def visit_GreaterThanNode(self, n: GreaterThanNode):
    print("visit_GreaterThanNode method not implemented.")

  def visit_LowerEqualNode(self, n: LowerEqualNode):
    print("visit_LowerEqualNode method not implemented.")

  def visit_GreaterEqualNode(self, n: GreaterEqualNode):
    print("visit_GreaterEqualNode method not implemented.")

  def visit_AndNode(self, n: AndNode):
    print("visit_AndNode method not implemented.")

  def visit_OrNode(self, n: OrNode):
    print("visit_OrNode method not implemented.")

  def visit_RangeBinaryNode(self, n: RangeBinaryNode):
    print("visit_RangeBinaryNode method not implemented.")

  def visit_PlusNode(self, n: PlusNode):
    print("visit_PlusNode method not implemented.")

  def visit_MultNode(self, n: MultNode):
    print("visit_MultNode method not implemented.")

  def visit_NotNode(self, n: NotNode):
    print("visit_NotNode method not implemented.")

  def visit_PowNode(self, n: PowNode):
    print("visit_PowNode method not implemented.")

  def visit_IntDivNode(self, n: IntDivNode):
    print("visit_IntDivNode method not implemented.")

  def visit_MinusNode(self, n: MinusNode):
    print("visit_MinusNode method not implemented.")

  def visit_DivNode(self, n: DivNode):
    print("visit_DivNode method not implemented.")

  def visit_ModNode(self, n: ModNode):
    print("visit_ModNode method not implemented.")
