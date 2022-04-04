import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdr_tests",
    version="0.0.1a0",
    author="Million Concepts",
    description="Planetary Data Reader test suite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MillionConcepts/pdr-tests",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["pdr", "pyarrow", "requests", "clize", "pytest"],
)
