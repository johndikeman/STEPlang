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

## appending to the stack

Anything that isn't in the list of reserved operators is pushed to the stack. If you have a string that is MORE THAN ONE WORD to push onto the stack, enclose it in single quotes. If it's just one word and you out quotes around it, bad stuff happens- so don't :-)

## reserved operators

### output

This pops the top of the stack and writes it to stdout.

### input

This grabs user input and pushes it to the stack.

TODO: figure out a more platform agnostic alternative to Python's ```input()``` because it might not work sometimes?¿ iunno

### pause

this pops the top value from the stack and waits for that number of seconds.

### dupe

This adds a copy of the top value of the stack to the stack. ((Every good value needs a friend))

### rand

Unimplemented.

TODO: implement this.

### goto

This pops the top value from the stack and starts to execute that number operator. After that number is executed, it continues like normal FROM that number. Ie if you went to zero, the next one executed would be one, and so on and so forth.

TODO: implement a "prev" op that sends the pointer back to where it was before the goto.

### +, -, *, /, %
These all do the things you would expect them to and push the result onto the stack.

### <, >, ==, !=
These also all do the things you would expect them to, and will push "yea" onto the stack if true, and "nope" onto the stack if not.

### ?
The question mark serves as the if in step. Include it WITH any other operator, and that operator is run if the top value of the stack is "yea". Example:

```
0. true yea ?output .0
```
(This prints "true")

The question marks can go anywhere inside the operator, so you can be silly if you wanna.

### end
This terminates the step script.



