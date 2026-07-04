# Hello Automation

## What this project is

A learning project for Python, Terminal, Git, and basic automation scripts. Week 1 covered setup and Python basics. Week 2 covered conditionals, comparisons, boolean logic, functions, debugging, and a small discount calculator.

## What I learned in Week 1

- Terminal basics: pwd, ls, cd, mkdir, touch, rm, clear, cat, code
- Python basics: print, strings, variables, comments, f-strings
- Numbers: int, float, arithmetic, percentages
- User input: input() returns text first, float(input()) converts it for math
- Git basics: status, add, commit, push, log
- Git states: untracked, unstaged, staged, working tree clean

## What I learned in Week 2

- Conditionals: `if`, `elif`, and `else`
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Boolean logic: `and`, `or`, `not`
- Functions: `def`, parameters, and `return`
- Debugging: reading Python error messages, finding the file and line number, fixing one bug at a time
- f-strings for money formatting, for example `€{final_price:.2f}`
- Git cleanup workflow: `git status`, `git add .`, `git commit`, `git push`

## Scripts

### Week 1

- `hello.py` — prints a simple hello message.
- `personal_intro.py` — prints my name, target role, and goals.
- `day3_extra.py` — extra Python basics practice.
- `income_calculator.py` — estimates gross monthly income, tax amount, and net monthly income.
- `main.py` — default starter file from the project setup.

### Week 2

- `budget_status.py` — checks whether my budget/savings are positive or negative and prints a status.
- `rent_check.py` — checks whether rent is safe, stretched, or dangerous compared to income.
- `move_decision.py` — checks whether I can move based on income, rent, savings buffer, and visa status.
- `error_log.md` — records bugs, mistakes, error messages, and how I fixed them.
- `discount_calculator.py` — calculates discount amount, final price, and discount category.

## Commands I practiced

- uv run python file.py
- git status
- git add .
- git commit -m "message"
- git push
- git log --oneline --max-count=10

## How to run scripts

```bash
uv run python income_calculator.py
uv run python budget_status.py
uv run python rent_check.py
uv run python move_decision.py
uv run python discount_calculator.py
```

## What confused me

- input() returns text first, not a number.
- working tree clean does not always mean GitHub is updated.
- untracked, unstaged, and staged are different Git states.
- Exact spelling of commands, file names, and variable names matters.
- Why we use float(input()) for calculator math.
- Difference between untracked and unstaged in Git.

## Next step

Day 15: Python loops with for loops and range().