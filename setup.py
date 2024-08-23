from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculation-simple",
    version="0.0.1",
    author="Carlos_Lopes",
    author_email="car.l1991@yahoo.com.br",
    description="Esse pacote tem o objetivo de fazer calculos simples de matetica uma calculadora",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Car-Lopes/package-calculadora",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)