from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'Python Mailing Library'
LONG_DESCRIPTION = 'A package that allows to send mails from python environment'

setup(
    name="mailpad",
    version=VERSION,
    author="Shivansh Dwivedi",
    author_email="<me@shivanshdwivedi.tech>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['langchain'],
    keywords=['mailpad','python', 'mail', 'email', 'email client', 'smtp'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license="MIT",
)