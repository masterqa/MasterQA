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

### Follow the [example](https://github.com/mdmintz/MasterQA/blob/master/examples/verify_test.py) to write your own tests:

```python
from masterqa import MasterQA

class MasterQATests(MasterQA):

    def test_xkcd(self):
        self.open("http://xkcd.com/1512/")
        self.click('a[rel="next"]')
        self.verify()
        self.open("http://xkcd.com/1520/")
        for i in range(2):
            self.click('a[rel="next"]')
        self.verify("Can you find the moon?")
        self.click('a[rel="next"]')
        self.verify("Do the drones look safe?")
        self.click_link_text('Blag')
        self.update_text("input#s", "Robots!\n")
        self.verify("Does it say 'Hooray robots' on the page?")
        self.open("http://xkcd.com/213/")
        for i in range(5):
            self.click('a[rel="prev"]')
        self.verify("Does the page say 'Abnormal Expressions'?")
```

You'll notice that tests are written based on [SeleniumBase](http://seleniumbase.com), with the key difference of using a different import: ``from masterqa import MasterQA`` rather than ``from seleniumbase import BaseCase``. Now the test class will import ``MasterQA`` instead of ``BaseCase``.

To add a manual verification step, use ``self.verify()`` in the code after each part of the script that needs manual verification. If you want to include a custom question, add text inside that call (in quotes). Example:

```python
self.verify()

self.verify("Can you find the moon?")
```

MasterQA is powered by [SeleniumBase](http://seleniumbase.com), the most advanced open-source automation platform on the [Planet](https://en.wikipedia.org/wiki/Earth).
