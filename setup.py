"""
The setup package to install MasterQA requirements
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='masterqa',
    version='1.1.3',
    description='Automation-Assisted Manual Testing - http://masterqa.com',
    long_description='Automation-Assisted Manual Testing. http://masterqa.com',
    platforms='Mac * Windows * Linux',
    url='http://masterqa.com',
    author='Michael Mintz',
    author_email='mdmintz@gmail.com',
    maintainer='Michael Mintz',
    license='The MIT License',
    install_requires=[
        'seleniumbase>=1.16.14',
        'flake8==3.5.0',
        ],
    packages=['masterqa'],
    entry_points={
        'nose.plugins': []
        }
    )
