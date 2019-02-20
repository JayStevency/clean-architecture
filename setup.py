import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clean-architecture",
    version="0.0.1",
    author="problem-labs",
    author_email="yjy1129@kookmin.ac.kr",
    long_description=long_description,
    url="https://github.com/problem-labs/clean-architecture",
    download_url="https://github.com/problem-labs/clean-architecture",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
