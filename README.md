# MasterQA
[![pypi](https://img.shields.io/pypi/v/masterqa.svg)](https://pypi.python.org/pypi/masterqa) [![Build Status](https://travis-ci.org/mdmintz/MasterQA.svg?branch=master)](https://travis-ci.org/mdmintz/MasterQA)

An automation-assisted manual testing tool that allows users to visually verify web pages after automation does the real work for them.

![](http://cdn2.hubspot.net/hubfs/100006/images/mqa_verify_results.png "MasterQA")

### Run the example test:
```bash
pip install masterqa

git clone https://github.com/mdmintz/MasterQA.git

cd MasterQA/examples

nosetests verify_test.py  # (This defaults to Firefox)
```

### How to write your own test scripts:

Follow the [example script](https://github.com/mdmintz/MasterQA/blob/master/examples/verify_test.py) to learn how.

Have the following import in your script:
```python
from masterqa import MasterQA
```

Then have the test class import ``MasterQA``.

Write tests as you would normally with [SeleniumBase](http://seleniumbase.com).

To do manual verification, add a ``self.verify()`` after each part of the script that needs manual verification. If you want to include a custom question, add text inside that call (in quotes).

Type ``c`` and hit enter on the command prompt when you're ready to exit the Results Page (the script is in ipdb mode at this point).
