"""
The setup package to install MasterQA dependencies
"""
from setuptools import setup, find_packages  # noqa
import os
import sys


this_directory = os.path.abspath(os.path.dirname(__file__))
long_description = None
total_description = None
try:
    with open(os.path.join(this_directory, "README.md"), "rb") as f:
        total_description = f.read().decode("utf-8")
    description_lines = total_description.split('\n')
    long_description_lines = []
    for line in description_lines:
        if not line.startswith("<meta ") and not line.startswith("<link "):
            long_description_lines.append(line)
    long_description = "\n".join(long_description_lines)
except IOError:
    long_description = (
        "Automation-Assisted Manual Testing - https://masterqa.com")

if sys.argv[-1] == "publish":
    reply = None
    input_method = input
    if not sys.version_info[0] >= 3:
        input_method = raw_input  # noqa
    reply = str(input_method(
        ">>> Confirm release PUBLISH to PyPI? (yes/no): ")).lower().strip()
    if reply == "yes":
        print("\n*** Checking code health with flake8:\n")
        os.system("python -m pip install 'flake8==5.0.4'")
        flake8_status = os.system("flake8 --exclude=recordings,temp")
        if flake8_status != 0:
            print("\nWARNING! Fix flake8 issues before publishing to PyPI!\n")
            sys.exit()
        else:
            print("*** No flake8 issues detected. Continuing...")
        print("\n*** Removing existing distribution packages: ***\n")
        os.system("rm -f dist/*.egg; rm -f dist/*.tar.gz; rm -f dist/*.whl")
        os.system("rm -rf build/bdist.*; rm -rf build/lib")
        print("\n*** Installing build: *** (Required for PyPI uploads)\n")
        os.system("python -m pip install --upgrade 'build>=0.9.0'")
        print("\n*** Installing twine: *** (Required for PyPI uploads)\n")
        os.system("python -m pip install --upgrade 'twine>=4.0.2'")
        print("\n*** Installing tqdm: *** (Required for PyPI uploads)\n")
        os.system("python -m pip install --upgrade tqdm")
        print("\n*** Rebuilding distribution packages: ***\n")
        os.system("python -m build")  # Create new tar/wheel
        print("\n*** Publishing The Release to PyPI: ***\n")
        os.system("python -m twine upload dist/*")  # Requires ~/.pypirc Keys
        print("\n*** The Release was PUBLISHED SUCCESSFULLY to PyPI! :) ***\n")
    else:
        print("\n>>> The Release was NOT PUBLISHED to PyPI! <<<\n")
    sys.exit()

setup(
    name="masterqa",
    version="1.7.1",
    description="Automation-Assisted Manual Testing - https://masterqa.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=["Windows", "Linux", "Mac OS-X"],
    url="https://github.com/masterqa/MasterQA",
    author="Michael Mintz",
    author_email="mdmintz@gmail.com",
    maintainer="Michael Mintz",
    license="MIT",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",  # noqa: E501
    install_requires=[
        "seleniumbase>=4.9.7",
        "sbvirtualdisplay>=1.1.1",
        "pdbp>=1.2.5",
        "tabcompleter>=1.1.0",
    ],
    packages=["masterqa"],
    entry_points={
        "nose.plugins": []
        }
    )
