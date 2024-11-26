# Project Description
- Everytime we want to create a project in python we need to create a virtual environment, and the command line interface (CLI) might be complicated and can cause confusion, sometimes it might cause frustration and time consuming when you have to navigate to a long folder path or mistype something and then you have to retype everything again.
- VENVGEN will allow you to create your own <i>venv environment</i> without the necessity to remember the CLI commands.
- On top of that, you can edit the environment - install or uninstall the libraries.
- The program also checks for the validity of the libraries that you try to install. It also checks if you mis-deleted your venv by accident and helps you to recover the venv with according pre-installed libraries.

# How to install the software
```python
pip install venvgen
```

# How to use the software
- After Installation into your python environment, you can use the software easily in the terminal with friendly UI by just type
```python
venvgen
```
in the terminal and the program will start running.

# NOT WORKING NOTICE:
- This library is no longer working under MacOS 18 and Windows 11. The developer is currently busy with the school work. This library will be fixed soon. Stay tune!

## Release Note
- 0.0.1: Beta version, buggy, just can use the first option only.
- 0.0.2: Still buggy but now can use some of the second option.
- 0.0.4: Update the code structure and checking system.
- 1.0.0: A full version for MacOS (not fully tested, may cause unexpected bug)
- 2.0.0: Windows user now can use the program properly (not fully tested, may cause unexpected bug)
- 2.0.9: Supported all python 3 version. (The lower version support fixed)

# Developer Note
- Software compatibility with these Operating Systems: MacOS, Windows. (Linux is not tested or tried to run yet).

# Note for Windows Users
- Please install the package on to your main python environment, as the numpy in the virtual environment has undetermined behaviours and cannot be fixed. I will try to find a way to work around. Until then, please use `pip install venvgen` on your main environment.
- Ensure that the library and the main python environment is correctly added to your PATH (environment variable).

