#Setup.py is resposible in creating my machine learning application as a package, 
# then you can install or use this package in your project
#setup.py is a file give metadata about your project and also the dependencies of your project
#version : #whenever new vr come auto update the vr.


from setuptools import find_packages #this will automatically find package in the directory that we have created
from setuptools import setup
from typing import List



HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
   
    
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name="Machine-Learning-WIth-Deployment",
    version="0.0.1", 
    author="Yugal",
    author_email="yugalchambhare2001@gmail.com",
    packages=find_packages(),
        install_requires=get_requirements("requirements.txt")
    )