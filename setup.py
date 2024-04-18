from setuptools import setup, find_packages

# read the contents of the README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="gym-cooking-lipo",
    version="0.0.2",
    description="A variant of https://github.com/DavidRother/cooking_zoo used in LIPO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={"": ["*.png", "*.txt", "*.json"]},
    include_package_data=True,
    install_requires=[
        "gym==0.18.3",
        "numpy>=1.21.2",
        "pygame==2.0.1",
        "PettingZoo==1.9.0",
    ],
)
