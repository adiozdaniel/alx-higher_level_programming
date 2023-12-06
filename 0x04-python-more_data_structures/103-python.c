#include <Python.h>

/**
* print_python_list - Prints information about a Python list.
*
* This function takes a PyObject pointer representing a Python list as input
* and prints various information about the list
*
* @p: pointer to a Python list object
*/
void print_python_list(PyObject *p)
{
	/* Check if the input is a valid Python list */
	if (!PyList_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a Python list.");
		PyErr_Print();
		return;
	}

	/* Get the size of the list */
	Py_ssize_t size = PyObject_Size(p);

	if (size < 0)
	{
		PyErr_Print();
		return;
	}

	/* Print general information about the list */
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);

	/* Iterate through the list and print the type of each element */
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
* print_python_bytes - Prints information about a Python bytes object.
*
* This function takes a PyObject pointer representing a Python bytes object as
* input and prints various information about the object
*
* @p: pointer to a Python bytes object
*/
void print_python_bytes(PyObject *p)
{
	/* Check if the input is a valid Python bytes object */
	if (!PyBytes_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a Python bytes object.");
		PyErr_Print();
		return;
	}

	/* Get the size of the bytes object */
	Py_ssize_t size = PyObject_Size(p);

	if (size < 0)
	{
		PyErr_Print();
		return;
	}

	/* Print general information about the bytes object */
	printf("[.] bytes object info\n");
	printf("  Size: %zd\n", size);

	/* Print the first 10 bytes of the bytes object's content */
	printf("  first 10 bytes: ");
	const char *bytes_data = PyBytes_AsString(p);

	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		unsigned char byte = (unsigned char)bytes_data[i];

		printf("%02x", byte);
		if (i < 9)
		{
			printf(" ");
		}
	}

	printf("\n");
}
