## Day 5 - Thu 25 Jun 2026

Time studied: about 60-75 minutes

What I studied:
Python input(), f-strings, float conversion, and Git diff.

What I built:
I upgraded income_calculator.py so the user can enter gross hourly rate, hours per month, and tax rate percentage.

Commands used:
cd
pwd
ls
cat
uv run python
git status
git diff
git add
git commit
git push

Error I hit:
I used the wrong variable name when calculating tax_rate. I wrote a name that did not match the variable I created.

How I fixed it:
I read the error message, checked the line number, matched the variable name correctly, saved the file, and ran the program again.

What I learned:
- input() always returns a string first.
- float() converts text like "6.96" into a decimal number.
- tax_rate_percent / 100 converts 32 into 0.32.
- git diff shows the exact line changes before committing.
- git add stages the latest version of a file.
- If I edit after git add, I need to run git add again.
- "working tree clean" means no uncommitted changes are left.

GitHub commit:
Day 5: add user input to income calculator

Tomorrow's next task:
Day 6 - Git basics: status, add, commit, log. Recheck commits and make sure at least 3 commits are visible.