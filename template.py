import os
from pathlib import Path
import logging # cause I want to log all the info during runtime


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
# have to create a logging string
# level: The root logger will be set to the specified severity level.
# filename: This specifies the file.
# filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# format: This is the format of the log message.


# Logging is a very useful tool in a programmer’s toolbox. It can help you develop a better understanding of the flow of a program and discover
#  scenarios that you might not even have thought of while developing.

# Logs provide developers with an extra set of eyes that are constantly looking at the flow that an application is going through. They can store
#  information, like which user or IP accessed the application. If an error occurs, then they can provide more insights than a stack trace by 
# telling you what the state of the program was before it arrived at the line of code where the error occurred.

# By logging useful data from the right places, you can not only debug errors easily but also use the data to analyze the performance of the
#  application to plan for scaling or look at usage patterns to plan for marketing.

# Python provides a logging system as a part of its standard library, so you can quickly add logging to your application. In this article, 
# you will learn why using this module is the best way to add logging to your application as well as how to get started quickly, and you will
#  get an introduction to some of the advanced features available. logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

#creating project folder structure
project_name="textSummarizer"
#### ⭐⭐give all the files required for this project so that it can automatically create from this 
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # inside this common I will write all the utility
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", #It will contain training and prediction pipeline 
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", #YAML is human friendly data serialization language and it can be read by PyYAML module
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", #notebook for the experiment 
    "test.py"
]

for filepath in list_of_files:
# first of all we required to convert the path to the operating system format otherwise it throws error cause for linux we use forward slash and for windows we use back slash
# so for this we use path() libray
    filepath=Path(filepath)
# after that in gitbash from copy 
    filedir,filename=os.path.split(filepath) #it splits and returns my filedirectory and filename
# after that in gitbash from copy
    if filedir!="": # ⭐⭐.i.e. if folder is not present
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory :{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is already exist")       