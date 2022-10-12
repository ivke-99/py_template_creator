"""
A setuptools based setup module.
"""

from setuptools import setup, find_packages
from os import path
import re

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md")) as f:
    long_description = f.read()


def find_version(*file_paths):
    """
    Reads out software version from provided path(s).
    """
    version_file = open("/".join(file_paths), 'r').read()
    lookup = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                       version_file, re.M)

    if lookup:
        return lookup.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name="py_template_creator",
    version=find_version("py_template_creator", "__init__.py"),
    description="Python package for project creation",
    long_description=long_description,
    url="https://github.com/ivke-99/py_template_creator",
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["doc"]),
    include_package_data=True,
    namespace_packages=["py_template_creator"],
    author="Ivan Djuraki",
    author_email="ivandjuraki@protonmail.com",
    license="Apache 2.0",
    entry_points={'console_scripts': ['py_template_creator = py_template_creator.__main__:main']},
    install_requires=[
        "cookiecutter",
        "mrkutil"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
    ],
)
