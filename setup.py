import setuptools
import pathlib

with open("README.md", "r") as desc:
    long_description = desc.read()
with open('saveEditor/__version__.txt', 'rt') as readVer:
    ver = readVer.read()

setuptools.setup(
    name="botw-save-editor",
    version=ver,
    author="SDarkMagic",
    author_email="TheSDarkMagic@gmail.com",
    description="A program for converting data between JSON and .sav file formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SDarkMagic/botw-save-editor",
    include_package_data=True,
    packages=['saveEditor'],
    entry_points={
        'console_scripts': ['sav_to_json=saveEditor.sav_to_json:main', 'json_to_sav=saveEditor.json_to_sav:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "pathlib",
        "struct",
        "argparse"
    ],
)