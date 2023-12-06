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

/**
* main - main function
* Return: void
*/
int main(void)
{
	/* Example usage */
	Py_Initialize();

	/* Create a Python list */
	PyObject *pyList = PyList_New(3);

	PyList_SetItem(pyList, 0, PyLong_FromLong(42));
	PyList_SetItem(pyList, 1, PyUnicode_DecodeUTF8("Hello", 5, "strict"));
	PyList_SetItem(pyList, 2, PyFloat_FromDouble(3.14));

	/* Create a Python bytes object */
	const char *byteData = "PythonBytes";

	PyObject *pyBytes = PyBytes_FromStringAndSize(byteData, strlen(byteData));

	/* Print information about the Python list and bytes object */
	print_python_list(pyList);
	printf("\n");
	print_python_bytes(pyBytes);

	/* Release the Python objects */
	Py_XDECREF(pyList);
	Py_XDECREF(pyBytes);

	/* Finalize the Python interpreter */
	Py_Finalize();

	return (0);
}
