#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info about the given python list
 * @p: the python object
 */
void print_python_list_info(PyObject *p)
{
	long int size;
	int i;
	PyListObject *obj;

	/* Validate that p is a Python list before proceeding */
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Invalid Python list\n");
		return;
	}

	size = PyList_Size(p);
	obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
