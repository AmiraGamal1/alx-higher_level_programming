#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
/**
  * print_python_list_info - print python object list info
  * @p: PyObject
  * Return: nothings
  */

void print_python_list_info(PyObject *p)
{
	int i;
	PylistObject *l_obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", l_obj->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", l_obj->allocated);
	for (i = 0; i < l_obj->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, l_obj->ob_item[i]->ob_type->tp_name);
	}
}
