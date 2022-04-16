from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="numeros_primos",
    version="0.0.1",
    author="Anderson Roberto de Oliveira",
    author_email="andersonrobertobru@gmail.com",
    description="Validação de numero primo",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andersonro"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=2.7',
)
