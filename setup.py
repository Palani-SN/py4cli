from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py4cli",
    version="0.0.1",
    description="python for command line interface development",
    py_modules=["py4cli/base"],
    package_dir={"": "SRCS"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Palani-SN/py4cli",
    author="Palani-SN",
    author_email="psn396@gmail.com",

    install_requires = [
        "blessings ~= 1.7",
    ],

    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    },
)
