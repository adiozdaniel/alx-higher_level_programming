# THIS IS A TEST DIRECTORY

It contains the files used to debug the functions

## 0. Print list

### For testing [0-print_dlistint.c](../0-print_dlistint.c)

#### Tested by: [0-main.c](0-main.c)

* Compile: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 0-main.c ../0-print_dlistint.c -o a```

* Run: ```./a```
* **Expected output:**

```py
9
8
-> 2 elements
```

## 1. List length

### For testing [1-dlistint_len.c](../1-dlistint_len.c)

### Tested by: [1-main.c](1-main.c)

* Compile: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 1-main.c ../1-dlistint_len.c -o b```

* Run: ```./b```
* **Expected output:**

```py
-> 2 elements
```

## 2. Add node

### For testing [2-add_dnodeint.c](../2-add_dnodeint.c)

#### Tested by: [2-main.c](2-main.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 2-main.c ../2-add_dnodeint.c 0-print_dlistint.c -o c```
* Running: ```./c```
* **Expected result:**

```py
1024
402
98
4
3
2
1
0
```

## 3. Add node at the end

### For Testing: [3-add_dnodeint_end.c](../3-add_dnodeint_end.c)

#### Tested by: [3-main.c](3-main.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 3-main.c ../3-add_dnodeint_end.c ../0-print_dlistint.c -o d```
* Running: ```./d```
* **Expected result:**

```py
0
1
2
3
4
98
402
1024
```

## 4. Free list

### For testing: [4-free_dlistint.c](../4-free_dlistint.c)

#### Tested by: [4-main.c](4-main.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 4-main.c 3-add_dnodeint_end.c 0-print_dlistint.c 4-free_dlistint.c -o e```
* Running: ```valgrind ./e```
* **Expected result:**

```py
==4197== Memcheck, a memory error detector
==4197== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==4197== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==4197== Command: ./e
==4197== 
0
1
2
3
4
98
402
1024
==4197== 
==4197== HEAP SUMMARY:
==4197==     in use at exit: 0 bytes in 0 blocks
==4197==   total heap usage: 9 allocs, 9 frees, 1,216 bytes allocated
==4197== 
==4197== All heap blocks were freed -- no leaks are possible
==4197== 
==4197== For counts of detected and suppressed errors, rerun with: -v
==4197== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

## 5. Get node at index

### Testing [5-get_dnodeint.c](../5-get_dnodeint.c)

#### Tested by: [5-main.c](5-main.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 5-main.c ../3-add_dnodeint_end.c ../0-print_dlistint.c ../4-free_dlistint.c ../5-get_dnodeint.c -o h```
* Running: ```./h```
* **Expected result:**

```py
0
1
2
3
4
98
402
1024
98
```

## 6. Sum list

### For Testing: [6-sum_dlistint.c](../6-sum_dlistint.c)

#### Tested by: [6-main.c](6-main.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra 6-main.c -std=gnu89 ../3-add_dnodeint_end.c ../4-free_dlistint.c ../6-sum_dlistint.c -o i```
* Running: ```./i```
* **Expected result:**

```py
sum = 1534
```

## 7. Insert at index

### For testing: [7-insert_dnodeint.c](../7-insert_dnodeint.c), [2-add_dnodeint.c](../2-add_dnodeint.c), [3-add_dnodeint_end.c](../3-add_dnodeint_end.c)

#### Tested by: [7-main.c](7-main.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 7-main.c 2-add_dnodeint.c 3-add_dnodeint_end.c 0-print_dlistint.c 4-free_dlistint.c 7-insert_dnodeint.c -o j```
* Running: ```./j```
* **Expected result:**

```py
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
4096
98
402
1024
```

## 8. Delete at index

### For testing [8-delete_dnodeint.c](../8-delete_dnodeint.c)

#### Tested by: [8-main.c](8-main.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 8-main.c 3-add_dnodeint_end.c 0-print_dlistint.c 4-free_dlistint.c 8-delete_dnodeint.c -o k```
* Running: ```./k```
* **Expected result:**

```py
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
402
1024
-----------------
1
2
3
4
402
1024
-----------------
2
3
4
402
1024
-----------------
3
4
402
1024
-----------------
4
402
1024
-----------------
402
1024
-----------------
1024
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
```

## 11. crackme5

### [103-keygen.c](../103-keygen.c)

#### Tested by: [103-keygen.c](../103-keygen.c)

* Compiling: ```gcc -Wall -pedantic -Werror -Wextra -std=gnu89 ../103-keygen.c -o keygen5```
* Running:
  * ```./crackme5 julien javascript```
  * ```./crackme5 julien `./keygen5 julien` ```
* **Expected result:**
  * ```Segmentation fault (core dumped)```
  * ```Congrats!```
