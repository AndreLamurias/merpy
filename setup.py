from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="merpy",
    version="1.7.2",
    description="Use Minimal Named-Entity Recognizer (MER) inside python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andre Lamurias",
    author_email="alamurias@lasige.di.fc.ul.pt",
    maintainer="Francisco M Couto",
    maintainer_email="alamurias@lasige.di.fc.ul.pt",
    packages=["merpy"],
    keywords=["ner", "named-entity recognition", "entity linking", "ontologies"],
    url="https://github.com/lasigeBioTM/merpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"merpy": ["MER/*", "MER/data/*"]},
    install_requires=["requests"],
    extras_require={"dev": ["setuptools-changelog"]},
)
