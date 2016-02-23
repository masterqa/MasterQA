# MasterQA

### Acceptance Testing Tool
MasterQA allows testers to quickly verify web pages while assisted by automation.

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

Have the test class import ``MasterQA``.

Write tests as you would normally with SeleniumBase.

To do manual verification, add a ``self.verify()`` after each part of the script that needs manual verification. If you want to include a custom question, add the text inside the call. Follow the example script if you're having trouble.

Type ``c`` and hit enter on the command prompt when you're ready to exit the Results Page (the script is in ipdb mode at this point).
