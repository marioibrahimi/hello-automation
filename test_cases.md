# City Calculator Manual Test Cases

## Test 1 - Exact valid city

Input:
Bucharest

Expected output:
City: Bucharest
Total: $860

Actual output:
City: Bucharest
Total: $860

Result:
PASS

## Test 2 — Exact valid city

Input:
Tbilisi

Expected output:
City: Tbilisi
Total: $780

Actual output:
City: Tbilisi
Total: $780

Result:
PASS

## Test 3 — Exact valid city

Input:
Chernivtsi

Expected output:
City: Chernivtsi
Total: $595

Actual output:
City: Chernivtsi
Total: $595

Result:
PASS

## Test 4 — Lowercase valid city

Input:
bucharest

Expected output:
City: Bucharest
Total: $860

Actual output:
City: Bucharest
Total: $860

Result:
PASS

## Test 5 — Uppercase valid city

Input:
TBILISI

Expected output:
City: Tbilisi
Total: $780

Actual output:
City: Tbilisi
Total: $780

Result:
PASS

## Test 6 — Valid city with outer spaces

Input:
  Chernivtsi  

Expected output:
City: Chernivtsi
Total: $595

Actual output:
City: Chernivtsi
Total: $595

Result:
PASS

## Test 7 — Invalid city

Input:
Paris

Expected output:
City not found.
Available cities: Chernivtsi, Bucharest, Tbilisi

Actual output:
First run:
City not found.
Availale cities: Chernivtsi, Bucharest, Tbilisi

Retest:
City not found.
Available cities: Chernivtsi, Bucharest, Tbilisi

Result:
PASS after fix

## Test 8 — Empty input

Input:
Press Enter without typing anything

Expected output:
City not found.
Available cities: Chernivtsi, Bucharest, Tbilisi

Actual output:
City not found.
Available cities: Chernivtsi, Bucharest, Tbilisi

Result:
PASS

## Test 9 — Mixed capitalization

Input:
bUcHaReSt

Expected output:
City: Bucharest
Total: $860

Actual output:
City: Bucharest
Total: $860

Result:
PASS


## Test 10 — Lowercase with outer spaces

Input:
  tbilisi  

Expected output:
City: Tbilisi
Total: $780

Actual output:
City: Tbilisi
Total: $780

Result:
PASS