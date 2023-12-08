#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
* print_python_list - Prints information about a Python list
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

	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t i = 0;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	for (; i < size; ++i)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];

		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
		{
			Py_ssize_t item_size = PyObject_Size(item);
			const char *bytes_data = ((PyBytesObject *)item)->ob_sval;
			Py_ssize_t j;

			printf("[.] bytes object info\n");
			printf("  size: %zd\n", item_size);
			printf("  trying string: %s\n", bytes_data);
			printf("  first 6 bytes: ");
			for (j = 0; j < item_size && j < 6; ++j)
			{
				unsigned char byte = (unsigned char)bytes_data[j];

				printf("%02x", byte);
				if (j < 5)
					printf(" ");
			}
			printf("\n");
		}
	}
}

/**
* print_python_bytes - Prints information about a Python bytes object.
*
* This function takes a PyObject pointer representing a Python bytes object as
* input and prints several informations about the object
*
* @p: pointer to a Python bytes object
* returns nothing
*/
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{/* the error in the checker comes from this code!*/
		printf("[.] bytes object info\n");
		fprintf(stderr, " [Error] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyObject_Size(p);
	const char *bytes_data = ((PyBytesObject *)p)->ob_sval;
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", bytes_data);
	printf("  first 6 bytes: ");
	for (i = 0; i < size && i < 6; ++i)
	{
		unsigned char byte = (unsigned char)bytes_data[i];

		printf("%02x", byte);
		if (i < 5)
			printf(" ");
	}
	printf("00");
	printf("\n");
}
