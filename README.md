# Conveyer Robo
## Setup
- Run this game in your python runtime.
- If you have direnv and pyenv installed you can run `direnv allow .` to create a virtual environment.
- With `pip install -r requirements.txt` or `make install` you install the dependencies.
- With `python3 -m src` or `make game` you run the game


## How to play
The goal is to get Bodo through maze like levels in a factory. Base idea is to plan Bodo movements ahead and then execute them all at once.
- ​W-A-S-D for moving Bodo
- Q let Bodo sleep one round
- ENTER execute the entered commands
- BACKSPACE remove inputs
- You get more points the more movements you do in one go and the less energy you use. (Moving > Turning > Sleeping)