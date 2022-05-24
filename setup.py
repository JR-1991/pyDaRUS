import setuptools
from setuptools import setup

with open("README.rst") as f:
    readme = f.read()

setup(
    name='pyDaRUS',
    version='1.0.5',
    author='easyDataverse',
    license='MIT License',
    packages=setuptools.find_packages(),
    long_description=readme,
    install_requires=[
        'easyDataverse',
        'fastapi',
        'uvicorn',
        'pydantic',
        'jinja2',
        'pyDataverse',
        'pandas',
        'pyaml',
    ]
)