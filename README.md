# Project run instructions

Use the project's virtual environment to run scripts. From PowerShell or a terminal, run:

```powershell
C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe path\to\your_script.py
```

To install dependencies into the venv (already installed `pygame`):

```powershell
C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe -m pip install -r requirements.txt
```

If VS Code still shows unresolved imports, select the interpreter `C:/Users/robin/PycharmProjects/.venv/Scripts/python.exe` via the Command Palette: "Python: Select Interpreter".
