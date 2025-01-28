from setuptools import find_packages,setup
from typing import List
HYPEH_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        if HYPEH_E_DOT in requirements:
            requirements.remove(HYPEH_E_DOT)
    return requirements
setup(
  name='ML Project',
  version='0.0.1',
  author="Ebin Paul",
  author_email="emailebin@gmal.com" ,
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
    
)