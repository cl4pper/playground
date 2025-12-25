# Python Playground

Hi, hope youy day's going well.

This repo is focused on Python challenges and some exercises.

## Working with virtual environment

### Starting your environment

- Run ```python3 -m venv <NAME>```

### Working with your environment

- ```source <NAME>/bin/activate``` to start it
- and ```deactivate``` stop it.

### Working with dependencies
- While active, run ```pip freeze > <FILE_NAME>.txt``` to save the installed dependencies into a txt file.
- After activating your environment, run ```pip install -r <FILE_NAME>.txt``` to install the respective dependencies.
