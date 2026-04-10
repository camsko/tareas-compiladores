# Gestión de contexto
import tempfile, os

with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    path = f.name
    f.write("hola")

with open(path) as f:
    assert f.read() == "hola"

os.unlink(path)