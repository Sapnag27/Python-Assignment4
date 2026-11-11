# Practical-4: Recursion, Exceptions and Debugging

Python practical covering recursion, searching with recursion, input validation
using a custom exception, and debugging a recursive function.

## Files

| File | Description |
|------|-------------|
| `part-a.py` | Recursive `factorial(n)` |
| `part-b.py` | `factorial` with `ValueError` validation and a recursive `recursive_search` function, with test calls |
| `part-c.py` | Custom `InvalidInputError` and user input validation using `try / except / else / finally` |
| `part-d.py` | Buggy vs. fixed factorial with a debugging note |
| `practical4_recursion_exceptions.py` | All parts combined in one file |
| `main.py` | Entry point |
| `additional_tests.py` | Extra assert-based tests |

## How to run

```bash
python part-a.py
python part-b.py
python part-c.py
python part-d.py
python additional_tests.py
```

## Expected output

**part-a.py**
```
Factorial of 4: 24
```

**part-b.py**
```
120
2
-1
1
1
120
0
2
-1
```

**part-c.py** (input `9`)
```
Enter a non-negative integer: 9
Input accepted.
Input validation attempt finished.
Factorial: 362880
```

**part-d.py**
```
Buggy factorial(4): 0
Fixed factorial(0): 1
Fixed factorial(4): 24
```
