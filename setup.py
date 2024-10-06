from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list[str]:
    "This function will return the list of packages"
    ...
    requirements = []
    # import pdb; pdb.set_trace()
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
    
    requirements = [requirement.replace("\n", "") for requirement in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements


setup(
    name="Ml Project",
    description="This project is created while learning ml",
    version="0.0.1",
    author="Happy Kumar Sharma",
    author_email="happycse54@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
