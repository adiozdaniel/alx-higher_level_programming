# ![plot](css/title.svg)

## Resources

* [3.1.3. Lists](https://intranet.alxswe.com/rltoken/VarQbHxfmbnpGnaGp3Nb_A)
* [Data structures](https://intranet.alxswe.com/rltoken/2aa8Mp-V2eSieGeX3OX8yQ) (until ```5.3. Tuples and Sequences``` included)
* [Learn to Program 6 : Lists](https://intranet.alxswe.com/rltoken/BX2_CuHj1sq4eYGiXbCYSg)

### Learning Objectives

* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the ```del``` statement and how to use it

## Requirements

### Python Scripts

* Allowed editors: ```vi, vim, emacs```
* All the files can be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All the files end with a new line
* The first line of all the files are exactly ```#!/usr/bin/python3```
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* The code is using the pycodestyle (version ```2.8.*```)
* All the files are executable (given execution permission)
* The length of the files can be tested using ```wc```

### C

* Allowed editors: ```vi, vim, emacs```
* All the files can be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All the files end with a new line
* Your code should use the ```Betty``` style. It will be checked using [betty-style.pl](https://github.com/alx-tools/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl)
* No global variables used
* No more than 5 functions per file
* The ```main.c``` files are used for testing purposes
* All prototypes are included in the guarded header file called ```lists.h```

## Tasks

### 0. Print a list of integers

This is a function that prints all integers of a list.

* Prototype: ```def print_list_integer(my_list=[]):```
* Format: one integer per line. See example
* No module imported! 🥴
* It is assumed that, the list only contains integers 😋
* No casting of integers into strings 🥴
* ```str.format()``` used to print integers 😋

```py
guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$
```

### 1. Secure access to an element in a list

This is a function that retrieves an element from a list like in C.

* Prototype: ```def element_at(my_list, idx):```
* If ```idx``` is negative, the function should return ```None```
* If ```idx``` is out of range (> of number of element in ```my_list```), the function should return ```None```
* No module imported! 🥴
* No use of: ```try/except``` 🥴

```py
guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$
```

### 2. Replace element

This is a function that replaces an element of a list at a specific position (like in C).

* Prototype: ```def replace_in_list(my_list, idx, element):```
* If ```idx``` is negative, the function should not modify anything, and returns the original list
* If ```idx``` is out of range (> of number of element in ```my_list```), the function should not modify anything, and returns the original list
* No module imported! 🥴
* No use of: ```try/except``` 🥴

```py
guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$
```

### 3. Print a list of integers... in reverse!

This is a function that prints all integers of a list, in reverse order.

* Prototype: ```def print_reversed_list_integer(my_list=[]):```
* Format: one integer per line. See example
* No module imported! 🥴
* It is assumed that, the list only contains integers 😋
* No casting of integers into strings 🥴
* ```str.format()``` is used to print integers 😋

```py
guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$
```

### 4. Replace in a copy

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

* Prototype: ```def new_in_list(my_list, idx, element):```
* If ```idx``` is negative, the function should return a copy of the original ```list```
* If ```idx``` is out of range (> of number of element in ```my_list```), the function should return a copy of the original ```list```
* No module imported! 🥴
* No use of: ```try/except``` 🥴

```py
guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$
```

### 5. Can you C me now?

This is a function that removes all characters ```c``` and ```C``` from a string.

* Prototype: ```def no_c(my_string):```
* The function should return the new string
* No module imported! 🥴
* No use of ```str.replace()``` 🥴

```py
guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$
```

### 6. Lists of lists = Matrix

This is a function that prints a matrix of integers.

* Prototype: ```def print_matrix_integer(matrix=[[]]):```
* Format: see example
* No module imported! 🥴
* It is assumed that, the list only contains integers 😋
* No casting of integers into strings 🥴
* ```str.format()``` Used to print integers 😋

```py
guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$
```

### 7. Tuples addition

This is a function that adds 2 tuples.

* Prototype: ```def add_tuple(tuple_a=(), tuple_b=()):```
* Returns a tuple with 2 integers:
  * The first element should be the addition of the first element of each argument
  * The second element should be the addition of the second element of each argument
* No module imported! 🥴
* It is assumed that, the two tuples only contains integers 😋
* If a tuple is smaller than 2, use the value ```0```for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

```py
guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$
```

### 8. More returns!

This is a function that returns a tuple with the length of a string and its first character.

* Prototype: ```def multiple_returns(sentence):```
* If the sentence is empty, the first character should be equal to ```None```
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$
```

### 9. Find the max

This is a function that finds the biggest integer of a list.

* Prototype: ```def max_integer(my_list=[]):```
* If the list is empty, return ```None```
* It is assumed that, the list only contains integers 😋
* No module imported! 🥴
* No use of the builtin ```max()```

```py
guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$
```

### 10. Only by 2

This is a function that finds all multiples of 2 in a list.

* Prototype: ```def divisible_by_2(my_list=[]):```
* Return a new list with ```True``` or ```False```, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* No module imported! 🥴

### 11. Delete at

This is a function that deletes the item at a specific position in a list.

* Prototype: ```def delete_at(my_list=[], idx=0):```
* If ```idx``` is negative or out of range, nothing change (returns the same list)
* No use of ```pop()```
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$
```

### 12. Switch

Complete the source code in order to switch value of ```a``` and ```b```

* You can find the source code [```here```](https://intranet.alxswe.com/rltoken/9kg8R2hfPSN5pClcVAeGlA)
* The program is exactly 5 lines

```py
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$
```

### 13. Linked list palindrome

Technical interview preparation:

* You are not allowed to google anything
* Whiteboard first
Write a function in C that checks if a singly linked list is a palindrome.

* Prototype: ```int is_palindrome(listint_t **head);```
* Return: ```0``` if it is not a palindrome, ```1``` if it is a palindrome
* An empty list is considered a palindrome

```py
carrie@ubuntu:0x03$
carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
carrie@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
carrie@ubuntu:0x03$
```

### 14. CPython #0: Python lists

CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.

* All files can be interpreted/compiled on Ubuntu 14.04 LTS

![aww](css/7e7834b535261d05532fb80a9304f7051c4ad7ac.gif)

Create a C function that prints some basic info about Python lists.

* Prototype: ```void print_python_list_info(PyObject *p);```
* Format: see example
* Python version: 3.4
* The shared library will be compiled with this command line: ```gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c```
* OS: ```Ubuntu 14.04 LTS```
* Start by reading:
  * listobject.h
  * object.h
  * [```Common Object Structures```](https://intranet.alxswe.com/rltoken/jmRTk4m1VSzjsu3QTGaC6w)
  * [```List Objects```](https://intranet.alxswe.com/rltoken/7V1HlQRESjCqrKrw_O_Urw)

```py
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
julien@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py 
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
julien@CPython:~/CPython$
```

![greeting](../files/greeting.svg)
