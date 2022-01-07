import rich
from rich import print
from rich.console import Console
from rich.progress import track

import subprocess
def takeFileInput(text, style='green bold'):
    c.print(text, style=style)
    file = input('')

    try:
        with open(file, 'r') as f:
            for m in track(f.readlines(), 'Installing...'):
                i = subprocess.run(['pip', 'install', m], capture_output=True, text=True)
                print(i.stdout)
    except FileNotFoundError:
        takeFileInput('The file you selected was not found!', 'red bold')

c = Console()

takeFileInput('Select a file.')