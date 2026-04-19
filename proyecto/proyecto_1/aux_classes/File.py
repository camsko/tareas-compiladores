from pathlib import Path

class File:
  
  def __init__(self, path: str):
    p = Path(path)
    self.name = p.stem
    self.text = p.read_text(encoding="utf-8")
    self.lines = self.text.splitlines(keepends=True)
    self.extension = p.suffix
    self.path = path
  
  def __repr__(self):
    return f"File({self.name}{self.extension} in {self.path})\n"