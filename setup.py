from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements
    """
    requirements = []
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Raajvir Mehta",
    author_email="raajvirmehta@gmail.com",

    package_dir={"": "src"},               
    packages=find_packages(where="src"),   

    install_requires=get_requirements("requirements.txt"),
)
