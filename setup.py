from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .\n")
        

#declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Onkar Sherkar"
DESCRIPTION = "This is 1st machine learning project"

REQUIREMENT_FILE_NAME = "requirements.txt"


setup(   
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)





