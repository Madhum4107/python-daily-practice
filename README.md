# Python Fundamentals — Practice Log

A beginner repository documenting variables, data types, arithmetic, conditional logic, and input/output exercises.

> Learning exercises—not portfolio showcase projects. The code is intentionally small and focuses on fundamentals.

## Topics

| Topic | Examples |
|---|---|
| Variables and data types | `variable.py`, `datatype.py` |
| Arithmetic | `operators.py`, `question.3.py` |
| Conditionals | `if else.py`, `ifelse.py`, comparison, pass/fail, status examples |
| Input/output | `question.1.py`–`question.4.py` |

## Run

Requires Python 3.

```bash
python datatype.py
python "if else comparator.py"
python "if else exesise.py"
```

Most examples use console input. Read the prompt, enter a value, and follow the output.

## Validation

```bash
python -m compileall -q .\n\nAvoid naming files after Python standard-library modules (for example `operator.py`) because they can shadow imports and break the interpreter.
```

The CI workflow checks Python syntax on pushes and pull requests. The exercises are learning snippets and have not all been converted into reusable modules yet.

**Madhumitha M** · B.E. CSE (AI & ML), 2028
