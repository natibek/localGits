import io

import setuptools

__version__ = "0.0.1"

description = "localgit is a tool for managing local git repo clones."

long_description = io.open("README.md", encoding="utf-8").read()

setuptools.setup(
    name="localgit",
    version=__version__,
    url="https://github.com/natibek/localgit/tree/main",
    author="Nathnael Bekele",
    author_email="nwtbekele@gmail.com",
    python_requires=(">=3.11.0"),
    license="Apache 2.0",
    description=description,
    long_description=long_description,
    packages=["src"],
    entry_points={
        "console_scripts": [
            "localgit=src.localgit:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache 2.0",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)
