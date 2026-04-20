from aux_classes.File import Path, File

# This class loads specified files from the tests folder, or all of them if not specified.
class FileManager:
  def __init__(self):
    self.testFiles: list[File] = []

  # Loads files using Path class
  def loadTestFiles(self, fileName = "*"):
    fileName = fileName.replace(".py", "")
    for file in (Path(__file__).parent.parent / "tests").rglob(f"{fileName}.py"):
      self.testFiles.append(File(file))
    return self.testFiles