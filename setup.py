from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
#declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Onkar Sherkar"
DESCRIPTION = "This is 1st machine learning project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


setup(   
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = PACKAGES,
    install_requires = get_requirements_list()
)





