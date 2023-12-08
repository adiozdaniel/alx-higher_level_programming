# Expected Outputs cases

This is specifically for **[103-python.c](../103-python.c)**

## Compilation

This compilation depends on the specific place you have stored your python Include files, reference to the header files.
If you have python version 3.4 installed, then the expected path will be: ```usr/include/python3.4```.
This is the path after ```-I/usr/include/python3.4```.
If you have used other applications like ```snap```, then it might be different.

For you to know the path of your ```python```:

* Depending on the version... ```which python3```.
* Navigate to this directory to locate include files

In my case, I just downloaded [python](https://www.python.org/downloads/) and extracted it directly:

* Custom compilation: ```gcc -g -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPythonHBTN.so -fPIC -I/usr/local/include/python3.4m/ ../103-python.c```

## Running

```./[0-main.py]```

[replace this with ```main```file]

### Expected outputs:

**[0-main.py](0-main.py)**

```py
[Expected]
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00

(90 chars long)
[stderr]: [Anything]
(0 chars long)
```

**[main_1.py](main_1.py)**

```py
[Expected]
[.] bytes object info
  size: 3
  trying string: aaa
  first 4 bytes: 61 61 61 00

(82 chars long)
[stderr]: [Anything]
(0 chars long)
```

**[main_2.py](main_2.py)**

```py
[Expected]
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20

(159 chars long)
[stderr]: [Anything]
(0 chars long)
```

**[main_3.py](main_3.py)**

```py
[Expected]
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

(285 chars long)
[stderr]: [Anything]
(0 chars long) [Diff had to be removed because it was too long]
```

**[main_4.py](main_4.py)**

```py
[Expected]
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

(463 chars long)
[stderr]: [Anything]
(0 chars long) [Diff had to be removed because it was too long]
```

**[main_5.py](main_5.py)**

```py
[Expected]
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

(860 chars long)
[stderr]: [Anything]
(0 chars long) [Diff had to be removed because it was too long]
```

**[main_6.py](main_6.py)**

```py
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
```

**[main_7.py](main_7.py)**

```py
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
```

**[main_8.py](main_8.py)**

```py
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
```

**[main_9.py](main_9.py)**

```py
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
```

**[main_10.py](main_10.py)**

```py
[Expected]
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object

(139 chars long)
[stderr]: [Anything]
(0 chars long)
```
