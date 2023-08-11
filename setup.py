from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'Python Mailing Library'
LONG_DESCRIPTION = 'A package that allows to send mails from python environment'

# Setting up
setup(
    name="mailpad",
    version=VERSION,
    author="Shivansh Dwivedi",
    author_email="<me@shivanshdwivedi.tech>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[# No external dependencies],
    keywords=['mailpad','python', 'mail', 'email', 'email client', 'smtp'],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)