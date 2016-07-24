"""
The setup package to install MasterQA requirements
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='masterqa',
    version='1.0.21',
    url='http://masterqa.com',
    author='Michael Mintz',
    author_email='@mintzworld',
    maintainer='Michael Mintz',
    description='Automation-Assisted Manual Testing - http://masterqa.com',
    license='The MIT License',
    install_requires=[
        'seleniumbase==1.2.4',
        'flake8==2.6.2',
        ],
    packages=['masterqa'],
    entry_points={
        'nose.plugins': []
        }
    )
