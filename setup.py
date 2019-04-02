"""
The setup package to install MasterQA requirements
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='masterqa',
    version='1.1.4',
    description='Automation-Assisted Manual Testing - http://masterqa.com',
    long_description='Automation-Assisted Manual Testing. http://masterqa.com',
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
