#include <Python.h>

static PyObject*
hello_world(PyObject *self, PyObject *args) {
	printf("Hello world\n");

	Py_RETURN_NONE;
}

static PyMethodDef HelloMethods[] = {
	{"hello_world", (PyCFunction)hello_world, METH_NOARGS, "hello1: hello_world"},
	{NULL, NULL, 0, NULL}
};

// module define
static struct PyModuleDef hellomodule = {
	PyModuleDef_HEAD_INIT,
	"hello",
	NULL,
	-1,
	HelloMethods
};


// method init
PyMODINIT_FUNC PyInit_hello (void) {
	return PyModule_Create(&hellomodule);
}

