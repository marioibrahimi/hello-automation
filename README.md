# Hello Automation

## What this project is

A learning project for Python, Terminal, Git, and basic automation scripts. Week 1 covered setup and Python basics. Week 2 covered conditionals, comparisons, boolean logic, functions, debugging, and a small discount calculator. Week 3 covered loops, lists, dictionaries, nested dictionaries, and the first mini city cost calculator.

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
- f-strings for money formatting, for example `${final_price:.2f}`
- Git cleanup workflow: `git status`, `git add .`, `git commit`, `git push`

## What I learned in Week 3

- For loops: repeat through a known group or list.
- While loops: repeat while a condition stays true.
- Lists: store multiple values in one container.
- Dictionaries: store values using labels/keys, like drawers with names.
- Nested dictionaries: dictionaries inside dictionaries, like drawers inside drawers.
- input(): asks the user for a value in the Terminal.
- .strip(): removes spaces before and after user input.
- .title(): converts input like `bucharest` into `Bucharest` so it matches the dictionary key.
- if selected_city in cities: checks if the selected city exists as a key before opening the dictionary.
- else: runs when the city is not found.

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

### Week 3

- `city_list.py` — loops through a list of cities and prints them.
- `savings_countdown.py` — calculates how many months are needed to reach a savings target.
- `expenses_list.py` — stores expenses in a list and calculates the total.
- `city_costs.py` — stores city cost data in a dictionary.
- `nested_city_costs.py` — stores multiple cities using nested dictionaries and calculates totals.
- `city_monthly_calculator.py` — asks the user for a city and returns the estimated monthly cost.

## Commands I practiced

- uv run python file.py
- git status
- git add .
- git commit -m "message"
- git push
- git log --oneline -5
- git log --oneline --max-count=10

## How to run scripts

```bash
uv run python income_calculator.py
uv run python budget_status.py
uv run python rent_check.py
uv run python move_decision.py
uv run python discount_calculator.py
uv run python city_list.py
uv run python savings_countdown.py
uv run python expenses_list.py
uv run python city_costs.py
uv run python nested_city_costs.py
uv run python city_monthly_calculator.py
```

## Example output

Example from `city_monthly_calculator.py`:

```bash
Which city do you want to check? bucharest

City cost estimate
City: Bucharest
Rent: $500
Food: $300
Transport: $50
Internet: $10
Total: $860
```

## What confused me

- input() returns text first, not a number.
- working tree clean does not always mean GitHub is updated.
- untracked, unstaged, and staged are different Git states.
- Exact spelling of commands, file names, and variable names matters.
- Why we use float(input()) for calculator math.
- Difference between untracked and unstaged in Git.
- A dictionary key must match exactly unless I clean the input first.
- `else` cannot exist alone; it must belong to an `if`.
- Indentation matters because Python uses it to know what belongs inside `if`, `else`, loops, and other blocks.

## Next step

Day 22: Functions deeper — split the city monthly calculator into smaller reusable functions.