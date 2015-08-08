# STEPlang
an esoteric stack-based programming language.


# USAGE

```python
python step.py <filepath>
```

# ABOUT
I built step to alleviate a problem that I had always had with stack-based languages- that I could somehow never get my operators in the correct order. Now there's no confusion, since the step programmer has to explicitly define the order of operations.

# DOCUMENTATION

## defining order

To add a set of instructions to the operation queue, enclose it in the number followed by a period and then a period followed by the number. Example:
```
0. (This is the first code block) .0
1. (This is the second code block) .1
```
If one operation encloses another, the code from the first operation will be run twice. Example:
```
1. 0. (This is run twice .0 (this is run once) .1
```
