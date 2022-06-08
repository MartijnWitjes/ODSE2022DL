import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="ODSE2022DL",
    version="0.0.1",
    author="Martijn Witjes",
    author_email="martijnwitjes@gmail.com",
    description="Python package for the Open Data Science 2022 workshop Deep Learning in Python",
    long_description="Python package for the Open Data Science 2022 workshop Deep Learning in Python",
    long_description_content_type="text/markdown",
    url="https://github.com/MartijnWitjes/ODSE2022DL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)