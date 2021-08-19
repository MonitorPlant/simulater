#include <Python.h>


static PyObject* update_coord(PyObject *self, PyObject *args)
{
	printf("Hi\n");

	Py_RETURN_NONE;
}

static PyMethodDef MoveMethods[] = {
	{"update_coord", (PyCFunction)update_coord, METH_NOARGS, "move1: update_coord"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef movemodule = {
	PyModuleDef_HEAD_INIT,
	"move",
	NULL,
	-1,
	MoveMethods
};

PyMODINIT_FUNC PyInit_move(void) {
	return PyModule_Create(&movemodule);
}

