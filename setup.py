from importlib.metadata import entry_points
from setuptools import find_packages, setup

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point Systen for Dunder Mifflin",
    author="Felipe Mendes",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie=dundie.__main__:main"
        ]
    }
)