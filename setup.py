from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirement_list = List[str] = []
    return  requirement_list

setup(
    name='sensor',
    version='0.0.1',
    author='Dipanshu',
    packages=find_packages(),
    install_requires=get_requirements(),
)