# Always prefer setuptools over distutils
from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="my_ezql",
    version="0.2.4",
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
    include_package_data=True,
    install_requires=["mysql-connector-python","pandas"]
)