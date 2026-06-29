class Symbol:
  name: str
  kind: str
  symbol_type: str
  lineno: int

  def __init__(self, n: str = "", k: str = "builtin", s_t: str = "", l: int = -1):
    self.name = n
    self.kind = k
    self.symbol_type = s_t
    self.lineno = l
  
  def __repr__(self):
    return "Symbol(" + self.name + ", " + self.kind + ", " + self.symbol_type + ", " + str(self.lineno) + ")"
    

class SymbolTable:

  def __init__(self, name: str):
    self.name = name
    self.symbols = {}

  def add(self, s: Symbol):
    self.symbols[s.name] = s

  def __repr__(self):
    text = "SymbolTable - " + self.name + "{\n"
    for key, value in self.symbols.items():
      text += "\t" + key + ": " + str(value) + "\n"
    text += "}"
    return text

class SymbolTableStack:
  def __init__(self):
    self.scopes = []

  def push(self, table: SymbolTable):
    self.scopes.append(table)
  
  def pop(self):
    self.scopes.pop()
  
  def current(self) -> SymbolTable:
    return self.scopes[-1]
  
  def find_symbol(self, name: str) -> Symbol:
    for scope in reversed(self.scopes):
      if name in scope.symbols:
        return scope.symbols[name]
    return None

  def __repr__(self):
    text = "SymbolTableStack[\n"
    for scope in self.scopes:
      text += "\t" + str(scope).replace("\n", "\n\t") + "\n"
    text += "]\n"
    return text