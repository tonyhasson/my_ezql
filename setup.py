# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
#HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="my_ezql",
    version="0.2.3",
    description="Using Mysql the easy way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Tony Hasson",
    author_email="tony.hasson1@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["my_ezql","tests"],
    #py_modules=["my_module"],
    # package_dir={"": str(r"C:\Users\tonyh\PycharmProjects\ezql\my_ezql")},
    #packages=find_packages(include=['my_ezql']),
    #package_dir={'': 'my_ezql'},
    #packages=find_packages(include=['my_ezql', 'my_ezql.*']),
    include_package_data=True,
    install_requires=["mysql-connector-python","pandas"]
)