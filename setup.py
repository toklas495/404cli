from setuptools import setup, find_packages

setup(
    name="404cli",
    version="0.1",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "typer[all]",
        "rich",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "404cmd = main:app",
        ],
    },
)
