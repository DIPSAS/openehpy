import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml-openehr-py-client",
    version="0.0.1",
    author="S. Falkflaug | F. Bentzen | C. Olsen | A. Sølvberg",
    author_email="stfa@dips.no",
    description="A simple Python-OpenEHR connection framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dipscloud.visualstudio.com/DIPS_SL/_git/ML.OpenEHR.Py.Client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)