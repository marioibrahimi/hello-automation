# Error Log

## Day 12 - NameError in income_calculator.py

### What I was practicing
Basic debugging: reading a traceback, finding the file, finding the line number, identifying the error type, and fixing one bug at a time.

### Error message
NameError: name 'tax_rate' is not defined

### File
income_calculator.py

### Line
Line 16

### Broken code
```python
tax_rate = tax_rate / 100
'''

WHY IT BROKE
It broke because I tried to use tax_rate before it existed

### FIX
'''python
tax_rate = tax_rate_percent / 100
'''

WHAT I LEARNED
I learned how to debug, to find the error, fix it and run it again.
