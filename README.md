# MasterQA
[![pypi](https://img.shields.io/pypi/v/masterqa.svg)](https://pypi.python.org/pypi/masterqa) [![Build Status](https://travis-ci.org/masterqa/MasterQA.svg?branch=master)](https://travis-ci.org/masterqa/MasterQA)

### MasterQA combines SeleniumBase automation with manual verification to greatly improve the productivity and sanity of QA teams.

## (NOTE: **[MasterQA is now part of SeleniumBase!](https://github.com/seleniumbase/SeleniumBase/tree/master/seleniumbase/masterqa)**)

![](https://seleniumbase.io/cdn/img/mqa_hybrid.png "MasterQA")

### Run the example test:

```bash
pip install masterqa

git clone https://github.com/masterqa/MasterQA.git

cd MasterQA/examples

pytest masterqa_test.py  # (Default browser: Chrome)
```

![](https://seleniumbase.io/cdn/gif/masterqa6.gif "MasterQA")

### Follow the [example](https://github.com/masterqa/MasterQA/blob/master/examples/masterqa_test.py) to write your own tests:

```python
from masterqa import MasterQA

class MasterQATests(MasterQA):
    def test_xkcd(self):
        self.open("https://xkcd.com/1512/")
        for i in range(4):
            self.click('a[rel="next"]')
        for i in range(3):
            self.click('a[rel="prev"]')
        self.verify()
        self.open("https://xkcd.com/1520/")
        for i in range(2):
            self.click('a[rel="next"]')
        self.verify("Can you find the moon?")
        self.click('a[rel="next"]')
        self.verify("Do the drones look safe?")
        self.open("https://store.xkcd.com/search")
        self.type("input.search-input", "book\n")
        self.verify("Do you see books in the search results?")
        self.open("https://xkcd.com/213/")
        for i in range(5):
            self.click('a[rel="prev"]')
        self.verify("Does the page say 'Abnormal Expressions'?")
```

You'll notice that tests are written based on [SeleniumBase](https://seleniumbase.io), with the key difference of using a different import: ``from masterqa import MasterQA`` rather than ``from seleniumbase import BaseCase``. Now the test class will import ``MasterQA`` instead of ``BaseCase``.

To add a manual verification step, use ``self.verify()`` in the code after each part of the script that needs manual verification. If you want to include a custom question, add text inside that call (in quotes). Example:

```python
self.verify()

self.verify("Can you find the moon?")
```

MasterQA is powered by [SeleniumBase](https://seleniumbase.io), the most advanced open-source automation platform on the [Planet](https://en.wikipedia.org/wiki/Earth).
