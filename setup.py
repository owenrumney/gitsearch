from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gitsearch-cli',
    version='v0.3',
    packages=['gitsearch'],
    url='',
    license='',
    author='Owen Rumney',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='owen@owenrumney.co.uk',
    install_requires=["requests==2.20.0", "tabulate==0.8.2"],
    description='Search git from the command line',
    scripts=['git-search'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
