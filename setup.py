from setuptools import find_packages, setup
from typing import List


def get_requirements() ->List[str]:
    ''' this function will return a list of requirements '''
    requirement_list:List[str] = []
    ''' append each requirement from requirements.txt file to requirement_list variable'''
    return requirement_list

setup(
    name = "flipkart",
    version = "0.0.1",
    author = "Srada",
    author_email = "sradasrinivas@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)