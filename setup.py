import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="complex_roots",
    version="0.0.1",
    author="Sijme-Jan Paardekooper",
    author_email="s.j.paardekooper@qmul.ac.uk",
    description="Find complex roots of function in rectangular domain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SijmeJan/complex_roots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy','scipy'],
)
