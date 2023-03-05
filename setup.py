#with setup.py we will be able to build the ML application as a package and even deploy in python PyPI and anybody can use it

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return the list of Requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name = 'mlproject',
version='0.0.1',
author='Rahul K',
author_email='rahulrk2495@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)