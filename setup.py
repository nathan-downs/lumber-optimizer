from setuptools import setup, find_packages

setup(
    name="lumber-optimizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Nathan Downs",
    description="A package for optimizing lumber cutting optimization of standard length stock",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nathan-downs/lumber-optimizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)