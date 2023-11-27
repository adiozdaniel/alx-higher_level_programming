# 0x00. Python - Hello, World

![plot](../files/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)

## Author’s disclaimer

```b
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.

Enjoy!

- Guillaume

```

## Resources

* [The Python tutorial](https://intranet.alxswe.com/rltoken/JsFCs_NBzMAR7-XPAZ9BoA) (only the first three chapters below)
* [Whetting Your Appetite](https://intranet.alxswe.com/rltoken/kifRlLG2iMX5AZiW8lrCMg)
* [Using the Python Interpreter](https://intranet.alxswe.com/rltoken/RVpfAuagCo9SdfYeoHd6jg)
* [An Informal Introduction to Python](https://intranet.alxswe.com/rltoken/bVps0ZPWq7qVZ7vc-eJGTw) (Read up until “3.1.2. Strings” included)
* [How To Use String Formatters in Python 3](https://intranet.alxswe.com/rltoken/Ju0J8BxkuPX5yKZctyKfsQ)
* [Learn to Program](https://intranet.alxswe.com/rltoken/szBsJ-Qyig_RrImN7RGlOg)
* [Pycodestyle – Style Guide for Python Code](https://intranet.alxswe.com/rltoken/tgYt-0zVy1T4sDlE9ohxnA)

### Learning Objectives

* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using ```print```
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code with ```pycodestyle```

## Requirements

### Python Scripts

* Editor used: ```Vs Code with Vim extension``` 😋
* All these files can be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All these files end with a new line
* The first line of all these files are exactly ```#!/usr/bin/python3```
* These code uses pycodestyle (version ```2.8.*```)
* All these files have permissions to be executable
* The length of these files has been tested using ```wc```

### Shell Scripts

* Editor used: ```Vs Code with Vim extension``` 😋
* All these scripts can be tested on Ubuntu 20.04 LTS
* All these scripts are exactly two lines long (```wc -l file``` should print 2)
* All these files are with a new line
* The first line of all these files start with exactly ```#!/bin/bash```
* All these files have permissions to be executable

### C Scripts

* Editor used: ```Vs Code with Vim extension``` 😋
* All these files can be compiled on Ubuntu 20.04 LTS using gcc, using the options ```-Wall -Werror -Wextra -pedantic -std=gnu89```
* All these files end with a new line
* These code uses the ```Betty``` style. It can be checked using [```betty-style.pl```](https://github.com/alx-tools/Betty/blob/master/betty-style.pl) and [```betty-doc.pl```](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl)
* I have not used any global variables 🥴
* There are no more than five functions per file
* In the following examples, the ```main.c``` files are shown as examples. You can use them to test these functions. You can use any other ```main.c``` files at compilation.
* The prototypes of all these functions are included in the header file called ```lists.h```
* The header file(s) include guards

## More Info

### Zen

```b
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

### Pycodestyle

```Pycodestyle``` is now the [```new standard of Python style code```](https://intranet.alxswe.com/rltoken/UQ25jC6sA5XqZl6ZZIdAaw)

![plot](../files/Flyingcircus_2.jpg)

## Tasks

### 0. Run Python file

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable ```$PYFILE```

```bash
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```

### 1. Run inline

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable ```$PYCODE```

```Bash
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Best School: 98
guillaume@ubuntu:~/py/0x00$
```

### 2. Hello, print

Write a Python script that prints exactly ```"Programming is like building a multilingual puzzle```, followed by a new line.

* Use the function ```print```

```Python3
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

### 3. Print integer

Complete this [```source code```](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable ```number```, followed by ```Battery street```, followed by a new line.

* You can find the source code [```here```](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
* The output of the script should be:
  * the number, followed by ```Battery street```,
  * followed by a new line
* You are not allowed to cast the variable ```number``` into a string
* Your code must be 3 lines long
* You have to use f-strings [```tips```](https://intranet.alxswe.com/rltoken/Ju0J8BxkuPX5yKZctyKfsQ)

```Python3
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```

### 4. Print float

Complete the source code in order to print the float stored in the variable ```number``` with a precision of 2 digits.

* You can find the source code [```here```](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
* The output of the program should be:
  * ```Float:```, followed by the float with only 2 digits
  * followed by a new line
* No casting of ```number``` to string in this code
* I have used f-strings

```Python3
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```

### 5. Print string

Complete this [```source code```](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable ```str```, followed by its first 9 characters.

* You can find the source code [```here```](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
* The output of the program should be:
  * 3 times the value of ```str```
  * followed by a new line
  * followed by the 9 first characters of ```str```
  * followed by a new line
* No loops or conditional statements
* The program is maximum 5 lines long

```Python3
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$
```

### 6. Play with strings

Complete this [```source code```](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print ```Welcome to Holberton School!```

* You can find the source code [```here```](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
* No loops or conditional statements
* Variables used ```str1``` and ```str2```
* Program is exactly 5 lines long

```Python
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$
```

### 7. Copy - Cut - Paste

Complete this [```source code```](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)

* You can find the source code [```here```](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
* No loops or conditional statements
* Your program should be exactly 8 lines long
* ```word_first_3``` should contain the first 3 letters of the variable ```word```
* ```word_last_2``` should contain the last 2 letters of the variable ```word```
* ```middle_word``` should contain the value of the variable ```word``` without the first and last letters

```Python
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$
```

### 8. Create a new sentence

Complete this [```source code```](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print ```object-oriented programming with Python```, followed by a new line.

* You can find the source code [```here```](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
* No loops or conditional statements
* Program is exactly 5 lines long
* No new variables
* No use string literals

```Python3
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$
```

### 9. Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

* Your script should be maximum 98 characters long (please check with ```wc -m 9-easter_egg.py```)

```Python3
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
```

### 10. Linked list cycle

**Technical interview preparation:**

* Whiteboard first
* This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.

* Prototype: ```int check_cycle(listint_t *list);```
* Return: ```0``` if there is no cycle, ```1``` if there is a cycle

Requirements:

* Only these functions are allowed: ```write, printf, putchar, puts, malloc, free```
* compile with ```gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle```
* then run with ```./cycle```

Sample output:

```b
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
```

### 11. Hello, write

Write a Python script that prints exactly ```and that piece of art is useful - Dora Korpar, 2015-10-19```, followed by a new line.

* Use the function ```write``` from the ```sys``` module
* No use of ```print```
* This script prints to ```stderr```
* This script exits with the status code ```1```

```python
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$
```

### 12. Compile

Write a script that compiles a Python script file.

The Python file name will is stored in the environment variable ```$PYFILE```

The output filename has is ```$PYFILEc``` (ex: ```export PYFILE=my_main.py``` => output filename: ```my_main.pyc```)
To test:

* ```cat main.pyc | zgrep -c "Best School"```
  * ```1```
* ```od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT```
  * expected output can be a bit different

```b
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
```

### 13. ByteCode -> Python #1

Write the Python function ```def magic_calculation(a, b):``` that does exactly the same as the following Python bytecode:

```b
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

* Tip: [Python bytecode](https://intranet.alxswe.com/rltoken/B38QeZHREbvgq-wY7Ze3vQ)

**coded with lots of love 😘 to:**
The Queen of my heart ~ 🥰 Centrine Adioz 🥰
