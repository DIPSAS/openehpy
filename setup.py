import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openehpy",
    version="0.0.1",
    author="Steinar Falkflaug | Fredrik Bentzen | Christer Olsen | Adrian Sølvberg | Bjørn Fjukstad",
    author_email="bfj@dips.no",
    description="A package for retrieving data from an openEHR server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dipsas/openehpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)