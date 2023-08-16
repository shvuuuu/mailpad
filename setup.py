from setuptools import setup, find_packages

VERSION = "1.0.2"
DESCRIPTION = "Python Mailing Library"
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name="mailpad",
    version=VERSION,
    author="Shivansh Dwivedi",
    author_email="<me@shivanshdwivedi.tech>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://mailpad.tech/",
    packages=find_packages(),
    install_requires=['langchain'],
    keywords=['mailpad','python', 'mail', 'email', 'email client', 'smtp'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)