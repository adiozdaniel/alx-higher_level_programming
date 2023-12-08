#include <Python.h>
#include <object.h>
#include <listobject.h>

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
	if (!PyList_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Invalid Python List\n");
		PyErr_Print();
		return;
	}

	Py_ssize_t size = PyObject_Size(p);

	if (size < 0)
	{
		PyErr_SetString(PyExc_TypeError, "Invalid Bytes Object\n");
		PyErr_Print();
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);

	Py_ssize_t i = 0;

	for (; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		if (item == NULL)
		{
			printf("[ITEM] Invalid List Size");
			return;
		}

		/* Get the type name without using Py_TYPE*/
		const char *type_name = item->ob_type->tp_name;

		printf("Element %zd: %s\n", i, type_name);
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
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object");
		return;
	}

	Py_ssize_t size = PyObject_Size(p);

	if (size < 0)
	{
		PyErr_SetString(PyExc_TypeError, "Object has invalid size.");
		PyErr_Print();
		return;
	}

	printf("[.] bytes object info\n");
	printf("  Size: %zd\n", size);

	const char *bytes_data = PyBytes_AsString(p);

	if (bytes_data == NULL)
	{
		printf("[ERROR] Invalid Bytes Object");
		return;
	}

	printf("  first 10 bytes: ");
	Py_ssize_t i = 0;

	for (; i < size && i <= 10; ++i)
	{
		unsigned char byte = (unsigned char)bytes_data[i];

		printf("%02x", byte);
		if (i < 9)
			printf(" ");
	}

	printf("\n");
}
