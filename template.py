import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')


project_name="textSummarizerNlp"

#Required initial file paths are added in the listfor the project.
list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipnb"
]
#Create the files using the list
for filepath in list_of_files:
    #Handling path differences depending on operating system
    #Path function detects the operating system 
    #Then, creates the files accordingly
    filepath=Path(filepath)
    #Seperate the folder name and the file in it 
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        #Create folder if it does not exist
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating dir: {filedir} for the file: {filename}")
    #To avoid overwriting on a existing file
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath, "w") as f:
            f.write("")
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} has already been created!")