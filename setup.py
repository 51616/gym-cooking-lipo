from setuptools import setup, find_packages


DISTNAME = "gym-cooking-lipo"
DESCRIPTION = "A variant of https://github.com/DavidRother/cooking_zoo used in LIPO"

setup(
    name="gym_cooking",
    version="0.0.1",
    description="Cooking gym with graphics and ideas based on https://github.com/DavidRother/cooking_zoo",
    author="David Rother, Rose E. Wang",
    email="david@edv-drucksysteme.de",
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
