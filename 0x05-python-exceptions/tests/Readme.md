# Testing Documentation

This directory contains codes that test the python functions in the main parent directory.

## [0-safe_print_list.py](../0-safe_print_list.py)

To test the above function:

* Grant permission to [**0-main.py**](0-main.py) by running: ```chmod 0-main.py```
* To test: ```./0-main.py```

### Expected output with: [0-main.py](0-main.py):

```py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```

## [1-safe_print_integer.py](../1-safe_print_integer.py)

To test the above function:

* Grant permission to [**1-main.py**](1-main.py) by running: ```chmod 1-main.py```
* To test: ```./1-main.py```

### Expected output with: [1-main.py](1-main.py)

```py
89
-89
School is not an integer
```

## [2-safe_print_list_integers.py](../2-safe_print_list_integers.py)

To test the above function:

* Grant permission to [**2-main.py**](2-main.py) by running: ```chmod 2-main.py```
* To test: ```2-main.py```

### Expected output with: [2-main.py](2-main.py)

```py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```

## [3-safe_print_division.py](../3-safe_print_division.py)

To test the above function:

* Grant permission to: [**3-main.py**](3-main.py) by running: ```chmod 3-main.py```
* To test: ```3-main.py```

### Expected Output with: [3-main.py](3-main.py)

```py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```

## [4-list_division.py](../4-list_division.py)

To test the above function:

* Grant permission to: [**4-main.py**](4-main.py) by running: ```chmod 4-main.py```
* To test: ```./4-main.py```

### Expected output with: [4-main.py](4-main.py)

```py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
```

## [5-raise_exception.py](../5-raise_exception.py)

To test the above function:

* Grant permission to: [**5-main.py**](5-main.py) by running: ```chmod 5-main.py```
* To test: ```./5-main.py```

### Expected output with: [5-main.py](5-main.py)

```py
Exception raised
```

## [6-raise_exception_msg.py](../6-raise_exception_msg.py)

To test the above function:

* Grant permission to: [**6-main.py**](6-main.py) by running: ```chmod 6-main.py```
* To test: ```./6-main.py```

### Expected output with: [6-main.py](6-main.py)

```py
C is fun
```

## [100-safe_print_integer_err.py](../100-safe_print_integer_err.py)

To test the above function:

* Grant permission to: [**100-main.py**](100-main.py) by running: ```chmod 100-main.py```
* To test: ```./100-main.py```

### Expected output with: [100-main.py](100-main.py)

* 1st Output with no arguments:

```py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
School is not an integer
```

* 2nd Output with arguments:(```./100-main.py 2> /dev/null```)

```py
89
-89
School is not an integer
```

## [101-safe_function.py](../101-safe_function.py)

To test the above function:

* Grant permission to: [**101-main.py**](101-main.py) by running: ```chmod 101-main.py```
* To test: ```./101-main.py```

### Expected output with: [101-main.py](101-main.py)

* 1st Output with no arguments:

```py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
```

* 2nd Output with arguments:(```./101-main.py 2> /dev/null```)

```py
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None
```

## [103-python.c](../103-python.c)

To test the above function:

* Compile the library: ```gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 ../103-python.c```
* Grant permission to: [**103-tests.py**](103-tests.py) by running: ```chmod 103-tests.py```
* To test: ```./103-tests.py```

### Expected output with: [103-tests.py](103-tests.py)

```py
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: ??
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
[.] float object info
  value: 6.0
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: School
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
[.] float object info
  value: 3.14
[-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793]
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: float
[.] float object info
  value: -1.0
Element 1: float
[.] float object info
  value: -0.1
Element 2: float
[.] float object info
  value: 0.0
Element 3: float
[.] float object info
  value: 1.0
Element 4: float
[.] float object info
  value: 3.14
Element 5: float
[.] float object info
  value: 3.14159
Element 6: float
[.] float object info
  value: 3.14159265
Element 7: float
[.] float object info
  value: 3.141592653589793
[.] float object info
  [ERROR] Invalid Float Object
[*] Python list info
  [ERROR] Invalid List Object
```
