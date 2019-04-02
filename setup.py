"""
The setup package to install MasterQA requirements
"""

from setuptools import setup, find_packages  # noqa
from os import path


this_directory = path.abspath(path.dirname(__file__))
long_description = None
try:
    with open(path.join(this_directory, 'README.md'), 'rb') as f:
        long_description = f.read().decode('utf-8')
except IOError:
    long_description = (
        'Automation-Assisted Manual Testing - http://masterqa.com')

setup(
    name='masterqa',
    version='1.1.5',
    description='Automation-Assisted Manual Testing - http://masterqa.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms='Mac * Windows * Linux',
    url='http://masterqa.com',
    author='Michael Mintz',
    author_email='mdmintz@gmail.com',
    maintainer='Michael Mintz',
    license='The MIT License',
    install_requires=[
        'seleniumbase',
        ],
    packages=['masterqa'],
    entry_points={
        'nose.plugins': []
        }
    )
