# ![plot](css/title.svg)

## Resources

* [Data structures](https://intranet.alxswe.com/rltoken/GmgoSUtBbHBW8suWkws51g)
* [Lambda, filter, reduce and map](https://intranet.alxswe.com/rltoken/53f4kKVT0-jyzrJstOSJWg)
* [Learn to Program 12 Lambda Map Filter Reduce](https://intranet.alxswe.com/rltoken/v9eyFryhkYmxDI13iTx2VA)

### Learning Objectives

* Why Python programming is awesome
* What are sets and how to use them
* What are the most common methods of set and how to use them
* When to use sets versus lists
* How to iterate into a set
* What are dictionaries and how to use them
* When to use dictionaries versus lists or sets
* What is a key in a dictionary
* How to iterate over a dictionary
* What is a lambda function
* What are the map, reduce and filter functions

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

## Tasks

### 0. Squared simple

This is a function that computes the square value of all integers of a matrix.

Prototype: ```def square_matrix_simple(matrix=[]):```
```matrix``` is a 2 dimensional array
Returns a new matrix:
Same size as ```matrix```
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, ```map```, etc.

```py
guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$
```

### 1. Search and replace

This is a function that replaces all occurrences of an element by another in a new list.

* Prototype: ```def search_replace(my_list, search, replace):```
* ```my_list``` is the initial list
* ```search``` is the element to replace in the list
* ```replace``` is the new element
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$
```

### 2. Unique addition

This is a function that adds all unique integers in a list (only once for each integer).

* Prototype: ```def uniq_add(my_list=[]):```
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$
```

### 3. Present in both

This is a function that returns a set of common elements in two sets.

* Prototype: ```def common_elements(set_1, set_2):```
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$
```

### 4. Only differents

Write a function that returns a set of all elements present in only one set.

* Prototype: ```def only_diff_elements(set_1, set_2):```
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$
```

### 5. Number of keys

This is a function that returns the number of keys in a dictionary.

* Prototype: ```def number_keys(a_dictionary):```
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$
```

### 6. Print sorted dictionary

This is a function that prints a dictionary by ordered keys.

* Prototype: ```def print_sorted_dictionary(a_dictionary):```
* It is assumed that all keys are strings 😋
* Keys are sorted by alphabetic order
* Only keys of the first level are sorted(but the keys of a dictionary inside the main dictionary, remain unsorted). 😋
* Dictionary values can have any type 😋
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$
```

### 7. Update dictionary

This is a function that replaces or adds key/value in a dictionary.

* Prototype: ```def update_dictionary(a_dictionary, key, value):```
* ```key``` argument will be always a string
* ```value``` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/0x04$
```

### 8. Simple delete by key

This is a function that deletes a key in a dictionary.

* Prototype: ```def simple_delete(a_dictionary, key=""):```
* ```key``` argument will be always a string
* If a key doesn’t exist, the dictionary won’t change
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/0x04$
```

### 9. Multiply by 2

This is a function that returns a new dictionary with all values multiplied by 2

* Prototype: ```def multiply_by_2(a_dictionary):```
* It is assumed that all values are only integers
* It returns a new dictionary
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/0x04$
```

### 10. Best score

This is a function that returns a key with the biggest integer value.

* Prototype: ```def best_score(a_dictionary):```
* It is assumed that all values are only integers
* If no score found, return ```None```
* It is assumed that all students have a different score
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$
```

### 11. Multiply by using map

This is a function that returns a list with all values multiplied by a number without using any loops.

* Prototype: ```def multiply_list_map(my_list=[], number=0):```
* Returns a new list:
  * Same length as ```my_list```
  * Each value is multiplied by ```number```
* Initial list should is not modified
* No module imported! 🥴
* I have used ```map```
* The file is max 3 lines

```py
guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$
```

### 12. Roman to Integer

**Technical interview preparation**:

* No googling anything 🥴
* Whiteboard first
This is a function ```def roman_to_int(roman_string):``` that converts a [```Roman numeral```](https://intranet.alxswe.com/rltoken/oSuwqUrL0BL_hi4VqVvs_g) to an integer.

* It is assumed that the number will be between 1 to 3999.
* ```def roman_to_int(roman_string)``` it returns an integer
* If the ```roman_string``` is not a string or ```None```, return 0

```py
guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/0x04$
```

### 13. Weighted average!

This is a function returns the weighted average of all integers tuple ```(<score>, <weight>)```

* Prototype: ```def weight_average(my_list=[]):```
* Returns ```0``` if the list is empty
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./100-main.py
Average: 2.80
guillaume@ubuntu:~/0x04$
```

### 14. Squared by using map

This is a function that computes the square value of all integers of a matrix using ``````map

* Prototype: ```def square_matrix_map(matrix=[]):```
* ```matrix``` is a 2 dimensional array
* Returns a new matrix:
  * Same size as ```matrix```
  * Each value should be the square of the value of the input
* Initial matrix should not be modified
* No module imported! 🥴
* I have used ```map```
* No use of ```for``` or ```while``` 🥴
* The file is max 3 lines

```py
guillaume@ubuntu:~/0x04$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$
```

### 15. Delete by value

This a function that deletes keys with a specific value in a dictionary.

* Prototype: ```def complex_delete(a_dictionary, value):```
* If the value doesn’t exist, the dictionary won’t change
* All keys having the searched value have to be deleted
* No module imported! 🥴

```py
guillaume@ubuntu:~/0x04$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
guillaume@ubuntu:~/0x04$
```

### 16. CPython #1: PyBytesObject

Create two C functions that print some basic info about Python lists and Python bytes objects.

![Ni! Ni!](css/8030f8429cb90b3fc145b994112e2dae8c4030e0.gif)
**BE AWARE:** This task was set by a witch who is not happy with the progress of your entire community!!!

Python lists:

* Prototype: ```void print_python_list(PyObject *p);```
* Format: see example

Python bytes:

* Prototype: ```void print_python_list(PyObject *p);```
* Format: see example
* Line “first X bytes”: print a maximum of 10 bytes
* If ```p``` is not a valid ```PyBytesObject```, print an error message (see example)
* Read ```/usr/include/python3.4/bytesobject.h```
About:

* Python version: 3.4
* Your shared library will be compiled with this command line: ```gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c```
* You are not allowed to use the following macros/functions:
  * ```Py_SIZE```
  * ```Py_TYPE```
  * ```PyList_GetItem```
  * ```PyBytes_AS_STRING```
  * ```PyBytes_GET_SIZE```

```py
julien@ubuntu:~/CPython$ python3 103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
julien@ubuntu:~/CPython$
```

![greeting](../files/greeting.svg)
