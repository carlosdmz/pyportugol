# pyportugol
Small project for a "Portugol" transpiler made in Python 3.6. This code transpiles
a text input from main.py in the giving order:
1. Splits texts into lines of code.
2. Lexes tokens from line.
2. Parses tokens.
3. Evaluate tokens into expressions and statements.

The result is a portugol-like toy programming language that can:
- Print stuff (numbers, strings, etc).
- Read input (number only, but make it infer types is easy to be implemented though).
- Basic math stuff (add, sub, mul, div).
- Numeric comparison (more, less, more-equals, less-equals).
- Basic programming logic (if-else).
- Loops with steps and expressions evaluation.
