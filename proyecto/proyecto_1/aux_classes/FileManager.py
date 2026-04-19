from aux_classes.File import Path, File

class FileManager:
  def __init__(self):
    self.testFiles: list[File] = []

  def loadTestFiles(self, file_name = "*"):
    for file in (Path(__file__).parent.parent / "tests").rglob(f"{file_name}.py"):
      self.testFiles.append(File(file))
    return self.testFiles