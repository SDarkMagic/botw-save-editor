import setuptools
import pathlib

with open("README.md", "r") as desc:
    long_description = desc.read()

setuptools.setup(
    name="botw-save-editor",
    version='1.0.0',
    author="SDarkMagic",
    author_email="TheSDarkMagic@gmail.com",
    description="A program for converting data between JSON and .sav file formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SDarkMagic/botew-save-editor",
    include_package_data=True,
    packages=['saveEditor'],
#    package_dir={'bmpm': 'scripts'},
    entry_points={
        'console_scripts': ['sav_to_json=saveEditor.save_to_json:main', 'json_to_save=saveEditor.json_to_sav:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "pathlib"

    ],
)