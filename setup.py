"""
The setup package to install MasterQA requirements
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='masterqa',
    version='1.0.26',
    url='http://masterqa.com',
    author='Michael Mintz',
    author_email='@mintzworld',
    maintainer='Michael Mintz',
    description='Automation-Assisted Manual Testing - http://masterqa.com',
    license='The MIT License',
    install_requires=[
        'seleniumbase>=1.3.12',
        'flake8==3.3.0',
        ],
    packages=['masterqa'],
    entry_points={
        'nose.plugins': []
        }
    )
