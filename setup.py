import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ibspy-homonecloco", # Replace with your own username
    version="0.0.1",
    author="Ricardo H. Ramirez-Gonzalez",
    author_email="ricardo.ramirez-gonzalez@jic.ac.ul",
    description="A package to detect IBS regions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Uauy-Lab/IBSpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)