import setuptools
from setuptools import setup

setup(
    name='pyDaRUS',
    version='1.0.3',
    author='easyDataverse',
    license='MIT License',
    packages=setuptools.find_packages(),
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