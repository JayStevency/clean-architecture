import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clean-architecture",
    version="0.0.1",
    author="jaystevency",
    author_emial="yjy1129@kookmin.ac.kr",
    long_description=long_description,
    url="https://github.com/problem-labs/clean-architecture",
    pakages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)