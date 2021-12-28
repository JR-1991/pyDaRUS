import setuptools
from setuptools import setup

setup(
    name='pyDaRUS',
    version='1.0.0',
    author='easyDataverse',
    license='MIT License',
    packages=setuptools.find_packages(),
    install_requires=[
        'easyDataverse',
        'pydantic',
        'jinja2',
        'pyDataverse',
        'pandas',
        'datamodel_code_generator',
        'pyaml',
    ]
)