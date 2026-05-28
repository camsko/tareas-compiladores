## Instalación de bibliotecas

### Linux / MacOS

```bash
pip3 install -r requirements.txt
```

### Windows

```cmd
pip install -r requirements.txt
```

This program has several files.

- Main.py[Main.py] is the file that runs the lexer for the chosen files.
- Lexer.py[Lexer.py] is the file that contains all the logic for the lexer. It receives the file as data from FileManager and outputs the detected tokens to the terminal.
- aux_classes/FileManager.py[aux_classes/FileManager.py] loads the files specified in the fileName parameter of loadTestFiles into the lexer. By default, it loads all files in the /tests/ folder.
- aux_classes/File.py[aux_classes/File.py] is a class that contains the data of the file to be loaded.
- /tests/ contains all the tests you can load to this lexer.

In order to use this program, load your desired test(s) into the /tests/ folder. If you want to tokenize a specific file, you specify the name of the file in line 7 of Main.py[Main.py] (the function call to loadTestFiles()). Do not add "./tests/" to the beginning of the file name. If you want to tokenize all files in the /tests/ folder, leave the parameters blank.

To run the program, execute the command ```pip install -r requirements`` to install the ply package. Then, execute the command python3 Main.py. The output will be printed to the terminal.