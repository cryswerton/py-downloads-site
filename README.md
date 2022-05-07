# Simple Shell Cleaner

## What is it?
A simple Python App that's served only on the local network just to exchange files between the devices on the same network.

### Note
This was only tested on Windows machines

## How to Install It

To use it you need Python and pip installed and working on you machine.

### Set up with pipenv

To install all the dependencies you need to install pipenv in the same directory of the project downloaded with the git clone command:
```
pip install pipenv
```
Create the virtual environment:
```
pipenv shell
```
Now, install all the dependencies:
```
pipenv install
```

### Run the App
```
flask run --host=0.0.0.0
```

### Enjoy the App!