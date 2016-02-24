# MasterQA
[![pypi](https://img.shields.io/pypi/v/masterqa.svg)](https://pypi.python.org/pypi/seleniumbase) [![Build Status](https://travis-ci.org/mdmintz/MasterQA.svg?branch=master)](https://travis-ci.org/mdmintz/SeleniumBase)

An automation-powered acceptance testing tool that allows users to quickly verify web pages.

### Run the example test:
```bash
pip install masterqa

git clone https://github.com/mdmintz/MasterQA.git

cd MasterQA/examples

py.test verify_test.py
```

### How to write your own test scripts:

Have the following import in your script
```python
from masterqa import MasterQA
```

The have the test class import ``MasterQA``.

Write tests as you would normally with SeleniumBase.

To do manual verification, add a ``self.verify()`` after each part of the script that needs manual verification. If you want to include a custom question, add text inside the call. [Follow the example script to learn how](https://github.com/mdmintz/MasterQA/blob/master/examples/verify_test.py).

Type ``c`` and hit enter on the command prompt when you're ready to exit the Results Page (the script is in ipdb mode at this point).
