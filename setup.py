"""
The setup package to install MasterQA requirements
"""

from setuptools import setup, find_packages  # noqa

setup(
    name='masterqa',
    version='1.0.2',
    url='https://github.com/mdmintz/MasterQA',
    author='Michael Mintz',
    author_email='@mintzworld',
    maintainer='Michael Mintz',
    description='Acceptance Testing Tool: https://github.com/mdmintz/MasterQA',
    license='The MIT License',
    install_requires=[
        'seleniumbase==1.1.34',
        'flake8==2.5.4',
        ],
    packages=['masterqa'],
    entry_points={
        'nose.plugins': []
        }
    )
