from aux_classes.File import Path, File

class FileManager:
  def __init__(self):
    self.testFiles: list[File] = []

  def loadTestFiles(self):
    for file in (Path(__file__).parent.parent / "tests").rglob("*.py"):
      self.testFiles.append(File(file))
    return self.testFiles