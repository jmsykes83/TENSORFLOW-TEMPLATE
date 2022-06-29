import os
import re
import shutil
from distutils.core import Command
from pathlib import Path

from setuptools import find_packages, setup

_deps = ['tensorflow', 
        'pandas', 
        'numpy',
        'matplotlib',
]

deps = {b: a for a, b in (re.findall(r"^(([^!=<>~]+)(?:[!=<>~].*)?$)", x)[0] for x in _deps)}
#TODO This needs to be updated ref: https://github.com/huggingface/transformers/blob/main/setup.py
setup(
   name='Tensorflow-Template',
   version='0.0.0.dev0',
   description=' This is a template for setting up a tensorflow project. ',
   long_description=open("README.md", "r", encoding="utf-8").read(),
   long_description_content_type="text/markdown",
   license="MIT License",
   packages=['Tensorflow-Template'],  
   package_dir={"": "src"},
   packages=find_packages("src"),
   python_requires=">=3.9.0",
   author='Jason Sykes',
   author_email='jmsykes83@yahoo.com',
   url='https://github.com/jmsykes83',
   install_requires=deps, #external packages acting as dependencies
)