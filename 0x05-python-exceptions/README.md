# ![plot](css/title.svg)

## Resources

* [Errors and Exceptions](https://intranet.alxswe.com/rltoken/Yj7sDOzmKwICSHr7WEAW3A)
* [Learn to Program 11 Static & Exception Handling](https://intranet.alxswe.com/rltoken/xASzXarhF1sBhzYkJ14LvQ) (starting at minute 7)

### Learning Objectives

* Why Python programming is awesome
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

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

### 0. Safe list printing

This is a function that prints ```x``` elements of a list.

* Prototype: ```def safe_print_list(my_list=[], x=0):```
* ```my_list``` can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* ```x``` represents the number of elements to print
* ```x``` can be bigger than the length of ```my_list```
* Returns the real number of elements printed
* You have to use ```try: / except:```
* You are not allowed to import any module
* You are not allowed to use ```len()```

```py
guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$
```

### 1. Safe printing of an integers list

This is a function that prints an integer with ```"{:d}".format().```

* Prototype: ```def safe_print_integer(value):```
* ```value``` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns ```True``` if ```value``` has been correctly printed (it means the ```value``` is an integer)
* Otherwise, returns ```False```
* I have used ```try: / except:``` 😋
* I have used ```"{:d}".format()``` to print as integer 😋
* No module imported! 🥴
* ```type()``` not used anywhere 🥴

### 2. Print and count integers

This is a function that prints the first ```x``` elements of a list and only integers.

* Prototype: ```def safe_print_list_integers(my_list=[], x=0):```
* ```my_list``` can contain any type (integer, string, etc.)
* All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
* ```x``` represents the number of elements to access in ```my_list```
* ```x``` can be bigger than the length of ```my_list``` - if it’s the case, an exception is expected to occur
* Returns the real number of integers printed
* I have used ```try: / except:``` 😋
* I have used ```"{:d}".format()``` to print an integer 😋
* No module imported! 🥴
* ```len()``` is not used anywhere 🥴

### 3. Integers division with debug

This is a function that divides 2 integers and prints the result.

* Prototype: ```def safe_print_division(a, b):```
* You can assume that ```a``` and ```b``` are integers
* The result of the division should print on the ```finally:``` section preceded by ```Inside result:```
* Returns the value of the division, otherwise: ```None```
* I have used ```try: / except: / finally:``` 😋
* I have used ```"{}".format()``` to print the result 😋
* No module imported! 🥴

### 4. Divide a list

This is a function that divides element by element 2 lists.

* Prototype: ```def list_division(my_list_1, my_list_2, list_length):```
* ```my_list_1``` and ```my_list_2``` can contain any type (integer, string, etc.)
* ```list_length``` can be bigger than the length of both lists
* Returns a new list (length = ```list_length```) with all divisions
* If 2 elements can’t be divided, the division result should be equal to ```0```
* If an element is not an integer or float:
  * print: ```wrong type```
* If the division can’t be done (```/0```):
  * print: ```division by 0```
* If ```my_list_1``` or ```my_list_2``` is too short
  * print: ```out of range```
* I have used ```try: / except: / finally:``` 😋
* No module imported! 🥴

### 5. Raise exception

This is a function that raises a type exception.

* Prototype: ```def raise_exception():```
* No module imported! 🥴

### 6. Raise a message

This is a function that raises a name exception with a message.

* Prototype: ```def raise_exception_msg(message=""):```
* No module imported! 🥴

### 7. Safe integer print with error message

This a function that prints an integer.

* Prototype: ```def safe_print_integer_err(value):```
* ```value``` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns ```True``` if ```value``` has been correctly printed (it means the ```value``` is an integer)
* Otherwise, returns ```False``` and prints in ```stderr``` the error precede by ```Exception:```
* I have used ```try: / except:``` 😋
* I have used ```"{:d}".format()``` to print as integer 😋
* I have not used ```type()``` anywhere 🥴

### 8. Safe function

This is a function that executes a function safely.

* Prototype: ```def safe_function(fct, *args):```
* You can assume ```fct``` will be always a pointer to a function
* Returns the result of the function,
* Otherwise, returns ```None``` if something happens during the function and prints in ```stderr``` the error precede by ```Exception:```
* I have used ```try: / except:``` 😋

### 9. ByteCode -> Python #4

This is a Python function ```def magic_calculation(a, b):``` that does exactly the same as the following Python bytecode:

```py
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```

### 10. CPython #2: PyFloatObject

Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.

![disaster](css/070710952984e4d126e114405cefe83af2271ce8.gif)

Python lists:

* Prototype: ```void print_python_list(PyObject *p);```
* Format: see example
* If ```p``` is not a valid ```PyListObject```, print an error message (see example)

Python bytes:

* Prototype: ```void print_python_bytes(PyObject *p);```
* Format: see example
* Line “first X bytes”: print a maximum of 10 bytes
* If ```p``` is not a valid ```PyBytesObject```, print an error message (see example)

Python float:

* Prototype: ```void print_python_float(PyObject *p);```
* Format: see example
* If ```p``` is not a valid ```PyFloatObject```, print an error message (see example)
* Read ```/usr/include/python3.4/floatobject.h```

About:

* Python version: 3.4
* I have used C standard library
* The shared library can be compiled with: ```gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c```
* Am not allowed to use the following macros/functions:
  * Py_SIZE
  * Py_TYPE
  * PyList_Size
  * PyList_GetItem
  * PyBytes_AS_STRING
  * PyBytes_GET_SIZE
  * PyBytes_AsString
  * PyBytes_AsStringAndSize
  * PyFloat_AS_DOUBLE
  * PySequence_GetItem
  * PySequence_Fast_GET_SIZE
  * PySequence_Fast_GET_ITEM
  * PySequence_ITEM
  * PySequence_Fast_ITEMS

**NOTE:**

* The python script will be launched using the ```-u``` option (Force ```stdout``` to be unbuffered).
* It is strongly advised to either use ```setbuf(stdout, NULL);``` or ```fflush(stdout)``` in your C functions IF you choose to use ```printf```. The reason to that is that Python```s```print ```and libC```s ```printf``` don’t share the same buffer, and the output can appear disordered.

**NOTE:** Check out the [testing documentation](tests/Readme.md)

![greeting](../files/greeting.svg)
